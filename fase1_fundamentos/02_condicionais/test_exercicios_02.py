"""Testes do Módulo 02. Não edite este arquivo."""

from exercicios_02 import (
    calcular_frete,
    classificar_numero,
    comissao,
    eh_bissexto,
    eh_par,
    jokenpo,
    maior_de_dois,
    maior_de_tres,
    situacao_aluno,
    situacao_voto,
    tipo_triangulo,
    valor_estacionamento,
)


def test_01_eh_par():
    assert eh_par(4) is True
    assert eh_par(7) is False
    assert eh_par(0) is True
    assert eh_par(-3) is False


def test_02_maior_de_dois():
    assert maior_de_dois(3, 8) == 8
    assert maior_de_dois(8, 3) == 8
    assert maior_de_dois(5, 5) == 5
    assert maior_de_dois(-2, -9) == -2


def test_03_classificar_numero():
    assert classificar_numero(10) == "positivo"
    assert classificar_numero(-5) == "negativo"
    assert classificar_numero(0) == "zero"
    assert classificar_numero(0.5) == "positivo"


def test_04_situacao_aluno():
    assert situacao_aluno(9) == "Aprovado"
    assert situacao_aluno(7) == "Aprovado"
    assert situacao_aluno(6.9) == "Recuperação"
    assert situacao_aluno(5) == "Recuperação"
    assert situacao_aluno(4.9) == "Reprovado"
    assert situacao_aluno(0) == "Reprovado"


def test_05_maior_de_tres():
    assert maior_de_tres(4, 9, 2) == 9
    assert maior_de_tres(9, 4, 2) == 9
    assert maior_de_tres(2, 4, 9) == 9
    assert maior_de_tres(5, 5, 1) == 5
    assert maior_de_tres(1, 5, 5) == 5
    assert maior_de_tres(5, 1, 5) == 5
    assert maior_de_tres(-1, -7, -3) == -1


def test_06_situacao_voto():
    assert situacao_voto(10) == "não vota"
    assert situacao_voto(15) == "não vota"
    assert situacao_voto(16) == "facultativo"
    assert situacao_voto(17) == "facultativo"
    assert situacao_voto(18) == "obrigatório"
    assert situacao_voto(69) == "obrigatório"
    assert situacao_voto(70) == "facultativo"
    assert situacao_voto(85) == "facultativo"


def test_07_eh_bissexto():
    assert eh_bissexto(2024) is True
    assert eh_bissexto(2023) is False
    assert eh_bissexto(1900) is False
    assert eh_bissexto(2000) is True
    assert eh_bissexto(2100) is False


def test_08_calcular_frete():
    assert calcular_frete(250, False) == 0
    assert calcular_frete(250, True) == 10
    assert calcular_frete(200, False) == 0
    assert calcular_frete(199.99, False) == 15
    assert calcular_frete(100, True) == 25


def test_09_comissao():
    assert comissao(4000) == 200.0
    assert comissao(5000) == 250.0
    assert comissao(8000) == 560.0
    assert comissao(10000) == 700.0
    assert comissao(20000) == 2000.0


def test_10_tipo_triangulo():
    assert tipo_triangulo(3, 3, 3) == "equilátero"
    assert tipo_triangulo(3, 3, 5) == "isósceles"
    assert tipo_triangulo(5, 3, 5) == "isósceles"
    assert tipo_triangulo(3, 5, 5) == "isósceles"
    assert tipo_triangulo(3, 4, 5) == "escaleno"
    assert tipo_triangulo(1, 2, 10) == "inválido"
    assert tipo_triangulo(10, 2, 1) == "inválido"
    assert tipo_triangulo(1, 1, 2) == "inválido"


def test_11_jokenpo():
    assert jokenpo("pedra", "pedra") == "empate"
    assert jokenpo("papel", "papel") == "empate"
    assert jokenpo("pedra", "tesoura") == "jogador 1"
    assert jokenpo("tesoura", "papel") == "jogador 1"
    assert jokenpo("papel", "pedra") == "jogador 1"
    assert jokenpo("tesoura", "pedra") == "jogador 2"
    assert jokenpo("papel", "tesoura") == "jogador 2"
    assert jokenpo("pedra", "papel") == "jogador 2"


def test_12_valor_estacionamento():
    assert valor_estacionamento(10) == 0
    assert valor_estacionamento(15) == 0
    assert valor_estacionamento(16) == 8
    assert valor_estacionamento(60) == 8
    assert valor_estacionamento(61) == 12
    assert valor_estacionamento(120) == 12
    assert valor_estacionamento(121) == 16
    assert valor_estacionamento(300) == 24
