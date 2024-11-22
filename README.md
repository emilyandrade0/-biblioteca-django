# Projeto de Coleção de Livros

Este projeto é uma API RESTful construída com Django e Django REST Framework para gerenciar coleções de livros. O sistema permite que usuários registrem coleções de livros, associem livros a essas coleções e restrinjam permissões de edição com base no dono da coleção.

## Funcionalidades

- **Livros**: Gerenciar livros, incluindo título, autor, categoria e data de publicação.
- **Categorias**: Criar e listar categorias de livros.
- **Autores**: Criar e listar autores de livros.
- **Coleções**: Criar coleções de livros, associar livros a coleções e permitir que cada usuário só edite suas próprias coleções.

## Tecnologias Utilizadas

- **Django**: Framework web para construir a API.
- **Django REST Framework**: Framework para criar a API RESTful.
- **django-filter**: Biblioteca para filtrar resultados na API.
- **drf-spectacular**: Gerar a documentação da API (Swagger/OpenAPI).

## Endpoints

A API possui os seguintes endpoints:

### Livros

- **GET /api/livros/**: Lista todos os livros.
- **POST /api/livros/**: Cria um novo livro.
- **GET /api/livros/{id}/**: Recupera os detalhes de um livro específico.
- **PUT /api/livros/{id}/**: Atualiza um livro específico.
- **DELETE /api/livros/{id}/**: Deleta um livro específico.

### Categorias

- **GET /api/categorias/**: Lista todas as categorias.
- **POST /api/categorias/**: Cria uma nova categoria.
- **GET /api/categorias/{id}/**: Recupera os detalhes de uma categoria específica.
- **PUT /api/categorias/{id}/**: Atualiza uma categoria específica.
- **DELETE /api/categorias/{id}/**: Deleta uma categoria específica.

### Autores

- **GET /api/autores/**: Lista todos os autores.
- **POST /api/autores/**: Cria um novo autor.
- **GET /api/autores/{id}/**: Recupera os detalhes de um autor específico.
- **PUT /api/autores/{id}/**: Atualiza um autor específico.
- **DELETE /api/autores/{id}/**: Deleta um autor específico.

### Coleções

- **GET /api/colecoes/**: Lista todas as coleções.
- **POST /api/colecoes/**: Cria uma nova coleção (apenas usuários autenticados).
- **GET /api/colecoes/{id}/**: Recupera os detalhes de uma coleção específica.
- **PUT /api/colecoes/{id}/**: Atualiza uma coleção (apenas o colecionador da coleção).
- **DELETE /api/colecoes/{id}/**: Deleta uma coleção (apenas o colecionador da coleção).

## Superusuário

Dados do superusuário para acessar o sistema:

- **Username**: `adm`
- **Email**: `adm@gmail.com`
- **Senha**: `12345`

## Autenticação e Permissões

- **Permissões para Coleções**: Somente o colecionador de uma coleção pode editar ou deletar sua coleção. Outros usuários podem apenas visualizar as coleções.
- **Autenticação**: Os usuários precisam estar autenticados para criar ou modificar coleções.

## Documentação Swagger

A documentação da API pode ser acessada em [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) após rodar o servidor Django. Ela fornece uma interface interativa para testar os endpoints.

## Testes Unitários

Este projeto inclui testes automatizados para garantir que as funcionalidades da API estejam funcionando conforme esperado. Você pode rodar os testes utilizando o Django Test Framework.

### Rodando os Testes

Para rodar os testes, basta usar o seguinte comando:

```bash
python manage.py test
