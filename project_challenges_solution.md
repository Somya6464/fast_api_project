1. I am facing issue to run Redis localhost servie because my windows system actively refused it.
solution => For that I user Docker desktop and create a saperate container that runs the redis service so it don't depend on my local system that's how I use Redis into my project for email otp storage work.

2. In mail service it gives config issues in connection.
solution => For that we enable 2-step verification into the sender gmail -> then goto app passwords -> genrate the password 16 digit -> set it into the .env file.

3. while implementing otp storage into the DB temporaryly it take space and more computation
solution => To solve this we use redis for temp signup data storage so we are not need to connect from db again & again and no storage needed or table creation as well.

4. After creating books table I want to add one more column. I add it into my code but I can't migrate it.
solution => so for all table migrations of changes make by alembic 
ex: alembic revision --autogenerate -m "add author_id to books"
alembic upgrade head
python -m alembic revision --autogenerate -m "add author_id to books"
python -m alembic upgrade head

5. At the time, when I upload my new work on render I need redis setup so fr that we use unstash for now that integrate redis + render

6. While deploying my Auth module which was my major part where I setup mail_service, redis and all, so for that we need multiple ports and after solving all issue find by (python -c "import app.main") this command. we got port issue form render and we resolve it by handling multiple ports from (main.py)

7. Got issue to send OTP verification email, due to port connectionTimeOut 
solution: use resend -> create account and change mail send working as per resend. But for free use may be it won't work for free,
but when you have domain purchased then you can do this easyly.In my case I don't have any purchased domain.

8. HOW WE CONTAINARIZE OUR FAST API APP + POSTGREs DB USING DOCKER.

- create and file named `Dockerfile` 
- Then create a `composed.yml` file for DB informations
- Then verify ki requirements.txt file updated hai kya
- DB connection wali file code me hai kya
- Run docker compose from project root with this command : docker-compose up --build
- Now it start's db container and make your FastApi app image. connect them with `fastapi-net`.
- Test Link: `http://localhost:8000/docs` / db link : `http://localhost:5432` 
- user: `postgres`/ pass: `password` / DB: `fastapi_db`
