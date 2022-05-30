# Django Rest Framework App
```bash
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework
# Install dependencies in the requirement file
pip install -r requirements.txt

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..

# To run the django application
python manage.py runserver 8000 # 8000 is the port number
```
To migrate your models :
`python manage.py makemigrations` 
than 
`python manage.py migrate`

To test the app content and interactive console with it from shell :
`python manage.py shell`
like to insert into a model (table):
`from <app_name>.models import <table_name>`
`<table_name>.objects.create(field_1="content")`
Note : the id field comes by default in the model and it is the primary key you can change it from settings "https://docs.djangoproject.com/en/4.0/topics/db/models/#automatic-primary-key-fields"
TO convert the returned value to Python dict :
```python
from django.forms.models import model_to_dict

data = model_to_dict(<return_object_from_db_fetch_of_model>)

```
#### To seralize in django :
is that you have your model instance (model_data) and turn it to Python dict and return it as JSON to client .

