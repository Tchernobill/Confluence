import os
import requests
from bs4 import BeautifulSoup

# ==== USER CONFIGURATION ====
START_PAGE = 1
END_PAGE = 358

BASE_URL = "https://nmg.thecomicseries.com/comics/"
SAVE_FOLDER = r"C:\Users\tcher\OneDrive\Documents\Yan\03.Hobbies\Writing\Confluence\References\Never Mind The Gap"
FILENAME_TEMPLATE = "Never Mind The Gap - Page {num:03d}.png"

# Ensure save folder exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Main loop
for page_num in range(START_PAGE, END_PAGE + 1):
    url = f"{BASE_URL}{page_num}"
    print(f"[INFO] Fetching page {page_num}: {url}")

    try:
        # Load webpage
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Locate comic image (id="comicimage")
        img_tag = soup.find("img", {"id": "comicimage"})
        if not img_tag:
            print(f"[WARN] No comic image found on page {page_num}. Skipping.")
            continue

        img_url = img_tag["src"]

        # Some URLS on ComicFury may be relative
        if img_url.startswith("/"):
            img_url = "https:" + img_url

        # Prepare output filename
        filename = FILENAME_TEMPLATE.format(num=page_num)
        filepath = os.path.join(SAVE_FOLDER, filename)

        # Download image
        print(f"       → Downloading image: {img_url}")
        img_data = requests.get(img_url, timeout=15)
        img_data.raise_for_status()

        # Save PNG
        with open(filepath, "wb") as f:
            f.write(img_data.content)

        print(f"[OK] Saved: {filepath}")

    except Exception as e:
        print(f"[ERROR] Failed on page {page_num}: {e}")

print("\n✔ Done! All pages processed.")
