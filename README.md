# api-articles

## Descrição
Aplicação web desenvolvida em Python utilizando o framework Django, criada para a publicação e gerenciamento de artigos.

## Instalação
Certifique-se de ter o Python e o Docker instalados em sua máquina.

1. Clonar o repositório
    ```bash
    git@github.com:lbrighi/articles-api.git
    ```

2. Rodar a aplicação com docker
    ```bash
    docker compose up --build
    ```
    Ao rodar a aplicaçao o banco é populado.

    Acesse a aplicação em [http://localhost:8000](http://localhost:8000).


## Ambiente de teste

Usuário:
    ```
    teste@email.com
    ```

Senha:
    ```
    123456
    ```

Swagger:
    ```
    http://localhost:8000/api/swagger/
    ```

## Front-End
Acesse a aplicação em [https://github.com/lbrighi/articles-web](https://github.com/lbrighi/articles-web)
