import base64
import os

html_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\index.html"
gsap_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\assets\gsap.min.js"
font_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\assets\fonts\Anton-Regular.ttf"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(gsap_path, "r", encoding="utf-8") as f:
    gsap_code = f.read()

with open(font_path, "rb") as f:
    font_b64 = base64.b64encode(f.read()).decode("utf-8")

html = html.replace('<script src="assets/gsap.min.js"></script>', f'<script>{gsap_code}</script>')
font_orig = 'src: url("assets/fonts/Anton-Regular.ttf") format("truetype");'
font_inlined = f'src: url("data:font/truetype;charset=utf-8;base64,{font_b64}") format("truetype");'
html = html.replace(font_orig, font_inlined)

standalone_path = r"c:\Users\Lenovo\OneDrive\Desktop\Project Hope\kohli-765-runs\standalone.html"
with open(standalone_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"standalone.html updated ({len(html)} bytes)")
