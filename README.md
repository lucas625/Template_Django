# Template_Django

[![Build Status](https://travis-ci.org/lucas625/Template_Django.svg?branch=master)](https://travis-ci.org/lucas625/Template_Django) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/43e28987829f4de1a99b94d6798640d9)](https://www.codacy.com/manual/lucas625/Template_Django?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lucas625/Template_Django&amp;utm_campaign=Badge_Grade)

Template de projeto Django.

- [Template-Django](#template-django)
  - [Equipe](#equipe)
  - [Requerimentos](#requerimentos)
  - [Guias](#guias)
  - [Instalação](#instala%c3%a7%c3%a3o)
  - [Rodando o projeto](#rodando-o-projeto)
  - [Tópicos Adicionais](#t%c3%b3picos-adicionais)

## Equipe

Desenvolvedor: [Lucas Aurelio](https://github.com/lucas625)

## Requerimentos

- [Pyenv](https://github.com/pyenv/pyenv#installation)
- [Pipenv](https://github.com/pypa/pipenv)
- [Node.js](https://nodejs.org/en/)

## Guias

- [The Twelve-Factor App](https://12factor.net/)

## Instalação

Siga os seguintes passos para fazer a instalação das dependências do projeto

1. Git

   - Instale o [Git](https://git-scm.com/)

2. Projeto

   - Baixe o projeto
     - ```$ git clone https://github.com/lucas625/Template_Django.git```

3. Instale [Pyenv](https://github.com/pyenv/pyenv)

   - **Caso esteja usando o windows, pode ser mais fácil apenas baixar o python 3.7**

4. Instale [Pipenv](https://github.com/pyenv/pyenv)

5. Prepare o ambiente

    1. Vá para a pasta do projeto
    2. ```$ pipenv --python 3.7```
    3. ```$ pipenv shell```
    4. ```$ pipenv install --dev```

6. Node.js

   - Instale o Node.js
     - ```$ sudo apt-get install nodejs```

7. Npm

   - Instale o npm
     - ```$ sudo apt-get install npm```
   - Atualize o npm
     - ```$ sudo npm install -g npm@next```
   - Use o npm para atualizar o node

        ```sh
        sudo npm cache clean -f
        sudo npm install -g n
        sudo n stable
        ```

   - Instale as dependências do node
     - ```$ npm install```

8. Pre-commit

    - Instale os hooks do pre-commit
      - ```$ pre-commit install```

## Rodando o projeto

Após ter todas as dependências instaladas você pode seguir os próximos passos.

1. Segurança do projeto

   - Adicione as variáveis de ambiente
        - Ubuntu

            ```sh
            export SECRET_KEY=$(python resources/scripts/get_secret_key.py)
            export ALLOWED_HOSTS=$(python resources/scripts/get_allowed_hosts.py)
            export DEBUG='True'
            ```

        - Windows

            ```sh
            set SECRET_KEY='Qualquer coisa'
            set ALLOWED_HOSTS='[*]'
            set DEBUG='True'
            ```

2. Migrações

    - O Django necessita que você rode migrações:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Testando

    - Testar sem cobertura

        ```python manage.py test --no-input --debug-mode```

    - Testar com cobertura

        ```coverage run manage.py test --no-input --debug-mode -v 2```

4. Rodar o projeto
   - Rodar apenas servidor
     - ```$ python manage.py runserver```

   - Rodar o servidor em conjunto com o webpack
     - ```$ npm run start```

## Tópicos Adicionais

- Linter
  - O linter utilizado é o pylint com a extensão do django.

    ```pylint --load-plugins pylint_django pasta```

    - É necessário rodar o pylint para todos os arquivos e fazer as correções necessárias sempre antes de realizar um commit.
