# GigConnect

  Briefly describe what GigConnect is and its purpose.
  Example: “GigConnect is a platform designed to connect freelancers with job opportunities, offering a user-friendly experience for both freelancers and employers.”

## Features:

  List the main features of your application.
  Example:
      User authentication (login/signup)
      Job listings and applications
      Messaging between freelancers and employers
      Profile management for freelancers and employers

## Tech Stack:

  Include the technologies used in each part of the application.  
  Example:  
  * API:
    - Django
    - Django REST Framework
  * Frontend:
    - Next.js
    - React

## Installation

Prerequis :
- Python 3.10+
- Mariadb
- python virtualenv
- and pip

start by create a python virtual environment  
```bash
python -m venv venv 
```
install project dependancies from the requirements.txt :
```bash
pip install -r requirements.txt
```
To start the application you should make migration to detect and apply last change into database.  
Before that add database credentials in `.env` file, make a copy of `.env.exemple` to `.env`.  
After adding database credentials into `.env` file apply migrations :
```bash
python manage.py migrate
```
run users application tests to see if all works fine before running the server : 
```bash
python manage.py test users
```
then run the project 
```bash
python manage.py runserver
```
