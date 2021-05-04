# Hospital  Management System

 Note - 1: Postgres database should be installed. configure postgres credential and connection by creating .env file by following .env.example file.
 

## step - 1
clone the project <br >
` git clone https://github.com/sangrampattnaik/hospital_management.git`


## step - 2
create a virtual environment with name venv and activate <br >
`virtualenv venv` <br >
`source venv/bib/activate`


## step - 3
install depedancies <br >
`pip install -r requirements.txt`
or <br >
`make initial-setup`


## step - 4
create databases <br >
`make migrate` <br >
or <br >

`python manage.py makemigrations`
`python manage.py migrate`


## step - 5
create admin <br >
`make superuser` <br >
or <br >
`python manage.py superadmin`


## step - 6
create test data <br >
`make test-data` <br >
or <br >
`python manage.py test_data`

## step - 7
runserver <br >
`make runserver` <br >
or <br >
`python manage.py runserver`