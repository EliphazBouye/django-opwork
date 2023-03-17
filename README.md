# Django Upwork Clone

How to run the project :  
Prerequis :
- Python 3.10 and greater
- Mariadb
- python virtualenv
- and pip

start by create a python virtual environment  
```bash
python -m venv venv 
```
install project requirements from the requirements.txt :
```bash
pip install -r requirements.txt
```
To start the application you should make migration to detect and apply last change into database.  
Before that add database credentials in `.env` file, make a copy of `.env.exemple` to `.env`.  
After adding database credentials into `.env` file apply migrations :
```bash
python manage.py migrate
```
run all tests to see if all works fine before running the server : 
```bash
python manage.py test opwork
```
then run the project 
```bash
python manage.py runserver
```