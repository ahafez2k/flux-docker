FROM python:latest

WORKDIR /app

COPY requirements.txt .

ARG FLASK_ENV
RUN if ["$FLASK_ENV" = "production"]; \
    then pip install -r requirements.txt --only=production; \
    else pip install -r requirements.txt; \
    fi

COPY . . 

EXPOSE 5000

CMD [ "python", "src/app.py" ]
