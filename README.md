# Livros API com Interface Web

Este projeto é uma aplicação que integra uma API RESTful de gerenciamento de livros com uma interface web para cadastrar e avaliar livros, ainda em desenvolvimento. A API foi construída com Django e Django Ninja, enquanto a interface web foi desenvolvida com o framework Flet. A aplicação permite realizar operações Criar, listar em livros, além de possibilitar avaliações dos usuários.

## Tecnologias Utilizadas

- **Python 3.x**
- **Django 5.x** - Framework para desenvolvimento web.
- **Django Ninja** - Framework para criar APIs RESTful com Django.
- **Flet** - Framework para criação de interfaces gráficas com Python.
- **SQLite** - Banco de dados para persistência dos dados.
- **requests** - Biblioteca para realizar requisições HTTP.

## Funcionalidades

- **Cadastro de Livros**: O usuário pode cadastrar novos livros, informando o nome e o tipo de formato (Físico ou Amazon Kindle).
- **Exibição de Livros**: A interface exibe a lista de livros cadastrados na API.
- **Avaliação de Livros**: O usuário pode avaliar um livro atribuindo uma nota de 0 a 5 e escrevendo um comentário.
- **Exibição de Detalhes**: A página de detalhes do livro exibe informações como nome, nota e comentários do livro selecionado.

## Estrutura do Projeto

### Arquivos principais

- **`main.py`**: Contém o código da interface web utilizando o Flet, que interage com a API para exibir e cadastrar livros.
- **`connect.py`**: Realiza as requisições à API para obter os dados dos livros.
- **API Django**: A API que fornece os endpoints para gerenciar os livros e suas avaliações.

### Componentes principais da API

- **Livros**: Entidade que armazena informações sobre os livros, incluindo nome, formato (streaming), categorias, notas e comentários.
- **Categorias**: Classificações de livros para facilitar a busca e organização.

## Endpoints da API

### Livros

- **GET `/livros/`**: Retorna uma lista de todos os livros cadastrados.
- **POST `/livros/`**: Cria um novo livro com os dados fornecidos no corpo da requisição.
  - Campos obrigatórios: `nome`, `streaming`, `categorias`
  - `streaming` pode ser `"F"` (Físico) ou `"AK"` (Amazon Kindle).
- **PUT `/livros/{livro_id}`**: Atualiza a avaliação de um livro existente, permitindo adicionar uma `nota` (de 0 a 5) e `comentarios`.

### Sorteio de Livros

- **GET `/livros/sortear/`**: Retorna um livro aleatório, com filtros opcionais como `nota_minima`, `categorias`, e `reler`.

## Instalação e Configuração

### Pré-requisitos

- Python 3.x
- Virtualenv (recomendado)

### Passos para executar a aplicação

1. Clone o repositório:
   
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>

2. Crie e ative um ambiente virtual:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows

3. Inicie o servidor Django
   ```bash
    python manage.py runserver

4. Para a interface execute:
   ```bash
    python main.py

##Como usar

- Cadastro de Livros: Ao acessar a interface, o usuário pode digitar o nome do livro, escolher se é físico ou digital (Kindle) e clicar em "Cadastrar".
- Avaliação de Livros: Ao clicar sobre um livro na lista, o usuário será direcionado para a página de avaliação, onde pode deixar uma nota e um comentário.
- Exibição de Livros: Todos os livros cadastrados serão exibidos na página inicial.

## Licença
Esse README cobre todos os pontos principais, incluindo a estrutura, uso e explicações detalhadas sobre os módulos e classes do projeto.

   
