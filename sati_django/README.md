## How to run

```

virtualenv sati
-- Make notes about virtualenv
source sati/bin/activate



pip install -r requirements.txt
-- pip install -r sati_django/requirements.txt 


python manage.py makemigrations

python manage.py sqlmigrate satiUTFPR 0001

python manage.py migrate

python manage.py runserver

# go to http://localhost:8000/

```
