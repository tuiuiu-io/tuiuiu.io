tuiuiu.io
=========


![tuiuiu](https://raw.githubusercontent.com/tuiuiu-io/tuiuiu.io/master/tuiuiu-io-s.png)


Saas application based on Wagtail.oi using django_tenants.


# Up & Running
   
etc/hosts
---------

    127.0.0.1       tuiuiu.io
    
   
create postgres database 
------------------------
      
    $ docker run -ti -e POSTGRES_PASSWORD=tuiuiutenant -e POSTGRES_USER=tuiuiutenant -e POSTGRES_DB=tuiuiutenant -p 5432:5432 -d postgres
    
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

   1. Tom Turner under the name `django-tenants`_.
   2. Bernardo Pires under the name `django-tenant-schemas`_.
   3. Vlada Macek under the name of `django-schemata`_.
   4. Tom Dyson under the name `wagtail`_
