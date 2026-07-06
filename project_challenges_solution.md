1. I am facing issue to run Redis localhost servie because my windows system actively refused it.
solution => For that I user Docker desktop and create a saperate container that runs the redis service so it don't depend on my local system that's how I use Redis into my project for email otp storage work.

2. In mail service it gives config issues in connection.
solution => For that we enable 2-step verification into the sender gmail -> then goto app passwords -> genrate the password 16 digit -> set it into the .env file.

3. while implementing otp storage into the DB temporaryly it take space and more computation
solution => To solve this we use redis for temp signup data storage so we are not need to connect from db again & again and no storage needed or table creation as well.

4. 
