<h1>☁️ Cloud Computing Roadmap</h1>

<p>
A structured roadmap to become a <strong>Cloud Engineer</strong> or
<strong>Cloud Solutions Architect</strong>. Follow each phase in order to
build strong fundamentals before moving to advanced cloud technologies.
</p>

<hr>

<h2>📌 Phase 1: Build the Non-Negotiable Foundations</h2>

<p>
Before touching any cloud platform, master the core concepts that modern
infrastructure is built upon.
</p>

<h3>🐧 Linux Administration</h3>

<p>
More than <strong>90% of cloud servers run Linux</strong>, making it one of
the most important skills for every cloud professional.
</p>

<p><strong>Learn how to:</strong></p>

<ul>
    <li>Navigate the Linux command line</li>
    <li>Manage files and permissions</li>
    <li>Monitor CPU, memory, and disk usage</li>
    <li>Work with processes and services</li>
    <li>Connect to remote servers using SSH</li>
</ul>

<h3>🌐 Networking Basics</h3>

<p>
Networking is the backbone of cloud computing. Without networking knowledge,
you cannot securely connect, manage, or troubleshoot cloud resources.
</p>

<p><strong>Topics to cover:</strong></p>

<ul>
    <li>Chapter 1: what is Networking </li>
    <p>
        Networking is a collection of devices connected with each others so they exchange data.
        ex: 5 houses(computers) connected through roads(wired/wifi), so people(data) can send letters(data packets) 
        If I want to see a youtube video then It pass through this process :-  Phone -> wifi -> Router -> IPs -> Internet -> Google servers
    </p>
    <p>
        <h2>Why Do We Need Networking?</h2>
        Without networking 
        <ul>
            <li>No Internet</li>
            <li>No Netflix</li>
            <li>No WhatsApp</li>
            <li>No AWS</li>
        </ul>
        Everthing depends on networking today.
        <h4>What Actually Travels?</h4>
        <b>Everything becomes packets.</b>
        ex: Sending courier (send many small boxes, but at the end they combined at the destination) packets work's like that.
        <h2>Components of Network</h2>
        <ul>
            <li>Client: Requests data{Laptop, Mobile}</li>
            <li>Server: Provides data {Google server, Netflix server}</li>
            <li>Router: Connect different networks</li>
            <li>Switch: Connect devices inside the same LAN {It contains only lan cable ports which directly connected through main Router}</li>
            <li>Cable/WiFi: The Road</li>
            <li>Internet: The worlds biggest network</li>
            <li>ISP: Internet Service Provider {Airtel, Geo, Idea}</li>
        </ul>
        <h2>What is a Packet?</h2>
        <p>It's a small piece of data that contains {source add. / destination add. / data||payload / control information}</p>
        <h4> <b>The Internet is a network of networks.</b></h4>
        
    </p>
    <li>TCP/IP</li>
    <li>IP Addresses</li>
    <li>Ports</li>
    <li>DNS</li>
    <li>HTTP &amp; HTTPS</li>
    <li>Subnets</li>
    <li>Firewalls</li>
    <li>Routing</li>
</ul>
<h4> <b> Terminal Knowledge </b></h4>
<B>Process Monitoring</B>
<p>Process monitoring = checking what programs are running on a server and how much CPU/RAM/resources they are consuming.
    Commands: ps (process status) / top(give live updates) / pgrep <processname>(helps to find PID) / kill <PID>(kill the process) / kill -9 <PID>(kill any process forcefully) / fg (bring jobs foreground) / bg (run stopped jobs in background)
</p>
<br>
<br>
<br>

<B>Performance Monitoring</B>
<p>
    Process Monitoring tells you what is running; Performance Monitoring tells you how healthy and capable the whole system is.
    Think of it like checking the health of a car:
For Server it's: 
 ├── CPU
 ├── RAM
 ├── Disk
 ├── Network
 └── Processes

Process Monitoring
        ↓
Individual processes

Performance Monitoring
        ↓
