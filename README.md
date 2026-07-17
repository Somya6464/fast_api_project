<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Production-Ready Backend & DevOps Pipeline</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #24292e;
            background-color: #ffffff;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        h1 {
            font-size: 2em;
            border-bottom: 2px solid #eaecef;
            padding-bottom: 0.3em;
            margin-top: 24px;
            margin-bottom: 16px;
            color: #0366d6;
        }
        
        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
            margin-top: 24px;
            margin-bottom: 16px;
            color: #0366d6;
        }
        
        h3 {
            font-size: 1.25em;
            margin-top: 24px;
            margin-bottom: 16px;
            color: #24292e;
        }
        
        p {
            margin-top: 0;
            margin-bottom: 16px;
        }
        
        ul, ol {
            padding-left: 2em;
            margin-bottom: 16px;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
            display: block;
            overflow: auto;
        }
        
        th, td {
            border: 1px solid #dfe2e5;
            padding: 8px 16px;
            text-align: left;
        }
        
        th {
            background-color: #f6f8fa;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background-color: #f6f8fa;
        }
        
        code {
            background-color: rgba(27, 31, 35, 0.05);
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 85%;
        }
        
        pre {
            background-color: #f6f8fa;
            padding: 16px;
            overflow: auto;
            border-radius: 6px;
            margin-bottom: 16px;
            position: relative;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            font-size: 100%;
            line-height: 1.45;
        }
        
        .code-block {
            background-color: #24292e;
            color: #e1e4e8;
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
            margin-bottom: 16px;
        }
        
        .code-block code {
            background-color: transparent;
            color: #e1e4e8;
            padding: 0;
        }
        
        a {
            color: #0366d6;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        strong {
            font-weight: 600;
        }
        
        em {
            font-style: italic;
        }
        
        .emoji {
            margin-right: 4px;
        }
        
        blockquote {
            border-left: 4px solid #dfe2e5;
            color: #6a737d;
            padding-left: 16px;
            margin-bottom: 16px;
        }
        
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        
        .badge-primary {
            background-color: #0366d6;
            color: white;
        }
        
        .badge-success {
            background-color: #28a745;
            color: white;
        }
        
        .badge-info {
            background-color: #17a2b8;
            color: white;
        }
        
        hr {
            border: 0;
            border-top: 1px solid #eaecef;
            margin: 24px 0;
        }
        
        .json-example {
            background-color: #f6f8fa;
            border: 1px solid #dfe2e5;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 16px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 14px;
            overflow-x: auto;
        }
        
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            
            h1 {
                font-size: 1.5em;
            }
            
            h2 {
                font-size: 1.25em;
            }
            
            table {
                font-size: 14px;
            }
            
            th, td {
                padding: 6px 10px;
            }
        }
    </style>
