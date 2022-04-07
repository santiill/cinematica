# An API for Cinematica

---
# Built With

> ### Django - The framework used
> ### Django Rest Framework - The toolkit used to build API
> ### PostgreSQL - The database used
> ### unittest - For testing purposes

# Postman Collections

### [Collections](https://documenter.getpostman.com/view/17623351/UVRGD3f1)

# Deployed to Heroku

### [Heroku](https://cinematica1.herokuapp.com/)

---

![Cineomatica Diagram (1) (1)](https://user-images.githubusercontent.com/72644178/162143011-7f7f4a25-6175-4175-95e0-216120f10d18.png)

---
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
# Prerequisites
This is a project written using Python, Django and Django Rest Framework
1. Clone the repository

https://github.com/santiill/cinematica.git

2. Create the virtual enviroment
 

python3 -m venv venv
source venv/bin/activate

3. Install the requirements

pip install -r requirements.txt

4. Create a new PostgreSQL database

In your terminal:

psql postgres
CREATE DATABASE databasename
\c databasename

8. Create a new superuser

python manage.py createsuperuser

9. Run the server

python manage.py runserver
