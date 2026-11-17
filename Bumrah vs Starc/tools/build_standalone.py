import os
import base64

PROJECT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\Bumrah vs Starc"
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
font_css_old = 'src: url("assets/fonts/Anton-Regular.ttf") format("truetype");'
font_css_new = f'src: url("data:font/truetype;charset=utf-8;base64,{font_b64}") format("truetype");'
html = html.replace(font_css_old, font_css_new)

with open(STANDALONE_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print(f"standalone.html generated ({len(html)} bytes)")
