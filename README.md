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

## Run tests with coverage

### Generate and display the coverage report in the terminal

### Generate an HTML report (optional)

```

  coverage run manage.py test
      
  coverage report
  
  coverage html
      
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
## Use app
- register as admin
- log in
- create book
- go to http://0.0.0.0:8000/swagger/
- test all apis

### References

* Docker deployment with HTTPS:
    * [Django Docker Deployment with HTTPS using Let's Encrypt]
    * (https://londonappdeveloper.com/django-docker-deployment-with-https-using-letsencrypt/)