import pathlib
from playwright.sync_api import sync_playwright

current_dir = pathlib.Path(__file__).resolve().parent

save_dir = current_dir / "html"
with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://poliinfo3.net/")
    page.screenshot(path="example.png")
    html = page.content()
    with open(save_dir / "test.html", mode="w", encoding="utf-8") as f:
        f.write(html)
    browser.close()