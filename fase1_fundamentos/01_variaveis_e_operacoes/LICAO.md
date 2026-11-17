# Módulo 01: Variáveis e operações

## 1. O que é um programa?

Um programa é uma lista de instruções que o computador executa **de cima para baixo**, uma linha por vez.
Crie um arquivo `teste.py` com o conteúdo abaixo e rode no terminal com `python teste.py`:

```python
print("Olá, mundo!")
print(2 + 3)
```

Saída:

```
Olá, mundo!
5
```

`print()` mostra algo na tela. É a sua principal ferramenta para "ver" o que o programa está fazendo.

## 2. Variáveis

Uma variável é um **nome que guarda um valor**. Pense numa etiqueta colada numa caixa.

```python
nome = "Ana"
idade = 30
salario = 2500.50

print(nome)    # Ana
print(idade)   # 30
```

- O `=` **não** significa "igual" como na matemática. Significa "guarde o valor da direita no nome da esquerda".
- Tudo depois de `#` é um **comentário**: o Python ignora, serve só para humanos lerem.
- Nomes de variáveis: use letras minúsculas e `_` para separar palavras (`salario_mensal`). Sem acentos, sem espaços, sem começar com número.

Uma variável pode mudar de valor:

```python
pontos = 10
pontos = pontos + 5   # pega o valor atual (10), soma 5, guarda de volta
print(pontos)         # 15
```

## 3. Tipos de dados

| Tipo | Nome no Python | Exemplos |
|---|---|---|
| Número inteiro | `int` | `7`, `-3`, `2026` |
| Número decimal | `float` | `3.14`, `2500.50` (use **ponto**, não vírgula) |
| Texto | `str` (string) | `"Ana"`, `'olá'` |
| Verdadeiro/falso | `bool` | `True`, `False` |

Para descobrir o tipo de um valor: `print(type(3.14))` mostra `<class 'float'>`.

## 4. Operações matemáticas

| Operador | Significado | Exemplo | Resultado |
|---|---|---|---|
| `+` | soma | `7 + 2` | `9` |
| `-` | subtração | `7 - 2` | `5` |
| `*` | multiplicação | `7 * 2` | `14` |
| `/` | divisão | `7 / 2` | `3.5` |
| `//` | divisão inteira (descarta o resto) | `7 // 2` | `3` |
| `%` | resto da divisão | `7 % 2` | `1` |
| `**` | potência | `7 ** 2` | `49` |

A ordem segue a matemática: parênteses primeiro, depois `**`, depois `* / // %`, depois `+ -`.

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
```

**Dica de lógica:** `%` é muito útil. `numero % 2` dá `0` se o número for par e `1` se for ímpar.

## 5. Texto (strings)

```python
nome = "Ana"
saudacao = "Olá, " + nome + "!"   # juntar textos com + (concatenação)
print(saudacao)                     # Olá, Ana!

print("ha" * 3)                     # hahaha
```

A forma mais prática de montar textos é a **f-string**: coloque `f` antes das aspas e as variáveis entre `{}`:

```python
nome = "Ana"
idade = 30
print(f"{nome} tem {idade} anos")   # Ana tem 30 anos

preco = 19.9
print(f"R$ {preco:.2f}")            # R$ 19.90  (:.2f = 2 casas decimais)
```

## 6. Convertendo tipos

```python
int("42")      # 42      (texto -> inteiro)
float("3.5")   # 3.5     (texto -> decimal)
str(42)        # "42"    (número -> texto)
int(3.9)       # 3       (corta a parte decimal, não arredonda)
round(3.9)     # 4       (arredonda)
```

## 7. Lendo dados do usuário

```python
nome = input("Qual o seu nome? ")
print(f"Prazer, {nome}!")
```

**Atenção:** `input()` sempre devolve texto. Para fazer contas, converta:

```python
idade = int(input("Sua idade: "))
print(f"Ano que vem você terá {idade + 1} anos")
```

## 8. Funções: só o necessário para os exercícios

Os exercícios usam **funções**. Vamos estudá-las a fundo no módulo 04; por enquanto, basta entender este modelo:

```python
def dobro(numero):        # "def" cria uma função chamada dobro, que recebe um valor "numero"
    resultado = numero * 2
    return resultado      # "return" devolve a resposta

print(dobro(5))           # 10
print(dobro(21))          # 42
```

- O código **dentro** da função fica recuado com **4 espaços**. O recuo é obrigatório no Python.
- `return` entrega o resultado para quem chamou a função. É diferente de `print`: `print` só mostra na tela, `return` devolve o valor para ser usado.

Nos exercícios, você vai substituir o `pass` (que significa "não faz nada ainda") pelo seu código, terminando com um `return`.

## Exercícios

Abra `exercicios.py`, resolva um por vez e rode os testes depois de cada um:

```bash
pytest fase1_fundamentos/01_variaveis_e_operacoes -v
```

Se travar por mais de 20 minutos num exercício, pule para o próximo e volte depois. Se continuar travado(a), me peça uma dica.
