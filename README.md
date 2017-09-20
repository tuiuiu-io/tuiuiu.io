tuiuiu.io
=========


![tuiuiu](https://raw.githubusercontent.com/tuiuiu-io/tuiuiu.io/master/tuiuiu-io-s.png)


Saas application based on Wagtail.oi


# Up & Running
   
etc/hosts
---------

    127.0.0.1       tuiuiu.io
    
    
install node
---------
    $ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash
    $ command -v nvm
    $ nvm install 6

git clone
---------
    
    $ git clone git@github.com:caputomarcos/tuiuiu.io.git
    $ cd tuiuiu.io 
    $ virtualenv env --python=python3 && source env/bin/activate
    $ nvm use 6 && npm i
    $ make develop 
    $ cd app 
    $ python manage.py migrate_schemas
    $ python manage.py load_initial_data
    $ python manage.py runserver 
        
or 

    $ git clone git@github.com:caputomarcos/tuiuiu.io.git
    $ cd tuiuiu.io 
    $ virtualenv env --python=python3 && source env/bin/activate
    $ nvm use 6 && npm i
    $ make develop 
    $ cd app 
    $ docker build -t tuiuiu/io:v1.11.1 -t tuiuiu/io:latest .
    $ docker run --name tuiuiu.io -e "DJANGO_MIGRATE=true" -e "LOAD_INITIAL_DATA=true" -e "DJANGO_COLLECTSTATIC=true" -e "GUNICORN_RELOAD=true" -p 8000:8000 -d tuiuiu/io:latest
    $ docker logs -f tuiuiu.io 
        
or 
    
    
    $ mkdir tuiuiu.io && cd tuiuiu.io 
    $ virtualenv env --python=python3 && source env/bin/activate
    $ pip install git+https://github.com/caputomarcos/tuiuiu.io.git
    $ tuiuiu start app       
    $ cd app 
    $ python manage.py migrate_schemas
    $ python manage.py load_initial_data
    $ python manage.py runserver 
    
    
credentials
-----------

    user: admin
    pass: 123123123#

    
Credits
-------

Thank you for the wonderful work, Great Job!

   1. Tom Dyson under the name `wagtail`_
