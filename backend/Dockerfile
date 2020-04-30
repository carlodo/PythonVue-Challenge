FROM python:3.7-alpine
ADD . /usr/app
WORKDIR /usr/app

# For bcrypt python package.
RUN apk add python3-dev libffi-dev musl-dev gcc

RUN pip install -e '.[dev]'
RUN pip install -e '.[tests]'
