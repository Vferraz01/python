"""Testes do Módulo 01. Não edite este arquivo."""

import pytest

from exercicios import (
    aplicar_desconto,
    area_retangulo,
    caixa_eletronico,
    celsius_para_fahrenheit,
    converter_minutos,
    formatar_preco,
    media,
    pagamento,
    saudacao,
    soma,
    ultimo_digito,
)


def test_01_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(2.5, 0.5) == 3.0


def test_02_area_retangulo():
    assert area_retangulo(4, 5) == 20
    assert area_retangulo(1.5, 2) == 3.0


def test_03_media():
    assert media(7, 8, 9) == 8.0
    assert media(10, 0, 5) == 5.0
    assert media(6, 7, 7) == pytest.approx(6.6667, rel=1e-3)


def test_04_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(100) == 212.0
    assert celsius_para_fahrenheit(0) == 32.0
    assert celsius_para_fahrenheit(-40) == -40.0


def test_05_saudacao():
    assert saudacao("Ana") == "Olá, Ana!"
    assert saudacao("Carlos") == "Olá, Carlos!"


def test_06_ultimo_digito():
    assert ultimo_digito(2026) == 6
    assert ultimo_digito(7) == 7
    assert ultimo_digito(130) == 0


def test_07_formatar_preco():
    assert formatar_preco(19.9) == "R$ 19.90"
    assert formatar_preco(5) == "R$ 5.00"
    assert formatar_preco(1234.567) == "R$ 1234.57"


def test_08_aplicar_desconto():
    assert aplicar_desconto(200, 15) == 170.0
    assert aplicar_desconto(100, 0) == 100.0
    assert aplicar_desconto(59.90, 10) == 53.91


def test_09_converter_minutos():
    assert converter_minutos(125) == "2h 5min"
    assert converter_minutos(60) == "1h 0min"
    assert converter_minutos(45) == "0h 45min"


def test_10_pagamento():
    assert pagamento(20, 160, 10) == 3500.0
    assert pagamento(15.5, 100, 0) == 1550.0
    assert pagamento(10, 0, 3) == 45.0


def test_11_caixa_eletronico():
    assert caixa_eletronico(377) == "100: 3 | 50: 1 | 10: 2 | resto: 7"
    assert caixa_eletronico(100) == "100: 1 | 50: 0 | 10: 0 | resto: 0"
    assert caixa_eletronico(9) == "100: 0 | 50: 0 | 10: 0 | resto: 9"
