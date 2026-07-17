<h1>🚀 FastAPI Production-Ready Backend & DevOps Pipeline</h1>

<p>A robust, scalable, and fully-featured FastAPI backend project, complete with JWT authentication, PostgreSQL, Redis caching, and a full Phase 4 DevOps deployment pipeline.</p>

<p><strong>🔗 LIVE LINK:</strong> <a href="https://fast-api-project-z7yg.onrender.com/docs">https://fast-api-project-z7yg.onrender.com/docs</a></p>

<hr>

<h2>🛠️ Tech Stack</h2>
<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Technologies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Backend</strong></td>
      <td>FastAPI, Python, Uvicorn, OAuth2, JWT (python-jose)</td>
    </tr>
    <tr>
      <td><strong>Database</strong></td>
      <td>PostgreSQL, SQLAlchemy (ORM), Alembic (Migrations)</td>
    </tr>
    <tr>
      <td><strong>Caching & Limits</strong></td>
      <td>Redis (TTL Caching), SlowAPI (Rate Limiting)</td>
    </tr>
    <tr>
      <td><strong>Testing</strong></td>
      <td>PyTest, HTTPX</td>
    </tr>
    <tr>
      <td><strong>External Tools</strong></td>
      <td>BeautifulSoup4 (Web Crawling), Requests (3rd Party APIs)</td>
    </tr>
    <tr>
      <td><strong>Frontend</strong></td>
      <td>Flutter (Dart)</td>
    </tr>
    <tr>
      <td><strong>DevOps & Cloud</strong></td>
      <td>Docker, Docker Compose, GitHub Actions, AWS (EC2, Nginx, HTTPS), Terraform, Kubernetes</td>
    </tr>
    <tr>
      <td><strong>Monitoring</strong></td>
      <td>Prometheus, Grafana</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>⚡ FastAPI Important Commands</h2>
<ol>
  <li>Firstly create an env to start the project work.</li>
  <li>By entering all package names which are used, run this command: <code>pip install -r requirements.txt</code> (this will install all the mentioned packages).</li>
  <li>Then create some essential files, initialize them inside <code>main.py</code>.</li>
  <li>For running the server use: <code>uvicorn main:app --reload</code></li>
  <li>Sometimes we use <code>ipython</code> command for:
    <pre><code>In [1]: import db, models
In [2]: db.create_table()</code></pre>
    Run these commands which will help us to create a table in PostgreSQL directly.
  </li>
  <li>To send custom response codes we import <code>status</code> and use it with API methods.</li>
</ol>

<hr>

<h2>🏗️ Core Architecture Concepts</h2>

<h3>Dependency Injection</h3>
<ul>
  <li><strong>Means:</strong> Create a service class for single responsibility which we use anywhere whenever we want by importing it.</li>
  <li><code>Depends()</code>: It is an in-built method in FastAPI which we can use for dependency injection.</li>
</ul>

<h3>Middleware</h3>
<ul>
  <li><strong>Means:</strong> This is the protected layer that comes between every request/response.</li>
</ul>

<h3>SQLite and SQLAlchemy</h3>
<ul>
  <li><strong>Que:</strong> Why we are not using SQLite in FastAPIs?</li>
  <li><strong>Ans:</strong> It doesn't have ORM, need to write complex SQL queries, creates messy code.</li>
</ul>

<h3>All about JWT</h3>
<ul>
  <li>JSON Web Token</li>
  <li>Token has 3 parts: <code>{header, payload, signature}</code></li>
  <li>Need to install a library: <code>pip install python-jose</code></li>
  <li>jose: JavaScript Object Signature and Encryption</li>
</ul>

<h3>CORS Handling</h3>
<ul>
  <li><strong>CORS:</strong> Cross-Origin Resource Sharing</li>
  <li>Its usage is when your frontend or backend runs on different ports (in web specially).</li>
  <li>So it whitelists the frontend port so it can access the APIs.</li>
</ul>

<h3>Work with .env files</h3>
<ul>
  <li>In large projects we create <code>config.py</code> where we load env instance and then create a settings class like we created into our project.</li>
  <li>Then declare all env values into this class.</li>
  <li>Finally import this class wherever you want and use the values (shown in <code>main.py</code>, <code>db.py</code>).</li>
</ul>

<hr>

