import cv2
import os
from PIL import Image
import re

# ============ CONFIGURATION ===============
INPUT_FOLDER = r"C:\Users\tcher\OneDrive\Documents\Yan\03.Hobbies\Writing\Confluence\References\Never Mind The Gap"
OUTPUT_SUBFOLDER = "Panels"
PANEL_MIN_AREA = 50000   # Ignore tiny artefacts
# ==========================================

def extract_page_number(filename):
    """Extracts the numerical page number from a filename like 'Never Mind The Gap - Page 001.png'."""
    match = re.search(r'Page\s*(\d+)', filename)
    if match:
        return int(match.group(1))
    return None

# Prepare output
output_path = os.path.join(INPUT_FOLDER, OUTPUT_SUBFOLDER)
os.makedirs(output_path, exist_ok=True)

# Process all images
for file in os.listdir(INPUT_FOLDER):
    if not file.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    page_number = extract_page_number(file)
    if page_number is None:
        print(f"[SKIP] Could not detect page number in {file}")
        continue

    print(f"[INFO] Processing Page {page_number:03d}: {file}")

    # Load image
    img_path = os.path.join(INPUT_FOLDER, file)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect panel borders (threshold works well for comics)
    _, thresh = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)

    # Find contours = potential panels
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    panel_index = 1

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Skip noise or tiny contours
        if w * h < PANEL_MIN_AREA:
            continue

        # Crop panel
        panel = img[y:y+h, x:x+w]

        # Output filename
        panel_name = f"Page{page_number:03d}_Panel{panel_index}.png"
        panel_path = os.path.join(output_path, panel_name)

        # Save with Pillow (better PNG handling)
        Image.fromarray(cv2.cvtColor(panel, cv2.COLOR_BGR2RGB)).save(panel_path)
        print(f"   → Saved {panel_name}")

        panel_index += 1

    if panel_index == 1:
        print("   [WARN] No panels detected for this page")

print("\n✔ All pages processed!")