</head>
<body>
    <h1><span class="emoji">🚀</span>FastAPI Production-Ready Backend & DevOps Pipeline</h1>
    
    <p>A robust, scalable, and fully-featured FastAPI backend project, complete with JWT authentication, PostgreSQL, Redis caching, and a full Phase 4 DevOps deployment pipeline (Docker, AWS, Terraform, Kubernetes, and Monitoring).</p>
    
    <p><span class="emoji">🔗</span><strong>Live API Documentation</strong>: <a href="https://fast-api-project-z7yg.onrender.com/docs">https://fast-api-project-z7yg.onrender.com/docs</a></p>
    
    <hr>
    
    <h2><span class="emoji">🛠️</span>Tech Stack</h2>
    
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
                <td>FastAPI, Python, Uvicorn, OAuth2, JWT (<code>python-jose</code>)</td>
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
    
    <h2><span class="emoji">✨</span>Key Features</h2>
    
    <ul>
        <li><span class="emoji">🔐</span><strong>Authentication</strong>: User registration/login with JWT (OAuth2) and Email OTP verification.</li>
        <li><span class="emoji">🛡️</span><strong>Security</strong>: Role-based access control, CORS handling, and Rate Limiting (via <code>slowapi</code>).</li>
        <li><span class="emoji">⚡</span><strong>Performance</strong>: Redis caching with Time-To-Live (TTL) to reduce redundant API calls.</li>
        <li><span class="emoji">📦</span><strong>Data Management</strong>: Advanced CRUD operations, file uploads, pagination, and search/filtering.</li>
        <li><span class="emoji">🕸️</span><strong>Integrations</strong>: Secure 3rd-party API integration (e.g., Spotify) and ethical web crawling (with owner permission).</li>
        <li><span class="emoji">📝</span><strong>Reliability</strong>: Comprehensive unit testing, structured logging, and proper database schema design.</li>
    </ul>
    
    <hr>
    
    <h2><span class="emoji">🏗️</span>Core Architecture Concepts</h2>
    
    <ul>
        <li><strong>Dependency Injection</strong>: Utilizing FastAPI's built-in <code>Depends()</code> to create single-responsibility service classes that can be imported and reused anywhere.</li>
        <li><strong>Middleware</strong>: Implemented as a protected layer intercepting every request/response for logging, CORS, and security checks.</li>
        <li><strong>Environment Management</strong>: Centralized <code>config.py</code> using Pydantic <code>BaseSettings</code> to load and validate <code>.env</code> variables securely.</li>
        <li><strong>Database Choice</strong>: PostgreSQL is used over SQLite. While SQLite is lightweight, raw SQLite often leads to complex SQL queries and messy code. PostgreSQL + SQLAlchemy + Alembic ensures robust ORM capabilities and clean, version-controlled migrations.</li>
        <li><strong>Custom Responses</strong>: Utilizing FastAPI's <code>status</code> module to return precise, standard HTTP response codes.</li>
    </ul>
    
    <hr>
    
    <h2><span class="emoji"></span>Getting Started</h2>
    
    <h3>1. Prerequisites</h3>
    <ul>
        <li>Python 3.9+</li>
        <li>PostgreSQL installed and running</li>
        <li>Redis server (for caching)</li>
    </ul>
    
    <h3>2. Installation & Setup</h3>
    
    <div class="code-block">
        <code># 1. Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 2. Install all required packages
pip install -r requirements.txt

# 3. Create a .env file based on .env.example and fill in your credentials
# (DB_URL, SECRET_KEY, REDIS_URL, etc.)

# 4. Run database migrations (Alembic)
alembic upgrade head

# 5. (Optional) Interactive DB setup via IPython
ipython
>>> import db, models
>>> db.create_table()  # Creates tables in PostgreSQL directly
>>> exit()

# 6. Start the development server
uvicorn main:app --reload</code>
    </div>
    
    <h3>3. Environment Variables (<code>.env</code> example)</h3>
    
    <div class="code-block">
        <code>DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_db
SECRET_KEY=your-super-secret-jwt-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379/0</code>
    </div>
    
    <hr>
    
    <h2><span class="emoji">🧪</span>Testing</h2>
    
    <p>We use <code>pytest</code> for unit and integration testing.</p>
    
    <div class="code-block">
        <code># Install testing dependencies
pip install pytest httpx

# Run all tests
pytest

# Run with verbose output and print statements
pytest -v -s</code>
    </div>
    
    <p><em>Note: If you encounter HTTP client errors during testing, ensure <code>httpx</code> is installed.</em></p>
    
    <hr>
    
    <h2><span class="emoji">🌐</span>Advanced Integrations</h2>
    
    <ul>
        <li><strong>3rd Party APIs</strong>: Uses the <code>requests</code> library to fetch data (e.g., Spotify song lists) and serve it through our secure endpoints, masking the original source URL from the end user.</li>
        <li><strong>Web Crawling</strong>: Uses <code>beautifulsoup4</code> to extract specific HTML widgets/data. <em>Ethical Note: Always obtain explicit permission from the site owner before crawling to avoid copyright issues.</em></li>
        <li><strong>Pagination</strong>: Applied to crawled or large dataset responses to ensure optimal performance and manageable payload sizes.</li>
    </ul>
    
    <hr>
    
    <h2><span class="emoji">🚢</span>Deployment (Render)</h2>
    
    <p>For quick cloud deployment, the project is configured for Render.</p>
    
    <div class="code-block">
        <code># Generate the requirements file
