FROM python:3.6
LABEL maintainer="alagunasalahaddin@live.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

RUN apt-get update \
    && apt-get install -y gettext curl sudo \
    # && curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - \
    # && apt-get install -y nodejs \
    && apt-get install -y nano python3-dev python3-setuptools \
    	libpng-dev libtiff5-dev libjpeg62-turbo-dev zlib1g-dev \
        libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
        libopenjpeg-dev pngquant imagemagick libmagickcore-dev libmagickwand-dev \
    && apt-get autoremove -y --purge \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install opencv-python numpy
# RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

RUN python manage.py migrate

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD exec gunicorn cms.wsgi:application --bind 0.0.0.0:8000 --workers 3
