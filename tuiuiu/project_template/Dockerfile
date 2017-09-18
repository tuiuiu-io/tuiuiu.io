FROM python:3

EXPOSE 8000

ENV GUNICORN_VERSION=19.7.1
ENV PYTZ_VERSION=2017.2

RUN apt-get update && apt-get upgrade && apt-get install -y \
    vim \
    wget \
    git-core \
&& rm -rf /var/lib/apt/lists/*


# create directory which can be a place for generated static content
# volume can be used to serve these files with a webserver
RUN mkdir -p /var/www/static
VOLUME /var/www/static

# create directory for application source code
# volume can be used for live-reload during development
RUN mkdir -p /usr/src/tuiuiu.io
WORKDIR /usr/src/tuiuiu.io

# copy project files
COPY . /usr/src/tuiuiu.io
VOLUME /usr/src/tuiuiu.io

# add gunicorn config
RUN mkdir -p /etc/gunicorn
COPY gunicorn.conf /etc/gunicorn/

# install gunicorn, django and pytz
RUN pip install gunicorn==$GUNICORN_VERSION
RUN pip install pytz==$PYTZ_VERSION
RUN pip install git+https://github.com/tuiuiu-io/tuiuiu.io.git

# run start.sh on container start
CMD bash start.sh
