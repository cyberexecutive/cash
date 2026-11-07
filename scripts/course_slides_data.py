# -*- coding: utf-8 -*-
"""
Base de dados completa dos 38 slides e 6 Quizzes do curso:
'Gestão e Fluxo de Caixa para Empresas: Precificação de Produtos e Controle Financeiro de Pequenos Negócios'
"""

SLIDES_DATA = [
    # -------------------------------------------------------------------------
    # SLIDE 01: CAPA GERAL
    # -------------------------------------------------------------------------
    {
        "slide_num": 1,
        "type": "cover",
        "category": "FORMAÇÃO PRÁTICA • GESTÃO EMPRESARIAL 2026",
        "title": 'Gestão e Fluxo de Caixa <br><span class="gradient-text">para Empresas</span>',
        "subtitle": 'O método prático, direto ao ponto e sem juridiquês para dominar o fluxo de caixa, precificar produtos e serviços com lucro real e blindar as finanças do seu pequeno negócio.',
        "cards": [
            {
                "icon": "emerald",
                "title": "6 Módulos Práticos",
                "desc": "Da separação PF/PJ ao fluxo de caixa diário, precificação científica, DRE gerencial e controle de inadimplência."
            },
            {
                "icon": "amber",
                "title": "6 Quizzes da Vida Real",
                "desc": "Dilemas reais do pequeno empresário: o desconto do fornecedor, a guerra de preços, o cliente VIP que atrasa e a segunda filial."
            },
            {
                "icon": "cyan",
                "title": "Certificado Executivo",
                "desc": "Emissão oficial personalizada com autenticação criptográfica CASH-2026, selo verde dólar e 6 horas de formação executiva."
            }
        ],
        "tip": "<strong>Dica de Navegação:</strong> Use as setas do teclado <strong>← →</strong> para navegar, <strong>M</strong> para a trilha de aulas e clique em qualquer card ou ilustração para <strong>ampliar em tela cheia</strong>."
    },

    # -------------------------------------------------------------------------
    # MÓDULO 01: O CORAÇÃO FINANCEIRO: SEPARAÇÃO PF/PJ E PRÓ-LABORE (Slides 2 a 7)
    # -------------------------------------------------------------------------
    {
        "slide_num": 2,
        "type": "lesson",
        "category": "MÓDULO 01 • O CORAÇÃO FINANCEIRO: SEPARAÇÃO PF/PJ",
        "title": "O Erro Mortal Nº 1: Misturar Dinheiro Pessoal e da Empresa",
        "subtitle": "Por que empresários que faturam R$ 50 mil vivem endividados e não sabem se o negócio realmente dá lucro.",
        "cards": [
            {
                "icon": "rose",
                "title": "A Ilusão do Caixa Único",
                "desc": "Pagar o colégio dos filhos, a conta de luz da casa e o supermercado direto no cartão da empresa cria uma névoa que cega o gestor. O negócio parece dar dinheiro, mas o caixa vive no vermelho."
            },
            {
                "icon": "emerald",
                "title": "A Regra dos Três Potes",
                "desc": "Pote 1: Caixa Operacional PJ (para fornecedores, salários e impostos). Pote 2: Reserva de Emergência PJ (colchão para meses fracos). Pote 3: Conta Pessoal PF (onde só entra o seu pró-labore fixo)."
            },
            {
                "icon": "cyan",
                "title": "Blindagem Jurídica e Fiscal",
                "desc": "Misturar contas viola o princípio da entidade contábil e abre brechas para desconsideração da personalidade jurídica na Justiça do Trabalho, expondo seu patrimônio pessoal a bloqueios judiciais."
            }
        ],
        "callout": {
            "type": "danger",
            "title": "Sintoma Crítico",
            "text": "Se você precisa olhar o extrato da conta da empresa para saber se pode jantar fora no fim de semana, sua empresa não é um negócio: é um caixa eletrônico desgovernado prestes a colapsar."
        },
        "svg_badge": "MÓDULO 01 • PILAR BÁSICO",
        "svg_icon": "shield"
    },
    {
        "slide_num": 3,
        "type": "lesson",
        "category": "MÓDULO 01 • O CORAÇÃO FINANCEIRO: SEPARAÇÃO PF/PJ",
        "title": "A Definição Inteligente do Pró-Labore do Dono",
        "subtitle": "Como calcular um salário fixo justo para você sem sufocar o capital de giro da sua empresa.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Pró-Labore vs. Distribuição de Lucro",
                "desc": "Pró-labore é a remuneração pelo seu trabalho diário (custo operacional fixo). Lucro é a remuneração pelo risco do seu capital investido (apurado após o fechamento trimestral ou anual)."
            },
            {
                "icon": "emerald",
                "title": "O Cálculo do Custo de Vida Mínimo",
                "desc": "Mapeie seus custos pessoais essenciais (moradia, saúde, alimentação). O pró-labore inicial deve cobrir essa base sem excessos. Se o negócio crescer, você recolhe lucro no final do ciclo, não no dia a dia."
            },
            {
                "icon": "amber",
                "title": "Data Fixa e Transferência Única",
                "desc": "Defina um dia do mês (ex: todo dia 05). Faça uma única transferência da conta PJ para a sua conta PF. A partir desse momento, seus gastos pessoais são pagos exclusivamente pela conta PF."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Regra Prática de Mercado",
            "text": "Quanto custaria contratar um gerente profissional competente para fazer exatamente o que você faz hoje? Esse valor de mercado é a melhor âncora para balizar o seu pró-labore."
        },
        "svg_badge": "MÓDULO 01 • PRÓ-LABORE",
        "svg_icon": "wallet"
    },
    {
        "slide_num": 4,
        "type": "lesson",
        "category": "MÓDULO 01 • O CORAÇÃO FINANCEIRO: SEPARAÇÃO PF/PJ",
        "title": "Categorização de Despesas: Custos Fixos vs. Variáveis",
        "subtitle": "A estrutura de custos é o alicerce de qualquer decisão de corte, precificação e sobrevivência.",
        "cards": [
            {
                "icon": "rose",
                "title": "Custos e Despesas Fixas",
                "desc": "Existem faça sol ou faça chuva, mesmo que a empresa venda zero: aluguel, contador, internet, folha base de funcionários, sistemas e seguros. Precisam ser monitorados e enxugados permanentemente."
            },
            {
                "icon": "amber",
                "title": "Custos e Despesas Variáveis",
                "desc": "Aumentam proporcionalmente às vendas: matéria-prima, comissão de vendedores, embalagens, fretes de entrega e taxas de maquininhas de cartão. Se não vendeu nada, esse custo é zero."
            },
            {
                "icon": "emerald",
                "title": "A Métrica da Alavancagem Operacional",
                "desc": "Quanto menor o seu custo fixo, menor a pressão de vendas para cobrir as contas. Empresas com custos fixos enxutos e custos variáveis flexíveis sobrevivem a qualquer crise econômica."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Frase de Sabedoria Corporativa",
            "text": "'Custos fixos são como unhas: crescem sozinhos e precisam ser cortados toda semana com tesoura afiada.' — Carlos Alberto Sicupira"
        },
        "svg_badge": "MÓDULO 01 • ESTRUTURA DE CUSTOS",
        "svg_icon": "scale"
    },
    {
        "slide_num": 5,
        "type": "lesson",
        "category": "MÓDULO 01 • O CORAÇÃO FINANCEIRO: SEPARAÇÃO PF/PJ",
        "title": "O Custo Invisível dos Impostos e das Maquininhas",
        "subtitle": "Como antecipações automáticas de cartão e bitributação corroem silenciosamente até 20% do faturamento.",
        "cards": [
            {
                "icon": "rose",
                "title": "A Armadilha da Antecipação Automática",
                "desc": "Vendeu em 10x e antecipou tudo no dia seguinte? As taxas compostas das maquininhas costumam morder de 12% a 24% ao ano. Você transfere o lucro do seu trabalho diretamente para a adquirente."
            },
            {
                "icon": "cyan",
                "title": "Simples Nacional e MEI Descomplicados",
                "desc": "Entenda em qual anexo do Simples sua empresa se enquadra (Comércio: Anexo I ~4%; Serviços: Anexo III ~6% ou V ~15,5% com fator R). O imposto deve entrar como custo variável direto em cada venda."
            },
            {
                "icon": "emerald",
                "title": "Incentivo Ativo ao PIX e Boleto",
                "desc": "Crie políticas comerciais inteligentes: ofereça 5% de desconto no PIX. Você fideliza o cliente, economiza 3% de taxa de cartão e recebe o dinheiro na hora, sem risco de chargeback."
            }
        ],
        "callout": {
            "type": "warning",
            "title": "Atenção ao Ralo Oculto",
            "text": "Audite seu extrato da maquininha todo dia 1º. Tarifas de aluguel de POS, taxas de cancelamento e antecipação automática são cobradas sem aviso em letras miúdas."
        },
        "svg_badge": "MÓDULO 01 • TAXAS & TRIBUTOS",
        "svg_icon": "calculator"
    },
    {
        "slide_num": 6,
        "type": "lesson",
        "category": "MÓDULO 01 • O CORAÇÃO FINANCEIRO: SEPARAÇÃO PF/PJ",
        "title": "O Ponto de Equilíbrio (Break-Even): O Número da Paz",
        "subtitle": "Descubra exatamente em que dia do mês a sua empresa empata as contas e começa a gerar lucro real.",
        "cards": [
            {
                "icon": "cyan",
                "title": "O Que é o Ponto de Equilíbrio",
                "desc": "É o faturamento exato onde a Receita Total é igual à soma dos Custos Fixos + Custos Variáveis. Lucro = Zero. A partir desse centavo adicional, cada nova venda injeta dinheiro limpo no caixa."
            },
            {
                "icon": "emerald",
                "title": "A Fórmula Executiva",
                "desc": "Ponto de Equilíbrio = Custos Fixos Mensais ÷ % Margem de Contribuição Média. Exemplo: Custos Fixos de R$ 12.000 com margem média de 40% exigem faturamento de R$ 30.000 (R$ 1.000/dia)."
            },
            {
                "icon": "amber",
                "title": "Meta Diária de Sobrevivência",
                "desc": "Transforme o ponto de equilíbrio em meta visível no painel da equipe: 'Precisamos vender R$ 1.200 por dia útil até o dia 22 para pagar todas as contas do mês; do dia 23 em diante é o nosso lucro'."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Estratégia de Alta Performance",
            "text": "Ao saber o seu Ponto de Equilíbrio, você elimina a ansiedade no início do mês e consegue focar a força comercial com clareza matemática absoluta."
        },
        "svg_badge": "MÓDULO 01 • PONTO DE EQUILÍBRIO",
        "svg_icon": "target"
    },
    {
        "slide_num": 7,
        "type": "quiz",
        "quiz_id": 1,
        "category": "MÓDULO 01 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 01: O 13º dos Colaboradores vs. As Férias da Família do Sócio",
        "subtitle": "Coloque à prova sua disciplina executiva diante de uma tentação comum no caixa da empresa.",
        "scenario": 'Chega a primeira semana de dezembro e o saldo bancário da sua empresa exibe confortáveis R$ 38.000. Sua família planeja uma viagem de férias e você é pressionado a retirar R$ 15.000 para pagar passagens e hotel. No entanto, no dia 20 vencem a 2ª parcela do 13º salário da equipe (R$ 14.000), o DAS do Simples (R$ 4.500) e fornecedores essenciais (R$ 16.000). Qual a decisão executiva correta?',
        "options": [
            {
                "letter": "A",
                "desc": "Retira os R$ 15.000 da conta PJ para a viagem, afinal 'o ano foi duro e nós merecemos', contando que as vendas de Natal nas próximas semanas com certeza cobrirão o 13º e os fornecedores.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Mantém o dinheiro intocado na conta da empresa para honrar 100% dos compromissos legais e operacionais, e custeia o lazer pessoal exclusivamente com o pró-labore acumulado na sua conta PF.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Paga a viagem com o cartão de crédito da empresa em 12 vezes sem juros, postergando o problema para o ano seguinte na esperança de que janeiro tenha vendas recordes.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Decisão executiva de alto nível! Dinheiro na conta da empresa não é lucro disponível: é patrimônio operacional reservado para honrar compromissos trabalhistas, fiscais e mercantis. Vendas futuras de Natal são apenas projeções incertas, mas o 13º salário e os fornecedores são obrigações certas e inegociáveis.",
        "svg_badge": "DESAFIO 01 • SEPARAÇÃO PF/PJ",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 02: O FLUXO DE CAIXA NA PRÁTICA: DIÁRIO, REALIZADO E PROJETADO (Slides 8 a 13)
    # -------------------------------------------------------------------------
    {
        "slide_num": 8,
        "type": "lesson",
        "category": "MÓDULO 02 • O FLUXO DE CAIXA NA PRÁTICA",
        "title": "A Diferença Crucial: Caixa vs. Competência",
        "subtitle": "Vender não é receber. Comprar não é pagar. O motivo exato pelo qual empresas 'lucrativas' quebram.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Regime de Competência (DRE)",
                "desc": "Registra o fato no momento em que a venda acontece ou a compra é faturada, não importando a data do dinheiro. Mostra se a operação é economicamente lucrativa no papel."
            },
            {
                "icon": "emerald",
                "title": "Regime de Caixa (Fluxo de Caixa)",
                "desc": "Registra estritamente o dia e a hora em que o dinheiro entra e sai da conta bancária. É o oxigênio real do negócio: boleto não se paga com 'promessa de recebimento'."
            },
            {
                "icon": "rose",
                "title": "A Morte por Inadimplência ou Prazo",
                "desc": "Se você fatura R$ 100 mil com 30% de margem no papel, mas parcelou tudo em 6x para clientes e tem que pagar fornecedores em 15 dias à vista, seu negócio quebra com lucro recorde na DRE."
            }
        ],
        "callout": {
            "type": "warning",
            "title": "Máxima de Wall Street para PMEs",
            "text": "'Faturamento é vaidade, lucro é sanidade, mas caixa é rei absoluto (Cash is King).' Sem caixa no dia 10, a melhor empresa do mundo fecha as portas."
        },
        "svg_badge": "MÓDULO 02 • CAIXA VS COMPETÊNCIA",
        "svg_icon": "bank"
    },
    {
        "slide_num": 9,
        "type": "lesson",
        "category": "MÓDULO 02 • O FLUXO DE CAIXA NA PRÁTICA",
        "title": "A Estrutura do Fluxo de Caixa Diário",
        "subtitle": "A rotina executiva de 15 minutos diários que impede surpresas, fraudes e rombos contábeis.",
        "cards": [
            {
                "icon": "cyan",
                "title": "1. Saldo Inicial do Dia",
                "desc": "A soma exata dos saldos de todas as contas bancárias da empresa + dinheiro físico no caixa físico no início da manhã."
            },
            {
                "icon": "emerald",
                "title": "2. Entradas Reais (Créditos)",
                "desc": "Recebimentos em PIX, liquidações de duplicatas de clientes, repasses de operadoras de cartão e rendimentos de aplicações."
            },
            {
                "icon": "rose",
                "title": "3. Saídas Reais (Débitos)",
                "desc": "Pagamentos efetivados de fornecedores, guias de impostos, salários, pró-labore, tarifas bancárias e contas de consumo."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Conciliação Bancária Obrigatória",
            "text": "Saldo Inicial + Entradas - Saídas = Saldo Final. Se a sua planilha disser R$ 10.450 e o extrato do banco acusar R$ 9.800, investigue na mesma hora: pode ser tarifa oculta ou desvio interno."
        },
        "svg_badge": "MÓDULO 02 • ROTINA DIÁRIA",
        "svg_icon": "chart"
    },
    {
        "slide_num": 10,
        "type": "lesson",
        "category": "MÓDULO 02 • O FLUXO DE CAIXA NA PRÁTICA",
        "title": "Fluxo de Caixa Projetado: Olhando 30, 60 e 90 Dias à Frente",
        "subtitle": "Como antecipar o 'buraco' no caixa semanas antes e agir como um estrategista, não como um bombeiro.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Mapeamento das Obrigações Futuras",
                "desc": "Lance todos os boletos já emitidos, parcelas de fornecedores, previsão de folha de pagamento e datas de recolhimento tributário para os próximos 3 meses."
            },
            {
                "icon": "emerald",
                "title": "Projeção Conservadora de Recebíveis",
                "desc": "Considere apenas recebíveis certos (cartões já autorizados e boletos faturados para bons pagadores, descontando uma taxa histórica de 5% de inadimplência)."
            },
            {
                "icon": "amber",
                "title": "Identificação Prévia do Déficit",
                "desc": "Se o gráfico aponta que no dia 18 do próximo mês o caixa ficará negativo em R$ 7.000, você tem 4 semanas para negociar com fornecedores, lançar uma promoção à vista ou adiar compras."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Poder de Negociação",
            "text": "Negociar prorrogação de prazo com o fornecedor com 20 dias de antecedência demonstra profissionalismo. Ligar no dia do vencimento pedindo arrego queima o crédito da sua empresa."
        },
        "svg_badge": "MÓDULO 02 • PROJEÇÃO ESTATÍSTICA",
        "svg_icon": "target"
    },
    {
        "slide_num": 11,
        "type": "lesson",
        "category": "MÓDULO 02 • O FLUXO DE CAIXA NA PRÁTICA",
        "title": "Ciclo Operacional, Ciclo Financeiro e Capital de Giro",
        "subtitle": "A equação do tempo: quanto mais demora para você receber, mais dinheiro próprio você precisa imobilizar.",
        "cards": [
            {
                "icon": "cyan",
                "title": "PMR (Prazo Médio de Recebimento)",
                "desc": "Em quantos dias, em média, o dinheiro entra na sua conta após a venda (ex: se vende muito em 30/60 dias, seu PMR é de 45 dias)."
            },
            {
                "icon": "rose",
                "title": "PMP (Prazo Médio de Pagamento)",
                "desc": "Em quantos dias seus fornecedores exigem receber pela matéria-prima ou mercadoria (ex: 15 ou 28 dias)."
            },
            {
                "icon": "amber",
                "title": "O Intervalo do Perigo (Ciclo Financeiro)",
                "desc": "Se você paga o fornecedor em 20 dias, mas só recebe do cliente em 45 dias, existe um 'gap' de 25 dias no qual a sua empresa financia o cliente com capital de giro próprio."
            }
        ],
        "callout": {
            "type": "warning",
            "title": "O Efeito Tesoura",
            "text": "Crescer rápido demais sem capital de giro quebra empresas! Se as vendas dobram, a necessidade de bancar estoque e prazo também dobra. Cresça no ritmo do seu colchão de caixa."
        },
        "svg_badge": "MÓDULO 02 • CICLOS & CAPITAL",
        "svg_icon": "scale"
    },
    {
        "slide_num": 12,
        "type": "lesson",
        "category": "MÓDULO 02 • O FLUXO DE CAIXA NA PRÁTICA",
        "title": "A Reserva de Segurança da Empresa (Colchão PJ)",
        "subtitle": "Quantos meses de custos fixos o seu negócio precisa ter aplicados para nunca depender de cheque especial.",
        "cards": [
            {
                "icon": "emerald",
                "title": "O Tamanho Ideal da Reserva PJ",
                "desc": "Calcule seus Custos Fixos Mensais (aluguel, salários, pró-labore base, serviços). Multiplique por 3 a 6 meses. Exemplo: R$ 15.000/mês de custo fixo = Reserva PJ ideal de R$ 45.000 a R$ 90.000."
            },
            {
                "icon": "cyan",
                "title": "Onde Guardar o Dinheiro da Empresa",
                "desc": "O dinheiro da Reserva PJ não pode ficar na conta-corrente (rende zero e gera tentação de gastar). Aplique em CDB PJ com liquidez diária (100% do CDI) ou Fundos DI com taxa zero em bancos digitais corporativos."
            },
            {
                "icon": "amber",
                "title": "A Regra dos Aportes Graduais",
                "desc": "Não tem a reserva ainda? Separe religiosamente 5% a 10% do faturamento líquido de cada mês até atingir a meta. Essa disciplina constrói a independência financeira do seu negócio."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Tranquilidade Executiva",
            "text": "Com 3 a 6 meses de reserva em caixa, quedas sazonais de faturamento em janeiro ou crises no fornecedor tornam-se meros contratempos contornados com serenidade."
        },
        "svg_badge": "MÓDULO 02 • RESERVA PJ",
        "svg_icon": "shield"
    },
    {
        "slide_num": 13,
        "type": "quiz",
        "quiz_id": 2,
        "category": "MÓDULO 02 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 02: O Fornecedor Oferece 12% de Desconto à Vista",
        "subtitle": "Avalie o custo de oportunidade e o risco de desfalcar o caixa operacional em troca de uma 'vantagem'.",
        "scenario": 'Seu principal fornecedor de insumos liga oferecendo uma condição relâmpago: um lote de R$ 20.000 sai por R$ 17.600 (12% de desconto) se pago hoje no PIX à vista. Seu saldo bancário livre é de R$ 21.000. Porém, ao consultar seu Fluxo de Caixa Projetado, você nota que em 12 dias vencem a folha de pagamento e o aluguel no valor de R$ 15.000, com previsão de entradas seguras de apenas R$ 8.000 nesse período. Qual a decisão executiva correta?',
        "options": [
            {
                "letter": "A",
                "desc": "Paga os R$ 17.600 à vista no PIX para embolsar os R$ 2.400 de desconto imediatamente, e no dia 12 entra no cheque especial da empresa ou toma capital de giro bancário para pagar a folha.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Recusa a compra integral à vista para não asfixiar o caixa, ou propõe pagar 40% no ato e o saldo restante em 30/60 dias preservando o saldo mínimo de segurança da folha.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Usa o dinheiro do lote à vista e atrasa 15 dias o salário da equipe e o aluguel, alegando que 'o desconto foi bom para a empresa e todos devem colaborar'.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Análise cirúrgica de fluxo de caixa! Um 'desconto' de R$ 2.400 não compensa o custo financeiro e o estresse de entrar no cheque especial (juros de 8% a 14% ao mês) nem o risco inadmissível de atrasar a folha de pagamento. O bom gestor protege a liquidez antes de perseguir descontos.",
        "svg_badge": "DESAFIO 02 • FLUXO DE CAIXA",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 03: PRECIFICAÇÃO ESTRATÉGICA: ACABANDO COM O PREJUÍZO DISFARÇADO (Slides 14 a 19)
    # -------------------------------------------------------------------------
    {
        "slide_num": 14,
        "type": "lesson",
        "category": "MÓDULO 03 • PRECIFICAÇÃO ESTRATÉGICA",
        "title": "A Armadilha do Markup Simples: 'Compro por 50 e Vendo por 100'",
        "subtitle": "Por que dobrar o custo da mercadoria quase sempre resulta em prejuízo silencioso no fim do mês.",
        "cards": [
            {
                "icon": "rose",
                "title": "A Mente Ingênua do Dobro",
                "desc": "'Paguei R$ 50 no produto e vendo por R$ 100, então meu lucro é de 50%, certo?' Errado! Desse R$ 100 saem 6% de Simples, 4% de taxa de cartão, 5% de comissão, 5% de frete e 25% de rateio de custo fixo."
            },
            {
                "icon": "amber",
                "title": "A Conta Verdadeira",
                "desc": "R$ 100 - R$ 50 (custo) - R$ 20 (impostos e variáveis) - R$ 25 (fatia dos custos fixos) = Sobram misérrimos R$ 5 de lucro líquido real (5%), e não os 50% que o dono imaginava."
            },
            {
                "icon": "emerald",
                "title": "Precificação Não é Opinião: É Matemática",
                "desc": "Para lucrar de verdade, você precisa calcular de baixo para cima: considerar todas as mordidas variáveis e o rateio proporcional de custos fixos antes de determinar a etiqueta de venda."
            }
        ],
        "callout": {
            "type": "danger",
            "title": "Alerta de Falência",
            "text": "Empresas que usam markup 'chutado' sem planilha de composição vendem muito, trabalham 14 horas por dia e no final do ano descobrem que pagaram para trabalhar."
        },
        "svg_badge": "MÓDULO 03 • MARKUP ENGANOSO",
        "svg_icon": "calculator"
    },
    {
        "slide_num": 15,
        "type": "lesson",
        "category": "MÓDULO 03 • PRECIFICAÇÃO ESTRATÉGICA",
        "title": "A Fórmula Científica do Preço de Venda e Margem",
        "subtitle": "O método de divisor para blindar sua margem de contribuição em qualquer segmento comercial ou industrial.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Os 4 Componentes do Preço",
                "desc": "1. Custo Direto Unitário (Custo da mercadoria / insumos). 2. % Despesas Variáveis (Impostos + Maquininha + Comissão + Frete). 3. % Rateio de Custos Fixos. 4. % Lucro Líquido Desejado."
            },
            {
                "icon": "emerald",
                "title": "A Fórmula do Divisor",
                "desc": "Preço de Venda = Custo Direto ÷ [1 - (% Despesas Variáveis + % Despesas Fixas + % Lucro Desejado)]. Se o custo é R$ 60 e a soma dos percentuais é 45% (0,45), Preço = 60 ÷ 0,55 = R$ 109,09."
            },
            {
                "icon": "amber",
                "title": "Margem de Contribuição em Reais",
                "desc": "Margem de Contribuição = Preço de Venda - Custos e Despesas Variáveis. É o valor líquido em reais que cada produto vendido deixa no caixa para pagar os custos fixos da empresa."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Regra de Ouro",
            "text": "Sempre calcule a margem sobre o PREÇO DE VENDA (Margem), nunca sobre o custo (Markup). 50% de markup equivale a apenas 33% de margem real."
        },
        "svg_badge": "MÓDULO 03 • FÓRMULA DO PREÇO",
        "svg_icon": "chart"
    },
    {
        "slide_num": 16,
        "type": "lesson",
        "category": "MÓDULO 03 • PRECIFICAÇÃO ESTRATÉGICA",
        "title": "Precificação de Serviços: A Hora Técnica e a Ociosidade",
        "subtitle": "Como calcular o preço da sua hora de trabalho sem desconsiderar férias, 13º e tempo improdutivo.",
        "cards": [
            {
                "icon": "rose",
                "title": "O Erro das 160 Horas Mês",
                "desc": "Nenhum profissional de serviços produz 8 horas faturáveis por dia, 20 dias por mês. Há tempo gasto respondendo e-mails, elaborando propostas, reuniões comerciais e deslocamento. A capacidade real faturável raramente passa de 100 a 110 horas/mês."
            },
            {
                "icon": "cyan",
                "title": "A Composição da Hora Técnica",
                "desc": "Custo da Hora = (Seu Pró-Labore Almejado + Encargos/Férias/13º + Custos Fixos do Escritório/Ferramentas) ÷ Horas Faturáveis Efetivas no Mês."
            },
            {
                "icon": "emerald",
                "title": "Adicionando a Margem de Lucro PJ",
                "desc": "A hora técnica calculada cobre apenas os custos e o seu salário. Sobre ela, adicione a Margem de Lucro da Empresa (20% a 35%) e a alíquota de impostos (ISS/Simples) para formar a proposta comercial."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Dica de Contratos Recorrentes",
            "text": "Prefira contratos de mensalidade (fee mensal) com escopo fechado do que cobrar por hora picada. A recorrência estabiliza o fluxo de caixa da empresa de serviços."
        },
        "svg_badge": "MÓDULO 03 • SERVIÇOS & HORA",
        "svg_icon": "scale"
    },
    {
        "slide_num": 17,
        "type": "lesson",
        "category": "MÓDULO 03 • PRECIFICAÇÃO ESTRATÉGICA",
        "title": "Ancoragem de Valor e Combos: Fuja da Guerra de Preços",
        "subtitle": "Quem é escolhido apenas pelo preço mais baixo é abandonado no primeiro centavo do concorrente.",
        "cards": [
            {
                "icon": "amber",
                "title": "A Ancoragem Psicológica de Preço",
                "desc": "Apresente 3 opções de proposta: Pacote Básico (R$ 1.200), Pacote Executivo Recomendado (R$ 1.900) e Pacote Premium Completo (R$ 3.800). A presença do plano Premium faz o plano Executivo parecer extremamente vantajoso."
            },
            {
                "icon": "emerald",
                "title": "A Magia dos Combos (Cross-Selling)",
                "desc": "Junte um produto de alta margem com um de alto giro. Ex: Produto A (R$ 100, margem 20%) + Acessório B (R$ 40, margem 60%). No combo por R$ 125, o cliente sente economia e sua margem em reais sobe 35%."
            },
            {
                "icon": "cyan",
                "title": "Venda Benefício e Rapidez, Não Tempo",
                "desc": "O cliente não quer comprar 10 horas de consultoria ou um produto de plástico: ele quer o problema resolvido no menor tempo possível e sem dor de cabeça."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Posicionamento Estratégico",
            "text": "Seja o mais barato da cidade ou seja o melhor. O meio do caminho (qualidade média e preço médio) é onde morrem as pequenas empresas sem identidade."
        },
        "svg_badge": "MÓDULO 03 • VALOR PERCEBIDO",
        "svg_icon": "target"
    },
    {
        "slide_num": 18,
        "type": "lesson",
        "category": "MÓDULO 03 • PRECIFICAÇÃO ESTRATÉGICA",
        "title": "A Matemática Perigosa dos Descontos",
        "subtitle": "Por que dar 10% de desconto pode exigir que você venda 50% mais unidades para manter o mesmo lucro.",
        "cards": [
            {
                "icon": "rose",
                "title": "O Desconto Sai Inteiramente do Lucro",
                "desc": "Se seu produto custa R$ 100 com custo de R$ 70 (lucro de R$ 30), e você dá 10% de desconto (vende a R$ 90), o custo continua sendo R$ 70! Seu lucro despenca de R$ 30 para R$ 20 (uma queda brutal de 33,3% no lucro líquido!)."
            },
            {
                "icon": "amber",
                "title": "A Tabela de Compensação de Volume",
                "desc": "Com margem de 20%, se você conceder míseros 5% de desconto, precisará vender 33% a mais em volume físico de produtos apenas para empatar o lucro em reais que tinha antes."
            },
            {
                "icon": "emerald",
                "title": "Substitutos Inteligentes para o Desconto",
                "desc": "Em vez de baixar o preço em R$ 20, ofereça um brinde ou serviço adicional cujo custo para você seja de R$ 4, mas cujo valor percebido pelo cliente seja de R$ 30. Você preserva sua margem intacta."
            }
        ],
        "callout": {
            "type": "warning",
            "title": "Regra Inviolável",
            "text": "Vendedor que dá desconto sem autorização e sem contrapartida (ex: pagamento à vista ou volume maior) está roubando o lucro da empresa para bater meta individual fácil."
        },
        "svg_badge": "MÓDULO 03 • DESCONTOS",
        "svg_icon": "calculator"
    },
    {
        "slide_num": 19,
        "type": "quiz",
        "quiz_id": 3,
        "category": "MÓDULO 03 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 03: O Concorrente Baixou 25% na Guerra de Preços",
        "subtitle": "Tome uma decisão estratégica sob a pressão de um cliente exigindo equiparação imediata de preço.",
        "scenario": 'Seu produto campeão de vendas é vendido a R$ 200, com custo unitário de insumos de R$ 120 e custos variáveis de R$ 30 (Margem de Contribuição = R$ 50 por unidade). Um concorrente local anuncia o mesmo produto por R$ 150. Um cliente antigo entra na sua loja com o anúncio na mão e diz: "Ou você cobre o preço de R$ 150 agora, ou perco a viagem e compro tudo lá". Qual a decisão correta?',
        "options": [
            {
                "letter": "A",
                "desc": "Cobre a oferta imediatamente para não perder o cliente de jeito nenhum, vendendo a R$ 150 mesmo sabendo que seus custos somam exatos R$ 150 (lucro zero absoluto).",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Não cobre o preço de R$ 150 (que destruiria sua margem operacional), mas contrapropõe agregar um diferencial imediato (ex: entrega expressa gratuita ou garantia estendida) mantendo o preço em R$ 190 à vista.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Baixa para R$ 140 para 'ensinar uma lição ao concorrente' e quebrar o rival no preço, operando no prejuízo deliberado.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Maturidade empresarial exemplar! Vender a R$ 150 tendo custo de R$ 150 significa assumir o risco de devolução, garantia e trabalho operacional sem deixar um único centavo para pagar o aluguel e a folha. Concorrentes que queimam preço sem fundamento quebram sozinhos em poucos meses.",
        "svg_badge": "DESAFIO 03 • GUERRA DE PREÇOS",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 04: DRE GERENCIAL E ANÁLISE DE LUCRATIVIDADE (Slides 20 a 25)
    # -------------------------------------------------------------------------
    {
        "slide_num": 20,
        "type": "lesson",
        "category": "MÓDULO 04 • DRE GERENCIAL & LUCRATIVIDADE",
        "title": "A DRE Gerencial Descomplicada: O Raio-X do Negócio",
        "subtitle": "A Demonstração do Resultado do Exercício explicada em uma única folha para donos de negócios.",
        "cards": [
            {
                "icon": "cyan",
                "title": "1. Faturamento Bruto a Líquido",
                "desc": "Vendas Totais (-) Devoluções e Cancelamentos (-) Impostos sobre Vendas (Simples/ICMS/ISS) = Receita Operacional Líquida."
            },
            {
                "icon": "rose",
                "title": "2. Custo das Vendas (CPV/CMV/CSV)",
                "desc": "(-) Custos diretos com mercadorias vendidas, matérias-primas ou execução dos serviços = Lucro Bruto / Margem de Contribuição."
            },
            {
                "icon": "emerald",
                "title": "3. Despesas Fixas e Lucro Final",
                "desc": "(-) Despesas Administrativas, Comerciais e Pró-labore = Lucro Operacional (EBITDA) (-) Despesas Financeiras e Juros = Lucro Líquido Real."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Instrumento de Diagnóstico",
            "text": "A DRE não serve para a Receita Federal: serve para VOCÊ saber se o seu modelo de negócio é viável ou se você está trabalhando para alimentar fornecedores e bancos."
        },
        "svg_badge": "MÓDULO 04 • DRE GERENCIAL",
        "svg_icon": "chart"
    },
    {
        "slide_num": 21,
        "type": "lesson",
        "category": "MÓDULO 04 • DRE GERENCIAL & LUCRATIVIDADE",
        "title": "Margem Bruta, Margem Operacional e Margem Líquida",
        "subtitle": "Os 3 termômetros que revelam se a empresa está saudável, anêmica ou à beira da UTI.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Margem Bruta (Lucro Bruto ÷ Receita Líquida)",
                "desc": "Mede a eficiência da sua compra e produção. No comércio saudável gira entre 40% e 60%; em serviços entre 50% e 80%. Se for baixa, sua precificação está errada."
            },
            {
                "icon": "amber",
                "title": "Margem Operacional (EBITDA)",
                "desc": "Mede a eficiência do negócio após pagar todas as despesas da estrutura física e equipe. O padrão saudável para pequenas empresas é entre 15% e 25%."
            },
            {
                "icon": "emerald",
                "title": "Margem Líquida (Lucro Líquido ÷ Faturamento)",
                "desc": "É o que realmente sobra limpo após impostos, juros e depreciação. Se sua margem líquida for menor que 8%, qualquer oscilação de mercado joga a empresa no prejuízo."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Métricas de Excelência",
            "text": "Empresas enxutas com margem líquida de 15% a 20% dormem em paz. Empresas com margem de 3% operam no fio da navalha."
        },
        "svg_badge": "MÓDULO 04 • MARGENS GERENCIAIS",
        "svg_icon": "scale"
    },
    {
        "slide_num": 22,
        "type": "lesson",
        "category": "MÓDULO 04 • DRE GERENCIAL & LUCRATIVIDADE",
        "title": "A Curva ABC: A Lei 80/20 Aplicada ao seu Negócio",
        "subtitle": "Descubra os 20% de produtos e clientes que geram 80% do seu lucro e demita os produtos zumbis.",
        "cards": [
            {
                "icon": "emerald",
                "title": "Classe A (As Estrelas do Negócio)",
                "desc": "Aproximadamente 20% dos itens que geram 70% a 80% do lucro total. Nunca podem faltar no estoque; merecem o melhor atendimento e campanhas prioritárias."
            },
            {
                "icon": "cyan",
                "title": "Classe B (Os Apoiadores)",
                "desc": "Cerca de 30% dos itens que geram 15% a 20% do faturamento. Complementam o mix de vendas e devem ter estoque controlado com reposição padrão."
            },
            {
                "icon": "rose",
                "title": "Classe C (Os Zumbis Comedores de Caixa)",
                "desc": "50% dos itens que geram menos de 5% do lucro. Ocupam espaço de prateleira, imobilizam capital precioso e geram perdas por validade ou obsolescência."
            }
        ],
        "callout": {
            "type": "warning",
            "title": "Ação Prática Imediata",
            "text": "Faça a Curva ABC todo trimestre. Elimine do seu catálogo 10% dos produtos Classe C que menos giram e veja seu caixa respirar aliviado na mesma semana."
        },
        "svg_badge": "MÓDULO 04 • CURVA ABC",
        "svg_icon": "target"
    },
    {
        "slide_num": 23,
        "type": "lesson",
        "category": "MÓDULO 04 • DRE GERENCIAL & LUCRATIVIDADE",
        "title": "Estoque Parado é Dinheiro Apodrecendo na Prateleira",
        "subtitle": "Como calcular o giro de estoque e transformar caixas empoeiradas em liquidez bancária.",
        "cards": [
            {
                "icon": "rose",
                "title": "O Custo de Oportunidade do Estoque",
                "desc": "R$ 40.000 parados em estoque há 6 meses não estão apenas 'guardados'. Estão sofrendo desvalorização, risco de quebra, furtos e custando os juros do capital de giro que você não tem."
            },
            {
                "icon": "cyan",
                "title": "Giro de Estoque = CMV ÷ Estoque Médio",
                "desc": "Se seu custo mensal de vendas é R$ 30.000 e seu estoque médio é R$ 60.000, seu estoque gira apenas 0,5x por mês (demora 60 dias para girar). Meta de varejo: girar a cada 20 a 30 dias."
            },
            {
                "icon": "emerald",
                "title": "Bota-Fora Estratégico de Caixa",
                "desc": "Produto parado há mais de 90 dias deve ser liquidado a preço de custo (ou margem mínima de 5%). O objetivo não é lucro: é recuperar o dinheiro vivo para reinvestir no que tem alta saída."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Mentalidade Comercial",
            "text": "Mais vale R$ 10.000 livres no banco rendendo 100% do CDI do que R$ 15.000 em mercadoria que ninguém compra na sua prateleira."
        },
        "svg_badge": "MÓDULO 04 • GESTÃO DE ESTOQUE",
        "svg_icon": "wallet"
    },
    {
        "slide_num": 24,
        "type": "lesson",
        "category": "MÓDULO 04 • DRE GERENCIAL & LUCRATIVIDADE",
        "title": "Indicadores de Desempenho (KPIs Financeiros)",
        "subtitle": "O painel de bordo que todo gestor moderno deve acompanhar semanalmente no celular.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Ticket Médio (Faturamento ÷ Nº Pedidos)",
                "desc": "Quanto cada cliente gasta em média por compra. Aumentar o ticket médio em 15% (com técnicas de cross-sell e combos) dobra o lucro sem precisar gastar mais em marketing."
            },
            {
                "icon": "amber",
                "title": "CAC vs. LTV (O Motor de Escala)",
                "desc": "CAC (Custo para adquirir cada cliente novo) vs. LTV (Valor total que esse cliente gasta ao longo da vida com você). A regra de ouro é LTV > 3x CAC."
            },
            {
                "icon": "emerald",
                "title": "Taxa de Queima (Burn Rate) & Runway",
                "desc": "Se o negócio operar no prejuízo temporário, quanto caixa é consumido por mês? Runway: quantos meses de vida a empresa tem com o saldo bancário atual."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Gestão Visual",
            "text": "Quem gerencia o que não mede navega no escuro. Mantenha 4 indicadores principais visíveis em uma planilha ou dashboard semanal."
        },
        "svg_badge": "MÓDULO 04 • KPIS FINANCEIROS",
        "svg_icon": "chart"
    },
    {
        "slide_num": 25,
        "type": "quiz",
        "quiz_id": 4,
        "category": "MÓDULO 04 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 04: O Contrato dos Sonhos que Paga em 60 Dias",
        "subtitle": "Avalie o risco de quebra por descasamento de fluxo de caixa em um contrato de grande porte.",
        "scenario": 'Uma grande rede corporativa propõe fechar um contrato anual com sua empresa: eles comprarão R$ 80.000 por mês (o que dobraria seu faturamento atual). Em contrapartida, impõem duas condições duras: pagamento faturado a 60 dias após a entrega e margem de contribuição reduzida de apenas 6% (lucro de R$ 4.800). Sua empresa possui apenas R$ 25.000 de capital de giro livre. Como proceder?',
        "options": [
            {
                "letter": "A",
                "desc": "Assina o contrato imediatamente, porque 'dobrar o faturamento dá status e nome no mercado', e depois corre atrás de empréstimos bancários para bancar os 60 dias de prazo.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Rejeita a proposta nos moldes atuais ou renegocia firme (ex: adiantamento de 30% ou parcelas quinzenais), pois bancar 60 dias de insumos e folha para R$ 80 mil exigiria mais de R$ 75 mil em capital de giro que a empresa não possui.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Aceita o contrato e atrasa propositalmente os pagamentos de todos os outros pequenos fornecedores para financiar a grande empresa.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Visão de C-Level! Esse é o clássico 'contrato suicida': a empresa dobra o faturamento, mas assume uma necessidade cavalar de capital de giro para uma margem de miséria (6%). Qualquer atraso no dia 60 colocaria a sua empresa em recuperação judicial. Clientes grandes devem ser sustentáveis, não sanguessugas de liquidez.",
        "svg_badge": "DESAFIO 04 • DRE & RISCO",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 05: CONTROLE DE INADIMPLÊNCIA, CRÉDITO E RENEGOCIAÇÃO (Slides 26 a 31)
    # -------------------------------------------------------------------------
    {
        "slide_num": 26,
        "type": "lesson",
        "category": "MÓDULO 05 • INADIMPLÊNCIA & CRÉDITO",
        "title": "A Anatomia do Calote: Como Prevenir Antes de Faturar",
        "subtitle": "Políticas simples de análise de crédito que evitam 90% dos problemas de cobrança.",
        "cards": [
            {
                "icon": "rose",
                "title": "Vender no 'Fio do Bigode' Acabou",
                "desc": "Vender a prazo sem contrato assinado ou sem consulta cadastral prévia em birôs (Serasa/Boa Vista) é transferir patrimônio da sua família para estranhos por pura ingenuidade."
            },
            {
                "icon": "cyan",
                "title": "A Regra dos Limites Escalonados",
                "desc": "Cliente novo? Venda à vista ou no cartão. Após 3 pedidos quitados em dia, libere um limite modesto no boleto (ex: R$ 2.000). Apenas clientes consolidados com histórico de 6 meses têm crédito expandido."
            },
            {
                "icon": "emerald",
                "title": "Contrato Padrão com Cláusula Executiva",
                "desc": "Tenha uma minuta contratual formal prevendo juros de 1% ao mês, multa moratória de 2% e cláusula expressa de autorização de protesto em cartório em caso de atraso superior a 15 dias."
            }
        ],
        "callout": {
            "type": "warning",
            "title": "Proteção Patrimonial",
            "text": "É infinitamente melhor perder uma venda duvidosa do que entregar sua mercadoria e ter que arcar com o prejuízo integral no caixa."
        },
        "svg_badge": "MÓDULO 05 • ANÁLISE DE CRÉDITO",
        "svg_icon": "shield"
    },
    {
        "slide_num": 27,
        "type": "lesson",
        "category": "MÓDULO 05 • INADIMPLÊNCIA & CRÉDITO",
        "title": "Régua de Cobrança Elegante, Firme e Automatizada",
        "subtitle": "Como cobrar sem perder a amizade com o cliente e sem parecer desesperado.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Passo 1: Lembrete Amigável (D-3 e D-0)",
                "desc": "3 dias antes do vencimento envie mensagem automática amigável via WhatsApp/E-mail com o código de barras ou PIX 'para facilitar seu controle financeiro'. No dia do vencimento, repita com gentileza."
            },
            {
                "icon": "amber",
                "title": "Passo 2: Contato Comercial Cordial (D+3 a D+7)",
                "desc": "3 a 5 dias após o vencimento: 'Notamos que o boleto não compensou no banco. Houve algum problema operacional com a emissão? Como podemos ajudar a regularizar?'"
            },
            {
                "icon": "rose",
                "title": "Passo 3: Cobrança Formal e Notificação (D+15)",
                "desc": "Notificação formal assinada pelo departamento financeiro informando sobre a suspensão de novos pedidos e o envio do título para protesto em cartório em 5 dias úteis caso não haja contato."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Regra Psicológica",
            "text": "Quem cobra primeiro e com método profissional recebe primeiro. O cliente em dificuldade financeira sempre prioriza o credor organizado e posterga o credor desleixado."
        },
        "svg_badge": "MÓDULO 05 • RÉGUA DE COBRANÇA",
        "svg_icon": "bank"
    },
    {
        "slide_num": 28,
        "type": "lesson",
        "category": "MÓDULO 05 • INADIMPLÊNCIA & CRÉDITO",
        "title": "Como Renegociar Dívidas com Bancos e Fornecedores",
        "subtitle": "A postura estratégica na mesa de negociação para trocar dívidas caras por prazos saudáveis.",
        "cards": [
            {
                "icon": "rose",
                "title": "Nunca Use Cheque Especial ou Rotativo PJ",
                "desc": "As taxas de cheque especial PJ e cartão corporativo passam de 12% a 15% ao mês. Se você deixar acumular, em 8 meses a dívida dobra. Esses créditos só servem para emergência de 48 horas."
            },
            {
                "icon": "cyan",
                "title": "Troca de Perfil de Endividamento",
                "desc": "Troque dívidas caras de curto prazo por linhas de longo prazo com garantia (Pronampe, Proger, BNDES ou empréstimo com garantia de recebíveis) com taxas anuais civilizadas e carência de 6 meses."
            },
            {
                "icon": "emerald",
                "title": "Negociação Frente a Frente com Fornecedor",
                "desc": "Apresente um plano de pagamento realista. Nenhum fornecedor quer a falência de um cliente. Proponha: 'Não consigo pagar os R$ 30 mil hoje, mas posso pagar 10 parcelas de R$ 3.300 e manter as compras novas à vista'."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Princípio da Transparência",
            "text": "Atenda sempre o telefone. Fugir do credor destrói a confiança. Comparecer com uma proposta técnica estruturada abre portas para acordos flexíveis."
        },
        "svg_badge": "MÓDULO 05 • RENEGOCIAÇÃO",
        "svg_icon": "scale"
    },
    {
        "slide_num": 29,
        "type": "lesson",
        "category": "MÓDULO 05 • INADIMPLÊNCIA & CRÉDITO",
        "title": "A Armadilha dos Empréstimos Rápidos para 'Tapar Buraco'",
        "subtitle": "Por que pegar dinheiro emprestado para cobrir despesa recorrente acelera a morte da empresa.",
        "cards": [
            {
                "icon": "rose",
                "title": "O Empréstimo Não Resolve Margem Negativa",
                "desc": "Se sua empresa tem custos fixos maiores que a receita, tomar R$ 50 mil no banco não resolve o problema: apenas adia a quebra e adiciona uma parcela de R$ 2.500 por mês sobre uma ferida aberta."
            },
            {
                "icon": "amber",
                "title": "Quando o Crédito é Válido",
                "desc": "Crédito bancário só se justifica em dois casos: 1. Investimento em maquinário ou tecnologia que comprovadamente aumente a margem. 2. Compra de estoque com desconto brutal garantido com giro imediato."
            },
            {
                "icon": "emerald",
                "title": "O Remédio Antes do Dinheiro",
                "desc": "Antes de assinar qualquer contrato bancário, corte despesas fixas em 15%, renegocie o pró-labore, audite a precificação e liquide estoque parado. O melhor dinheiro é o que você estanca de desperdício interno."
            }
        ],
        "callout": {
            "type": "danger",
            "title": "Sinal Vermelho",
            "text": "Tomar empréstimo para pagar folha de pagamento ou tributos em atraso sem reestruturar a operação é o último passo antes da recuperação judicial."
        },
        "svg_badge": "MÓDULO 05 • RISCO BANCÁRIO",
        "svg_icon": "calculator"
    },
    {
        "slide_num": 30,
        "type": "lesson",
        "category": "MÓDULO 05 • INADIMPLÊNCIA & CRÉDITO",
        "title": "Políticas Comerciais que Blindam o Faturamento",
        "subtitle": "Como desenhar termos de pagamento que incentivam a pontualidade e protegem a empresa.",
        "cards": [
            {
                "icon": "emerald",
                "title": "1. Sinal de Entrada Obrigatório (30% a 50%)",
                "desc": "Em encomendas ou projetos de serviço, exija entrada que cubra 100% dos custos diretos de matéria-prima. Assim, se o cliente der calote no final, seu prejuízo em dinheiro de bolso é zero."
            },
            {
                "icon": "cyan",
                "title": "2. Gatilhos de Entrega Fracionada",
                "desc": "Entregue o serviço ou mercadoria por etapas vinculadas ao pagamento: 'Fase 1 entregue após compensação da parcela 1; Fase 2 iniciada após quitação da parcela 2'."
            },
            {
                "icon": "amber",
                "title": "3. Cobrança Recorrente no Cartão (Tokenização)",
                "desc": "Em mensalidades de serviços ou planos de assinatura, utilize gateways que debitam no cartão de crédito do cliente automaticamente todo mês sem comprometer o limite total."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Segurança Preventiva",
            "text": "Quem impõe regras claras de pagamento ganha o respeito do mercado. Clientes sérios compreendem e valorizam empresas organizadas."
        },
        "svg_badge": "MÓDULO 05 • POLÍTICA COMERCIAL",
        "svg_icon": "wallet"
    },
    {
        "slide_num": 31,
        "type": "quiz",
        "quiz_id": 5,
        "category": "MÓDULO 05 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 05: O Maior Cliente Atrasou 25 Dias e Quer Pedido Urgente",
        "subtitle": "Equilibre a preservação do relacionamento comercial com a proteção absoluta do caixa.",
        "scenario": 'Seu cliente mais antigo e com maior volume de compras (responsável por 25% do faturamento da sua empresa) está com uma fatura de R$ 18.000 atrasada há 25 dias. Ele liga diretamente para o seu celular com um pedido novo e urgente de R$ 12.000 a prazo para entregar na segunda-feira, dizendo: "Manda o pedido que semana que vem eu acerto tudo junto". Como agir?',
        "options": [
            {
                "letter": "A",
                "desc": "Libera o novo pedido imediatamente sem questionar para não ofender o cliente antigo, torcendo para que a promessa de pagamento na semana que vem seja cumprida.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Com muita educação e firmeza comercial, explica que o sistema bloqueia novos despachos com pendências ativas, e propõe liquidar ao menos a fatura atrasada (ou pagar 50% dela) para liberar o novo pedido no ato.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Cancela o cliente, processa-o na mesma hora e bloqueia o telefone sem qualquer diálogo comercial prévio.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Postura impecável de liderança executiva! 'A culpa é do sistema' é uma técnica consagrada para tirar o atrito pessoal e manter a regra corporativa inegociável. Entregar mais mercadoria para um cliente já inadimplente só aumenta o tamanho do rombo. Quem quer comprar mais precisa demonstrar capacidade de pagar o que já levou.",
        "svg_badge": "DESAFIO 05 • GESTÃO DE COBRANÇA",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 06: O PLANO DE CRESCIMENTO E SOBERANIA FINANCEIRA (Slides 32 a 37)
    # -------------------------------------------------------------------------
    {
        "slide_num": 32,
        "type": "lesson",
        "category": "MÓDULO 06 • CRESCIMENTO & SOBERANIA FINANCEIRA",
        "title": "Orçamento Anual (Budget) e Planejamento Tributário",
        "subtitle": "Como desenhar as metas financeiras dos próximos 12 meses e economizar milhares de reais em impostos.",
        "cards": [
            {
                "icon": "cyan",
                "title": "O Orçamento Base Zero (OBZ)",
                "desc": "No final de cada ano, reconstrua o orçamento do zero. Não repita despesas só porque 'sempre foram pagas'. Cada linha de custo precisa justificar seu retorno operacional para o ano seguinte."
            },
            {
                "icon": "emerald",
                "title": "Revisão Periódica do Regime Tributário",
                "desc": "Converse com seu contador todo mês de novembro: Simples Nacional, Lucro Presumido ou Lucro Real? Conforme a empresa cresce e o faturamento muda, trocar de regime pode economizar de R$ 20 mil a R$ 100 mil por ano."
            },
            {
                "icon": "amber",
                "title": "Sazonalidade e Meta Trimestral",
                "desc": "Empresas têm meses fracos e meses fortes previsíveis. O orçamento anual permite acumular gordura nos meses de pico para atravessar os meses de baixa sem sobressaltos."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Visão Estratégica",
            "text": "Quem planeja o ano com antecedência controla o próprio destino. Quem vive mês a mês é refém das circunstâncias."
        },
        "svg_badge": "MÓDULO 06 • BUDGET ANUAL",
        "svg_icon": "chart"
    },
    {
        "slide_num": 33,
        "type": "lesson",
        "category": "MÓDULO 06 • CRESCIMENTO & SOBERANIA FINANCEIRA",
        "title": "A Máquina de Reinvestimento e Distribuição de Lucros",
        "subtitle": "Como remunerar os sócios com excelência mantendo o cofre da empresa cheio para expansão.",
        "cards": [
            {
                "icon": "emerald",
                "title": "A Regra 50 / 30 / 20 para o Lucro Líquido",
                "desc": "Do lucro líquido apurado ao fim do trimestre: 50% fica na empresa para Reinvestimento e expansão; 30% vai para a Reserva de Segurança PJ; 20% é distribuído como dividendo limpo aos sócios."
            },
            {
                "icon": "cyan",
                "title": "Dividendos Trimestrais, Não Mensais",
                "desc": "Distribuir lucro todo mês desestabiliza o capital de giro. Apure o resultado trimestral ou semestral com DRE fechada e balancete contábil. Assim, o sócio recebe uma bolada expressiva com segurança."
            },
            {
                "icon": "amber",
                "title": "Isenção Fiscal de Lucros no Brasil",
                "desc": "A distribuição de lucros apurados contabilmente é isenta de Imposto de Renda na pessoa física (conforme legislação vigente). O pró-labore sofre IR e INSS; o dividendo entra limpo na conta PF."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Crescimento Sustentável",
            "text": "Empresas que reinvestem 50% dos lucros em melhoria de processos, marketing e treinamento dobram de tamanho a cada 3 anos de forma autossustentável."
        },
        "svg_badge": "MÓDULO 06 • DIVIDENDOS & ESCALA",
        "svg_icon": "bank"
    },
    {
        "slide_num": 34,
        "type": "lesson",
        "category": "MÓDULO 06 • CRESCIMENTO & SOBERANIA FINANCEIRA",
        "title": "Tecnologia, ERPs Acessíveis e Automação de Caixa",
        "subtitle": "Abandone o caderninho de papel e planilhas confusas em favor de softwares modernos e baratos.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Softwares de Gestão Financeira para PMEs",
                "desc": "Plataformas como ContaAzul, Omie, Bling ou Tiny custam entre R$ 80 e R$ 250 por mês e automatizam emissão de NFe, controle de estoque, conciliação bancária Open Finance e envio de boletos."
            },
            {
                "icon": "emerald",
                "title": "Integração Bancária Automática (OFX / API)",
                "desc": "Elimine a digitação manual de extratos. Com a integração bancária diária, os pagamentos recebidos por PIX ou cartão são reconciliados automaticamente no sistema em poucos cliques."
            },
            {
                "icon": "amber",
                "title": "Redução Drástica de Erros Humanos",
                "desc": "Automatizar a rotina financeira economiza até 20 horas por mês do dono da empresa e evita esquecimentos de contas que geram multas e juros desnecessários."
            }
        ],
        "callout": {
            "type": "info",
            "title": "Investimento de Alto Retorno",
            "text": "Pagar R$ 100/mês em um software que salva 15 horas do seu tempo e evita uma multa de R$ 500 de imposto esquecido é o investimento com maior ROI da sua empresa."
        },
        "svg_badge": "MÓDULO 06 • AUTOMAÇÃO & ERP",
        "svg_icon": "target"
    },
    {
        "slide_num": 35,
        "type": "lesson",
        "category": "MÓDULO 06 • CRESCIMENTO & SOBERANIA FINANCEIRA",
        "title": "Governança em PMEs: A Reunião Mensal de Resultados",
        "subtitle": "Como liderar uma reunião de fechamento financeiro baseada em números frios, não em palpites e emoções.",
        "cards": [
            {
                "icon": "cyan",
                "title": "A Pauta Sagrada de Todo Dia 08",
                "desc": "1. Apresentação da DRE do mês anterior (Faturamento, Margens e Lucro Líquido). 2. Comparativo do Realizado vs. Orçado. 3. Curva de Inadimplência. 4. Projeção de Caixa para os próximos 60 dias."
            },
            {
                "icon": "rose",
                "title": "Cultura Contra Desculpas",
                "desc": "'O mercado tá fraco' não é diagnóstico aceitável. Analise os dados: Foi o número de clientes que caiu? O ticket médio que despencou? Ou o custo dos fornecedores que subiu sem repasse no preço?"
            },
            {
                "icon": "emerald",
                "title": "Plano de Ação Corretivo em 3 Passos",
                "desc": "Identificou o desvio? Defina: 1. Ação clara (ex: renegociar aluguel). 2. Responsável nominal. 3. Prazo limite de execução (ex: até o dia 20). Na reunião seguinte, cobra-se o resultado."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Alinhamento de Sócios",
            "text": "Reuniões mensais com ata e números claros evitam 95% dos desentendimentos e brigas societárias que destroem empresas familiares."
        },
        "svg_badge": "MÓDULO 06 • GOVERNANÇA",
        "svg_icon": "shield"
    },
    {
        "slide_num": 36,
        "type": "lesson",
        "category": "MÓDULO 06 • CRESCIMENTO & SOBERANIA FINANCEIRA",
        "title": "O Checklist Definitivo do Caixa Blindado",
        "subtitle": "Os 10 mandamentos práticos para garantir que sua empresa nunca mais passe sufoco financeiro.",
        "cards": [
            {
                "icon": "emerald",
                "title": "Rotinas Diárias e Semanais",
                "desc": "1. Conciliação bancária todo dia de manhã. 2. Acompanhamento do fluxo de caixa projetado a 30 dias. 3. Cobrança preventiva de boletos a vencer. 4. Conferência dos repasses de maquininhas."
            },
            {
                "icon": "cyan",
                "title": "Rotinas Mensais de Fechamento",
                "desc": "5. Emissão e análise da DRE Gerencial. 6. Pagamento do pró-labore em data fixa única. 7. Aplicação de 5% a 10% do resultado na Reserva PJ. 8. Atualização do Ponto de Equilíbrio."
            },
            {
                "icon": "amber",
                "title": "Diretrizes Estratégicas Permanentes",
                "desc": "9. Toda venda precisa ter margem de contribuição positiva calculada por fórmula. 10. Crescer no ritmo do capital de giro próprio, sem dependência tóxica de dívidas bancárias de curto prazo."
            }
        ],
        "callout": {
            "type": "tip",
            "title": "Compromisso de Sucesso",
            "text": "Imprima este checklist e coloque no mural do seu escritório. A constância na execução simples é o verdadeiro segredo das empresas milionárias e longevas."
        },
        "svg_badge": "MÓDULO 06 • CHECKLIST EXECUTIVO",
        "svg_icon": "wallet"
    },
    {
        "slide_num": 37,
        "type": "quiz",
        "quiz_id": 6,
        "category": "MÓDULO 06 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 06: Abrir a Segunda Filial ou Consolidar o Caixa?",
        "subtitle": "Decida o futuro do negócio diante do dilema clássico entre ambição de expansão e solidez financeira.",
        "scenario": 'Sua empresa teve 6 meses consecutivos de lucro expressivo e acumulou R$ 60.000 de reserva no banco. Um ponto comercial vizinho surge para alugar por um valor atrativo. Seus sócios se empolgam para alugar o imóvel e abrir uma filial imediatamente, gastando todos os R$ 60.000 em reforma e estoque. Seus custos fixos mensais atuais são de R$ 18.000. Qual a decisão executiva correta?',
        "options": [
            {
                "letter": "A",
                "desc": "Gasta todos os R$ 60.000 na nova filial sem pestanejar, porque 'quem não arrisca não petisca e o mercado pertence aos audaciosos'.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Preserva a Reserva PJ intocada (R$ 54.000 equivalem aos 3 meses de segurança obrigatória da matriz) e planeja a expansão com um cronograma seguro onde a filial só seja aberta quando houver capital de giro dedicado para bancar seus primeiros 6 meses de maturação.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Abre a filial e contrata um empréstimo adicional de R$ 80.000 no banco com juros de 2,5% ao mês para garantir que não falte nada.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Visão de Conselho de Administração! Torrar a reserva de emergência da matriz para abrir uma filial sem capital de giro de maturação é o caminho mais comum para quebrar as DUAS operações ao mesmo tempo. Negócios saudáveis expandem com caixa excedente à reserva de segurança, garantindo que a matriz continue forte aconteça o que acontecer.",
        "svg_badge": "DESAFIO 06 • CRESCIMENTO & SOBERANIA",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # SLIDE 38: CERTIFICAÇÃO EXECUTIVA OFICIAL
    # -------------------------------------------------------------------------
    {
        "slide_num": 38,
        "type": "certificate",
        "category": "MÓDULO 06 • CONCLUSÃO E CERTIFICAÇÃO FORMAL",
        "title": "Certificado Executivo em Gestão e Fluxo de Caixa Empresarial",
        "subtitle": "Emissão oficial personalizada com validação criptográfica, carga horária e selo de excelência executiva."
    }
]

