# Virtual Clinic

## Installations

### Installing dependencies on your PC

```bash
sudo apt-get update
sudo apt-get install mysql-server
sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo apt-get install libmysqlclient-dev
```
### Setting up the Database

- Open a new terminal and type: ```mysql -u root -p```
- MySQL monitor opens up
```mysql
CREATE DATABASE virtual_clinic CHARACTER SET UTF8;
CREATE USER admin@localhost IDENTIFIED BY 'Admin@vc1';
GRANT ALL PRIVILEGES ON virtual_clinic.* TO admin@localhost;
FLUSH PRIVILEGES;
```

### Setting up the Virtual Environment

```bash
virtualenv ENV
cd ENV
source bin/activate
pip install --upgrade setuptools
cd virtualclinic
pip install -r requirements.txt
```

## How to Run?
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- To run the tests

```python manage.py test```

### Credits
- [How to install MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)
- [How to install Django](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04)
- [How to use mysql with Django](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)
