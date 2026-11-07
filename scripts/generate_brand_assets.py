import os
import shutil
import base64
from PIL import Image
import numpy as np

base_dir = r"C:\cash"
img_dir = os.path.join(base_dir, "imagens")
css_dir = os.path.join(base_dir, "css")
js_dir = os.path.join(base_dir, "js")
scripts_dir = os.path.join(base_dir, "scripts")

for d in [base_dir, img_dir, css_dir, js_dir, scripts_dir]:
    os.makedirs(d, exist_ok=True)
print("Diretórios criados com sucesso em C:\\cash!")

# 1. Carrega emblema oficial anexado pelo usuário
src_path = r"C:\Users\Claudinei Lima\.gemini\antigravity\brain\2dfa7f41-7a33-4fa1-883e-ba1f0866407a\.user_uploaded\media_1794085872305_3f810adb.jpg"
im = Image.open(src_path).convert("RGB")
arr = np.array(im, dtype=np.float32) / 255.0

# 2. Converte para HSV para mudar o matiz para Verde Dólar (#10b981 / esmeralda / verde financeiro)
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
maxc = np.maximum(np.maximum(r, g), b)
minc = np.minimum(np.minimum(r, g), b)
deltac = maxc - minc

s = np.zeros_like(maxc)
nonzero_max = maxc > 1e-5
s[nonzero_max] = deltac[nonzero_max] / maxc[nonzero_max]

h = np.zeros_like(maxc)
nonzero_delta = deltac > 1e-5

mask_r = nonzero_delta & (maxc == r)
mask_g = nonzero_delta & (maxc == g)
mask_b = nonzero_delta & (maxc == b)

h[mask_r] = ((g[mask_r] - b[mask_r]) / deltac[mask_r]) % 6.0
h[mask_g] = ((b[mask_g] - r[mask_g]) / deltac[mask_g]) + 2.0
h[mask_b] = ((r[mask_b] - g[mask_b]) / deltac[mask_b]) + 4.0
h = (h / 6.0) % 1.0

v = maxc

# Mapeia azul/ciano para Verde Dólar vibrante e nobre (matiz ~0.42 a 0.44 = 150° a 160°)
blue_mask = (h >= 0.46) & (h <= 0.76) & (s > 0.08)

h_shifted = np.copy(h)
rel = (h[blue_mask] - 0.46) / (0.76 - 0.46)
h_shifted[blue_mask] = 0.44 - rel * 0.06

s_shifted = np.copy(s)
s_shifted[blue_mask] = np.clip(s[blue_mask] * 1.15, 0.0, 1.0)

# Reconverte para RGB
c = v * s_shifted
x_val = c * (1.0 - np.abs(((h_shifted * 6.0) % 2.0) - 1.0))
m = v - c

h6 = (h_shifted * 6.0).astype(int) % 6

r_new = np.zeros_like(v)
g_new = np.zeros_like(v)
b_new = np.zeros_like(v)

m0 = h6 == 0
r_new[m0], g_new[m0], b_new[m0] = c[m0], x_val[m0], 0
m1 = h6 == 1
r_new[m1], g_new[m1], b_new[m1] = x_val[m1], c[m1], 0
m2 = h6 == 2
r_new[m2], g_new[m2], b_new[m2] = 0, c[m2], x_val[m2]
m3 = h6 == 3
r_new[m3], g_new[m3], b_new[m3] = 0, x_val[m3], c[m3]
m4 = h6 == 4
r_new[m4], g_new[m4], b_new[m4] = x_val[m4], 0, c[m4]
m5 = h6 == 5
r_new[m5], g_new[m5], b_new[m5] = c[m5], 0, x_val[m5]

r_final = np.clip((r_new + m) * 255.0, 0, 255).astype(np.uint8)
g_final = np.clip((g_new + m) * 255.0, 0, 255).astype(np.uint8)
b_final = np.clip((b_new + m) * 255.0, 0, 255).astype(np.uint8)

# 3. Recorte circular alfa perfeito com suavização antialiasing
h_img, w_img = arr.shape[:2]
cy, cx = (h_img - 1) / 2.0, (w_img - 1) / 2.0
y_grid, x_grid = np.ogrid[:h_img, :w_img]
dist = np.sqrt((x_grid - cx)**2 + (y_grid - cy)**2)

r_inner = 497.0
r_outer = 507.0
alpha = np.clip((r_outer - dist) / (r_outer - r_inner), 0.0, 1.0)
alpha = alpha * alpha * (3.0 - 2.0 * alpha)
a_final = (alpha * 255.0).astype(np.uint8)

rgba_arr = np.dstack([r_final, g_final, b_final, a_final])
logo_png = Image.fromarray(rgba_arr, "RGBA")

# 4. Salva logo-cyber-executive.png
png_dest = os.path.join(img_dir, "logo-cyber-executive.png")
logo_png.save(png_dest, format="PNG", optimize=True)
print(f"Salvo logo oficial: {png_dest}")

# Capa de anúncio 1x1 em JPG de alta qualidade
cover_dest = os.path.join(img_dir, "anuncio-hotmart-1x1.jpg")
bg_black = Image.new("RGB", logo_png.size, (4, 9, 7))
bg_black.paste(logo_png, (0, 0), logo_png)
bg_black.save(cover_dest, format="JPEG", quality=95)
print(f"Salvo anúncio/capa: {cover_dest}")

# 5. Gera Favicons e ícones
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
ico_images = [logo_png.resize(size, Image.Resampling.LANCZOS) for size in ico_sizes]

favicon_ico_root = os.path.join(base_dir, "favicon.ico")
favicon_ico_img = os.path.join(img_dir, "favicon.ico")
ico_images[0].save(favicon_ico_root, format="ICO", sizes=ico_sizes, append_images=ico_images[1:])
ico_images[0].save(favicon_ico_img, format="ICO", sizes=ico_sizes, append_images=ico_images[1:])

logo_png.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(img_dir, "favicon-32x32.png"), "PNG", optimize=True)
logo_png.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(img_dir, "favicon-16x16.png"), "PNG", optimize=True)
logo_png.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(img_dir, "apple-touch-icon.png"), "PNG", optimize=True)
logo_png.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(img_dir, "android-chrome-192x192.png"), "PNG", optimize=True)
logo_png.resize((512, 512), Image.Resampling.LANCZOS).save(os.path.join(img_dir, "android-chrome-512x512.png"), "PNG", optimize=True)
print("Favicons e ícones gerados com sucesso!")

# 6. Gera SVG vetorial de altíssima definição
with open(png_dest, "rb") as f:
    b64_png = base64.b64encode(f.read()).decode("ascii")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="greenBgGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#059669" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#040907" stop-opacity="0"/>
    </radialGradient>
    <filter id="neonGreenGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <circle cx="512" cy="512" r="500" fill="url(#greenBgGlow)"/>
  <circle cx="512" cy="512" r="496" fill="none" stroke="#10b981" stroke-width="8" filter="url(#neonGreenGlow)" opacity="0.85"/>
  <circle cx="512" cy="512" r="486" fill="none" stroke="#34d399" stroke-width="3" opacity="0.9"/>
  <image href="data:image/png;base64,{b64_png}" x="0" y="0" width="1024" height="1024"/>
</svg>'''

svg_dest = os.path.join(img_dir, "logo-cyber-executive.svg")
with open(svg_dest, "w", encoding="utf-8") as f:
    f.write(svg_content)
print(f"Salvo SVG vetorial: {svg_dest}")

