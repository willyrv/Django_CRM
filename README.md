# Tutorial

This django project was created following the tutorial [here](https://www.youtube.com/watch?v=t10QcFx7d5k)

# System requirements

You need to have installed the following packages:

* mysql-server
* libmysqlclient-dev

The application will assume that Mysql server is running at *localhost* on port 
*3306*. Also it assumes that there is a database called *djangocrmdb* and that 
the user *django* with password *DjangoAdmin*12345* has all privileges on the 
*djangocrmdb* database. 

You can use the script *mydb.py* to create the database if needed.

Don't forget to create a superuser

```bash
python manage.py createsuperuser
```

### To update the changes to the database and apply them, run

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

You can run the application by doing

```bash
python manage.py runserver
```

The app should run on *http://localhost:8000*


