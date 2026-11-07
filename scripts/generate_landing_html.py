# -*- coding: utf-8 -*-
import os

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gestão e Fluxo de Caixa para Empresas | Formação Executiva Prática 2026</title>
  <meta name="description" content="Gestão e Fluxo de Caixa para Empresas: Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios. 6 módulos, 6 desafios da vida real e Certificado Executivo.">
  <meta name="keywords" content="fluxo de caixa, gestao financeira empresas, precificacao produtos, controle financeiro pme, margem de contribuicao, dre gerencial, capital de giro, pro labore">
  <meta name="author" content="Claudinei Gonçalves de Lima | Cyber Executive">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#040907">

  <!-- Favicon e Ícones Oficiais -->
  <link rel="icon" type="image/svg+xml" href="imagens/logo-cyber-executive.svg?v=1.0">
  <link rel="icon" type="image/png" sizes="32x32" href="imagens/favicon-32x32.png?v=1.0">
  <link rel="icon" type="image/png" sizes="16x16" href="imagens/favicon-16x16.png?v=1.0">
  <link rel="shortcut icon" href="favicon.ico?v=1.0">
  <link rel="apple-touch-icon" sizes="180x180" href="imagens/apple-touch-icon.png?v=1.0">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://cyberexecutive.github.io/cash/landing.html">

  <!-- Open Graph / Facebook / WhatsApp / LinkedIn -->
  <meta property="og:site_name" content="Cash Flow Pro 2026">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://cyberexecutive.github.io/cash/landing.html">
  <meta property="og:title" content="Gestão e Fluxo de Caixa para Empresas | Formação Prática">
  <meta property="og:description" content="Treinamento prático ensinando precificação de produtos e controle financeiro de pequenos negócios. 6 módulos, 6 desafios reais e Certificado Oficial.">
  <meta property="og:image" content="https://cyberexecutive.github.io/cash/imagens/anuncio-hotmart-1x1.jpg">
  <meta property="og:image:alt" content="Gestão e Fluxo de Caixa para Empresas - Formação 2026">
  <meta property="og:locale" content="pt_BR">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Gestão e Fluxo de Caixa para Empresas | Formação 2026">
  <meta name="twitter:description" content="Domine seu fluxo de caixa diário, pare de misturar despesas pessoais com o caixa da empresa, precifique com margem real e construa reservas de sobrevivência.">
  <meta name="twitter:image" content="https://cyberexecutive.github.io/cash/imagens/anuncio-hotmart-1x1.jpg">

  <!-- Estilos e Fontes -->
  <link rel="stylesheet" href="css/landing.css?v=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">

  <!-- Dados Estruturados Schema.org (JSON-LD) para Google Search -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Course",
        "@id": "https://cyberexecutive.github.io/cash/landing.html#course",
        "name": "Gestão e Fluxo de Caixa para Empresas",
        "description": "Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios: Separação PF/PJ, Fluxo de Caixa Diário e Projetado, Precificação e Margem Real, DRE Gerencial, Gestão de Inadimplência e Governança Financeira.",
        "provider": {
          "@type": "Organization",
          "name": "Cyber Executive",
          "url": "https://cyberexecutive.github.io/cash/"
        },
        "educationalCredentialAwarded": "Certificado Executivo em Gestão Financeira Empresarial & Fluxo de Caixa (6 Horas)",
        "inLanguage": "pt-BR",
        "hasCourseInstance": {
          "@type": "CourseInstance",
          "courseMode": "online",
          "courseWorkload": "PT6H"
        },
        "offers": [
          {
            "@type": "Offer",
            "name": "Acesso Completo Individual",
            "price": "47.00",
            "priceCurrency": "BRL",
            "availability": "https://schema.org/InStock",
            "url": "https://pay.kiwify.com.br/",
            "category": "Kiwify Checkout"
          },
          {
            "@type": "Offer",
            "name": "Acesso Completo Individual",
            "price": "47.00",
            "priceCurrency": "BRL",
            "availability": "https://schema.org/InStock",
            "url": "https://pay.hotmart.com/",
            "category": "Hotmart Checkout"
          }
        ]
      },
      {
        "@type": "FAQPage",
        "@id": "https://cyberexecutive.github.io/cash/landing.html#faq",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Como recebo o acesso ao treinamento após a compra?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "O acesso é liberado instantaneamente! Assim que o seu pagamento (PIX ou cartão) for aprovado pela Kiwify ou Hotmart, você recebe a chave de acesso e o link direto para navegar pelo computador, tablet ou celular."
            }
          },
          {
            "@type": "Question",
            "name": "Para quem é indicado este treinamento?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Para donos de micro e pequenas empresas, MEIs, profissionais liberais, gestores e autônomos que desejam organizar o caixa, eliminar o estresse de pagar contas no susto e precificar seus produtos com margem garantida de lucro."
            }
          },
          {
            "@type": "Question",
            "name": "O certificado tem validade formal?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sim! O certificado é emitido com carga horária de 6 horas, data de conclusão, código criptográfico individual CSH-2026 e assinatura executiva formal do CEO Claudinei Gonçalves de Lima."
            }
          },
          {
            "@type": "Question",
            "name": "Preciso ter conhecimento prévio em contabilidade ou matemática financeira?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Não! O treinamento foi estruturado com linguagem direta, visual intuitivo e focado na rotina diária real de quem toca um negócio, sem jargões contábeis complexos ou fórmulas complicadas."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>

  <!-- ==========================================
       BARRA DE NAVEGAÇÃO
       ========================================== -->
  <header class="lp-header">
    <div class="lp-container lp-header-inner">
      <a href="index.html" class="lp-logo">
        <img src="imagens/logo-cyber-executive.svg" alt="Cyber Executive Logo" width="36" height="36" class="lp-logo-img">
        <span class="lp-logo-text">CASH <span>FLOW</span> 2026</span>
      </a>

      <nav class="lp-nav">
        <a href="#diferenciais" class="lp-nav-link">Metodologia</a>
        <a href="#modulos" class="lp-nav-link">Conteúdo (6 Módulos)</a>
        <a href="#certificado" class="lp-nav-link">Certificado</a>
        <a href="#faq" class="lp-nav-link">Dúvidas</a>
      </nav>

      <div class="lp-header-actions">
        <a href="index.html" class="lp-btn lp-btn-secondary" title="Experimente o Módulo 01 gratuitamente">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          Demonstração
        </a>
        <a href="#inscricao" class="lp-btn lp-btn-primary">
          Garantir Vaga
        </a>
      </div>
    </div>
  </header>

  <!-- ==========================================
       HERO SECTION
       ========================================== -->
  <section class="lp-hero">
    <div class="lp-container lp-hero-grid">
      <div class="lp-hero-content">
        <div class="lp-badge">
          <span class="lp-badge-dot"></span>
          FORMAÇÃO PRÁTICA EXECUTIVA 2026
        </div>

        <h1 class="lp-hero-title">
          Gestão e Fluxo de Caixa para Empresas
        </h1>

        <p class="lp-hero-subtitle">
          Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios. Sem planilhas confusas, sem vídeos monótonos e com foco em lucro real e liquidez imediata.
        </p>

        <ul class="lp-hero-bullets">
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span><strong>Separação PF/PJ:</strong> Fim definitivo da confusão entre bolso do sócio e caixa da empresa</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span><strong>Precificação Científica:</strong> Aprenda a calcular margem de contribuição e ponto de equilíbrio real</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span><strong>6 Casos da Vida Real:</strong> Desafios interativos simulando crises, clientes inadimplentes e estoque</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span><strong>Certificado Executivo Oficial:</strong> Reconhecimento formal de 6 Horas com código criptográfico</span>
          </li>
        </ul>

        <div class="lp-hero-ctas">
          <a href="#inscricao" class="lp-btn lp-btn-primary lp-btn-lg">
            Garantir Minha Vaga por R$ 47,00
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="index.html" class="lp-btn lp-btn-outline lp-btn-lg">
            Acessar Demonstração Gratuita
          </a>
        </div>

        <div class="lp-hero-trust">
          <div class="lp-trust-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Acesso Imediato e Vitalício</span>
          </div>
          <div class="lp-trust-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            <span>Microlearning Dinâmico (6 Horas)</span>
          </div>
          <div class="lp-trust-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>Pagamento 100% Seguro</span>
          </div>
        </div>
      </div>

      <div class="lp-hero-visual">
        <div class="lp-visual-card">
          <img src="imagens/anuncio-hotmart-1x1.jpg" alt="Gestão e Fluxo de Caixa para Empresas" class="lp-cover-img" width="560" height="560">
          <div class="lp-visual-tag">
            <span class="lp-tag-pulse"></span>
            Metodologia Ativa • Simulação Prática
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       DIFERENCIAIS / METODOLOGIA
       ========================================== -->
  <section id="diferenciais" class="lp-section lp-section-alt">
    <div class="lp-container">
      <div class="lp-section-header">
        <span class="lp-section-tag">POR QUE É DIFERENTE?</span>
        <h2 class="lp-section-title">Chega de Aulas Gravadas de 40 Horas Que Você Nunca Termina</h2>
        <p class="lp-section-desc">Criamos um treinamento direto ao ponto, desenhado para a rotina corrida de donos e gestores de pequenas empresas.</p>
      </div>

      <div class="lp-cards-grid">
        <div class="lp-card">
          <div class="lp-card-icon emerald">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <h3 class="lp-card-title">Microlearning Executivo</h3>
          <p class="lp-card-desc">Cada slide entrega um conceito essencial e aplicável em menos de 2 minutos. Aprenda no seu ritmo, no computador ou no celular.</p>
        </div>

        <div class="lp-card">
          <div class="lp-card-icon emerald">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </div>
          <h3 class="lp-card-title">Tomada de Decisão Real</h3>
          <p class="lp-card-desc">Ao final de cada módulo, enfrente um cenário real da sua rotina: cliente inadimplente pedindo mais prazo, fornecedor aumentando preço e cálculo de margem.</p>
        </div>

        <div class="lp-card">
          <div class="lp-card-icon emerald">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 class="lp-card-title">Precificação Sem Mistérios</h3>
          <p class="lp-card-desc">Pare de 'chutar' preços copiando concorrentes ou somando percentuais aleatórios. Domine o Markup, Margem de Contribuição e Ponto de Equilíbrio.</p>
        </div>

        <div class="lp-card">
          <div class="lp-card-icon emerald">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 class="lp-card-title">Reserva de Sobrevivência</h3>
          <p class="lp-card-desc">Construa o colchão financeiro da pessoa jurídica para suportar meses de baixa temporada ou crises sem depender de cheque especial bancário.</p>
        </div>

        <div class="lp-card">
          <div class="lp-card-icon emerald">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          </div>
          <h3 class="lp-card-title">DRE Gerencial Descomplicada</h3>
          <p class="lp-card-desc">Entenda se a sua empresa dá lucro ou prejuízo de verdade no mês, sem precisar esperar o fechamento contábil formal de fim de ano.</p>
        </div>

        <div class="lp-card">
          <div class="lp-card-icon emerald">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 12l-4-4-4 4M12 16V8"/></svg>
          </div>
          <h3 class="lp-card-title">Controle Diário em 15 Minutos</h3>
          <p class="lp-card-desc">Rotina prática para registrar entradas, saídas e conciliação bancária diária, mantendo o controle total da empresa sem burocracia excessiva.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       CONTEÚDO PROGRAMÁTICO (6 MÓDULOS)
       ========================================== -->
  <section id="modulos" class="lp-section">
    <div class="lp-container">
      <div class="lp-section-header">
        <span class="lp-section-tag">GRADE EXECUTIVA</span>
        <h2 class="lp-section-title">O Que Você Vai Aprender (Passo a Passo)</h2>
        <p class="lp-section-desc">38 slides interativos organizados em 6 módulos lógicos, do diagnóstico do caixa à governança financeira.</p>
      </div>

      <div class="lp-modules-list">
        <!-- Módulo 01 -->
        <div class="lp-module-item">
          <div class="lp-mod-num">01</div>
          <div class="lp-mod-body">
            <div class="lp-mod-header">
              <h3 class="lp-mod-title">Separação PF/PJ & Pró-Labore Blindado</h3>
              <span class="lp-mod-badge demo">Módulo Aberto na Demonstração</span>
            </div>
            <p class="lp-mod-desc">O pecado capital que mata 70% dos pequenos negócios. Como definir um Pró-labore fixo e sustentável, separar contas bancárias, cartões corporativos e organizar a rotina de retiradas.</p>
            <div class="lp-mod-quiz-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Desafio Prático 01: O boleto da escola no cartão corporativo da PJ
            </div>
          </div>
        </div>

        <!-- Módulo 02 -->
        <div class="lp-module-item">
          <div class="lp-mod-num">02</div>
          <div class="lp-mod-body">
            <div class="lp-mod-header">
              <h3 class="lp-mod-title">Fluxo de Caixa Diário, Realizado e Projetado</h3>
              <span class="lp-mod-badge locked">Acesso Completo</span>
            </div>
            <p class="lp-mod-desc">A diferença entre 'ter dinheiro na conta' e 'ter lucro'. Como controlar entradas e saídas diárias, projetar os próximos 30, 60 e 90 dias e nunca mais ser pego de surpresa na folha de pagamento.</p>
            <div class="lp-mod-quiz-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Desafio Prático 02: Grande contrato fechado, mas o recebimento só cai em 60 dias
            </div>
          </div>
        </div>

        <!-- Módulo 03 -->
        <div class="lp-module-item">
          <div class="lp-mod-num">03</div>
          <div class="lp-mod-body">
            <div class="lp-mod-header">
              <h3 class="lp-mod-title">Precificação Estratégica & Margem Real</h3>
              <span class="lp-mod-badge locked">Acesso Completo</span>
            </div>
            <p class="lp-mod-desc">Como calcular custos diretos, despesas fixas proporcionais, impostos, taxas de maquininha de cartão e margem líquida real. Aprenda quando dar desconto e quando recusar clientes que geram prejuízo.</p>
            <div class="lp-mod-quiz-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Desafio Prático 03: Cliente pede 20% de desconto para fechar lote no PIX
            </div>
          </div>
        </div>

        <!-- Módulo 04 -->
        <div class="lp-module-item">
          <div class="lp-mod-num">04</div>
          <div class="lp-mod-body">
            <div class="lp-mod-header">
              <h3 class="lp-mod-title">DRE Gerencial, Ponto de Equilíbrio & Curva ABC</h3>
              <span class="lp-mod-badge locked">Acesso Completo</span>
            </div>
            <p class="lp-mod-desc">O painel de bordo da sua empresa. Como montar uma Demonstração do Resultado do Exercício simplificada, calcular exatamente quanto precisa faturar por dia para pagar as contas e focar nos produtos mais rentáveis (Curva ABC).</p>
            <div class="lp-mod-quiz-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Desafio Prático 04: Faturamento recorde no mês, mas o saldo bancário está zerado
            </div>
          </div>
        </div>

        <!-- Módulo 05 -->
        <div class="lp-module-item">
          <div class="lp-mod-num">05</div>
          <div class="lp-mod-body">
            <div class="lp-mod-header">
              <h3 class="lp-mod-title">Inadimplência, Crédito & Renegociação de Dívidas</h3>
              <span class="lp-mod-badge locked">Acesso Completo</span>
            </div>
            <p class="lp-mod-desc">Como cobrar clientes de forma profissional e sem perder o relacionamento. Gestão de risco de crédito, políticas de prazos e como renegociar dívidas bancárias ou fornecedores sem juros abusivos.</p>
            <div class="lp-mod-quiz-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Desafio Prático 05: Cliente principal atrasa 45 dias e pede novo fornecimento
            </div>
          </div>
        </div>

        <!-- Módulo 06 -->
        <div class="lp-module-item">
          <div class="lp-mod-num">06</div>
          <div class="lp-mod-body">
            <div class="lp-mod-header">
              <h3 class="lp-mod-title">Orçamento Empresarial, Reinvestimento & Governança</h3>
              <span class="lp-mod-badge locked">Acesso Completo</span>
            </div>
            <p class="lp-mod-desc">O plano de voo anual do negócio. Como reinvestir o lucro de forma inteligente (máquinas, marketing, pessoas), política de distribuição de dividendos e estruturação da governança para crescer com segurança.</p>
            <div class="lp-mod-quiz-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              Desafio Prático 06: Lucro acumulado no semestre: comprar carro novo ou reinvestir na operação?
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       CERTIFICAÇÃO OFICIAL
       ========================================== -->
  <section id="certificado" class="lp-section lp-section-alt">
    <div class="lp-container lp-cert-grid">
      <div class="lp-cert-content">
        <span class="lp-section-tag">RECONHECIMENTO FORMAL</span>
        <h2 class="lp-section-title">Certificado Executivo Oficial (6 Horas)</h2>
        <p class="lp-section-desc">Ao concluir as 38 aulas práticas e acertar os 6 desafios de decisão da vida real, você emite instantaneamente o seu Certificado Executivo Oficial em PDF de alta resolução.</p>

        <ul class="lp-cert-features">
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Personalizado com seu <strong>Nome Completo</strong> e <strong>CPF</strong></span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Código Criptográfico Individual de Autenticidade (CSH-2026)</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Assinatura formal do CEO Claudinei Gonçalves de Lima</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Pronto para impressão em alta resolução ou anexo em currículos e LinkedIn</span>
          </li>
        </ul>

        <div style="margin-top: 24px;">
          <a href="#inscricao" class="lp-btn lp-btn-primary">
            Quero Minha Certificação Oficial
          </a>
        </div>
      </div>

      <div class="lp-cert-preview">
        <div class="lp-cert-frame">
          <div class="lp-cert-badge-floating">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Validação Criptográfica CSH-2026</span>
          </div>
          <div class="lp-cert-mockup">
            <div class="lp-cert-mock-top">
              <img src="imagens/logo-cyber-executive.svg" alt="Cyber Executive" width="48" height="48">
              <div class="lp-cert-mock-inst">CYBER EXECUTIVE • FORMAÇÃO CORPORATIVA</div>
              <div class="lp-cert-mock-title">CERTIFICADO DE FORMAÇÃO EXECUTIVA</div>
            </div>
            <div class="lp-cert-mock-body">
              <div class="lp-cert-mock-lead">Certificamos com distinção que</div>
              <div class="lp-cert-mock-name">SEU NOME COMPLETO AQUI</div>
              <div class="lp-cert-mock-desc">concluiu com êxito o treinamento prático avançado em <strong>Gestão e Fluxo de Caixa para Empresas: Precificação e Controle Financeiro</strong>, demonstrando proficiência analítica em planejamento de fluxo de caixa diário e projetado, precificação estratégica com margem real, DRE gerencial e governança de liquidez.</div>
            </div>
            <div class="lp-cert-mock-footer">
              <div>Carga Horária: 6 Horas</div>
              <div>CSH-2026-AUTH-VALID</div>
              <div>Cyber Executive Academy</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       CARD DE OFERTA / INSCRIÇÃO
       ========================================== -->
  <section id="inscricao" class="lp-section">
    <div class="lp-container">
      <div class="lp-section-header">
        <span class="lp-section-tag">INVESTIMENTO ESTRATÉGICO</span>
        <h2 class="lp-section-title">Assuma o Controle do Caixa da Sua Empresa Hoje</h2>
        <p class="lp-section-desc">Uma única decisão errada de precificação ou um mês no cheque especial custa 20 vezes mais do que este treinamento.</p>
      </div>

      <div class="lp-pricing-wrapper">
        <div class="lp-pricing-card featured">
          <div class="lp-pricing-ribbon">MELHOR CUSTO-BENEFÍCIO</div>

          <h3 class="lp-pricing-title">Acesso Completo Individual</h3>
          <p class="lp-pricing-subtitle">Acesso vitalício para quem deseja blindar a saúde financeira da empresa e construir um negócio rentável.</p>

          <div class="lp-pricing-price-box">
            <div class="lp-pricing-old">De R$ 197,00</div>
            <div class="lp-pricing-current">
              <span class="curr">R$</span>
              <span class="val">47</span>
              <span class="cents">,00</span>
            </div>
            <div class="lp-pricing-installments">ou 5x de R$ 10,25 no cartão de crédito / PIX</div>
          </div>

          <ul class="lp-pricing-features">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Acesso vitalício aos <strong>6 Módulos (38 Slides)</strong></span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>6 Casos Práticos</strong> com tomada de decisão da vida real</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Certificado Executivo Oficial</strong> em PDF (com Nome e CPF)</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Compatível com celular, tablet e computador</span>
            </li>
          </ul>

          <div class="lp-checkout-options">
            <a href="#" id="btn-checkout-kiwify" class="lp-btn lp-btn-kiwify lp-btn-block">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              PAGAR VIA KIWIFY
            </a>
            <a href="#" id="btn-checkout-hotmart" class="lp-btn lp-btn-hotmart lp-btn-block">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
              PAGAR VIA HOTMART
            </a>
          </div>

          <div class="lp-guarantee-note">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Pagamento 100% Seguro (PIX, Cartão ou Boleto)</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       PERGUNTAS FREQUENTES (FAQ)
       ========================================== -->
  <section id="faq" class="lp-section lp-section-alt">
    <div class="lp-container">
      <div class="lp-section-header">
        <span class="lp-section-tag">TIRE SUAS DÚVIDAS</span>
        <h2 class="lp-section-title">Perguntas Frequentes</h2>
        <p class="lp-section-desc">Tudo o que você precisa saber antes de iniciar sua capacitação executiva.</p>
      </div>

      <div class="lp-faq-container">
        <div class="lp-faq-item">
          <button class="lp-faq-question">
            <span>Como recebo o acesso ao treinamento após a compra?</span>
            <svg class="lp-faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="lp-faq-answer">
            <p>O acesso é liberado instantaneamente! Assim que o seu pagamento (PIX ou cartão) for aprovado, você recebe um e-mail com a chave de acesso e o link direto para navegar pelo computador, tablet ou celular.</p>
          </div>
        </div>

        <div class="lp-faq-item">
          <button class="lp-faq-question">
            <span>Para quem este treinamento é indicado?</span>
            <svg class="lp-faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="lp-faq-answer">
            <p>Para donos de micro e pequenas empresas, prestadores de serviços, comerciantes, MEIs, empreendedores individuais e gestores que precisam organizar a rotina financeira do negócio e ter clareza total sobre lucros e fluxo de caixa.</p>
          </div>
        </div>

        <div class="lp-faq-item">
          <button class="lp-faq-question">
            <span>O certificado tem validade formal?</span>
            <svg class="lp-faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="lp-faq-answer">
            <p>Sim! O certificado é emitido com carga horária de 6 horas, data de conclusão, código criptográfico individual CSH-2026 e assinatura executiva formal do CEO Claudinei Gonçalves de Lima, comprovando sua capacitação prática em gestão financeira.</p>
          </div>
        </div>

        <div class="lp-faq-item">
          <button class="lp-faq-question">
            <span>Preciso de planilhas complexas ou programas caros de gestão?</span>
            <svg class="lp-faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="lp-faq-answer">
            <p>Não! Ensinamos uma rotina limpa de 15 minutos diários que pode ser aplicada em um simples caderno de caixa, planilha básica do Google Sheets ou qualquer ERP simples que você já utilize.</p>
          </div>
        </div>

        <div class="lp-faq-item">
          <button class="lp-faq-question">
            <span>Em quanto tempo consigo concluir o curso?</span>
            <svg class="lp-faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="lp-faq-answer">
            <p>O formato é de microlearning dinâmico e interativo. A maioria dos participantes conclui todas as lições práticas e os 6 quizzes em cerca de 4 a 6 horas de estudo focado, avançando no seu próprio ritmo.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       RODAPÉ
       ========================================== -->
  <footer class="lp-footer">
    <div class="lp-container">
      <div class="lp-footer-links">
        <a href="#modulos">Conteúdo</a>
        <a href="#certificado">Certificação</a>
        <a href="#inscricao">Inscrição</a>
        <a href="index.html">Demonstração Interativa</a>
      </div>
      <p>© 2026 CASH FLOW PRO • Gestão e Fluxo de Caixa para Empresas.</p>
      <p style="margin-top: 6px; font-size: 0.8rem;">Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios.</p>
    </div>
  </footer>

  <script src="js/landing.js?v=1.0"></script>
</body>
</html>
"""

with open(r'C:\cash\landing.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Gerado C:\\cash\\landing.html com sucesso!")

