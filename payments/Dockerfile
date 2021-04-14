FROM python:3.9-alpine
LABEL maintainer "Gilberto Magalhães"

ENV PYTHONUNBUFFERED 1

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

USER user
