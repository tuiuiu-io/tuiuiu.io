Tuiuiu.io Project_Template
--------------------------

# Up & Running

### virtualenv

```bash
virtualenv env --python=python3 && source env/bin/activate
python manage.py migrate_schemas
python manage.py load_initial_data
python manage.py runserver 
```

### docker

```bash
docker build -t tuiuiu/tuiuiu.io:v1.11.1 -t tuiuiu/tuiuiu.io:latest .
docker run --name tuiuiu.io -e "DJANGO_MIGRATE=true" \ 
-e "LOAD_INITIAL_DATA=true" -e "DJANGO_COLLECTSTATIC=true" \
-e "GUNICORN_RELOAD=true" -p 8000:8000 -d tuiuiu/tuiuiu.io:latest
docker logs -f tuiuiu.io 
```

