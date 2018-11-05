## Steps to Deploy
- Django project `ProjectName: virtualclinic` and `Application Name: virtualclinic`
- After starting the virtual environment: 
```
pip install dj-database-url gunicorn psycopg2 whitenoise
```
- Make **requirements.txt** file by ```pip freeze > requirements.txt```
- Create a file named **Procfile** and added ```web: gunicorn virtualclinic.wsgi```
- Create a file named **runtime.txt** and added the python version being used, for me ```python-3.5.2```
- In **settings.py**
```python
import dj_database_url
# other settings.py code lines
ALLOWED_HOSTS = ['localhost','127.0.0.1','*']
# other settings.py code lines
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}
# other settings.py code lines
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'
```
- In **wsgi.py** file
```python
from whitenoise.django import DjangoWhiteNoise
# other configurations wsgi.py code lines
application = DjangoWhiteNoise(application)  # In the last line
```
- Creating the heroku app ```heroku create```
```bash
python manage.py collectstatic --noinput
heroku config:set DISABLE_COLLECTSTATIC=1
git add --all
git commit -m "deploying on heroku"
git push heroku master
heroku run python manage.py migrate
```
- Application will be live on the url generated
- If there is any issue in this steps, feel free to contact either by opening an issue or mailing me at shahmishal1998@gmail.com