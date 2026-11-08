# -*- coding: utf-8 -*-
"""
Compilador mestre de index.html para o curso:
'Gestão e Fluxo de Caixa para Empresas: Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios'
Gera estrutura 100% idêntica e compatível com styles.css e presentation.js.
"""
import os
import sys

from course_slides_data import SLIDES_DATA
from course_svg_assets import get_svg_slide_1, get_svg_generic

def generate_slide_html(slide):
    snum = slide["slide_num"]
    stype = slide["type"]
    active_cls = " active" if snum == 1 else ""

    if stype == "cover":
        cards_html = ""
        for c in slide["cards"]:
            cards_html += f'''
            <div class="info-card">
              <div class="card-header-line">
                <div class="card-icon {c['icon']}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
                <div class="card-title">{c['title']}</div>
              </div>
              <p class="card-desc">{c['desc']}</p>
            </div>'''

        svg_art = get_svg_slide_1()

        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: {slide['category']}
         ========================================== -->
    <section class="slide{active_cls}" id="slide-{snum}" data-index="{snum}">
      <div class="slide-body">
        <div class="content-col">
          <div class="slide-header-block">
            <div class="slide-category">
              <span></span> {slide['category']}
            </div>
            <h1 class="slide-title">
              {slide['title']}
            </h1>
            <p class="slide-subtitle">
              {slide['subtitle']}
            </p>
          </div>

          <div class="cards-grid-3">
            {cards_html}
          </div>

          <div class="navigation-tip-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            <span>{slide['tip']}</span>
          </div>

          <!-- Banner Informativo de Tela Cheia -->
          <div class="fullscreen-notice-banner" id="banner-fullscreen-tip">
            <div class="fs-notice-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
            </div>
            <div class="fs-notice-text">
              <strong>Visualização Otimizada:</strong> Abra o treinamento em <strong>Tela Cheia</strong> para a melhor experiência visual e leitura dos slides. Pressione <strong>F</strong> ou clique ao lado.
            </div>
            <button class="action-pill primary fs-prompt-btn" id="btn-fs-prompt" onclick="window.PresentationApp.toggleFullscreen()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
              <span id="btn-fs-prompt-text">Abrir em Tela Cheia (F)</span>
            </button>
          </div>

          <div class="slide-cta-row">
            <button class="action-pill primary" id="btn-start-course" onclick="window.PresentationApp.startCourse()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              Iniciar Treinamento
            </button>
            <button class="action-pill" onclick="window.PresentationApp.toggleModulesDrawer()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
              Ver Grade de Aulas
            </button>
          </div>
        </div>

        <div class="visual-col">
          <div class="visual-container">
            <div class="svg-illustration">
              {svg_art}
            </div>
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "lesson":
        cards_html = ""
        c_count = len(slide["cards"])
        grid_class = "cards-grid-3" if c_count == 3 else ("cards-grid-2" if c_count == 2 else "cards-grid-4")

        for c in slide["cards"]:
            icon_name = c["icon"]
            cards_html += f'''
            <div class="info-card zoomable-card">
              <div class="card-header-line">
                <div class="card-icon {icon_name}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
                <div class="card-title">{c['title']}</div>
                <div class="card-zoom-badge" title="Ampliar card">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
                </div>
              </div>
              <p class="card-desc">{c['desc']}</p>
            </div>'''

        co = slide["callout"]
        co_type = co.get("type", "tip")
        callout_html = f'''
          <div class="alert-callout {co_type}">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            <span><strong>{co['title']}:</strong> {co['text']}</span>
          </div>'''

        svg_art = get_svg_generic(slide.get("svg_badge", "GESTÃO EMPRESARIAL"), slide.get("svg_icon", "shield"))

        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: {slide['category']}
         ========================================== -->
    <section class="slide{active_cls}" id="slide-{snum}" data-index="{snum}">
      <div class="slide-body">
        <div class="content-col">
          <div class="slide-header-block">
            <div class="slide-category">
              <span></span> {slide['category']}
            </div>
            <h2 class="slide-title">
              {slide['title']}
            </h2>
            <p class="slide-subtitle">
              {slide['subtitle']}
            </p>
          </div>

          <div class="{grid_class}">
            {cards_html}
          </div>

          {callout_html}
        </div>

        <div class="visual-col">
          <div class="visual-container">
            <div class="svg-illustration">
              {svg_art}
            </div>
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "quiz":
        qid = slide["quiz_id"]
        opts_html = ""
        for i, opt in enumerate(slide["options"]):
            is_cor = "true" if opt["correct"] else "false"
            letter = opt["letter"]
            opts_html += f'''
              <button class="quiz-opt-btn" data-opt-idx="{i}" data-correct="{is_cor}">
                <div class="quiz-opt-letter">{letter}</div>
                <div class="quiz-opt-desc">{opt['desc']}</div>
                <div class="quiz-opt-zoom-btn" title="Ampliar texto da alternativa" tabindex="0" role="button">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
                </div>
              </button>'''

        svg_art = get_svg_generic(slide.get("svg_badge", f"DESAFIO {qid:02d}"), "quiz")

        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: QUIZ INTERATIVO {qid:02d}
         ========================================== -->
    <section class="slide{active_cls}" id="slide-{snum}" data-index="{snum}" data-quiz-slide="{qid}">
      <div class="slide-body">
        <div class="content-col">
          <div class="slide-header-block">
            <div class="slide-category">
              <span></span> {slide['category']}
            </div>
            <h2 class="slide-title">
              {slide['title']}
            </h2>
            <p class="slide-subtitle">
              {slide['subtitle']}
            </p>
          </div>

          <div class="quiz-container" data-quiz-id="{qid}">
            <div class="quiz-scenario-box">
              <div class="quiz-badge-tag">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                Cenário da Vida Real
              </div>
              <p class="quiz-scenario-text">
                "{slide['scenario']}"
              </p>
            </div>

            <div class="quiz-options-list">
              {opts_html}
            </div>

            <!-- Barra de Ações de Confirmação -->
            <div class="quiz-confirm-bar" id="quiz-confirm-bar-{qid}">
              <div class="quiz-confirm-info">
                <span>Alternativa selecionada. Deseja confirmar sua decisão?</span>
              </div>
              <div class="quiz-confirm-btns">
                <button class="action-pill primary btn-confirm-quiz">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                  Confirmar Decisão
                </button>
                <button class="action-pill btn-cancel-quiz">
                  Cancelar
                </button>
              </div>
            </div>

            <!-- Box de Feedback da Decisão -->
            <div class="quiz-feedback-box" id="quiz-feedback-{qid}" title="Clique para ampliar esta explicação em tela cheia">
              <div class="quiz-feedback-header">
                <span class="quiz-feedback-title"></span>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="quiz-score-badge">+10 Pontos</span>
                  <span class="quiz-feedback-zoom-hint" title="Ampliar em tela cheia" onclick="event.stopPropagation(); window.PresentationApp.openQuizFeedbackZoom({qid})">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                  </span>
                </div>
              </div>
              <div class="quiz-feedback-text">
                {slide['feedback_text']}
              </div>
              <div class="quiz-feedback-actions">
                <button class="action-pill primary" onclick="window.PresentationApp.nextSlide()">
                  Próxima Aula →
                </button>
                <button class="action-pill" onclick="window.PresentationApp.retryQuiz({qid})">
                  Refazer Questão
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="visual-col">
          <div class="visual-container">
            <div class="svg-illustration">
              {svg_art}
            </div>
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "certificate":
        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: CERTIFICAÇÃO EXECUTIVA OFICIAL
         ========================================== -->
    <section class="slide{active_cls}" id="slide-38" data-index="38">
      <div class="cert-slide-content">
        <!-- Barra com Dados Oficiais do Aluno Registrado -->
        <div class="cert-registered-bar">
          <div class="cert-student-profile-badge">
            <div class="cert-profile-avatar">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <div class="cert-profile-info">
              <span class="cert-profile-label">Titular do Certificado Oficial:</span>
              <div class="cert-profile-data">
                <strong class="cert-profile-name" id="cert-bar-student-name">Empresário(a) Estratégico(a)</strong>
                <span class="cert-profile-dot">•</span>
                <span class="cert-profile-cpf" id="cert-bar-student-cpf">CPF: 000.000.000-00</span>
              </div>
            </div>
          </div>

          <div class="cert-status-actions">
            <div class="cert-edition-status" id="cert-edition-status">
              <span class="cert-edition-pill" id="cert-edition-pill">1ª VIA ORIGINAL</span>
            </div>
            <button class="action-pill primary btn-print-cert" id="btn-print-certificate" onclick="window.PresentationApp.printCertificate()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
              <span id="btn-print-label">Imprimir / Salvar em PDF</span>
            </button>
          </div>
        </div>

        <!-- O Certificado Formal de Gestão e Fluxo de Caixa -->
        <div class="certificate-card" id="official-certificate">
          <!-- Elementos Tecnológicos de Canto -->
          <div class="cert-corner-bracket cert-corner-tl" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-tr" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-bl" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-br" aria-hidden="true"></div>

          <!-- Selo e Marca d'Água de 2ª Via -->
          <div class="cert-second-copy-badge" id="cert-second-copy-badge" style="display: none;">
            ★ SEGUNDA VIA OFICIAL ★
          </div>
          <div class="cert-second-copy-watermark" id="cert-second-copy-watermark" style="display: none;">
            2ª VIA OFICIAL
          </div>

          <!-- Marca D'água Tecnológica de Fundo Verde Dólar -->
          <div class="cert-tech-watermark" aria-hidden="true">
            <svg viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="250" cy="250" r="220" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 6" />
              <circle cx="250" cy="250" r="180" stroke="currentColor" stroke-width="1" />
              <circle cx="250" cy="250" r="140" stroke="currentColor" stroke-width="2" stroke-dasharray="12 4" />
              <path d="M250 30 V110 M250 390 V470 M30 250 H110 M390 250 H470" stroke="currentColor" stroke-width="2" />
              <path d="M95 95 L150 150 M350 350 L405 405 M405 95 L350 150 M150 350 L95 405" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 4" />
              <!-- Cifrão e Escudo no Centro -->
              <circle cx="250" cy="250" r="45" stroke="currentColor" stroke-width="2.5" fill="none" />
              <path d="M235 260 L245 235 L255 245 L265 225" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>

          <div class="cert-header">
            <!-- Brasão Oficial Centralizado no Topo -->
            <div class="cert-crest-wrap">
              <img src="imagens/logo-cyber-executive.png?v=1.0" alt="Brasão Oficial Cyber Executive" class="cert-top-crest" width="64" height="64" decoding="async" />
            </div>

            <div class="cert-badge-ribbon">
              ★ FORMAÇÃO EXECUTIVA OFICIAL ★
            </div>

            <h1 class="cert-title">Formação Executiva em Gestão &amp; Fluxo de Caixa para Empresas</h1>
            <p class="cert-sub">CONTROLE FINANCEIRO • PRECIFICAÇÃO ESTRATÉGICA • DRE GERENCIAL • GESTÃO DE LIQUIDEZ</p>
          </div>

          <div class="cert-body">
            <p class="cert-certifies">Certificamos com distinção e reconhecimento profissional que</p>
            <div class="cert-student-name-display" id="cert-display-name">Empresário(a) Estratégico(a)</div>
            <div class="cert-student-cpf-display" id="cert-display-cpf">CPF: 000.000.000-00</div>
            <p class="cert-statement">
              concluiu com êxito o treinamento prático e executivo <strong>Gestão e Fluxo de Caixa para Empresas</strong>,
              demonstrando proficiência comprovada em Separação Patrimonial PF/PJ e Fixação de Pró-Labore Sustentável,
              Planejamento e Controle de Fluxo de Caixa Diário e Projetado, Precificação Científica com Margem de Contribuição e Ponto de Equilíbrio Real,
              Elaboração e Análise de DRE Gerencial Descomplicada, Gestão de Inadimplência e Risco de Crédito, e Governança Orçamentária para PMEs.
            </p>

            <!-- Metadados de Carga Horária, Data e Aproveitamento -->
            <div class="cert-meta-grid">
              <div class="cert-meta-card">
                <div class="cert-meta-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                </div>
                <div class="cert-meta-text">
                  <span class="cert-meta-label">Carga Horária</span>
                  <span class="cert-meta-val">6 Horas • Executivo</span>
                </div>
              </div>

              <div class="cert-meta-card">
                <div class="cert-meta-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                </div>
                <div class="cert-meta-text">
                  <span class="cert-meta-label">Data de Conclusão</span>
                  <span class="cert-meta-val" id="cert-date-display">07 de Novembro de 2026</span>
                </div>
              </div>

              <div class="cert-meta-card">
                <div class="cert-meta-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                </div>
                <div class="cert-meta-text">
                  <span class="cert-meta-label">Aproveitamento</span>
                  <span class="cert-meta-val">100% • Aprovado</span>
                </div>
              </div>
            </div>
          </div>

          <div class="cert-footer-row">
            <!-- Assinatura Centralizada da Direção Executiva -->
            <div class="cert-signature-box central">
              <div class="cert-signature-space" title="Assinatura Digital Oficial">
                <img src="imagens/assinatura-ceo.png" alt="Assinatura Oficial - Diretor Executivo - CEO" class="cert-signature-img" />
              </div>
              <div class="cert-signature-line"></div>
              <div class="cert-signature-name">Diretor Executivo - CEO</div>
              <div class="cert-signature-role">Cyber Executive Academy • Gestão Financeira Corporativa</div>
              <div class="cert-code-tag" id="cert-auth-code">CSH-2026-X89</div>
              <div class="cert-second-copy-note" id="cert-second-copy-note" style="display: none;">
                1ª Emissão Original em <span id="cert-orig-date">--</span> • Via registrada pelo titular acadêmico.
              </div>
            </div>
          </div>
        </div>

        <div class="cert-actions-bar">
          <button class="action-pill" onclick="window.PresentationApp.goToSlide(1)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
            Voltar ao Início
          </button>
          <button class="action-pill" onclick="window.PresentationApp.restartCourse()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><polyline points="23 20 23 14 17 14"/><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"/></svg>
            Reiniciar Treinamento
          </button>
        </div>
      </div>
    </section>'''

    return ""

def compile_all():
    slides_body_list = []
    for slide in SLIDES_DATA:
        slides_body_list.append(generate_slide_html(slide))

    all_slides_html = "\n\n".join(slides_body_list)

    final_html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Gestão e Fluxo de Caixa para Empresas | Formação Executiva Prática 2026</title>
  <meta name="description" content="Gestão e Fluxo de Caixa para Empresas: Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios. Separação PF/PJ, DRE gerencial, margem e fluxo de caixa.">
  <meta name="keywords" content="gestão financeira, fluxo de caixa, precificação de produtos, pequenas empresas, controle financeiro, capital de giro, ponto de equilíbrio, MEI, PME">
  <meta name="author" content="Cyber Executive">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#040907">

  <!-- Favicon e Ícones Oficiais em Verde Dólar -->
  <link rel="icon" type="image/svg+xml" href="imagens/logo-cyber-executive.svg?v=1.0">
  <link rel="icon" type="image/png" sizes="32x32" href="imagens/favicon-32x32.png?v=1.0">
  <link rel="icon" type="image/png" sizes="16x16" href="imagens/favicon-16x16.png?v=1.0">
  <link rel="shortcut icon" href="favicon.ico?v=1.0">
  <link rel="apple-touch-icon" sizes="180x180" href="imagens/apple-touch-icon.png?v=1.0">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://cyberexecutive.github.io/cash/">

  <!-- Open Graph -->
  <meta property="og:site_name" content="Cash Flow Pro 2026">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://cyberexecutive.github.io/cash/">
  <meta property="og:title" content="Gestão e Fluxo de Caixa para Empresas | Formação Executiva">
  <meta property="og:description" content="Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios com certificação formal.">
  <meta property="og:image" content="https://cyberexecutive.github.io/cash/imagens/anuncio-hotmart-1x1.jpg">
  <meta property="og:image:alt" content="Gestão e Fluxo de Caixa para Empresas - Formação 2026">
  <meta property="og:locale" content="pt_BR">

  <!-- Estilos e Fontes -->
  <link rel="stylesheet" href="css/styles.css?v=2.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">
</head>
<body>

  <!-- Barra de Progresso Superior Global -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="top-progress-bar"></div>
  </div>

  <!-- Header Superior Fixo -->
  <header class="top-header">
    <div class="brand-badge">
      <img src="imagens/logo-cyber-executive.png?v=1.0" alt="Cyber Executive Logo" class="brand-badge-logo" />
      <span>CASH • GESTÃO E FLUXO DE CAIXA PARA EMPRESAS</span>
    </div>

    <div class="header-actions">
      <!-- Badge de Acesso / Botão de Desbloqueio do Aluno -->
      <div id="access-status-container">
        <button class="header-pill-badge" id="btn-header-unlock" title="Status de Acesso do Treinamento">
          <span class="badge-dot" id="access-badge-dot"></span>
          <span id="access-badge-text">⚡ Demonstração Gratuita</span>
          <span class="badge-action" id="badge-action-label">• 🔑 Já sou Aluno / Gestor</span>
        </button>
      </div>

      <!-- Botão Página de Vendas (Landing Page) -->
      <a href="landing.html" class="header-btn" title="Página de Apresentação e Vendas (Landing Page)" style="text-decoration: none;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/>
          <line x1="3" y1="6" x2="21" y2="6"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
      </a>

      <!-- Botão Trilha de Módulos (Menu Lateral) -->
      <button class="header-btn" id="btn-modules" title="Trilha de Módulos (M)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>

      <!-- Botão Modo Claro/Escuro -->
      <button class="header-btn" id="btn-theme" title="Alternar Modo Escuro / Claro (T)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="5"/>
          <line x1="12" y1="1" x2="12" y2="3"/>
          <line x1="12" y1="21" x2="12" y2="23"/>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
          <line x1="1" y1="12" x2="3" y2="12"/>
          <line x1="21" y1="12" x2="23" y2="12"/>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>
      </button>

      <!-- Botão Visão Geral de Todos os Slides -->
      <button class="header-btn" id="btn-overview" title="Grade de Slides (G)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="7" height="7"/>
          <rect x="14" y="3" width="7" height="7"/>
          <rect x="14" y="14" width="7" height="7"/>
          <rect x="3" y="14" width="7" height="7"/>
        </svg>
      </button>

      <!-- Botão Ajuda / Atalhos -->
      <button class="header-btn" id="btn-help" title="Atalhos do Teclado (?)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
          <line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
      </button>

      <!-- Botão Tela Cheia -->
      <button class="header-btn" id="btn-fullscreen" title="Modo Tela Cheia (F)">
        <svg id="fs-icon-enter" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>
        </svg>
        <svg id="fs-icon-exit" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none;">
          <path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/>
        </svg>
      </button>
    </div>
  </header>

  <!-- Viewport Principal da Apresentação -->
  <main id="presentation-viewport">
{all_slides_html}
  </main>

  <!-- Barra de Controles Flutuante Inferior (Dock) -->
  <footer class="bottom-dock">
    <div class="dock-controls">
      <button class="dock-btn" id="btn-prev" title="Slide Anterior (←)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"/>
        </svg>
      </button>

      <div class="dock-counter">
        <span class="current-num">01</span> / <span class="total-num">38</span>
      </div>

      <button class="dock-btn" id="btn-next" title="Próximo Slide (→)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
      </button>
    </div>

    <div class="dock-divider"></div>

    <div class="dock-dots" id="dock-dots-container">
      <!-- Gerado dinamicamente pelo JS -->
    </div>
  </footer>

  <!-- Modal de Visão Geral (Overview Grid) -->
  <div class="modal-overlay" id="overview-modal">
    <div class="overview-content">
      <div class="overview-header">
        <h3>Índice e Grade de Slides do Curso (38 Slides)</h3>
        <button class="close-modal-btn" id="close-overview-btn" title="Fechar (Esc)">✕</button>
      </div>
      <div class="overview-grid" id="overview-grid">
        <!-- Preenchido dinamicamente pelo JS -->
      </div>
    </div>
  </div>

  <!-- Modal de Ajuda e Atalhos -->
  <div class="modal-overlay" id="help-modal">
    <div class="overview-content" style="max-width: 650px;">
      <div class="overview-header">
        <h3>Atalhos e Dicas de Navegação</h3>
        <button class="close-modal-btn" id="close-help-btn" title="Fechar (Esc)">✕</button>
      </div>

      <div class="shortcuts-grid">
        <div class="shortcut-row">
          <span>Próxima Aula / Slide</span>
          <div>
            <span class="shortcut-key">→</span>
            <span class="shortcut-key">Espaço</span>
            <span class="shortcut-key">PgDn</span>
          </div>
        </div>

        <div class="shortcut-row">
          <span>Aula Anterior</span>
          <div>
            <span class="shortcut-key">←</span>
            <span class="shortcut-key">Backspace</span>
            <span class="shortcut-key">PgUp</span>
          </div>
        </div>

        <div class="shortcut-row">
          <span>Trilha de Módulos (Menu)</span>
          <span class="shortcut-key">M</span>
        </div>

        <div class="shortcut-row">
          <span>Tela Cheia</span>
          <span class="shortcut-key">F</span>
        </div>

        <div class="shortcut-row">
          <span>Grade de Miniaturas</span>
          <span class="shortcut-key">G</span> ou <span class="shortcut-key">O</span>
        </div>

        <div class="shortcut-row">
          <span>Alternar Modo Claro/Escuro</span>
          <span class="shortcut-key">T</span>
        </div>

        <div class="shortcut-row">
          <span>Fechar Modais / Zoom</span>
          <span class="shortcut-key">Esc</span>
        </div>
      </div>

      <div class="alert-callout tip">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
        <span>Você pode clicar em qualquer card, caixa de cenário ou ilustração para <strong>ampliar</strong> em tela cheia com facilidade!</span>
      </div>
    </div>
  </div>

  <!-- Modal de Card Ampliado (Zoom Modal) -->
  <div class="card-modal-overlay" id="card-zoom-modal" aria-hidden="true">
    <div class="card-modal-container" id="card-zoom-container">
      <button class="card-modal-close" id="card-zoom-close-btn" title="Fechar (Esc ou clique fora)" aria-label="Fechar card ampliado">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
      <div class="card-modal-content" id="card-zoom-content">
        <!-- Conteúdo do card injetado dinamicamente via JavaScript -->
      </div>
    </div>
  </div>

  <!-- Menu Gaveta Lateral da Trilha de Módulos (Drawer com Painel Flutuante) -->
  <aside class="modules-drawer" id="modules-drawer">
    <div class="drawer-backdrop" id="drawer-backdrop"></div>
    <div class="drawer-panel">
      <div class="drawer-header">
        <div class="drawer-title-group">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            Grade Executiva de Aulas
          </h3>
          <p>6 Módulos • 6 Desafios Práticos • Certificado Oficial</p>
        </div>
        <button class="drawer-close-btn" id="close-drawer-btn" title="Fechar Menu (Esc)">✕</button>
      </div>

      <div class="drawer-progress-box">
        <div class="drawer-progress-labels">
          <span>Progresso do Aluno</span>
          <strong id="drawer-progress-percent">0%</strong>
        </div>
        <div class="drawer-progress-track">
          <div class="drawer-progress-bar" id="drawer-progress-bar"></div>
        </div>
      </div>

      <div class="drawer-modules-list" id="drawer-modules-container">
        <!-- Preenchido dinamicamente pelo JS -->
      </div>
    </div>
  </aside>

  <!-- Modal de Paywall / Conclusão da Demonstração Gratuita -->
  <div class="modal-overlay" id="paywall-modal" aria-hidden="true">
    <div class="overview-content paywall-card-container">
      <button class="close-modal-btn" id="close-paywall-btn" title="Fechar (Esc)">✕</button>
      
      <div class="paywall-header">
        <div class="paywall-badge">
          🔒 CONTEÚDO EXCLUSIVO PARA ALUNOS
        </div>
        <h2 class="paywall-title">Você Concluiu a <span class="highlight-cyan">Demonstração Gratuita</span>!</h2>
        <p class="paywall-subtitle">
          Parabéns por completar as aulas do <strong>Módulo 01 (Separação PF/PJ &amp; Pró-Labore Blindado)</strong>. Para continuar sua formação prática e desbloquear todos os <strong>6 Módulos Completos (38 Slides)</strong> e o <strong>Certificado Oficial Executivo</strong>, garanta seu acesso com desconto especial de lançamento.
        </p>
      </div>

      <div class="paywall-benefits-list">
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">📈</div>
          <div>
            <strong>6 Módulos Completos sem Restrições (38 Aulas Práticas)</strong>
            <span>Separação PF/PJ, Fluxo Diário e Projetado, Precificação Científica, DRE, Inadimplência e Governança</span>
          </div>
        </div>
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">🎯</div>
          <div>
            <strong>6 Desafios Práticos da Vida Real com Tomada de Decisão</strong>
            <span>Simulações de decisões reais com pontuação individual e feedback estratégico imediato</span>
          </div>
        </div>
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">📜</div>
          <div>
            <strong>Certificado Oficial Executivo (6 Horas)</strong>
            <span>Personalizado com seu nome, CPF, código criptográfico individual CASH-2026 e assinatura executiva</span>
          </div>
        </div>
      </div>

      <div class="paywall-action-box">
        <div class="paywall-price-info">
          <span class="paywall-price-label">Acesso Vitalício por apenas:</span>
          <div class="paywall-price-value">R$ 47<small>,00</small> <span class="paywall-price-sub">(ou 5x de R$ 10,25)</span></div>
        </div>
        <div class="paywall-dual-buttons">
          <a href="https://pay.kiwify.com.br/SVqQtZZ" class="paywall-cta-btn paywall-btn-kiwify" id="btn-paywall-kiwify" target="_blank" rel="noopener" style="border-radius: 9999px !important;">
            PAGAR VIA KIWIFY
          </a>
          <a href="https://pay.hotmart.com/T108385988V" class="paywall-cta-btn paywall-btn-hotmart" id="btn-paywall-hotmart" target="_blank" rel="noopener" style="border-radius: 9999px !important;">
            PAGAR VIA HOTMART
          </a>
        </div>
      </div>

      <div class="paywall-footer-hint">
        <span>Já adquiriu o treinamento?</span>
        <button type="button" class="paywall-unlock-link" id="btn-paywall-enter-key">🔑 Inserir Chave de Acesso (Aluno ou Gestor)</button>
      </div>
    </div>
  </div>

  <!-- Modal de Inserção de Chave de Acesso / Desbloqueio -->
  <div class="unlock-modal-overlay" id="unlock-modal" aria-hidden="true">
    <div class="unlock-card">
      <button class="unlock-close-btn" id="close-unlock-btn" title="Fechar (Esc)">✕</button>

      <div class="unlock-header">
        <div class="unlock-icon-circle">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
        </div>
        <h3 class="unlock-title">Ativar Acesso do Treinamento (Aluno ou Gestor)</h3>
        <p class="unlock-desc">Insira abaixo sua <strong>Chave de Acesso do Aluno</strong> recebida no e-mail após a compra ou a <strong>Senha de Gestor</strong> para liberar todos os módulos e o certificado.</p>
      </div>

      <form id="form-unlock-key" onsubmit="event.preventDefault(); window.PresentationApp.submitUnlockKey();">
        <div class="unlock-input-group">
          <label for="input-unlock-key" class="unlock-label">Chave de Acesso ou Senha:</label>
          <input type="text" id="input-unlock-key" class="unlock-input" placeholder="Ex: ALUNO-CASH-8842-PRO ou GESTOR-..." autocomplete="off" autocorrect="off" autocapitalize="characters" spellcheck="false" required />
        </div>

        <div class="unlock-actions-row">
          <button type="submit" class="action-pill primary unlock-submit-btn" id="btn-submit-unlock">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Validar e Desbloquear
          </button>
        </div>
      </form>

      <div class="unlock-status-msg" id="unlock-status-msg" style="display: none;"></div>

      <div class="unlock-footer-note">
        <span>Não tem uma chave de acesso?</span>
        <a href="landing.html#inscricao" target="_blank" rel="noopener">Garanta sua vaga por apenas R$ 47,00</a>
      </div>
    </div>
  </div>

  <!-- Modal Cadastral Obrigatório de Nome e CPF do Aluno (Apenas ao emitir Certificado no Slide 38) -->
  <div class="modal-overlay" id="student-id-modal" aria-hidden="true">
    <div class="overview-content student-id-card" style="max-width: 520px;">
      <div class="overview-header" style="border-bottom: none; padding-bottom: 0;">
        <div class="student-id-badge">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          IDENTIFICAÇÃO DO ALUNO
        </div>
        <button class="close-modal-btn" id="close-student-id-btn" title="Fechar (Esc)">✕</button>
      </div>

      <div class="student-id-body">
        <h3 class="student-id-title">Dados para o Certificado Oficial</h3>
        <p class="student-id-sub">
          Para registrar seu progresso nos 6 Desafios Práticos e <strong>emitir seu Certificado Oficial Executivo</strong> com validação de autenticidade, informe seu Nome Completo e CPF.
        </p>

        <form id="form-student-id" onsubmit="event.preventDefault(); window.PresentationApp.submitStudentRegistration();">
          <div class="student-id-input-group">
            <label for="input-student-name">Nome Completo (como constará no Certificado):</label>
            <input type="text" id="input-student-name" class="unlock-input" placeholder="Ex: Seu Nome Completo Aqui" required autocomplete="name" />
          </div>

          <div class="student-id-input-group" style="margin-top: 14px;">
            <label for="input-student-cpf">CPF (para validação acadêmica do Certificado):</label>
            <input type="text" id="input-student-cpf" class="unlock-input" placeholder="000.000.000-00" maxlength="14" required autocomplete="off" />
          </div>

          <div class="student-id-actions" style="margin-top: 20px;">
            <button type="submit" class="action-pill primary" style="width: 100%; justify-content: center; padding: 12px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              Salvar Dados e Emitir Certificado
            </button>
          </div>
        </form>

        <p class="student-id-privacy-note">
          🔒 Seus dados são armazenados localmente e utilizados exclusivamente para emissão do seu Certificado Oficial.
        </p>
      </div>
    </div>
  </div>

  <!-- Toast Notification Flutuante -->
  <div class="course-toast" id="course-toast" role="alert" aria-live="polite"></div>

  <!-- Script da Engine Interativa -->
  <script src="js/presentation.js?v=2.1"></script>
</body>
</html>'''

    output_path = os.path.join(r"C:\cash", "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Sucesso! Gerado C:\\cash\\index.html com {len(SLIDES_DATA)} slides em {output_path}")

if __name__ == "__main__":
    compile_all()
