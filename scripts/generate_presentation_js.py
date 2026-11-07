# -*- coding: utf-8 -*-
import re

with open(r'C:\invest\js\presentation.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update header comment
header_old = """/**
 * Capacitação Executiva em Segurança da Informação e Conscientização Digital
 * Engine Interativa em JavaScript Puro
 */"""

header_new = """/**
 * Gestão e Fluxo de Caixa para Empresas
 * Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios.
 * Engine Interativa em JavaScript Puro
 */"""

code = code.replace(header_old, header_new)

# 2. Update modulesMeta
modules_meta_old = """  // Metadados dos 6 Módulos Práticos de Investimentos e Finanças
  const modulesMeta = [
    {
      "id": 1,
      "num": "01",
      "title": "Mentalidade Financeira & O Jogo do Dinheiro",
      "startSlide": 2,
      "endSlide": 7,
      "quizSlide": 7
    },
    {
      "id": 2,
      "num": "02",
      "title": "Orçamento sem Neura, Faxina & Reserva Anti-Crise",
      "startSlide": 8,
      "endSlide": 13,
      "quizSlide": 13
    },
    {
      "id": 3,
      "num": "03",
      "title": "Renda Fixa Inteligente & O Fim da Poupança",
      "startSlide": 14,
      "endSlide": 19,
      "quizSlide": 19
    },
    {
      "id": 4,
      "num": "04",
      "title": "Renda Variável: Ações de Valor, Dividendos & FIIs",
      "startSlide": 20,
      "endSlide": 25,
      "quizSlide": 25
    },
    {
      "id": 5,
      "num": "05",
      "title": "Criptoativos, Bitcoin & A Nova Fronteira Digital",
      "startSlide": 26,
      "endSlide": 31,
      "quizSlide": 31
    },
    {
      "id": 6,
      "num": "06",
      "title": "A Carteira Blindada, Rebalanceamento & Liberdade",
      "startSlide": 32,
      "endSlide": 37,
      "quizSlide": 37
    },
    {
      "id": 7,
      "num": "07",
      "title": "Dashboard Executivo & Certificação Oficial",
      "startSlide": 38,
      "endSlide": 38,
      "quizSlide": null
    }
  ];"""

modules_meta_new = """  // Metadados dos 6 Módulos Práticos de Gestão e Fluxo de Caixa para Empresas
  const modulesMeta = [
    {
      "id": 1,
      "num": "01",
      "title": "Separação PF/PJ & Pró-Labore Blindado",
      "startSlide": 2,
      "endSlide": 7,
      "quizSlide": 7
    },
    {
      "id": 2,
      "num": "02",
      "title": "Fluxo de Caixa Diário, Realizado e Projetado",
      "startSlide": 8,
      "endSlide": 13,
      "quizSlide": 13
    },
    {
      "id": 3,
      "num": "03",
      "title": "Precificação Estratégica & Margem Real",
      "startSlide": 14,
      "endSlide": 19,
      "quizSlide": 19
    },
    {
      "id": 4,
      "num": "04",
      "title": "DRE Gerencial, Ponto de Equilíbrio & Curva ABC",
      "startSlide": 20,
      "endSlide": 25,
      "quizSlide": 25
    },
    {
      "id": 5,
      "num": "05",
      "title": "Inadimplência, Crédito & Renegociação de Dívidas",
      "startSlide": 26,
      "endSlide": 31,
      "quizSlide": 31
    },
    {
      "id": 6,
      "num": "06",
      "title": "Orçamento Empresarial, Reinvestimento & Governança",
      "startSlide": 32,
      "endSlide": 37,
      "quizSlide": 37
    },
    {
      "id": 7,
      "num": "07",
      "title": "Dashboard Executivo & Certificação Oficial",
      "startSlide": 38,
      "endSlide": 38,
      "quizSlide": null
    }
  ];"""

code = code.replace(modules_meta_old, modules_meta_new)

# 3. Update state hashes and default student name
old_hashes = """    gestorAccessHashes: [
      'aede49990b5c69b2f43298921b966f8517753592f4227b91e2a4bb56ac030826',
      '5a4cde262de2aaf1f640c029c8508d817bf6188ab378daf0f0762c76864a474a'
    ],
    studentAccessHashes: [
      'ceada67ca7b75a2dc273acdf67ec3fb8063bf825af2eb99d5470e153ee68b835',
      'b6cfaa6b1c53f5fa921f0cfc85884c194a4d8e7c68d1722329ac531296a16174',
      'b45bb7a77108d5efc5d1695c42a25657dae7cfa58ab7b813543db9cd78174c6b',
      '0a529938776fb481b1e03d0a9264f8dfcf1665e4411895dd9bab2733901e65e3',
      'd9423d735a0f4b6e2baef9dc4fd4880be281e7237aff040c6e29ba739adb2288',
      'e809b9b295658316c1c9ff27b3063dded4cc34f7d3f4ed9d2c5337024d50c8da'
    ],"""

new_hashes = """    gestorAccessHashes: [
      'e273fe31900138572a84ccb206c0a63b22940b1809723e0f4a0d2f81c3802104',
      '10105dd84c40061d4ad4319aa2d7e236390fbd9e3c9e11c384e8e266a44694ea'
    ],
    studentAccessHashes: [
      'd77907c6bc72c46e73bad3d15be7674da557caf50cc48bc9e1ae9301f8966fdc',
      '101e639d9c0e8e096259ead9b683154bf34594fd71b45db89bb751614f9da5ee',
      '80f751cec14dd8973819bb1de7c6b7fd97030f04b86b863cf9892deb268e3ea5',
      '4138a9fe0a34d26f027d186f40cf45c85157680283b75055f12d3e7b3df4103f',
      'cb122134e03d56736b2a4649ac40c2e0012b215aeed81db60a807dc3442a33de',
      '509260e575dfa0d4669b110343939cc498c5d5adbd28a05c3d9006853327da8b'
    ],"""

code = code.replace(old_hashes, new_hashes)

# 4. Replace student name default
code = code.replace("studentName: 'Investidor(a) Estratégico(a)'", "studentName: 'Empresário(a) Estratégico(a)'")
code = code.replace("'Investidor(a) Estratégico(a)'", "'Empresário(a) Estratégico(a)'")

# 5. Replace localStorage keys
code = code.replace("'invest_quizzes'", "'cash_quizzes'")
code = code.replace("'invest_student_registered'", "'cash_student_registered'")
code = code.replace("'invest_student_name'", "'cash_student_name'")
code = code.replace("'invest_student_cpf'", "'cash_student_cpf'")
code = code.replace("'invest_cert_issued'", "'cash_cert_issued'")
code = code.replace("'invest_cert_first_date'", "'cash_cert_first_date'")
code = code.replace("'invest_course_unlocked'", "'cash_course_unlocked'")
code = code.replace("'invest_user_role'", "'cash_user_role'")

# 6. Replace auth code generator seed & prefix
code = code.replace("INVEST-FIN-2026-AUTH", "CASH-GEST-2026-AUTH")
code = code.replace("`INV-2026-${hash.slice(0, 4)}-${hash.slice(4, 8)}`", "`CSH-2026-${hash.slice(0, 4)}-${hash.slice(4, 8)}`")

# 7. Replace theme classes in modals
code = code.replace("dom.cardZoomContainer.className = 'card-modal-container theme-cyan';", "dom.cardZoomContainer.className = 'card-modal-container theme-emerald';")
code = code.replace('<div class="zoomed-icon cyan"', '<div class="zoomed-icon emerald"')

# 8. Replace access badge text in demo mode
code = code.replace("'🔒 Acesso Gratuito • Módulos 1 e 2'", "'🔒 Acesso Gratuito • Módulo 01'")
code = code.replace("'Modo Demo (Módulos 1-2). Clique para inserir chave de acesso ou senha de gestor'", "'Modo Demo (Módulo 01). Clique para inserir chave de acesso ou senha de gestor'")

# 9. Write to C:\cash\js\presentation.js
with open(r'C:\cash\js\presentation.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Gerado C:\\cash\\js\\presentation.js com sucesso!")

