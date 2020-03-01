# Template-Django

Site para o escritório B&amp;C Advogados.

- [Template-Django](#template-django)
  - [Requerimentos](#requerimentos)
  - [Instalação](#instala%c3%a7%c3%a3o)
    - [Windows](#windows)
    - [Ubuntu](#ubuntu)
  - [Rodando o projeto](#rodando-o-projeto)

## Requerimentos

- Windows 10 ou Ubuntu 18.04 ou superior
- Python 3.7 ou superior
- Virtualenv
- Node.js
- VS Code

## Instalação

### Windows

Siga os seguintes passos para fazer a instalação das dependências do projeto no windows 10.

1. Git
   - Instale o Git
     - Vá para o [site do git](https://git-scm.com/download/win) e faça download.
2. Projeto
   - Baixe o projeto
     - ```$ git clone https://github.com/lucas625/Template-Django.git```
   - Vá para a pasta do projeto
     - ```$ cd Template-Django```
3. Python
   - Instale o Python e o Pip
     - Vá para o [site do python](https://www.python.org/downloads/windows/) e faça download.
   - Verifique a versão do Python
     - ```$ python -V```
4. Pip
   - Atualize o Pip
     - ```$ python -m pip install --upgrade pip```
   - Verifique a versão do Pip
     - ```$ pip -V```
5. Virtualenv
   - Instale a Virtualenv
     - ```$ pip install virtualenv```
   - Crie a Virtualenv
     - ```$ python -m venv venv```
   - Inicie a Virtualenv
     - ```$ venv\Scripts\activate```
   - Verifique se a versão do Python é a desejada
     - ```$ python -V```
   - Atualize o Pip
     - ```$ python -m pip install --upgrade pip```
   - Instale as dependências do python
     - ```$ pip install -r requirements.txt```
6. Node.js
   - Instale o Node.js e o npm
     - Vá para o [site do Node](https://nodejs.org/en/download/) e faça download.
   - Verifique a versão do node
     - ```$ node --version```
   - Verifique a versão do npm
     - ```$ npm --version```
   - **OBS**: Em caso de algum erro verifique se o node e o npm estão na configurados nas variáveis de ambiente do windows.
   - Instale as dependências do node
     - ```$ npm install```

### Ubuntu

Siga os seguintes passos para fazer a instalação das dependências do projeto no ubuntu.

1. Geral
   - Atualize as informações de dependências do computador
     - ```$ sudo apt-get update```
2. Git
   - Instale o Git
     - ```$ sudo apt install git```
3. Projeto
   - Baixe o projeto
     - ```$ git clone https://github.com/lucas625/Template-Django.git```
   - Vá para a pasta do projeto
     - ```$ cd Template Django```
4. Python
   - Instale o Python
     - ```$ sudo apt-get install python3.7```
   - Verifique a versão do Python
     - ```$ python3 -V```
5. Pip
   - Instale o Pip
     - ```$ sudo apt install python3-pip```
   - Atualize o Pip
     - ```$ sudo -H pip3 install --upgrade pip```
   - Verifique a versão do Pip
     - ```$ pip3 -V```
6. Virtualenv
   - Instale a Virtualenv
     - ```$ sudo apt install python3-venv```
     - Caso o apt não funcione, use:
       - ```$ pip3 install virtualenv```
   - Crie a Virtualenv
     - ```$ python3 -m venv venv```
   - Inicie a Virtualenv
     - ```$ source venv/bin/activate```
   - Verifique se a versão do Python é a desejada
     - ```$ python -V```
   - Atualize o Pip
     - ```$ pip install --upgrade pip```
   - Instale as dependências do python
     - ```$ pip install -r requirements.txt```
7. Node.js
   - Instale o Node.js
     - ```$ sudo apt-get install nodejs```
8. Npm
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

   - Feche a abra o terminal na pasta do projeto para garantir que o node foi atualizado, lembrando de iniciar a **virtualenv**.
   - Instale as dependências do node
     - ```$ npm install```

9. Pre-commit
   - Instale os hooks do pre-commit
     - ```$ pre-commit install```

## Rodando o projeto

Após ter todas as dependências instaladas você pode seguir os próximos passos.

1. Segurança do projeto

   - Crie um arquivo **.env** e adicione as seguintes chaves:

    ```.env
    SECRET_KEY = qualquer_coisa
    ```

    - **OBS**: Este arquivo não pode ser adicionado ao github por questões de segurança.

2. Migrações

    - O Django necessita que você rode migrações:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Rodar o projeto
   - Rodar o servidor em conjunto com o webpack
     - ```$ npm run start```
