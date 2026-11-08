# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

src_p = r"C:\invest\imagens\certificado-preview.jpg"
out_p = r"C:\cash\imagens\certificado-preview.jpg"

im = Image.open(src_p).convert("RGB")
arr = np.array(im, dtype=np.float32)

r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]

# Detect cyan/blue regions (b > r and g > r)
cyan_mask = (b > r + 15) & (g > r + 10)

# Shift cyan/blue to Dollar green (#10b981)
# Green should dominate, blue reduced, red adjusted
new_r = r.copy()
new_g = g.copy()
new_b = b.copy()

# In cyan areas, boost green and lower blue
new_g[cyan_mask] = np.clip(np.maximum(g[cyan_mask], b[cyan_mask]) * 1.05, 0, 255)
new_b[cyan_mask] = np.clip(r[cyan_mask] * 0.8 + (b[cyan_mask] - r[cyan_mask]) * 0.35, 0, 255)

out_arr = np.stack([new_r, new_g, new_b], axis=2).astype(np.uint8)
out_im = Image.fromarray(out_arr)
out_im.save(out_p, quality=95)
print(f"Gerado {out_p} com sucesso!")