Entire system
<i> 4 things we mostly measure </i>
CPU / RAM / DISK / NETWORK
disk usage: df -h
ex :- and use% is important for me.
Filesystem   Size   Used   Avail   Use%
/dev/sda1     100G    90G    10G    90%
<br>
<br>
use these commands to find which usage that much disk space: 
- du -sh *
- du -sh /var/*
</p>
<br>
<br>
<B>Network Monitoring</B>
<p>
    You may want to know:
    <ul>
        <li>How much data is coming in?</li>
        <li>How much is going out?</li>
        <li>Are there network errors?</li>
        <li>Is traffic unusually high?</li>
    </ul>
    <br>
    use commands like: 
    <ul>
        <li>ss</li>
        <li>ip</li>
        <li>iftop</li>
        <li>nload</li>
        <li>vmstat: it provide details about (cpu,process,I/O,system activity)</li>
        <li>iostat: it provide details about systems I/O </li>
    </ul>
    <br>
    <br>
    <i>performance monitoring is not about CPU</i>
    ex:- anything looks good but user says it takes 10 sec. to load
    <br>
    Then in web application you might monitor:
    - Request count
    - Response time
    - Error rate
    - Database latency
    - HTTP 5xx errors
    <br>
    <br>
    <i> 4 Golden Rules</i>
    <ul>
        <li>Latency: How time api request takes to return</li>
        <li>Traffic: How much demand the system has</li>
        <li>Error: How many requests are failing</li>
        <li>Saturation:  resources apni max limit ko reach karne ke kitne duur hai, if they reach they become saturated</li>
    </ul>
       ```     PERFORMANCE MONITORING
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
       CPU           RAM           DISK
        │             │             │
   Processing      Memory       Storage
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                   NETWORK
                      │
                      ↓
                APPLICATION
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Latency      Errors      Traffic 
       ```

</p>
<h4><b>Networking Tools</b></h4>
<p>
    <i>
        Networking tools are command-line utilities used to monitor, diagnose, and troubleshoot network connections between computers and servers. These tools allow you to verify connectivity via ping, inspect active network sockets, trace the route of data packets, and analyze traffic passing through specific network interfaces.
    </i>
    <br>
    <br>
    ```
    Your Server
    │
    ├── Who am I?          → hostname / ip (ip a, ip route)
    ├── Where am I?        → ip addr
    ├── Where can I go?    → ping (ping google.com)
    ├── What route do I use? → traceroute (see the network path)
    ├── Can I connect?     → curl (curl "site link/ api link")
    ├── Which ports are open? → ss (ss -tuln)
    |-- ```
        -t → TCP
        -u → UDP
        -l → listening
        -n → don't resolve names; show numbers
        you see :
        0.0.0.0:22 (22-ssh) / 0.0.0.0:80 (80-HTTP) / 0.0.0.0:443 (443- HTTPS)
    |-- ```
    |-- nslookup (find ki aapka domain kis IP per running hai.)
    |-- wget "link" (used to download files from URLs)
    |-- hostname (check machine hostname)
    └── What's this domain's IP? → nslookup / dig

ping
 ↓
Can I reach the machine?

ss
 ↓
Is something listening on the port?

nc
 ↓
Can I connect to that port?

curl
 ↓
Does the HTTP/API service actually respond?

dig
 ↓
Does DNS point the domain where I expect?
    ```
    
</p>

<h4><b>Text Manipulation</b></h4>
<p>
    Text manipulation involves using command-line tools to search, filter, transform, and extract data from text files or streams. These utilities, such as `grep`, `sed`, `awk`, and `cut`, allow you to process large amounts of output, reformat configuration files, or parse logs directly within the terminal.
</p>



<h3>🔄 Version Control (Git &amp; GitHub)</h3>

<p>
Version control is essential for collaboration and tracking changes in your
projects.
</p>

<ul>
    <li>Git Fundamentals</li>
    <li>Branching &amp; Merging</li>
    <li>Pull Requests</li>
    <li>GitHub Repositories</li>
    <li>Collaboration Workflows</li>
    <li>git bisect: used to find the buggy commit or checkout from many commits.
        commands:
        - git bisect start
        - git bisect bad main (specify the issue branch)
        - git bisect good v1.2.0 (branch which work's)
        - git bisect bad (test and mark the branch bed if bug is there)
        - git bisect good (test and mark the branch good if bug is there)
        - git bisect reset (after commit find then cleanup and return the repo to it's original state)
    </li>
</ul>

<hr>

<h2>☁️ Phase 2: Choose One Cloud Provider</h2>

<p>
<strong>Do not try to learn all three cloud providers at once.</strong>
Master one platform first before exploring the others.
</p>

<h3>🌍 AWS (Amazon Web Services)</h3>

<ul>
    <li>Global market leader</li>
    <li>Highest industry demand</li>
    <li>Largest cloud ecosystem</li>
</ul>

<h3>🏢 Microsoft Azure</h3>

<ul>
    <li>Widely used in enterprise environments</li>
    <li>Strong Microsoft ecosystem integration</li>
</ul>

<h3>🤖 Google Cloud Platform (GCP)</h3>

<ul>
    <li>Excellent for AI and Machine Learning</li>
    <li>Popular among startups and data-driven companies</li>
</ul>

<h3>🎯 Core Services to Master</h3>

<h4>💻 Compute</h4>

<ul>
    <li>Virtual Machines (AWS EC2 / Azure VMs)</li>
    <li>Auto Scaling</li>
</ul>

<h4>💾 Storage</h4>

<ul>
    <li>Object Storage (AWS S3 / Azure Blob Storage)</li>
    <li>Block Storage</li>
</ul>

<h4>🗄️ Databases</h4>

<ul>
    <li>Managed SQL Databases</li>
    <li>NoSQL Databases (Amazon DynamoDB)</li>
    <li>Amazon RDS</li>
</ul>

<h4>🌐 Networking</h4>

<ul>
    <li>Virtual Private Cloud (VPC)</li>
    <li>Subnets</li>
    <li>Route Tables</li>
    <li>Security Groups</li>
</ul>

<h4>🔐 Identity &amp; Access Management (IAM)</h4>

<ul>
    <li>Users</li>
    <li>Roles</li>
    <li>Policies</li>
    <li>Principle of Least Privilege (PoLP)</li>
</ul>

<hr>

<h2>⚙️ Phase 3: Infrastructure as Code (IaC) &amp; Automation</h2>

<p>
Modern cloud environments are rarely built manually through a web console.
Infrastructure is created and managed using code.
</p>

<h3>🏗️ Terraform</h3>

<p>The industry-standard tool for provisioning cloud infrastructure.</p>

<ul>
    <li>Providers</li>
    <li>Resources</li>
    <li>Variables</li>
    <li>Modules</li>
    <li>State Management</li>
</ul>

<h3>🐍 Scripting</h3>

<p>Learn one scripting language:</p>

<ul>
    <li>Python (Recommended)</li>
    <li>Bash</li>
</ul>

<p>Use scripting to automate:</p>

<ul>
    <li>Infrastructure Tasks</li>
    <li>Deployments</li>
    <li>Backups</li>
    <li>Monitoring</li>
</ul>

<hr>

<h2>📦 Phase 4: Containers &amp; Orchestration</h2>

<p>
Modern applications are packaged into containers so they can run consistently
across different environments.
</p>

<h3>🐳 Docker</h3>

<ul>
    <li>Build Docker Images</li>
    <li>Create Dockerfiles</li>
    <li>Run Containers</li>
    <li>Manage Volumes</li>
    <li>Use Docker Compose</li>
</ul>

<h3>☸️ Kubernetes (K8s)</h3>

<p>A must-have skill for mid-level and advanced cloud roles.</p>

<ul>
    <li>Pods</li>
    <li>Deployments</li>
    <li>Services</li>
    <li>ConfigMaps</li>
    <li>Secrets</li>
    <li>Scaling</li>
    <li>Cluster Management</li>
</ul>

<hr>

<h2>🚀 Phase 5: CI/CD &amp; Monitoring</h2>

<h3>🔁 Continuous Integration &amp; Continuous Deployment</h3>

<p>
Understand how code moves automatically from a Git repository to production.
</p>

<ul>
    <li>GitHub Actions</li>
    <li>Jenkins</li>
</ul>

<h3>📊 Monitoring &amp; Observability</h3>

<p>Learn how to:</p>

<ul>
    <li>Read Application Logs</li>
    <li>Monitor Infrastructure</li>
    <li>Set Up Alerts</li>
    <li>Track Cloud Costs</li>
</ul>

<p><strong>Common Tools:</strong></p>

<ul>
    <li>AWS CloudWatch</li>
    <li>Azure Monitor</li>
</ul>

<hr>

<h2>🎓 Recommended Learning Path &amp; Certifications</h2>

<h3>🟢 Beginner Level</h3>

<p>
Start with a foundational certification to understand cloud concepts and
terminology.
</p>

<ul>
    <li>AWS Certified Cloud Practitioner</li>
    <li>Microsoft Azure Fundamentals (AZ-900)</li>
</ul>

<h3>🔵 Associate Level</h3>

<p>
Move to hands-on certifications that focus on designing and managing cloud
infrastructure.
</p>

<ul>
    <li>AWS Certified Solutions Architect – Associate</li>
    <li>Microsoft Azure Administrator (AZ-104)</li>
</ul>

<hr>

<h2>🛣️ Learning Path Summary</h2>

<pre>
Linux
   ↓
Networking
   ↓
Git &amp; GitHub
   ↓
Choose One Cloud Provider
   ↓
Core Cloud Services
   ↓
Terraform
   ↓
Python / Bash
   ↓
Docker
   ↓
Kubernetes
   ↓
CI/CD
   ↓
Monitoring &amp; Observability
   ↓
Cloud Certifications
</pre>

<hr>

<h2>🎯 Final Goal</h2>

<p>By completing this roadmap, you will gain practical knowledge in:</p>

<ul>
    <li>✅ Linux Administration</li>
    <li>✅ Networking Fundamentals</li>
    <li>✅ Git &amp; GitHub</li>
    <li>✅ Cloud Infrastructure</li>
    <li>✅ Infrastructure as Code (Terraform)</li>
    <li>✅ Automation with Python/Bash</li>
    <li>✅ Docker</li>
    <li>✅ Kubernetes</li>
    <li>✅ CI/CD Pipelines</li>
    <li>✅ Monitoring &amp; Observability</li>
    <li>✅ Industry Certifications</li>
</ul>

<hr>

<h3>🚀 Happy Learning!</h3>
