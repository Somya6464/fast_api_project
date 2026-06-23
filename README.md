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


<h3> All about JWT </h3>
- JSON web Token
- Tokean has 3 parts {header, payload, signature}
- need to install a library {pip install python-jose} 
- jose: javascript object signature and encryption


<h3> CORS Handling </h3>
- CORS: cross origin resource shearing
- It usage when your frontend or backend runs on different ports (in web specially)
- so it white list the frontend port so it was access the api's 

<h3> Work with .env files </h3>
- In large project we create config.py where we load env instance and then create a settings class like we created into our project
- then declair all env values into this class 
- Finally import this class whereever you want and use the values. shown in main.py, db.py

<h3> Testing with PyTest </h3>
- install : pip install pytest
- create api's as usually you do
- and then write the test cases into test file 
- Finally type {pytest} in terminal to start test cases
- if error comes then install: pip install httpx or httpx2
- And run again or resolve error accordingly.

<h3> 3rd Part Api integration </h3>
- like using spotify api get the list of songs and then return those from our personal api's.
- SO the 3rd party url was secure and user don't know the source at all.
- Install: pip install request

<h3> web crawling use to extract some data from someones site or page to use it into on map </h3>
- Install : pip install beautifulsoup4
- Before using someones site data we need permission from the owner of the site, so we can't get copyRight issues.
- and extract the widgets like flutter using the class of that HTML page

<h3> Pagination </h3>
- use the web crawling to get the data from a new site and perform pagination on that data.

<h3> Caching </h3>
- Use to speed up the processes, means once we get data we store it to use again so we don't need to call api for that again. 
- Time-to-live (TTL)

<h3> Rate Limiting </h3>
- Prevent user or Attackers to making Too many requests to crash our servers.
- So into this we set the api hit limit for user wise so a user may not hit an api above his rate limit.
- Install: pip install slowapi


<h3> Project Deployment </h3>
- 












<h1>Some important things we should know</h1>
- In this we have unicorn: it's basically a default server to run the application.

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc4MTYzMTY2N30.Fcj4bu2WrtP5DtDn-sU_cC9qp5JoeIy0dIWbQFlZFs8",
  "token_type": "bearer"
}