# OnlineBookStore

## Database
    
```
    create database
    connect to database
    update database in .env
```


## Dev Steps

```
    pip install -r requirements.txt
    
    python manage.py makemigrations

    python manage.py migrate
    
    python manage.py runserver
```

## Deploy Steps

1. clone repo

2. copy `.env`

3. set `.env` values

4. fresh installation

```
     docker-compose down                                                                                                                                                  git:main*
     docker-compose up --build
```

## Run tests


### References

* Docker deployment with HTTPS:
    * [Django Docker Deployment with HTTPS using Let's Encrypt]
    * (https://londonappdeveloper.com/django-docker-deployment-with-https-using-letsencrypt/)