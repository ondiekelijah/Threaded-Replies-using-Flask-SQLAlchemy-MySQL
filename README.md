# Threaded comments using Common Table Expressions (CTE) for a MySQL Flask blog or CMS

Credits to [miguelgrinberg](https://blog.miguelgrinberg.com/post/implementing-user-comments-with-sqlalchemy) & [peterspython](https://www.peterspython.com/en/blog/threaded-comments-using-common-table-expressions-cte-for-a-mysql-flask-blog-or-cms)

Also read more about the implementation [here](https://www.peterspython.com/en/blog/threaded-comments-using-common-table-expressions-cte-for-a-mysql-flask-blog-or-cms) or [here](https://blog.miguelgrinberg.com/post/implementing-user-comments-with-sqlalchemy)

Set up & Installation.

### 1 .Clone/Fork the git repo and create an environment 
                    
**Windows**
          
```bash
git clone https://github.com/Dev-Elie/Threaded-Replies-using-Flask-SQLAlchemy-MySQL.git
cd Threaded-Replies-using-Flask-SQLAlchemy-MySQL
py -3 -m venv venv

```
          
**macOS/Linux**
          
```bash
git clone https://github.com/Dev-Elie/Threaded-Replies-using-Flask-SQLAlchemy-MySQL.git
cd Threaded-Replies-using-Flask-SQLAlchemy-MySQL
python3 -m venv venv

```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```
### 4 .Migrate/Create a database

Applies for windows/macOS/Linux <br>
**NB** First create a MySQL database then execute then <br>
create a .env file and paste the following lines of code;
```
SECRET_KEY = 'secret-key'
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://mysql-username:mysql-db-pass@localhost/db-name"
SQLALCHEMY_TRACK_MODIFICATIONS = True
```
Once done execute

```python manage.py```

### 5. Run the application 

**For linux and macOS**
Make the run file executable by running the code

```chmod 777 run```

Then start the application by executing the run file

```./run```

**On windows**
```
set FLASK_APP=main
flask run
```
#### During your experiment, you can manage your posts and comments from the Flask Admin panel. **http://localhost:5000/admin/**

![sample query result](https://github.com/Dev-Elie/Threaded-Replies-using-Flask-SQLAlchemy-MySQL/blob/main/static/img/mysql-query-result.png)

</br>
<div align="center"><h1>Follow me on Twitter</h1></div>
<p align="center"> <a href="https://twitter.com/dev_elie" target="blank"><img src="https://img.shields.io/twitter/follow/dev_elie?logo=twitter&style=for-the-badge" alt="dev_elie" /></a> </p>