pip freeze > requirements.txt</code>
    </div>
    
    <p>The live application is automatically deployed and accessible at:<br>
    👉 <a href="https://fast-api-project-z7yg.onrender.com/docs">https://fast-api-project-z7yg.onrender.com/docs</a></p>
    
    <hr>
    
    <h2><span class="emoji">⚙️</span>Phase 4: DevOps & Infrastructure</h2>
    
    <p>This project includes a complete DevOps learning and implementation pipeline without starting over.</p>
    
    <h3><span class="emoji">🐳</span>Docker & CI/CD</h3>
    <ul>
        <li><strong>Docker</strong>: <code>Dockerfile</code> and <code>docker-compose.yml</code> to run FastAPI and PostgreSQL together seamlessly.</li>
        <li><strong>GitHub Actions</strong>: Automated pipeline to run <code>pytest</code>, build the Docker image, and push it to a container registry on every push/PR.</li>
    </ul>
    
    <h3><span class="emoji">☁️</span>AWS & Terraform</h3>
    <ul>
        <li><strong>Terraform</strong>: Infrastructure as Code (IaC) scripts to automate the creation of AWS EC2 instances and configure Security Groups.</li>
        <li><strong>AWS Deployment</strong>: Dockerized app deployed on EC2, fronted by <strong>Nginx</strong> as a reverse proxy, with <strong>HTTPS</strong> configured via Let's Encrypt.</li>
    </ul>
    
    <h3><span class="emoji">☸️</span>Kubernetes (K8s)</h3>
    <ul>
        <li>Deploy the application using K8s manifests.</li>
        <li>Scale replicas for high availability.</li>
        <li>Configure <strong>Ingress</strong> for external access.</li>
        <li>Store sensitive data securely using K8s <strong>Secrets</strong>.</li>
    </ul>
    
    <h3><span class="emoji">📊</span>Monitoring</h3>
    <ul>
        <li><strong>Prometheus</strong>: Integrated to scrape custom and default FastAPI metrics.</li>
        <li><strong>Grafana</strong>: Dashboards created to visualize API health, request rates, and cache hit ratios.</li>
    </ul>
    
    <hr>
    
    <h2><span class="emoji">🔑</span>API Usage Example</h2>
    
    <p><strong>Authentication Response:</strong><br>
    Upon successful login, the API returns a JWT token structured as follows:</p>
    
    <div class="json-example">
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc4MTYzMTY2N30.Fcj4bu2WrtP5DtDn-sU_cC9qp5JoeIy0dIWbQFlZFs8",
  "token_type": "bearer"
}
    </div>
    
    <p><em>JWT Structure</em>: <code>{ header, payload, signature }</code> secured via <code>python-jose</code> (JavaScript Object Signature and Encryption).</p>
    
    <hr>
    
    <h2><span class="emoji"></span>Important Notes</h2>
    
    <ul>
        <li><strong>Uvicorn</strong>: The default ASGI server used to run the FastAPI application efficiently.</li>
        <li><strong>CORS</strong>: Configured to whitelist specific frontend ports (e.g., Flutter web or local dev servers) to allow secure cross-origin resource sharing.</li>
        <li><strong>Rate Limiting</strong>: Powered by <code>slowapi</code> to prevent attackers or overly aggressive users from crashing the server with too many requests.</li>
    </ul>
    
    <hr>
    
    <h2><span class="emoji">🤝</span>Contributing</h2>
    
    <ol>
        <li>Fork the repository.</li>
        <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>).</li>
        <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>).</li>
        <li>Open a Pull Request.</li>
    </ol>
    
    <hr>
    
</body>
</html>
