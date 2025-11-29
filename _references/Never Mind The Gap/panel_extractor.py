import os
import re
import io
import time
import json
import base64
import yaml
import requests
from PIL import Image

# ==========================
# Load CONFIG
# ==========================
with open("config.yaml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

API_KEY = cfg["openrouter_api_key"]
MODEL = cfg["model"]
INPUT_FOLDER = cfg["input_folder"]
OUTPUT_SUBFOLDER = cfg["output_subfolder"]

MIN_PANEL_AREA = cfg.get("min_panel_area", 20000)
MAX_RETRIES = cfg.get("max_retries", 3)
RETRY_DELAY = cfg.get("retry_delay", 2)

DEBUG_SAVE_AI_RESPONSE = cfg.get("debug_save_ai_response", False)

OUTPUT_FOLDER = os.path.join(INPUT_FOLDER, OUTPUT_SUBFOLDER)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ==========================
# Helpers
# ==========================

def extract_page_number(filename):
    match = re.search(r'Page\s*(\d+)', filename)
    return int(match.group(1)) if match else None


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def ai_request_with_retry(image_path):
    """Send the image to OpenRouter with retry + exponential backoff."""
    encoded = encode_image(image_path)

    prompt_text = """
You are an advanced comic panel detection system.
Return ONLY JSON: an array of bounding boxes in reading order.

Each box must be:
{
  "x": int,
  "y": int,
  "w": int,
  "h": int
}

Return JSON only.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Comic Panel Detector",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{encoded}"
                    }
                ]
            }
        ]
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"      [AI] Attempt {attempt}/{MAX_RETRIES}...")
            r = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=60
            )
            r.raise_for_status()

            content = r.json()["choices"][0]["message"]["content"]

            # OPTIONAL: Save raw debug output
            if DEBUG_SAVE_AI_RESPONSE:
                dbg_path = os.path.join(OUTPUT_FOLDER, "debug_ai_raw_output.txt")
                with open(dbg_path, "a", encoding="utf-8") as f:
                    f.write(f"\n--- {image_path} ---\n{content}\n")

            return json.loads(content)

        except Exception as e:
            print(f"      [WARN] AI error: {e}")
            if attempt < MAX_RETRIES:
                delay = RETRY_DELAY * (2 ** (attempt - 1))
                print(f"      Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("      [ERROR] Max retries reached.")
                return []


def load_cached_panels(json_path):
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def save_panels_metadata(json_path, metadata):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)


# ==========================
# MAIN PROCESSING LOOP
# ==========================

for file in os.listdir(INPUT_FOLDER):
    if not file.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    page_num = extract_page_number(file)
    if page_num is None:
        print(f"[SKIP] Cannot detect page number in {file}")
        continue

    print(f"\n[PROCESS] Page {page_num:03d}: {file}")

    img_path = os.path.join(INPUT_FOLDER, file)

    # JSON cache file
    json_cache = os.path.join(OUTPUT_FOLDER, f"Page{page_num:03d}.json")

    # Try loading cached result
    cached_panels = load_cached_panels(json_cache)
    if cached_panels:
        print(f"   [CACHE] Using cached panel metadata for Page {page_num:03d}")
        panels = cached_panels
    else:
        print(f"   [AI] No cache found — requesting panel detection…")
        panels = ai_request_with_retry(img_path)
        save_panels_metadata(json_cache, panels)

    img = Image.open(img_path)

    # Save each panel
    for i, p in enumerate(panels,  start=1):
        x, y, w, h = p["x"], p["y"], p["w"], p["h"]

        # Skip tiny detections
        if w * h < MIN_PANEL_AREA:
            continue

        crop = img.crop((x, y, x + w, y + h))
        out_name = f"Page{page_num:03d}_Panel{i}.png"
        out_path = os.path.join(OUTPUT_FOLDER, out_name)
        crop.save(out_path)

        print(f"      Saved {out_name}")

    print(f"   [DONE] Processed {len(panels)} panels.")

print("\n✔ All pages processed with AI + caching + retries.")

