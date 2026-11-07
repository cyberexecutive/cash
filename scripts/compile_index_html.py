# -*- coding: utf-8 -*-
"""
Compilador mestre de index.html para o curso:
'Gestão e Fluxo de Caixa para Empresas: Precificação de Produtos e Controle Financeiro de Pequenos Negócios'
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
            <button class="action-pill primary" onclick="window.PresentationApp.startCourse()">
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
          <div class="vector-art-wrapper cover-art-wrapper">
            {svg_art}
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "lesson":
        cards_html = ""
        c_count = len(slide["cards"])
        grid_class = "cards-grid-3" if c_count == 3 else ("cards-grid-2" if c_count == 2 else "cards-grid-4")

        icon_map = {
            "rose": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
            "emerald": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            "cyan": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
            "amber": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
            "violet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>'
        }

        for c in slide["cards"]:
            ic = icon_map.get(c["icon"], icon_map["emerald"])
            cards_html += f'''
            <div class="info-card zoomable-card">
              <div class="card-header-line">
                <div class="card-icon {c['icon']}">{ic}</div>
                <div class="card-title">{c['title']}</div>
                <div class="card-zoom-badge" title="Ampliar card">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
                </div>
              </div>
              <p class="card-desc">{c['desc']}</p>
            </div>'''

        callout_html = ""
        if "callout" in slide and slide["callout"]:
            co = slide["callout"]
            co_type = co.get("type", "info")
            callout_html = f'''
          <div class="slide-callout-box {co_type}">
            <div class="callout-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            </div>
            <div class="callout-content">
              <strong>{co['title']}:</strong> {co['text']}
            </div>
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
          <div class="vector-art-wrapper">
            {svg_art}
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
              <div class="quiz-opt-btn" data-opt-idx="{i}" data-correct="{is_cor}" role="button" tabindex="0">
                <span class="quiz-opt-letter">{letter}</span>
                <span class="quiz-opt-desc">{opt['desc']}</span>
                <span class="quiz-opt-zoom-btn" title="Ampliar texto da alternativa" tabindex="0" role="button">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
                </span>
              </div>'''

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
                  Confirmar Resposta
                </button>
                <button class="action-pill btn-cancel-quiz">
                  Cancelar
                </button>
              </div>
            </div>

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
                <button class="action-pill btn-zoom-feedback" onclick="window.PresentationApp.openQuizFeedbackZoom({qid})" title="Ampliar resposta em tela cheia">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
                  Ampliar em Tela Cheia
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="visual-col">
          <div class="vector-art-wrapper">
            {svg_art}
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "certificate":
        return f'''    <!-- ==========================================
         SLIDE 38: CERTIFICAÇÃO EXECUTIVA OFICIAL
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
                <span class="cert-profile-cpf" id="cert-bar-student-cpf">CPF/CNPJ: 000.000.000-00</span>
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

        <!-- O Certificado Formal de Gestão e Fluxo de Caixa Empresarial -->
        <div class="certificate-card" id="official-certificate">
          <!-- Elementos Tecnológicos de Canto -->
          <div class="cert-corner-bracket cert-corner-tl" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-tr" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-bl" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-br" aria-hidden="true"></div>

          <!-- Carimbo D'água Dinâmico de 2ª Via Oficial -->
          <div class="cert-second-copy-watermark" id="cert-second-copy-watermark" aria-hidden="true">
            <span class="watermark-text">2ª VIA OFICIAL</span>
            <span class="watermark-sub" id="cert-watermark-meta">REGISTRO DIGITAL AUDITADO</span>
          </div>

          <!-- Cabeçalho do Certificado -->
          <div class="cert-header">
            <div class="cert-institution-mark">
              <img src="imagens/logo-cyber-executive.png" alt="Cyber Executive Emblem" class="cert-emblem-img" />
              <div class="cert-inst-text">
                <span class="cert-inst-title">CYBER EXECUTIVE &amp; GESTÃO EMPRESARIAL</span>
                <span class="cert-inst-sub">DIVISÃO DE FORMAÇÃO EM CONTROLADORIA E FINANÇAS CORPORATIVAS</span>
              </div>
            </div>
            <div class="cert-doc-badge">
              <span class="cert-badge-dot"></span>
              CERTIFICAÇÃO EXECUTIVA FORMAL
            </div>
          </div>

          <!-- Título Principal -->
          <div class="cert-title-section">
            <h1 class="cert-main-title">CERTIFICADO DE EXCELÊNCIA</h1>
            <p class="cert-main-subtitle">GESTÃO FINANCEIRA, PRECIFICAÇÃO E FLUXO DE CAIXA PARA EMPRESAS</p>
          </div>

          <!-- Corpo do Certificado -->
          <div class="cert-body">
            <p class="cert-intro">Certificamos solenemente para os devidos fins de qualificação e governança corporativa que</p>
            <div class="cert-recipient-name" id="cert-display-name">Empresário(a) Estratégico(a)</div>
            <p class="cert-recipient-cpf" id="cert-display-cpf">Inscrito(a) sob o CPF/CNPJ nº 000.000.000-00</p>
            <p class="cert-statement">
              concluiu com êxito todas as etapas de avaliação, simulações táticas de decisão e estudos práticos do treinamento executivo de <strong>Gestão e Fluxo de Caixa para Pequenos Negócios</strong>, dominando separação patrimonial PF/PJ, conciliação diária, fluxo projetado a 90 dias, fórmula científica de precificação com margem de contribuição, DRE gerencial, curva ABC de clientes e recuperação ativa de recebíveis.
            </p>
          </div>

          <!-- Grade de Metadados Oficiais -->
          <div class="cert-meta-grid">
            <div class="cert-meta-item">
              <span class="cert-meta-label">CARGA HORÁRIA</span>
              <span class="cert-meta-value">06 Horas Práticas</span>
            </div>
            <div class="cert-meta-item">
              <span class="cert-meta-label">APROVEITAMENTO</span>
              <span class="cert-meta-value" id="cert-score-display">100% de Acerto nos Desafios</span>
            </div>
            <div class="cert-meta-item">
              <span class="cert-meta-label">DATA DE EMISSÃO</span>
              <span class="cert-meta-value" id="cert-issue-date">Novembro de 2026</span>
            </div>
            <div class="cert-meta-item">
              <span class="cert-meta-label">AUTENTICAÇÃO CRIPTOGRÁFICA</span>
              <span class="cert-meta-value cert-code" id="cert-auth-code">CASH-2026-X89-OFICIAL</span>
            </div>
          </div>

          <!-- Rodapé com Assinaturas e Selo Dólar Green -->
          <div class="cert-footer">
            <div class="cert-sign-col">
              <div class="cert-signature-line">
                <span class="cert-sign-cursive">Claudinei Lima</span>
              </div>
              <span class="cert-sign-role">Diretoria Executiva &amp; Controladoria</span>
              <span class="cert-sign-org">Cyber Executive Board</span>
            </div>

            <div class="cert-seal-col">
              <div class="cert-official-seal">
                <div class="cert-seal-inner">
                  <span class="cert-seal-star">★</span>
                  <span class="cert-seal-text">VERIFICADO</span>
                  <span class="cert-seal-year">2026</span>
                </div>
              </div>
            </div>

            <div class="cert-sign-col">
              <div class="cert-signature-line">
                <span class="cert-sign-cursive">Coordenação Fiscal</span>
              </div>
              <span class="cert-sign-role">Consultoria de Precificação &amp; PMEs</span>
              <span class="cert-sign-org">Divisão de Gestão Financeira</span>
            </div>
          </div>
        </div>
      </div>
    </section>'''

    return ""

def compile_index():
    print("Iniciando compilação de C:\\cash\\index.html...")
    slides_markup = "\n\n".join([generate_slide_html(s) for s in SLIDES_DATA])

    full_html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Gestão e Fluxo de Caixa para Empresas | Formação Executiva</title>
  
  <meta name="description" content="Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios. Domine o fluxo de caixa diário, DRE e precificação científica.">
  <meta name="keywords" content="gestão financeira, fluxo de caixa, precificação de produtos, pequenas empresas, controle financeiro, capital de giro, ponto de equilíbrio, MEI, PME">
  <meta name="author" content="Cyber Executive">
  <meta name="robots" content="index, follow">

  <!-- Favicon Padronizado Verde Dólar -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="imagens/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="imagens/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="imagens/apple-touch-icon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Gestão e Fluxo de Caixa para Empresas | Formação Executiva">
  <meta property="og:description" content="Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios com certificação formal.">
  <meta property="og:image" content="imagens/anuncio-hotmart-1x1.jpg">

  <link rel="stylesheet" href="css/styles.css?v=1.0">
</head>
<body>

  <!-- Top Progress Bar -->
  <div id="top-progress-bar" aria-hidden="true"></div>

  <!-- Top Header Flutuante -->
  <header class="top-header" role="banner">
    <div class="header-left">
      <img src="imagens/logo-cyber-executive.png" alt="Cyber Executive Logo" class="brand-logo" />
      <span class="header-course-title">CASH • GESTÃO E FLUXO DE CAIXA PARA EMPRESAS</span>
    </div>

    <div class="header-right">
      <!-- Status do Aluno / Acesso -->
      <div id="access-status-container">
        <button class="header-pill-badge" id="btn-header-unlock" title="Status de Acesso do Treinamento">
          <span class="badge-dot" id="access-badge-dot"></span>
          <span id="access-badge-text">⚡ Demonstração Gratuita</span>
          <span class="badge-action" id="badge-action-label">• 🔑 Já sou Aluno</span>
        </button>
      </div>

      <!-- Botão Página de Vendas (Landing Page) -->
      <a href="landing.html" class="header-btn" title="Página de Apresentação e Vendas (Landing Page)" style="text-decoration: none;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
        <span>Página de Vendas</span>
      </a>

      <!-- Botão Grade de Módulos (Drawer) -->
      <button class="header-btn" id="btn-modules" title="Abrir Trilha de Módulos e Aulas (M)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
        <span>Módulos</span>
      </button>

      <!-- Botão Visão Geral -->
      <button class="header-btn" id="btn-overview" title="Visão Geral dos Slides (G)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        <span>Visão Geral</span>
      </button>

      <!-- Botão Tema Claro/Escuro -->
      <button class="icon-btn" id="btn-theme" title="Alternar Modo de Contraste (T)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      </button>

      <!-- Botão Ajuda -->
      <button class="icon-btn" id="btn-help" title="Atalhos e Dicas (H ou ?)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      </button>

      <!-- Botão Tela Cheia -->
      <button class="icon-btn" id="btn-fullscreen" title="Alternar Tela Cheia (F)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
      </button>
    </div>
  </header>

  <!-- Viewport Principal da Apresentação -->
  <main id="presentation-viewport" role="main">
{slides_markup}
  </main>

  <!-- Dock de Navegação Inferior -->
  <nav class="bottom-dock" role="navigation" aria-label="Navegação do Curso">
    <button class="dock-arrow-btn" id="btn-prev" title="Slide Anterior (←)" aria-label="Slide Anterior">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
    </button>

    <div class="dock-counter">
      <span id="dock-current-num">01</span>
      <span class="dock-sep">/</span>
      <span id="dock-total-num">38</span>
    </div>

    <button class="dock-arrow-btn" id="btn-next" title="Próximo Slide (→)" aria-label="Próximo Slide">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
    </button>

    <div class="dock-dots-scroll-container" id="dock-dots-container"></div>
  </nav>

  <!-- Drawer Lateral de Módulos e Aulas -->
  <aside id="modules-drawer" class="modules-drawer" aria-hidden="true">
    <div class="drawer-header">
      <div class="drawer-header-title">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        <span>Trilha de Aprendizado</span>
      </div>
      <button class="drawer-close-btn" id="close-drawer-btn" title="Fechar Trilha (Esc)">✕</button>
    </div>

    <!-- Progresso Geral do Aluno -->
    <div class="drawer-progress-card">
      <div class="drawer-progress-header">
        <span class="drawer-progress-label">Seu Progresso no Treinamento</span>
        <strong class="drawer-progress-percent" id="drawer-progress-percent">0%</strong>
      </div>
      <div class="drawer-progress-track">
        <div class="drawer-progress-bar" id="drawer-progress-bar" style="width: 0%;"></div>
      </div>
    </div>

    <!-- Lista de Módulos Renderizada Dinamicamente -->
    <div class="drawer-modules-list" id="drawer-modules-container"></div>
  </aside>

  <!-- Modal Visão Geral de Slides -->
  <div class="modal-overlay" id="overview-modal" aria-hidden="true">
    <div class="overview-content">
      <div class="overview-header">
        <div class="overview-header-left">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          <h2 class="overview-title">Grade Completa de Slides</h2>
        </div>
        <button class="close-modal-btn" id="close-overview-btn" title="Fechar (Esc)">✕</button>
      </div>
      <div class="overview-grid" id="overview-grid"></div>
    </div>
  </div>

  <!-- Modal de Ajuda / Atalhos -->
  <div class="modal-overlay" id="help-modal" aria-hidden="true">
    <div class="overview-content help-content-container">
      <div class="overview-header">
        <div class="overview-header-left">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          <h2 class="overview-title">Atalhos de Teclado e Navegação</h2>
        </div>
        <button class="close-modal-btn" id="close-help-btn" title="Fechar (Esc)">✕</button>
      </div>
      <div class="shortcuts-grid">
        <div class="shortcut-item"><kbd>→</kbd> / <kbd>Espaço</kbd><span>Avançar para o próximo slide</span></div>
        <div class="shortcut-item"><kbd>←</kbd><span>Voltar para o slide anterior</span></div>
        <div class="shortcut-item"><kbd>F</kbd><span>Alternar visualização em Tela Cheia</span></div>
        <div class="shortcut-item"><kbd>M</kbd><span>Abrir Trilha de Módulos e Aulas</span></div>
        <div class="shortcut-item"><kbd>G</kbd><span>Abrir Visão Geral de Slides</span></div>
        <div class="shortcut-item"><kbd>T</kbd><span>Alternar modo de contraste</span></div>
        <div class="shortcut-item"><kbd>Esc</kbd><span>Fechar qualquer modal ativo</span></div>
        <div class="shortcut-item"><kbd>1</kbd> a <kbd>9</kbd><span>Navegar diretamente entre módulos</span></div>
      </div>
    </div>
  </div>

  <!-- Modal de Zoom de Card (~70% da Tela) -->
  <div class="card-modal-overlay" id="card-zoom-modal" aria-hidden="true">
    <div class="card-modal-container" id="card-zoom-container">
      <button class="card-modal-close" id="card-zoom-close-btn" title="Fechar (Esc)">✕</button>
      <div class="card-modal-body" id="card-zoom-content"></div>
    </div>
  </div>

  <!-- Modal de Zoom da Resposta do Quiz (Tela Cheia / ~70%) -->
  <div class="card-modal-overlay" id="quiz-feedback-zoom-modal" aria-hidden="true">
    <div class="card-modal-container theme-emerald" id="quiz-feedback-zoom-container">
      <button class="card-modal-close" id="quiz-feedback-zoom-close" title="Fechar (Esc)" onclick="window.PresentationApp.closeQuizFeedbackZoom()">✕</button>
      <div class="card-modal-body" id="quiz-feedback-zoom-content"></div>
    </div>
  </div>

  <!-- Modal de Paywall / Trava de Demonstração -->
  <div class="modal-overlay" id="paywall-modal" aria-hidden="true">
    <div class="overview-content paywall-card-container">
      <button class="close-modal-btn" id="close-paywall-btn" title="Fechar (Esc)">✕</button>
      
      <div class="paywall-header">
        <div class="paywall-badge">
          🔒 CONTEÚDO EXCLUSIVO PARA ALUNOS
        </div>
        <h2 class="paywall-title">Você Concluiu a <span class="highlight-cyan">Demonstração Gratuita</span>!</h2>
        <p class="paywall-subtitle">
          Parabéns por completar as aulas do <strong>Módulo 01 (O Coração Financeiro: Separação PF/PJ e Pró-Labore)</strong>. Para continuar sua formação prática e desbloquear todos os <strong>6 Módulos Completos (38 Slides)</strong> e o <strong>Certificado Oficial Executivo</strong>, garanta seu acesso com desconto especial de lançamento.
        </p>
      </div>

      <div class="paywall-benefits-list">
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">📈</div>
          <div>
            <strong>6 Módulos Completos sem Restrições (38 Aulas Práticas)</strong>
            <span>Separação PF/PJ, Fluxo de Caixa Diário e Projetado, Precificação com Margem Real, DRE Gerencial, Curva ABC e Combate à Inadimplência</span>
          </div>
        </div>
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">🎯</div>
          <div>
            <strong>6 Desafios Práticos da Vida Real com Tomada de Decisão</strong>
            <span>Simulações de cenários empresariais com pontuação individual e feedback estratégico imediato</span>
          </div>
        </div>
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">📜</div>
          <div>
            <strong>Certificado Oficial Executivo (6 Horas)</strong>
            <span>Personalizado com seu nome, CPF/CNPJ, código criptográfico CASH-2026 e assinaturas executivas</span>
          </div>
        </div>
      </div>

      <div class="paywall-action-box">
        <div class="paywall-price-info">
          <span class="paywall-price-label">ACESSO VITALÍCIO POR APENAS:</span>
          <div class="paywall-price-value">R$ 47<small>,00</small> <span class="paywall-price-sub">(ou 5x de R$ 10,25)</span></div>
        </div>
        <div class="paywall-dual-buttons">
          <a href="#" class="paywall-cta-btn paywall-btn-kiwify" id="btn-paywall-kiwify" target="_blank" rel="noopener" style="border-radius: 9999px !important;">
            PAGAR VIA KIWIFY
          </a>
          <a href="#" class="paywall-cta-btn paywall-btn-hotmart" id="btn-paywall-hotmart" target="_blank" rel="noopener" style="border-radius: 9999px !important;">
            PAGAR VIA HOTMART
          </a>
        </div>
      </div>

      <div class="paywall-footer-hint">
        <span>Já adquiriu o treinamento?</span>
        <button type="button" class="paywall-unlock-link" id="btn-paywall-enter-key">Inserir Chave de Acesso do Aluno</button>
      </div>
    </div>
  </div>

  <!-- Modal para Inserir Chave de Acesso -->
  <div class="modal-overlay" id="unlock-modal" aria-hidden="true">
    <div class="overview-content unlock-card-container">
      <button class="close-modal-btn" id="close-unlock-btn" title="Fechar (Esc)">✕</button>
      
      <div class="unlock-icon-circle">🔑</div>
      <h3 class="unlock-title">Ativação de Acesso do Aluno</h3>
      <p class="unlock-desc">Digite sua chave oficial de aluno para liberar todos os módulos:</p>
      
      <form id="form-unlock-key" onsubmit="return false;" class="unlock-form">
        <div class="unlock-input-wrap">
          <input type="text" id="input-unlock-key" class="unlock-input" placeholder="Ex: CASH-2026-ACESSO-FULL" autocomplete="off" spellcheck="false" autocapitalize="characters" />
          <button type="submit" class="action-pill primary" id="btn-submit-unlock">Ativar Acesso</button>
        </div>
        <div class="unlock-status-msg" id="unlock-status-msg"></div>
      </form>

      <p class="unlock-support-note">
        Dúvidas com o seu acesso? Verifique o e-mail cadastrado na compra ou fale com nosso suporte executivo.
      </p>
    </div>
  </div>

  <!-- Modal de Identificação Obrigatória do Aluno -->
  <div class="modal-overlay" id="student-id-modal" aria-hidden="true">
    <div class="overview-content student-id-card-container">
      <div class="student-id-icon-circle">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <h3 class="student-id-title">Identificação do Aluno</h3>
      <p class="student-id-desc">
        Informe seu <strong>Nome Completo</strong> e <strong>CPF ou CNPJ</strong> para personalizar seu Certificado Oficial Executivo e registrar seu progresso nas avaliações práticas.
      </p>

      <form id="form-student-id" onsubmit="event.preventDefault(); window.PresentationApp.submitStudentRegistration();" class="student-id-form">
        <div class="student-id-field">
          <label for="input-reg-name" class="student-id-label">Nome Completo (como constará no certificado):</label>
          <input type="text" id="input-reg-name" class="student-id-input" placeholder="Ex: Carlos Eduardo da Silva" required autocomplete="name" />
        </div>

        <div class="student-id-field">
          <label for="input-reg-cpf" class="student-id-label">CPF ou CNPJ (para autenticação de registro):</label>
          <input type="text" id="input-reg-cpf" class="student-id-input" placeholder="000.000.000-00" required maxlength="18" />
        </div>

        <div class="student-id-error-msg" id="student-id-error-msg"></div>

        <button type="submit" class="action-pill primary student-id-submit-btn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Confirmar Dados e Iniciar
        </button>
      </form>
    </div>
  </div>

  <!-- Toast Flutuante de Notificação -->
  <div id="course-toast" class="course-toast" aria-live="polite"></div>

  <script src="js/presentation.js?v=1.0"></script>
</body>
</html>'''

    output_path = r"C:\cash\index.html"
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(full_html)
    print(f"Sucesso! Gerado C:\\cash\\index.html com {len(SLIDES_DATA)} slides em {output_path}")

if __name__ == "__main__":
    compile_index()
