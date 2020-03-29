# Template_Django

[![Build Status](https://travis-ci.org/lucas625/Template_Django.svg?branch=master)](https://travis-ci.org/lucas625/Template_Django) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/43e28987829f4de1a99b94d6798640d9)](https://www.codacy.com/manual/lucas625/Template_Django?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lucas625/Template_Django&amp;utm_campaign=Badge_Grade)[![codecov](https://codecov.io/gh/lucas625/Template_Django/branch/master/graph/badge.svg)](https://codecov.io/gh/lucas625/Template_Django)

Django template project.

- [Template_Django](#templatedjango)
  - [Team](#team)
  - [Requirements](#requirements)
  - [Guidelines](#guidelines)
  - [Installation](#installation)
  - [Run the project](#run-the-project)
  - [Testing](#testing)
  - [Additional Topics](#additional-topics)

## Team

Developer: [Lucas Aurelio](https://github.com/lucas625)

## Requirements

- [Pyenv](https://github.com/pyenv/pyenv#installation)
- [Pipenv](https://github.com/pypa/pipenv)
- [Node.js](https://nodejs.org/en/)

## Guidelines

- [The Twelve-Factor App](https://12factor.net/)

## Installation

Follow the next steps to install the dependencies.

1. Git

   - Install [Git](https://git-scm.com/)

2. Project

   - Clone the project

        ```$ git clone https://github.com/lucas625/Template_Django.git```

3. Install [Pyenv](https://github.com/pyenv/pyenv)

   - **If you are using windows, it may be easier to just install python 3.7**

4. Install [Pipenv](https://github.com/pyenv/pyenv)

5. Prepare o ambiente

    - Setup the environment

        ```sh
        pipenv --python 3.7
        pipenv shell
        pipenv install --dev
        ```

6. Node.js

   - Install [Node.js](https://nodejs.org/en/download/)

        ```$ sudo apt-get install nodejs```

7. Npm

   - Install npm

        ```$ sudo apt-get install npm```

   - Update npm

        ```$ sudo npm install -g npm@next```

   - Use npm to update node

        ```sh
        sudo npm cache clean -f
        sudo npm install -g n
        sudo n stable
        ```

   - Install node dependecies

        ```$ npm install```

8. Pre-commit

    - Install pre-commit hooks

        ```$ pre-commit install```

## Run the project

After completing the installation of the project, follow the next steps to execute it.

1. Security

   - Add the environment variables to your current terminal

        - Ubuntu

            ```sh
            export SECRET_KEY=$(python resources/scripts/get_secret_key.py)
            export ALLOWED_HOSTS=$(python resources/scripts/get_allowed_hosts.py)
            export DEBUG='True'
            ```

        - Windows

            ```sh
            set SECRET_KEY='A CUSTOM SECRET KEY'
            set ALLOWED_HOSTS='[*]'
            set DEBUG='True'
            ```

2. Migrations

    - Execute Django migrations

        ```sh
        python manage.py makemigrations
        python manage.py migrate
        ```

3. Running
   - Run the server alone

        ```$ python manage.py runserver```

   - Run the server alongside webpack

        ```$ npm run start```

## Testing

- Testing without coverage

   ```python manage.py test --no-input --debug-mode```

- Testing with coverage

   ```coverage run manage.py test --no-input --debug-mode -v 2```

  - After testing with coverage you might want to see the report.

    ```coverage report```

## Additional Topics

- Linter

  - The linter for this project is pylint with django extension.

    ```pylint --load-plugins pylint_django package```

    - You must execute pylint for all packages and fix the issues before commiting.
