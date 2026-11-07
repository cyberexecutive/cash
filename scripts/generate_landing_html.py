# -*- coding: utf-8 -*-
"""
Gerador de landing.html para 'Gestão e Fluxo de Caixa para Empresas'
Baseado na estrutura 100% responsiva e de alta conversão de C:\invest\landing.html.
"""

with open(r'C:\invest\landing.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Substituições de metadados e títulos
replacements = [
    # Metas e Head
    ("Como Investir e Gerenciar o Seu Dinheiro | Formação Executiva Prática 2026",
     "Gestão e Fluxo de Caixa para Empresas | Formação Executiva Prática 2026"),
    ("Como Investir e Gerenciar o Seu Dinheiro. Formação 100% interativa com 6 módulos práticos, 6 desafios com tomada de decisão da vida real, renda fixa, ações, FIIs, criptoativos e certificação oficial em PDF.",
     "Gestão e Fluxo de Caixa para Empresas: Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios. 6 módulos, 6 desafios reais e Certificado Oficial."),
    ("como investir e gerenciar dinheiro, finanças pessoais, renda fixa, tesouro direto, ações dividendos, fundos imobiliários fiis, bitcoin criptoativos, orçamento 50 30 20",
     "fluxo de caixa, gestao financeira empresas, precificacao produtos, controle financeiro pme, margem de contribuicao, dre gerencial, capital de giro, pro labore"),
    ("#090d16", "#040907"),
    ("https://cyberexecutive.github.io/invest/landing.html", "https://cyberexecutive.github.io/cash/landing.html"),
    ("https://cyberexecutive.github.io/invest/", "https://cyberexecutive.github.io/cash/"),
    ("Invest Pro 2026", "Cash Flow Pro 2026"),
    ("Como Investir e Gerenciar o Seu Dinheiro | Formação Prática", "Gestão e Fluxo de Caixa para Empresas | Formação Prática"),
    ("Treinamento 100% interativo, prático e sem vídeos monótonos. 6 módulos, 6 desafios da vida real com tomada de decisão e Certificado Executivo Oficial.",
     "Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios. 6 módulos, 6 desafios reais e Certificado Oficial."),
    ("https://cyberexecutive.github.io/invest/imagens/anuncio-hotmart-1x1.jpg", "https://cyberexecutive.github.io/cash/imagens/anuncio-hotmart-1x1.jpg"),
    ("Como Investir e Gerenciar o Seu Dinheiro - Formação 2026", "Gestão e Fluxo de Caixa para Empresas - Formação 2026"),
    ("Como Investir e Gerenciar o Seu Dinheiro | Invest Pro 2026", "Gestão e Fluxo de Caixa para Empresas | Cash Flow Pro 2026"),
    ("Domine seu orçamento, saia das armadilhas dos grandes bancos, bata a inflação com Renda Fixa e monte uma carteira blindada global e cripto.",
     "Domine seu fluxo diário, precifique com margem real, separe de vez o dinheiro pessoal do caixa da empresa e construa um negócio rentável."),

    # Schema JSON-LD
    ('"name": "Como Investir e Gerenciar o Seu Dinheiro"', '"name": "Gestão e Fluxo de Caixa para Empresas"'),
    ("Formação executiva e individual em finanças pessoais e investimentos: Mentalidade Financeira, Orçamento sem Neura, Faxina de Dívidas, Renda Fixa Inteligente, Ações de Valor, Fundos Imobiliários (FIIs), Criptoativos e Carteira Blindada Global.",
     "Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios: Separação PF/PJ, Fluxo de Caixa Diário e Projetado, Precificação e Margem Real, DRE Gerencial, Gestão de Inadimplência e Governança Financeira."),
    ("Certificado de Formação Executiva em Gestão Financeira & Investimentos Estratégicos (6 Horas)",
     "Certificado Executivo em Gestão Financeira Empresarial & Fluxo de Caixa (6 Horas)"),

    # Header Navbar
    ("INVEST <span class=\"lp-text-gradient-cyan\">PRO 2026</span>",
     "CASH <span class=\"lp-text-gradient-cyan\">FLOW 2026</span>"),

    # Hero
    ("📈 FORMAÇÃO PRÁTICA 2026 • DO ZERO AO AVANÇADO",
     "📈 FORMAÇÃO PRÁTICA 2026 • GESTÃO EMPRESARIAL"),
    ("Como Investir e Gerenciar <span class=\"lp-text-gradient-cyan\">o Seu Dinheiro</span> sem Complicação",
     "Gestão e Fluxo de Caixa <span class=\"lp-text-gradient-cyan\">para Empresas</span>"),
    ("Um treinamento <strong>100% interativo, prático e sem vídeos cansativos</strong>. Domine seu orçamento, saia das armadilhas dos grandes bancos, bata a inflação com Renda Fixa Inteligente, lucre com Ações e FIIs, proteja seu patrimônio com Criptoativos e receba seu <strong>Certificado Oficial Executivo</strong>.",
     "Treinamentos práticos ensinando <strong>precificação de produtos e controle financeiro de pequenos negócios</strong>. Sem planilhas confusas, sem vídeos monótonos e com foco em lucro real, margem de contribuição e liquidez imediata."),
    ("6 Quizzes da Vida Real", "6 Casos Práticos Reais"),
    ("imagens/quiz-preview.jpg", "imagens/anuncio-hotmart-1x1.jpg"),

    # Seção Impacto / Estatísticas
    ("Não é o Quanto Você Ganha, <span class=\"lp-text-gradient-gold\">é o Quanto Você Constrói</span>",
     "Não é o Quanto Você Fatura, <span class=\"lp-text-gradient-gold\">é o Lucro Real no Caixa</span>"),
    ("A grande maioria das pessoas trabalha 40 horas por semana durante décadas, mas nunca aprendeu a alocar e proteger seu capital. Os números mostram a urgência de agir:",
     "Mais de 70% das micro e pequenas empresas fecham as portas antes de 5 anos por falta de fluxo de caixa e precificação errada. A boa gestão muda essa história:"),
    ("78%", "70%"),
    ("Das Famílias Endividadas", "Das PMEs Fecham por Falta de Caixa"),
    ("No Brasil vivem sufocadas por juros abusivos de cartão e cheque especial.", "Não por falta de vendas, mas por descontrole do fluxo e confusão PF/PJ."),
    ("R$ 1 Milhão", "15 Minutos"),
    ("Patrimônio com R$ 500/mês", "Rotina Diária de Conciliação"),
    ("Investidos com consistência a 12% ao ano chegam a mais de R$ 1.000.000 em 25 anos.", "O tempo necessário por dia para registrar entradas, saídas e nunca ser pego de surpresa."),
    ("15 Min", "+35%"),
    ("Rebalanceamento Mensal", "Margem Líquida com Preço Certo"),
    ("O tempo que você precisa dedicar por mês para gerenciar uma carteira blindada e vencedora.", "Eliminando produtos que dão prejuízo oculto e calculando impostos e taxas reais."),

    # Metodologia / Diferenciais
    ("Aprenda com Leveza, Bom Humor e Prática Real", "Aprenda com Prática Real e Foco em Resultados"),
    ("Lições práticas e diretas ao ponto. Absorva princípios testados pelos maiores mestres do mercado em minutos, sem perder tempo com teorias vazias.",
     "Lições práticas e diretas ao ponto. Cada slide entrega um conceito essencial e aplicável em menos de 2 minutos para quem toca um negócio."),
    ("Cada módulo tem um desafio prático: o bônus na conta, o carro quebrado no fim do mês, o gerente oferecendo capitalização e a dica do primo no churrasco.",
     "Ao final de cada módulo, enfrente um cenário real: cliente pedindo desconto no PIX, boletos da escola no cartão PJ e folha de pagamento em risco."),
    ("Criptoativos com Segurança", "Precificação Científica"),
    ("Entenda o papel real do Bitcoin como reserva matemática, diferencie projetos sérios de golpes e aprenda custódia fria (cold wallets).",
     "Pare de 'chutar' preços copiando concorrentes. Domine Markup, Custos Fixos proporcionais, Margem de Contribuição e Ponto de Equilíbrio."),
    ("Ao concluir a formação, emita seu certificado oficial executivo com carga horária de 6h, código de autenticidade criptográfico e assinatura institucional.",
     "Ao concluir a formação, emita seu certificado oficial executivo com carga horária de 6h, código criptográfico individual CSH-2026 e assinatura executiva."),

    # Módulos
    ("Mentalidade Financeira &amp; O Jogo do Dinheiro", "Separação PF/PJ &amp; Pró-Labore Blindado"),
    ("O paradoxo do salário alto, inflação do estilo de vida, as regras de ouro de Warren Buffett, o sistema dos 3 potes e raio-x dos vazamentos.",
     "O erro mortal do caixa único, como fixar um pró-labore sustentável, a regra das duas contas e regras sagradas do cartão corporativo."),
    ("Ativo vs Passivo", "Entidade Contábil"),
    ("Juros Compostos", "Pró-Labore Fixo"),

    ("Orçamento sem Neura, Faxina &amp; Reserva Anti-Crise", "Fluxo de Caixa Diário, Realizado e Projetado"),
    ("O método 50/30/20 simplificado, eliminação de boletos fantasmas, uso mestre do cartão sem juros, o método bola de neve e a sagrada reserva de emergência.",
     "A diferença crucial entre lucro contábil e dinheiro em caixa, método do fluxo direto, projeção de 30/60/90 dias e colchão de sobrevivência."),
    ("Método 50/30/20", "Entradas e Saídas"),
    ("Zero Dívidas", "Projeção 90 Dias"),

    ("Renda Fixa Inteligente &amp; O Fim da Poupança", "Precificação Estratégica &amp; Margem Real"),
    ("Por que a poupança perde para a inflação, o guia do Tesouro Direto (Selic, IPCA+, Prefixado), CDBs, LCIs e LCAs isentas de IR e a garantia do FGC até R$ 250k.",
     "Custos diretos vs despesas fixas proporcionais, Markup Multiplicador vs Margem por Dentro, margem de contribuição e armadilhas de maquininhas."),
    ("Tesouro Selic/IPCA", "Margem de Contribuição"),
    ("LCI/LCA Isenta", "Markup Científico"),

    ("Renda Variável: Ações de Valor, Dividendos &amp; FIIs", "DRE Gerencial, Ponto de Equilíbrio &amp; Curva ABC"),
    ("Virando sócio de grandes empresas (sem day trade), Fundos Imobiliários e aluguel mensal isento, a filosofia Barsi/Lynch, o filtro BESST e psicologia de mercado.",
     "Demonstração de resultados simplificada para quem não é contador, quanto faturar por dia para não fechar no vermelho e análise de produtos 80/20."),
    ("FIIs de Tijolo", "DRE Descomplicada"),
    ("Método BESST", "Ponto de Equilíbrio"),

    ("Criptoativos, Bitcoin &amp; A Nova Fronteira Digital", "Inadimplência, Crédito &amp; Renegociação de Dívidas"),
    ("O que é o Bitcoin e a escassez dos 21 milhões, separando projetos sérios de pirâmides e memecoins, custódia pessoal (cold wallets), estratégia DCA e alocação segura.",
     "Política de prazos e crédito, régua de cobrança profissional e elegante, riscos da antecipação de recebíveis e como negociar com bancos e fornecedores."),
    ("Ouro Digital", "Régua de Cobrança"),
    ("Cold Wallets", "Risco de Crédito"),

    ("A Carteira Blindada, Rebalanceamento &amp; Liberdade", "Orçamento Empresarial, Reinvestimento &amp; Governança"),
    ("O portfólio All-Weather de Ray Dalio, internacionalização com ETFs em dólar, o número da liberdade e a regra dos 4%, rebalanceamento em 15 minutos e os 5 mandamentos.",
     "Construção do orçamento anual da empresa, quando e quanto retirar de lucros e dividendos, reinvestimento em máquinas e os 5 indicadores do dono."),
    ("Ray Dalio", "Orçamento Anual"),
    ("Regra dos 4%", "Governança PME"),

    # Certificado
    ("Certificado Executivo de Formação Financeira", "Certificado Executivo em Gestão e Fluxo de Caixa"),
    ("Certificamos com distinção que <strong>o aluno concluiu com êxito</strong> o programa de capacitação em Gestão Financeira, Renda Fixa, Ações, FIIs, Criptoativos e Alocação Patrimonial Global.",
     "Certificamos com distinção que <strong>o empresário concluiu com êxito</strong> o programa prático em Gestão e Fluxo de Caixa para Empresas, Precificação Estratégica, DRE e Governança Financeira."),
    ("Registro de emissão individual (ex.: INV-2026-8942-BR).", "Registro de emissão individual (ex.: CSH-2026-8942-BR)."),

    # Preço & Checkout
    ("Acesso total para quem deseja assumir o controle definitivo do próprio dinheiro e investir com segurança.",
     "Acesso total para quem deseja blindar a saúde financeira da empresa e construir um negócio lucrativo e organizado."),
    ("Comece a Multiplicar Seu Patrimônio Hoje", "Assuma o Controle do Caixa da Sua Empresa Hoje"),

    # FAQ
    ("Preciso ter muito dinheiro para começar a aplicar o que aprendo?",
     "Preciso de planilhas complexas ou programas caros de gestão?"),
    ("De forma alguma! Você aprende a investir no Tesouro Direto com cerca de R$ 35, em cotas de Fundos Imobiliários com R$ 10 e em frações de Bitcoin com qualquer quantia a partir de R$ 20. O mais importante é o método e a consistência.",
     "Não! Ensinamos uma rotina limpa de 15 minutos diários que pode ser aplicada em um simples caderno de caixa, planilha básica do Google Sheets ou qualquer ERP simples que você já utilize."),
    ("O curso ensina 'Day Trade' ou promessas de ganho rápido?",
     "Para quem este treinamento é indicado?"),
    ("Não! O curso é 100% baseado em fundamentos testados pelos maiores investidores do mundo (Warren Buffett, Peter Lynch, Luiz Barsi, Ray Dalio). Nós ensinamos a construir patrimônio sólido e duradouro com responsabilidade, fugindo de pirâmides e especulações perigosas.",
     "Para donos de micro e pequenas empresas, prestadores de serviços, comerciantes, MEIs, profissionais liberais e autônomos que precisam organizar o caixa, eliminar contas no susto e precificar com lucro garantido."),

    # Rodapé
    ("© 2026 INVEST PRO • Como Investir e Gerenciar o Seu Dinheiro.",
     "© 2026 CASH FLOW PRO • Gestão e Fluxo de Caixa para Empresas."),
    ("Formação prática executiva focada em patrimônio individual, educação financeira e investimentos estratégicos.",
     "Treinamentos práticos ensinando precificação de produtos e controle financeiro de pequenos negócios.")
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
    else:
        print(f"Aviso: Não encontrou '{old[:40]}...'")

with open(r'C:\cash\landing.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Gerado C:\\cash\\landing.html 100% alinhado com o design system de invest!")