<h2>🧪 Testing with PyTest</h2>
<ul>
  <li>Install: <code>pip install pytest</code></li>
  <li>Create APIs as usually you do.</li>
  <li>And then write the test cases into test file.</li>
  <li>Finally type <code>pytest</code> in terminal to start test cases.</li>
  <li>If error comes then install: <code>pip install httpx</code> or <code>httpx2</code>.</li>
  <li>And run again or resolve error accordingly.</li>
</ul>

<hr>

<h2>🌐 Advanced Integrations</h2>

<h3>3rd Party API Integration</h3>
<ul>
  <li>Like using Spotify API to get the list of songs and then return those from our personal APIs.</li>
  <li>So the 3rd party URL was secure and user don't know the source at all.</li>
  <li>Install: <code>pip install requests</code></li>
</ul>

<h3>Web Crawling</h3>
<ul>
  <li>Used to extract some data from someone's site or page to use it into our map.</li>
  <li>Install: <code>pip install beautifulsoup4</code></li>
  <li>Before using someone's site data we need permission from the owner of the site, so we can't get copyright issues.</li>
  <li>Extract the widgets like Flutter using the class of that HTML page.</li>
</ul>

<h3>Pagination</h3>
<ul>
  <li>Use the web crawling to get the data from a new site and perform pagination on that data.</li>
</ul>

<h3>Caching</h3>
<ul>
  <li>Use to speed up the processes, means once we get data we store it to use again so we don't need to call API for that again.</li>
  <li>Time-to-live (TTL)</li>
</ul>

<h3>Rate Limiting</h3>
<ul>
  <li>Prevent user or Attackers from making too many requests to crash our servers.</li>
  <li>So into this we set the API hit limit for user-wise so a user may not hit an API above his rate limit.</li>
  <li>Install: <code>pip install slowapi</code></li>
</ul>

<hr>

<h2>🚢 Project Deployment using RENDER</h2>
<ul>
  <li>Generate the requirements.txt file using <code>pip freeze > requirements.txt</code> command.</li>
  <li><strong>LIVE LINK:</strong> <a href="https://fast-api-project-z7yg.onrender.com/docs">https://fast-api-project-z7yg.onrender.com/docs</a></li>
</ul>

<hr>

<h2>💼 Worked Tasks & Learned Technologies into this Project</h2>

<h3>Backend</h3>
<ul>
  <li>User registration/login</li>
  <li>JWT authentication (OAuth with email OTP verification)</li>
  <li>CRUD operations</li>
  <li>Caching (Redis)</li>
  <li>File uploads</li>
  <li>Pagination</li>
  <li>Search/filtering</li>
  <li>Role-based access</li>
  <li>Logging</li>
  <li>Unit tests</li>
</ul>

<h3>Database</h3>
<ul>
  <li>PostgreSQL</li>
  <li>Proper schema design</li>
  <li>Migrations (Alembic)</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>Flutter (Dart)</li>
</ul>

<hr>

<h2>⚙️ Phase 4: Add DevOps without starting over</h2>
<p>Now use the same project to learn DevOps.</p>

<h3>Docker</h3>
<ul>
  <li>Create a Dockerfile</li>
  <li>Use Docker Compose</li>
  <li>Run FastAPI + PostgreSQL together</li>
</ul>

<h3>GitHub Actions</h3>
<ul>
  <li>Run tests automatically</li>
  <li>Build Docker image</li>
  <li>Push image to a container registry</li>
</ul>

<h3>AWS</h3>
<ul>
  <li>Launch an EC2 instance</li>
  <li>Deploy your Dockerized app</li>
  <li>Configure Nginx</li>
  <li>Set up HTTPS</li>
</ul>

<h3>Terraform</h3>
<ul>
  <li>Create the EC2 instance</li>
  <li>Create security groups</li>
  <li>Automate infrastructure creation</li>
</ul>

<h3>Kubernetes</h3>
<ul>
  <li>Deploy your app</li>
  <li>Scale replicas</li>
  <li>Configure Ingress</li>
  <li>Store secrets securely</li>
</ul>

<h3>Monitoring</h3>
<ul>
  <li>Add Prometheus metrics</li>
  <li>Create Grafana dashboards</li>
</ul>

<hr>

<h2>💡 Some Important Things We Should Know</h2>
<ul>
  <li>In this we have Uvicorn: it's basically a default server to run the application.</li>
</ul>

<p><strong>JWT Token Example:</strong></p>
<pre><code>{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc4MTYzMTY2N30.Fcj4bu2WrtP5DtDn-sU_cC9qp5JoeIy0dIWbQFlZFs8",
  "token_type": "bearer"
}</code></pre>
