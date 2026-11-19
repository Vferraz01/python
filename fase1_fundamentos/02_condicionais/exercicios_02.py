"""
Módulo 02: Condicionais

Instruções:
- Leia LICAO.md antes de começar.
- Em cada função, apague o `pass` e escreva seu código.
- Depois de cada exercício, rode:
      pytest fase1_fundamentos/02_condicionais -v
- Não altere o nome das funções nem os parâmetros.
- Não use as funções prontas max() e min(): o objetivo é treinar a lógica.
"""


# ---------------------------------------------------------------------------
# Exercício 1: Par ou ímpar
# Devolva True se o número for par e False se for ímpar.
# Exemplos: eh_par(4) -> True, eh_par(7) -> False
# Desafio extra: dá para resolver em uma linha, sem if. Releia a seção 1.
# ---------------------------------------------------------------------------
def eh_par(numero):
    pass


# ---------------------------------------------------------------------------
# Exercício 2: Maior de dois
# Devolva o maior entre a e b. Se forem iguais, devolva qualquer um.
# Exemplo: maior_de_dois(3, 8) -> 8
# ---------------------------------------------------------------------------
def maior_de_dois(a, b):
    pass


# ---------------------------------------------------------------------------
# Exercício 3: Positivo, negativo ou zero
# Devolva "positivo", "negativo" ou "zero".
# Exemplo: classificar_numero(-5) -> "negativo"
# ---------------------------------------------------------------------------
def classificar_numero(numero):
    pass


# ---------------------------------------------------------------------------
# Exercício 4: Situação do aluno
# Média 7 ou mais:        "Aprovado"
# Média de 5 até abaixo de 7: "Recuperação"
# Média abaixo de 5:      "Reprovado"
# Exemplo: situacao_aluno(6.5) -> "Recuperação"
# ---------------------------------------------------------------------------
def situacao_aluno(media_final):
    pass


# ---------------------------------------------------------------------------
# Exercício 5: Maior de três
# Devolva o maior entre a, b e c (sem usar max()).
# Exemplo: maior_de_tres(4, 9, 2) -> 9
# Dica: teste com números repetidos, como (5, 5, 1) e (1, 5, 5).
# ---------------------------------------------------------------------------
def maior_de_tres(a, b, c):
    pass


# ---------------------------------------------------------------------------
# Exercício 6: Voto no Brasil
# Menos de 16 anos:              "não vota"
# 16 ou 17 anos, ou 70 ou mais:  "facultativo"
# De 18 a 69 anos:               "obrigatório"
# Exemplo: situacao_voto(17) -> "facultativo"
# ---------------------------------------------------------------------------
def situacao_voto(idade):
    pass


# ---------------------------------------------------------------------------
# Exercício 7: Ano bissexto
# Um ano é bissexto se:
#   - for divisível por 4 E não for divisível por 100,
#   - OU for divisível por 400.
# Devolva True ou False.
# Exemplos: 2024 -> True, 2023 -> False, 1900 -> False, 2000 -> True
# Dica: "divisível por 4" é o mesmo que "resto da divisão por 4 é zero".
# ---------------------------------------------------------------------------
def eh_bissexto(ano):
    pass


# ---------------------------------------------------------------------------
# Exercício 8: Frete
# Compras a partir de R$ 200 têm frete grátis; abaixo disso, o frete é R$ 15.
# Se `expresso` for True, soma-se R$ 10 ao frete (mesmo se for grátis).
# Devolva o valor do frete.
# Exemplos:
#   calcular_frete(250, False) -> 0
#   calcular_frete(250, True)  -> 10
#   calcular_frete(100, True)  -> 25
# ---------------------------------------------------------------------------
def calcular_frete(valor_compra, expresso):
    pass


# ---------------------------------------------------------------------------
# Exercício 9: Comissão de vendas
# O percentual depende do total vendido no mês:
#   até R$ 5.000 (inclusive):     5%
#   até R$ 10.000 (inclusive):    7%
#   acima de R$ 10.000:          10%
# O percentual vale sobre o total. Devolva a comissão arredondada
# para 2 casas.
# Exemplo: comissao(8000) -> 560.0
# ---------------------------------------------------------------------------
def comissao(total_vendas):
    pass


# ---------------------------------------------------------------------------
# Exercício 10: Tipo de triângulo
# Três medidas só formam um triângulo se CADA lado for MENOR que a soma
# dos outros dois. Se não formarem, devolva "inválido".
# Se formarem, devolva:
#   "equilátero": os três lados iguais
#   "isósceles":  exatamente dois lados iguais
#   "escaleno":   todos diferentes
# Exemplos: (3, 3, 3) -> "equilátero", (3, 4, 5) -> "escaleno",
#           (1, 2, 10) -> "inválido"
# ---------------------------------------------------------------------------
def tipo_triangulo(a, b, c):
    pass


# ---------------------------------------------------------------------------
# Exercício 11: Pedra, papel e tesoura
# Cada jogador escolhe "pedra", "papel" ou "tesoura".
# Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.
# Devolva "empate", "jogador 1" ou "jogador 2".
# Exemplo: jokenpo("pedra", "tesoura") -> "jogador 1"
# Dica: são 9 combinações, mas você não precisa de 9 ifs. Trate o empate
# primeiro e depois pense: em quais casos o jogador 1 vence?
# ---------------------------------------------------------------------------
def jokenpo(jogador1, jogador2):
    pass


# ---------------------------------------------------------------------------
# Exercício 12 (desafio): Estacionamento
# Regras de cobrança, pelo tempo em minutos:
#   até 15 minutos:  grátis (0)
#   até 60 minutos:  R$ 8
#   acima de 60:     R$ 8 pela primeira hora + R$ 4 por hora adicional
#                    OU FRAÇÃO (61 minutos já cobra uma hora adicional).
# Exemplos:
#   valor_estacionamento(10)  -> 0
#   valor_estacionamento(60)  -> 8
#   valor_estacionamento(61)  -> 12
#   valor_estacionamento(120) -> 12
#   valor_estacionamento(121) -> 16
# Dica: calcule os minutos que passaram da primeira hora. Quantas horas
# completas cabem neles (//)? Sobrou algum minuto (%)? Se sobrou, é mais
# uma hora.
# ---------------------------------------------------------------------------
def valor_estacionamento(minutos):
    pass
