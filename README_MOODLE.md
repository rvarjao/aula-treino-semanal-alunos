# Atividade — Programa Semanal de Treino

## Objetivo

Nesta atividade, você irá completar um sistema web simples para entender como estas partes se conectam:

- **Backend** (Python)
- **Banco de dados** (SQLite)
- **Frontend** (HTML + CSS)

O projeto foi entregue com partes incompletas. Sua missão é identificar os pontos marcados com `TODO` e completar o sistema.

## Estrutura do projeto

- `app.py` → lógica do sistema
- `schema.sql` → estrutura do banco
- `static/style.css` → estilo da página

## O que o sistema deve fazer

O sistema deve permitir cadastrar itens de um programa semanal de treino.

Cada registro deve ter:
- dia
- grupo muscular
- exercício
- carga

Exemplo:
- Segunda — Costas — Puxada frontal — 35kg
- Terça — Peito — Supino reto — 40kg

## Tarefas

### 1. Complete o banco de dados
No arquivo `schema.sql`, complete a criação da tabela `treino_semanal`.

### 2. Complete a inicialização do banco
No arquivo `app.py`, faça o sistema ler o arquivo `schema.sql` e executar o script SQL.

### 3. Complete a listagem
No arquivo `app.py`, escreva a consulta para buscar os treinos no banco.

### 4. Mostre os treinos na tela
No arquivo `app.py`, percorra a lista de treinos e monte o HTML com os dados.

### 5. Complete o cadastro
No arquivo `app.py`, escreva a query de inserção no banco.

### 6. Revise o formulário
No HTML da rota `/novo`, melhore os textos e placeholders.

### 7. Melhore o visual
No arquivo `static/style.css`, personalize a página.

## Como executar

1. Instale o Flask:
   `pip install flask`

2. Execute:
   `python app.py`

3. Abra no navegador:
   `http://localhost:5000`

## Entrega

Você deverá entregar:

### Arquivos
- `app.py`
- `schema.sql`
- pasta `static/`

### Prints
Envie pelo menos 2 prints:
1. tela principal com treinos cadastrados
2. tela de cadastro

## Critério principal
Mais importante do que deixar bonito é mostrar que você entendeu:
- como o formulário envia dados
- como o Python salva no banco
- como os dados aparecem na tela