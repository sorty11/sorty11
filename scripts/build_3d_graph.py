import xml.etree.ElementTree as ET
import re
import os

src_path = "profile-3d-contrib/profile-night-green.svg"
out_path = "assets/contribution_3d.svg"

if not os.path.exists(src_path):
    print(f"File not found: {src_path}")
    exit(1)

tree = ET.parse(src_path)
root = tree.getroot()

# Extract total contributions from child 5 if present
contrib_count = "115"
try:
    child5 = root[5]
    for text_el in child5.iter():
        if text_el.text and text_el.text.isdigit():
            contrib_count = text_el.text
            break
except Exception:
    pass

# child 0: style
style_str = ET.tostring(root[0], encoding="unicode")

# child 2: pure 3d isometric grid
grid_elem = root[2]
# Adjust transform to center it nicely
grid_str = ET.tostring(grid_elem, encoding="unicode")

# Create clean, architectural 3D SVG
svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 1280 620">
  {style_str}
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E121A"/>
      <stop offset="100%" stop-color="#0A0D14"/>
    </linearGradient>
    <style>
      .data-mono {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; }}
      @keyframes pulseDot {{ 0%, 100% {{ opacity: 0.4; }} 50% {{ opacity: 1; }} }}
      .pulse {{ animation: pulseDot 2.5s infinite ease-in-out; }}
    </style>
  </defs>

  <!-- Frame Background -->
  <rect x="2" y="2" width="1276" height="616" rx="12" fill="url(#cardBg)" stroke="#262C36" stroke-width="1.5"/>

  <!-- Top Header Metadata -->
  <text x="36" y="44" fill="#8B949E" class="data-mono" font-size="12" font-weight="600" letter-spacing="1.5">GITHUB CONTRIBUTION ACTIVITY · 2025 — 2026</text>
  <text x="36" y="68" fill="#F0F6FC" class="data-mono" font-size="18" font-weight="700">{contrib_count} <tspan fill="#8B949E" font-size="14" font-weight="400">contributions in the last year</tspan></text>
  
  <circle cx="1234" cy="40" r="4" fill="#39D353" class="pulse"/>
  <text x="1170" y="44" fill="#39D353" class="data-mono" font-size="11" font-weight="600">LIVE SYNC</text>

  <!-- Clean Divider -->
  <line x1="36" y1="84" x2="1244" y2="84" stroke="#1F242C" stroke-width="1"/>

  <!-- 3D Isometric Landscape Grid (Shifted up to fit viewport) -->
  <g transform="translate(0, -60)">
    {grid_str}
  </g>

  <!-- Bottom Legend -->
  <g transform="translate(1080, 582)">
    <text x="-38" y="11" fill="#6E7681" class="data-mono" font-size="11">Less</text>
    <rect x="0" y="0" width="12" height="12" rx="2" fill="#161B22" stroke="#30363D"/>
    <rect x="18" y="0" width="12" height="12" rx="2" fill="#0E4429"/>
    <rect x="36" y="0" width="12" height="12" rx="2" fill="#006D32"/>
    <rect x="54" y="0" width="12" height="12" rx="2" fill="#26A641"/>
    <rect x="72" y="0" width="12" height="12" rx="2" fill="#39D353"/>
    <text x="94" y="11" fill="#6E7681" class="data-mono" font-size="11">More</text>
  </g>

  <!-- Left Timestamp -->
  <text x="36" y="593" fill="#6E7681" class="data-mono" font-size="11">ISOMETRIC EXTRUSION · 52 WEEKS ACTIVITY MATRIX</text>
</svg>
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg_template)

print(f"Generated clean 3D contribution graph at: {out_path}")
