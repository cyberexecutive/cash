# -*- coding: utf-8 -*-
"""
Ilustrações vetoriais exclusivas (SVGs) para cada slide do curso:
'Gestão e Fluxo de Caixa para Empresas' no tema Verde Dólar.
"""

def get_svg_slide_1():
    return '''<svg viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="cov-glow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#10b981" stop-opacity="0.38" />
          <stop offset="100%" stop-color="#10b981" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="cov-green" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#34d399" />
          <stop offset="50%" stop-color="#10b981" />
          <stop offset="100%" stop-color="#059669" />
        </linearGradient>
      </defs>

      <!-- Glow de Fundo -->
      <circle cx="250" cy="200" r="170" fill="url(#cov-glow)" />

      <!-- Órbitas Tecnológicas -->
      <circle cx="250" cy="200" r="140" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="6 6" opacity="0.45" />
      <circle cx="250" cy="200" r="110" fill="none" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4 8" opacity="0.35" />

      <!-- Hexágono Central Verde Dólar -->
      <polygon points="250,110 320,150 320,240 250,285 180,240 180,150" fill="#04120a" stroke="url(#cov-green)" stroke-width="3.5" filter="drop-shadow(0 0 15px rgba(16,185,129,0.5))" />

      <!-- Símbolo de Crescimento e Cifrão R$ -->
      <g transform="translate(250, 195) scale(1.35)">
        <path d="M-22,12 L-6,-4 L6,4 L22,-14" fill="none" stroke="#34d399" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
        <polyline points="14,-14 22,-14 22,-6" fill="none" stroke="#34d399" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
        <text x="0" y="16" fill="#10b981" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="900" text-anchor="middle">R$</text>
      </g>

      <!-- Partículas Orbitais -->
      <circle cx="390" cy="200" r="4.5" fill="#10b981" />
      <circle cx="110" cy="200" r="4.5" fill="#34d399" />
      <circle cx="250" cy="60" r="3.5" fill="#059669" />
      <circle cx="250" cy="340" r="3.5" fill="#10b981" />

      <!-- Legenda Inferior -->
      <text x="250" y="335" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="700" letter-spacing="2.5" text-anchor="middle">GESTÃO &amp; FLUXO DE CAIXA 2026</text>
    </svg>'''


def get_svg_generic(badge_text="GESTÃO EMPRESARIAL", icon_type="shield"):
    icons = {
        "shield": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <path d="M250,145 L290,165 L290,215 Q290,245 250,260 Q210,245 210,215 L210,165 Z" fill="rgba(16,185,129,0.18)" stroke="#34d399" stroke-width="2.5" />
          <path d="M235,200 L245,212 L268,185" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
        ''',
        "wallet": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <rect x="210" y="160" width="80" height="55" rx="8" fill="rgba(16,185,129,0.22)" stroke="#34d399" stroke-width="2.5"/>
          <circle cx="265" cy="188" r="6" fill="#34d399"/>
          <path d="M210,172 L290,172" stroke="#10b981" stroke-width="2"/>
        ''',
        "chart": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <rect x="212" y="215" width="14" height="30" fill="#10b981" rx="3"/>
          <rect x="234" y="195" width="14" height="50" fill="#34d399" rx="3"/>
          <rect x="256" y="175" width="14" height="70" fill="#10b981" rx="3"/>
          <rect x="278" y="155" width="14" height="90" fill="#6ee7b7" rx="3"/>
          <polyline points="210,210 240,185 265,165 290,140" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
        ''',
        "calculator": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <rect x="215" y="150" width="70" height="85" rx="8" fill="rgba(16,185,129,0.2)" stroke="#34d399" stroke-width="2.5"/>
          <rect x="225" y="160" width="50" height="18" rx="4" fill="#022c22" stroke="#10b981" stroke-width="1.5"/>
          <circle cx="230" cy="190" r="4" fill="#34d399"/>
          <circle cx="250" cy="190" r="4" fill="#34d399"/>
          <circle cx="270" cy="190" r="4" fill="#34d399"/>
          <circle cx="230" cy="205" r="4" fill="#34d399"/>
          <circle cx="250" cy="205" r="4" fill="#34d399"/>
          <circle cx="270" cy="205" r="4" fill="#34d399"/>
          <circle cx="230" cy="220" r="4" fill="#34d399"/>
          <circle cx="250" cy="220" r="4" fill="#34d399"/>
          <circle cx="270" cy="220" r="4" fill="#10b981"/>
        ''',
        "bank": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <polygon points="250,150 288,170 212,170" fill="#34d399"/>
          <rect x="222" y="175" width="8" height="40" fill="#10b981"/>
          <rect x="246" y="175" width="8" height="40" fill="#10b981"/>
          <rect x="270" y="175" width="8" height="40" fill="#10b981"/>
          <rect x="210" y="218" width="80" height="8" rx="2" fill="#34d399"/>
        ''',
        "target": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <circle cx="250" cy="195" r="38" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 4"/>
          <circle cx="250" cy="195" r="24" fill="none" stroke="#34d399" stroke-width="2.5"/>
          <circle cx="250" cy="195" r="10" fill="#10b981"/>
        ''',
        "scale": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#10b981" stroke-width="3" filter="drop-shadow(0 0 12px rgba(16,185,129,0.4))"/>
          <line x1="250" y1="150" x2="250" y2="230" stroke="#34d399" stroke-width="3"/>
          <line x1="220" y1="168" x2="280" y2="168" stroke="#34d399" stroke-width="3"/>
          <path d="M210,195 L230,195 L220,168 Z" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="2"/>
          <path d="M270,195 L290,195 L280,168 Z" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="2"/>
        ''',
        "quiz": '''
          <polygon points="250,115 315,150 315,235 250,280 185,235 185,150" fill="#06180f" stroke="#f59e0b" stroke-width="3" filter="drop-shadow(0 0 15px rgba(245,158,11,0.4))"/>
          <circle cx="250" cy="190" r="35" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 5" />
          <text x="250" y="206" fill="#f59e0b" font-size="38" font-family="'JetBrains Mono', monospace" font-weight="900" text-anchor="middle">?</text>
        '''
    }

    icon_svg = icons.get(icon_type, icons["shield"])
    badge_color = "#f59e0b" if icon_type == "quiz" else "#34d399"

    return f'''<svg viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="gen-glow-{icon_type}" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="{badge_color}" stop-opacity="0.25" />
          <stop offset="100%" stop-color="{badge_color}" stop-opacity="0" />
        </radialGradient>
      </defs>

      <circle cx="250" cy="195" r="140" fill="url(#gen-glow-{icon_type})" />
      <circle cx="250" cy="195" r="115" fill="none" stroke="{badge_color}" stroke-width="1.2" stroke-dasharray="4 6" opacity="0.35" />

      {icon_svg}

      <rect x="150" y="322" width="200" height="26" rx="13" fill="#04120a" stroke="{badge_color}" stroke-width="1.2" opacity="0.85" />
      <text x="250" y="339" fill="{badge_color}" font-size="9.5" font-family="'JetBrains Mono', monospace" font-weight="700" letter-spacing="1.2" text-anchor="middle">{badge_text}</text>
    </svg>'''

