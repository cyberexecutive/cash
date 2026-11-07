# -*- coding: utf-8 -*-
with open(r'C:\invest\css\landing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace root variables
root_old = """:root {
  --lp-bg-dark: #050811;
  --lp-bg-surface: #0a1120;
  --lp-bg-surface-elevated: #0f1c34;
  --lp-border: rgba(6, 182, 212, 0.2);
  --lp-border-hover: rgba(6, 182, 212, 0.5);
  
  --lp-cyan: #06b6d4;
  --lp-cyan-glow: rgba(6, 182, 212, 0.4);
  --lp-cyan-light: #67e8f9;
  
  --lp-gold: #f59e0b;
  --lp-gold-glow: rgba(245, 158, 11, 0.4);
  --lp-gold-light: #fbbf24;
  
  --lp-emerald: #10b981;
  --lp-emerald-glow: rgba(16, 185, 129, 0.35);"""

root_new = """:root {
  --lp-bg-dark: #040907;
  --lp-bg-surface: #07150e;
  --lp-bg-surface-elevated: #0d2318;
  --lp-border: rgba(16, 185, 129, 0.22);
  --lp-border-hover: rgba(16, 185, 129, 0.55);
  
  --lp-cyan: #10b981;
  --lp-cyan-glow: rgba(16, 185, 129, 0.4);
  --lp-cyan-light: #34d399;
  
  --lp-gold: #f59e0b;
  --lp-gold-glow: rgba(245, 158, 11, 0.4);
  --lp-gold-light: #fbbf24;
  
  --lp-emerald: #10b981;
  --lp-emerald-glow: rgba(16, 185, 129, 0.35);"""

css = css.replace(root_old, root_new)

# Replace background radial gradients in body
body_bg_old = """  background: 
    radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.12) 0%, transparent 50%),
    radial-gradient(circle at 90% 20%, rgba(245, 158, 11, 0.08) 0%, transparent 45%),
    radial-gradient(circle at 10% 60%, rgba(6, 182, 212, 0.08) 0%, transparent 50%),
    var(--lp-bg-dark);"""

body_bg_new = """  background: 
    radial-gradient(circle at 50% 0%, rgba(16, 185, 129, 0.14) 0%, transparent 50%),
    radial-gradient(circle at 90% 20%, rgba(245, 158, 11, 0.08) 0%, transparent 45%),
    radial-gradient(circle at 10% 60%, rgba(16, 185, 129, 0.10) 0%, transparent 50%),
    var(--lp-bg-dark);"""

css = css.replace(body_bg_old, body_bg_new)

# Replace specific cyan hex/rgba references with Dollar green
css = css.replace('rgba(6, 182, 212,', 'rgba(16, 185, 129,')
css = css.replace('rgba(14, 165, 233,', 'rgba(5, 150, 105,')
css = css.replace('#06b6d4', '#10b981')
css = css.replace('#0ea5e9', '#059669')
css = css.replace('#38bdf8', '#34d399')
css = css.replace('#0284c7', '#047857')

# Update header title comment
header_comment_old = """/* ==========================================================================
   LANDING PAGE: TREINAMENTO EXECUTIVO EM CIBERSEGURANÇA CORPORATIVA
   Design de Alta Conversão, Futurista e Responsivo
   ========================================================================== */"""

header_comment_new = """/* ==========================================================================
   LANDING PAGE: GESTÃO E FLUXO DE CAIXA PARA EMPRESAS
   Design Executivo de Alta Conversão em Verde Dólar (#10b981)
   ========================================================================== */"""

css = css.replace(header_comment_old, header_comment_new)

with open(r'C:\cash\css\landing.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Gerado C:\\cash\\css\\landing.css com sucesso!")

