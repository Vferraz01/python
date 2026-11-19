# Módulo 02: Condicionais

Até agora, seus programas executavam **todas** as linhas, sempre na mesma ordem.
Neste módulo, o programa passa a **tomar decisões**: executar um trecho só se uma condição for verdadeira.

É aqui que a lógica de programação começa de verdade.

## 1. Comparações

Uma comparação faz uma pergunta e a resposta é sempre `True` (verdadeiro) ou `False` (falso).

| Operador | Pergunta | Exemplo | Resultado |
|---|---|---|---|
| `==` | é igual? | `5 == 5` | `True` |
| `!=` | é diferente? | `5 != 3` | `True` |
| `>` | é maior? | `5 > 3` | `True` |
| `<` | é menor? | `5 < 3` | `False` |
| `>=` | é maior ou igual? | `5 >= 5` | `True` |
| `<=` | é menor ou igual? | `4 <= 3` | `False` |

**Atenção ao erro mais comum do módulo:** `=` guarda um valor e `==` compara dois valores.

```python
idade = 18          # guarda 18 em idade
print(idade == 18)  # pergunta: idade é igual a 18? -> True
```

Textos também podem ser comparados, e a comparação diferencia maiúsculas de minúsculas:

```python
print("pedra" == "pedra")   # True
print("Pedra" == "pedra")   # False
```

O resultado de uma comparação é um valor como qualquer outro, então pode ir para uma variável ou para um `return`:

```python
def eh_maior_de_idade(idade):
    return idade >= 18

print(eh_maior_de_idade(20))   # True
print(eh_maior_de_idade(15))   # False
```

## 2. `if`: executar só se a condição for verdadeira

```python
saldo = 50
valor_compra = 80

if valor_compra > saldo:
    print("Saldo insuficiente")

print("Fim")
```

Regras:
- A linha do `if` termina com **dois-pontos** `:`.
- O código que depende da condição fica **recuado com 4 espaços**. É o recuo que diz ao Python o que está "dentro" do `if`.
- `print("Fim")` não está recuado, então roda sempre.

## 3. `else`: o caminho alternativo

```python
if valor_compra > saldo:
    print("Saldo insuficiente")
else:
    print("Compra aprovada")
```

Exatamente **um** dos dois blocos vai rodar, nunca os dois e nunca nenhum.

## 4. `elif`: várias possibilidades

`elif` significa "senão, se". Use quando houver mais de dois caminhos:

```python
def classificar_temperatura(graus):
    if graus < 15:
        return "frio"
    elif graus < 25:
        return "agradável"
    else:
        return "quente"
```

O Python testa as condições **de cima para baixo** e para na **primeira** verdadeira. Por isso, no `elif graus < 25`, já sabemos que `graus` é pelo menos 15: se fosse menor, o primeiro `if` teria pegado.

**A ordem importa.** Veja este erro:

```python
# ERRADO: 30 graus é < 100, então cai sempre no primeiro bloco
if graus < 100:
    return "agradável"
elif graus < 15:
    return "frio"      # nunca é alcançado
```

Uma boa regra: vá do caso mais restrito para o mais geral, ou do menor para o maior.

## 5. Combinando condições: `and`, `or`, `not`

| Operador | Significado | Verdadeiro quando... |
|---|---|---|
| `and` | "e" | **as duas** condições são verdadeiras |
| `or` | "ou" | **pelo menos uma** é verdadeira |
| `not` | "não" | inverte: `True` vira `False` e vice-versa |

```python
idade = 25
tem_cnh = True

if idade >= 18 and tem_cnh:
    print("Pode dirigir")

dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Fim de semana")

if not tem_cnh:
    print("Precisa tirar a CNH")
```

Cuidado com um erro clássico:

```python
# ERRADO: o Python entende isso de outro jeito, e o resultado é sempre verdadeiro
if dia == "sábado" or "domingo":

# CERTO: cada lado do "or" precisa ser uma comparação completa
if dia == "sábado" or dia == "domingo":
```

Para faixas de valores, o Python permite uma forma curta:

```python
if 18 <= idade <= 65:    # o mesmo que: idade >= 18 and idade <= 65
    print("Faixa de idade ativa")
```

Quando misturar `and` e `or` na mesma condição, use parênteses para deixar a ordem clara:

```python
if (a > 0 and b > 0) or c == 0:
```

## 6. `if` dentro de `if`

Dá para colocar uma decisão dentro de outra. Cada nível ganha mais 4 espaços:

```python
if usuario_logado:
    if eh_administrador:
        print("Painel de administração")
    else:
        print("Painel comum")
else:
    print("Faça login")
```

Use com moderação. Se passar de 2 ou 3 níveis, quase sempre existe um jeito mais simples com `elif` ou `and`.

## 7. Como pensar num problema com condições

Antes de programar, escreva os casos **em português**. Exemplo: "frete grátis acima de R$ 200":

1. Quais são os caminhos possíveis? Com frete grátis e sem frete grátis.
2. O que decide o caminho? O valor da compra.
3. E os **casos de borda**? Uma compra de **exatamente** R$ 200 tem frete grátis? Em "acima de", não. Em "a partir de", sim. Isso decide entre `>` e `>=`.

Os testes dos exercícios sempre verificam os casos de borda. Se um teste falhar com um valor "redondo", desconfie do `>` versus `>=`.

## Exercícios

Os exercícios deste módulo estão em `exercicios_02.py`. Para conferir:

```bash
pytest fase1_fundamentos/02_condicionais -v
```

Os exercícios 1 a 9 usam só o que está nesta lição. O 10 e o 11 exigem pensar em vários casos. O 12 é um desafio: rascunhe os casos no papel antes de programar.
