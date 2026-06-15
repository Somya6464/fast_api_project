some Fast api important commands
1. firstly creat an env to start the project work 
2. By enter all package name which is used run this commnad : pip install -r requirement.txt (this will install all the mentioned packages)
3. then create some essetials files , initialisze them inside main.py
4. For run server use : uvicorn main:app --reload
5. sometimes we use (ipython) command for 
In [1]: import db, models
In [2]: db.create_table()
run these command which will help us to create a table in postgres directly.

6. To send custom response code we import "status" and use with api methods. 

<h3>Dependency Injection </h3>
Means: create a service class for single responsibility which we use anywhere whenever we want by importing it.
Depends() : It's is in-build method in fast api which we can use for dependency injection.

<h3>Middlewere </h3>
Means: This is the protected layers comes between every request/response.


<h3>SQLite and SQLAlchemy </h3>
Que: why we are not using SQLite in Fast api's ?
ans: It doesn't have ORM, need to write complex sql queries, create messy code, 




<h1>Some important things we should know</h1>
- In this we have unicorn: it's basically a default server to run the application.

