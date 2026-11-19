"""
Módulo 01: Variáveis e operações

Instruções:
- Leia LICAO.md antes de começar.
- Em cada função, apague o `pass` e escreva seu código, terminando com `return`.
- Depois de cada exercício, rode:
      pytest fase1_fundamentos/01_variaveis_e_operacoes -v
- Não altere o nome das funções nem os parâmetros (os testes dependem deles).
"""


# ---------------------------------------------------------------------------
# Exercício 1: Soma
# Devolva a soma de a e b.
# Exemplo: soma(2, 3) -> 5
# ---------------------------------------------------------------------------
def soma(a, b):

    soma = a + b
    
    return soma



# ---------------------------------------------------------------------------
# Exercício 2: Área do retângulo
# Devolva a área de um retângulo (base vezes altura).
# Exemplo: area_retangulo(4, 5) -> 20
# ---------------------------------------------------------------------------
def area_retangulo(base, altura):

    area = base * altura

    return area


# ---------------------------------------------------------------------------
# Exercício 3: Média de três notas
# Devolva a média aritmética das três notas.
# Exemplo: media(7, 8, 9) -> 8.0
# Cuidado com a ordem das operações!
# ---------------------------------------------------------------------------
def media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3

    return media


# ---------------------------------------------------------------------------
# Exercício 4: Celsius para Fahrenheit
# Fórmula: F = C * 9 / 5 + 32
# Exemplo: celsius_para_fahrenheit(100) -> 212.0
# ---------------------------------------------------------------------------
def celsius_para_fahrenheit(celsius):

    fahrenheit = celsius * 9 / 5 + 32

    return fahrenheit


# ---------------------------------------------------------------------------
# Exercício 5: Saudação
# Devolva o texto "Olá, <nome>!" usando f-string.
# Exemplo: saudacao("Ana") -> "Olá, Ana!"
# ---------------------------------------------------------------------------
def saudacao(nome):

    saudacao = f"Olá, {nome}!"

    return saudacao


# ---------------------------------------------------------------------------
# Exercício 6: Último dígito
# Devolva o último dígito de um número inteiro positivo.
# Exemplo: ultimo_digito(2026) -> 6
# Dica: qual operador da tabela dá o "resto"? Resto da divisão por quanto?
# ---------------------------------------------------------------------------
def ultimo_digito(numero):

    return numero % 10



# ---------------------------------------------------------------------------
# Exercício 7: Formatar preço
# Devolva o valor como texto no formato "R$ 19.90" (sempre 2 casas decimais).
# Exemplo: formatar_preco(5) -> "R$ 5.00"
# ---------------------------------------------------------------------------
def formatar_preco(valor):

    return f"R$ {valor:.2f}"


# ---------------------------------------------------------------------------
# Exercício 8: Desconto
# Devolva o preço após aplicar um desconto percentual, arredondado
# para 2 casas decimais com round(valor, 2).
# Exemplo: aplicar_desconto(200, 15) -> 170.0   (15% de 200 é 30)
# ---------------------------------------------------------------------------
def aplicar_desconto(preco, percentual):

    desconto = preco * (percentual / 100)
    preco_final = preco - desconto

    return round(preco_final, 2)


# ---------------------------------------------------------------------------
# Exercício 9: Minutos em horas
# Receba um total de minutos e devolva um texto no formato "<h>h <m>min".
# Exemplos:
#   converter_minutos(125) -> "2h 5min"
#   converter_minutos(60)  -> "1h 0min"
#   converter_minutos(45)  -> "0h 45min"
# Dica: use // e %.
# ---------------------------------------------------------------------------
def converter_minutos(total_minutos):

    horas = total_minutos // 60
    minutos = total_minutos % 60

    return f"{horas}h {minutos}min"


# ---------------------------------------------------------------------------
# Exercício 10: Pagamento com horas extras
# Um funcionário recebe `valor_hora` por hora normal. Cada hora extra vale
# 50% a mais que a hora normal. Devolva o total a receber, arredondado para
# 2 casas decimais.
# Exemplo: pagamento(20, 160, 10) -> 3500.0
#   (160 * 20 = 3200 normais; hora extra = 30; 10 * 30 = 300; total 3500)
# ---------------------------------------------------------------------------
def pagamento(valor_hora, horas_normais, horas_extras):

    valor_hora_extra = valor_hora * 1.5
    total_horas_normais = valor_hora * horas_normais
    total_horas_extras = valor_hora_extra *  horas_extras
    total = total_horas_normais + total_horas_extras

    return round(total, 2)


# ---------------------------------------------------------------------------
# Exercício 11 (desafio): Caixa eletrônico
# Um caixa tem notas de 100, 50 e 10. Dado um valor inteiro, diga quantas
# notas de cada usar (sempre começando pelas maiores) e quanto sobra.
# Devolva exatamente neste formato:
#   "100: 3 | 50: 1 | 10: 2 | resto: 7"
# Exemplo: caixa_eletronico(377) -> "100: 3 | 50: 1 | 10: 2 | resto: 7"
# Dica: depois de calcular as notas de 100, quanto ainda falta pagar?
# ---------------------------------------------------------------------------
def caixa_eletronico(valor):

    notas_100 = valor // 100
    resto_100 = valor % 100

    notas_50 = resto_100 // 50
    resto_50 = resto_100 % 50

    notas_10 = resto_50 // 10
    resto_10 = resto_50 % 10

    return f"100: {notas_100} | 50: {notas_50} | 10: {notas_10} | resto: {resto_10}"

