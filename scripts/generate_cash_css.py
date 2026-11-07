import re

with open(r'C:\invest\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# We replace blue and cyan tones with dollar green / emerald tones
replacements = [
    # Backgrounds
    ('#090d16', '#040907'),
    ('#151e36', '#0b2417'),
    ('#05070c', '#020604'),
    ('rgba(18, 26, 44, 0.72)', 'rgba(8, 24, 16, 0.75)'),
    ('rgba(26, 38, 64, 0.85)', 'rgba(14, 38, 26, 0.88)'),
    ('rgba(18, 26, 44, 0.95)', 'rgba(8, 24, 16, 0.95)'),
    ('rgba(15, 23, 42,', 'rgba(6, 18, 12,'),

    # Accents & Borders
    ('#06b6d4', '#10b981'), # Cyan -> Dollar Green #10b981
    ('#0284c7', '#059669'), # Sky Navy -> Deep Emerald #059669
    ('#38bdf8', '#34d399'), # Light Sky -> Light Mint #34d399
    ('#0891b2', '#047857'), # Dark Cyan -> Dark Emerald #047857
    ('#0e7490', '#065f46'), # Deep Teal -> Deep Forest #065f46
    ('rgba(6, 182, 212,', 'rgba(16, 185, 129,'),
    ('rgba(2, 132, 199,', 'rgba(5, 150, 105,'),
    ('rgba(56, 189, 248,', 'rgba(52, 211, 153,'),

    # Certificate specific
    ('border: 4px solid #0284c7', 'border: 4px solid #10b981'),
    ('border: 4px solid #06b6d4', 'border: 4px solid #10b981'),
    ('color: rgba(2, 132, 199,', 'color: rgba(16, 185, 129,'),
    ('border-color: rgba(6, 182, 212,', 'border-color: rgba(52, 211, 153,'),
    ('#slide-38', '#slide-38'),
]

for old, new in replacements:
    css = css.replace(old, new)

# Write to C:\cash\css\styles.css
with open(r'C:\cash\css\styles.css', 'w', encoding='utf-8', newline='') as f:
    f.write(css)

print(f"Gerado C:\\cash\\css\\styles.css com {len(css)} caracteres no tema Verde Dólar!")

