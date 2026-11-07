# -*- coding: utf-8 -*-
"""
Script de Auditoria e Verificação de Integridade:
Curso: Gestão e Fluxo de Caixa para Empresas
"""
import os
import re
import sys

def run_checks():
    base_dir = r"C:\cash"
    print("==================================================")
    print(" INICIANDO AUDITORIA DO CURSO: CASH FLOW 2026")
    print("==================================================")
    errors = []

    # 1. Arquivos essenciais
    required_files = [
        "index.html",
        "landing.html",
        "favicon.ico",
        "css/styles.css",
        "css/landing.css",
        "js/presentation.js",
        "js/landing.js",
        "imagens/logo-cyber-executive.svg",
        "imagens/logo-cyber-executive.png",
        "imagens/favicon.ico",
        "imagens/favicon-16x16.png",
        "imagens/favicon-32x32.png",
        "imagens/apple-touch-icon.png",
        "imagens/android-chrome-192x192.png",
        "imagens/android-chrome-512x512.png",
        "imagens/anuncio-hotmart-1x1.jpg"
    ]

    for rel_path in required_files:
        full_p = os.path.join(base_dir, rel_path)
        if not os.path.exists(full_p):
            errors.append(f"Arquivo ausente: {rel_path}")
        else:
            size = os.path.getsize(full_p)
            print(f" [OK] {rel_path} ({size} bytes)")

    # 2. Verificação de index.html
    index_p = os.path.join(base_dir, "index.html")
    if os.path.exists(index_p):
        with open(index_p, "r", encoding="utf-8") as f:
            html = f.read()

        # Slides
        slide_indices = re.findall(r'data-index="(\d+)"', html)
        slide_indices_int = sorted(list(set(int(x) for x in slide_indices)))
        print(f" Slides encontrados: {len(slide_indices_int)} (De {min(slide_indices_int)} até {max(slide_indices_int)})")
        if len(slide_indices_int) != 38 or min(slide_indices_int) != 1 or max(slide_indices_int) != 38:
            errors.append(f"Esperados 38 slides contínuos (1 a 38), encontrados: {slide_indices_int}")

        # Quizzes
        quizzes = re.findall(r'data-quiz-id="(\d+)"', html)
        quizzes_int = sorted(list(set(int(x) for x in quizzes)))
        print(f" Quizzes encontrados: {quizzes_int}")
        if len(quizzes_int) != 6 or quizzes_int != [1, 2, 3, 4, 5, 6]:
            errors.append(f"Esperados 6 quizzes (1 a 6), encontrados: {quizzes_int}")

        # Elementos essenciais de DOM
        essential_ids = [
            "top-progress-bar", "btn-prev", "btn-next", "btn-fullscreen",
            "btn-modules", "btn-overview", "btn-help", "btn-theme", "btn-header-unlock",
            "overview-modal", "help-modal", "modules-drawer", "paywall-modal",
            "unlock-modal", "student-id-modal", "card-zoom-modal", "official-certificate",
            "cert-display-name", "cert-display-cpf", "cert-auth-code", "btn-print-certificate"
        ]
        for eid in essential_ids:
            if f'id="{eid}"' not in html:
                errors.append(f"Elemento essencial ausente no index.html: id='{eid}'")

    # 3. Verificação de presentation.js
    js_p = os.path.join(base_dir, "js", "presentation.js")
    if os.path.exists(js_p):
        with open(js_p, "r", encoding="utf-8") as f:
            js = f.read()

        if "totalSlides: 38" not in js:
            errors.append("presentation.js não contém 'totalSlides: 38'")
        if "maxDemoSlide: 7" not in js:
            errors.append("presentation.js não contém 'maxDemoSlide: 7'")
        if "openQuizFeedbackZoom" not in js:
            errors.append("presentation.js não contém openQuizFeedbackZoom")
        if "printCertificate" not in js:
            errors.append("presentation.js não contém printCertificate")
        if "GESTOR-CASH-2026-X89" in js:
            errors.append("FALHA DE SEGURANÇA: Chave mestre exposta em texto puro no presentation.js!")
        if "ALUNO-CASH-8842-PRO" in js:
            errors.append("FALHA DE SEGURANÇA: Chave de aluno exposta em texto puro no presentation.js!")

        # Confirma que os hashes corretos de Cash estão presentes
        if "e273fe31900138572a84ccb206c0a63b22940b1809723e0f4a0d2f81c3802104" not in js:
            errors.append("Hash do Gestor Cash não encontrado em presentation.js")
        if "d77907c6bc72c46e73bad3d15be7674da557caf50cc48bc9e1ae9301f8966fdc" not in js:
            errors.append("Hash do Aluno Cash não encontrado em presentation.js")

    # 4. Verificação de landing.html
    landing_p = os.path.join(base_dir, "landing.html")
    if os.path.exists(landing_p):
        with open(landing_p, "r", encoding="utf-8") as f:
            lp = f.read()
        if "btn-checkout-kiwify" not in lp:
            errors.append("Botão btn-checkout-kiwify não encontrado em landing.html")
        if "btn-checkout-hotmart" not in lp:
            errors.append("Botão btn-checkout-hotmart não encontrado em landing.html")
        if "R$ 47" not in lp:
            errors.append("Preço R$ 47 não encontrado em landing.html")

    # 5. Verificação de CSS
    css_p = os.path.join(base_dir, "css", "styles.css")
    if os.path.exists(css_p):
        with open(css_p, "r", encoding="utf-8") as f:
            styles = f.read()
        if "#10b981" not in styles:
            errors.append("Cor Verde Dólar (#10b981) não encontrada em styles.css")
        if "@media print" not in styles:
            errors.append("Regra @media print não encontrada em styles.css")

    print("==================================================")
    if errors:
        print(f"❌ FORAM ENCONTRADOS {len(errors)} ERROS NA AUDITORIA:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("✅ AUDITORIA CONCLUÍDA COM 100% DE SUCESSO!")
        print(" Todos os arquivos, requisitos, elementos e travas de segurança estão íntegros.")
        print("==================================================")

if __name__ == "__main__":
    run_checks()
