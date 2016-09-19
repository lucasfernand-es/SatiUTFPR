## How to run

```

virtualenv sati
-- Make notes about virtualenv
source sati/bin/activate



pip install -r requirements.txt
-- pip install -r sati_django/requirements.txt 


python manage.py makemigrations

python manage.py sqlmigrate sati 0001

python manage.py migrate

python manage.py runserver

# go to http://localhost:8000/

## Running in production

- Criar o banco com o nome 'satiutfpr'

- python manage.py migrate

- run inserts.sql dentro do banco para criar os eventos e etc.

- no terminal rode
    - python manage.py createsuperuser (nao precisa utilizar informacoes pessoas, podem ser falsas)
        - coloque um usuario
        - coloque um email
        - coloque uma senha
    
    - dentro de /sati/ViewController/authenticate.py -- Linha 23
        - set o usuario e senha para os definidos acima.

    

```
