import os
import base64

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-31-for-4"
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")
STANDALONE_HTML = os.path.join(PROJECT_DIR, "standalone.html")
GSAP_PATH = os.path.join(PROJECT_DIR, "assets", "gsap.min.js")
FONT_PATH = os.path.join(PROJECT_DIR, "assets", "fonts", "Anton-Regular.ttf")

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

with open(GSAP_PATH, "r", encoding="utf-8") as f:
    gsap_js = f.read()

with open(FONT_PATH, "rb") as f:
    font_b64 = base64.b64encode(f.read()).decode("ascii")

html = html.replace('<script src="assets/gsap.min.js"></script>', f'<script>{gsap_js}</script>')

# Replace font url with base64 data uri
font_data_uri = f'url("data:font/truetype;charset=utf-8;base64,{font_b64}")'
html = html.replace("url('assets/fonts/Anton-Regular.ttf')", font_data_uri)
html = html.replace('url("assets/fonts/Anton-Regular.ttf")', font_data_uri)

with open(STANDALONE_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print(f"standalone.html generated ({len(html)} bytes)")
