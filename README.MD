# AUTHOR 
BETH NDUTA

## INSTAGRAM CLONE APP

## DESCRIPTION OF THE PROJECT
As a user of the application you can:
* Sign in to the application to start using.
* Upload your pictures to the application
* See your profile with all your pictures
* Follow other users and see their pictures on your timeline
* Like a picture and leave a comment on it.

## TECHNOLOGIES USED
* Python3.10.4
* DJANGO, MVC Framework
* HTML, CSS, BOOTSTRAP
* JAVASCRIPT
* POSTGRESQL
* HEROKU


## SETUP/INSTALLATION REQUIREMENTS
To access the code:
- clone the repo https://github.com/bethnduta/Instagram-clone.git

* activate virtual environment using python3.10.4 as default handler virtualenv env && env\Scripts\activate

* Install dependencies
Install dependencies that will create an environment for the app to run pip install -r requirements.txt

* Create the database
--psql
* CREATE DATABASE instagram;

* env file
Create .env file and paste the following filling where necessary: SECRET_KEY = <'secret_key>' DBNAME = 'instagram' USER = '' PASSWORD = '' DEBUG = True

* Run initial migration
- python 3.10.4 manage.py runmigrations instagram
- python 3.10.4 manage.py migrate

* Run the app
python 3.10.4 manage.py runserver
-open terminal on localhost:8000

* Current Bugs
There are no known bugs as of now. Incase you find one feel free to solve the bug and push the changes

## SUPPORT AND CONTACT DETAILS

Incase you want to contribute to the project fork the repository and make changes. Incase you wish to brainstorm any idea concerning the project kindly keep in touch with me through my;
* email[bethnduta05@gmail.com]
* slack[bethnduta]

## LICENSE
MIT Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ACKNOWLEDGEMENTS
I acknowledge Maryann Mwikali as my technical mentor while learning Django
