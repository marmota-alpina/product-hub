# Product Hub API

**Product Hub API** é uma aplicação desenvolvida com Flask que fornece uma interface para gerenciamento de produtos. Utiliza uma arquitetura baseada em microsserviços para fornecer flexibilidade e escalabilidade.

## Visão Geral

Este projeto é uma API que permite a criação, leitura, atualização e exclusão (CRUD) de produtos. A API é construída com Flask e usa SQLAlchemy para interação com o banco de dados. A documentação da API é gerada automaticamente usando Flask-OpenAPI3.

## Tecnologias

- **Python:** ^3.10
- **Flask:** ^3.0.3
- **Flask-SQLAlchemy:** ^3.1.1
- **Flask-OpenAPI3:** ^3.1.3
- **Psycopg2-Binary:** ^2.9.9
- **Pydantic-Settings:** ^2.3.4
- **Flask-CORS:** ^4.0.1
- **Requests:** ^2.32.3

## Instalação

Para configurar o ambiente de desenvolvimento e instalar as dependências do projeto, siga estes passos:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/marmota-alpina/product-hub.git
   cd product-hub
   ```

2. **Instale o Poetry (se ainda não estiver instalado):**

   ```bash
   pip install poetry
   ```

3. **Instale as dependências do projeto:**

   ```bash
   poetry install
   ```

4. **Configure o banco de dados:**

   Certifique-se de que o banco de dados PostgreSQL esteja configurado e acessível. Atualize as variáveis de ambiente conforme necessário para conectar-se ao banco de dados.

5. **Execute as migrações do banco de dados:**

   ```bash
   poetry run flask db upgrade
   ```

## Uso

Para iniciar a API, execute o comando abaixo:

```bash
poetry run flask run
```

A API estará disponível em [http://localhost:5000](http://localhost:5000).

## Endpoints

A documentação da API está disponível em `/docs` e fornece detalhes sobre todos os endpoints disponíveis, incluindo exemplos de requisições e respostas.

## Contribuição

Se você deseja contribuir para o projeto, por favor, siga estas etapas:

1. Faça um fork do repositório: [Product Hub Fork](https://github.com/marmota-alpina/product-hub/fork)
2. Crie uma branch para suas alterações.
3. Faça um commit das suas alterações.
4. Envie um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato

Se você tiver alguma dúvida ou precisar de ajuda, sinta-se à vontade para entrar em contato:

- **Autor:** Jeferson Ferreira da Silva
- **E-mail:** jeferson.mab@gmail.com

---

Se precisar de mais alguma alteração ou informação adicional, é só me avisar!
