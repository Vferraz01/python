# Trilha: Engenheiro(a) de IA

Repositório de estudos em Python, do zero até IA aplicada.
Ritmo planejado: **4 horas por dia**.

## Roteiro

Os prazos são estimativas para 4h/dia. Se precisar de mais tempo em alguma fase, tudo bem: entender bem vale mais do que correr.

| Fase | Duração | Conteúdo | Ao final você consegue... |
|---|---|---|---|
| **1. Fundamentos** | semanas 1–6 | variáveis, tipos, condicionais, laços, funções, listas, dicionários, strings | resolver problemas simples de lógica sozinho(a) |
| **2. Lógica e algoritmos** | semanas 7–10 | recursão, busca, ordenação, Big-O, pilhas, filas | resolver desafios fáceis/médios de entrevista |
| **3. Python profissional** | semanas 11–16 | orientação a objetos, módulos, exceções, arquivos, `pytest`, Git, ambientes virtuais, SQL básico | construir programas organizados e testados |
| **4. Dados** | semanas 17–21 | NumPy, Pandas, Matplotlib, estatística básica, APIs HTTP | analisar dados reais e gerar gráficos |
| **5. Machine Learning** | semanas 22–28 | scikit-learn, regressão, classificação, avaliação, noções de redes neurais | treinar e avaliar modelos |
| **6. Engenharia de IA** | semanas 29–36 | APIs de LLMs, prompts, embeddings, RAG, agentes, FastAPI, Docker, deploy | colocar uma aplicação de IA no ar |
| **7. Portfólio** | semanas 37+ | 2–3 projetos completos no GitHub, currículo, entrevistas | se candidatar a vagas júnior |

### Sugestão de divisão das 4 horas diárias

- **1h** estudando o conteúdo (lição do módulo + documentação)
- **2h30** praticando (exercícios do repositório)
- **30min** revisando: refazer um exercício antigo sem olhar, anotar dúvidas

## Como usar este repositório

Cada módulo tem três arquivos:

- `LICAO.md`: a explicação do conteúdo. Leia primeiro.
- `exercicios.py`: os exercícios. Você escreve o código aqui, no lugar dos `pass`.
- `test_exercicios.py`: testes automáticos que conferem suas respostas. **Não edite este arquivo.**

### Configuração (uma vez só)

1. Instale o Python 3.12 ou mais novo: https://www.python.org/downloads/
   No Windows, marque a opção **"Add Python to PATH"** durante a instalação.
2. Instale o VS Code (https://code.visualstudio.com/) e a extensão **Python** dele.
3. Clone este repositório e, dentro da pasta, instale o pytest:

```bash
pip install -r requirements.txt
```

### Conferindo seus exercícios

Para rodar os testes de um módulo:

```bash
pytest fase1_fundamentos/01_variaveis_e_operacoes -v
```

- `PASSED` (verde): exercício certo.
- `FAILED` (vermelho): ainda não está certo. Leia a mensagem, ela mostra o valor esperado e o que seu código devolveu.

Quando terminar um módulo (ou travar em algum exercício), faça commit e me peça uma revisão.

## Progresso

### Fase 1: Fundamentos

- [x] 01: Variáveis e operações
- [ ] 02: Condicionais (`if`/`elif`/`else`)
- [ ] 03: Laços (`for`/`while`)
- [ ] 04: Funções
- [ ] 05: Listas e tuplas
- [ ] 06: Strings
- [ ] 07: Dicionários e conjuntos
- [ ] 08: Projeto da fase: gerenciador de despesas no terminal
