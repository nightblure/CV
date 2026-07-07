from playwright.sync_api import sync_playwright
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

html_path = BASE_DIR / "index.html"
pdf_path = BASE_DIR / "resume.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    try:
        page = browser.new_page()
        page.set_viewport_size({"width": 794, "height": 1123})
        page.goto(html_path.as_uri())
        page.wait_for_load_state("networkidle")

        page.pdf(
            path=str(pdf_path),
            print_background=True,
            prefer_css_page_size=True,
            scale=0.95
        )
    finally:
        browser.close()

print("PDF created")
