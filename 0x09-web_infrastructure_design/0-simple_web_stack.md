# Simple Web Stack

![Simple Web Stack Diagram](0-simple_web_stack.png)

## Components:
- Server: A physical or virtual machine that hosts the web server, application server, and database.
- Web Server (Nginx): Nginx is used to handle HTTP requests, serve static content, and act as a reverse proxy for the application server.
- Application Server: It runs the application code and processes dynamic requests. (Specify the application server you would use based on your stack.)
- Application Code Base: The website's code files, including HTML, CSS, JavaScript, and server-side scripts.
- MySQL Database: A relational database management system used to store and retrieve data for the website.
- Domain Name (foobar.com): The human-readable web address used to access the website. The www record points to the server's IP address.

## Communication Flow:
1. The user enters the domain name www.foobar.com in their browser.
2. The browser sends a request to the DNS server to resolve the IP address associated with the domain name.
3. The DNS server responds with the IP address 8.8.8.8, which points to the web server.
4. The user's request is sent to the web server (Nginx) at the resolved IP address.
5. Nginx receives the request and forwards it to the application server based on the configured rules.
6. The application server processes the request, interacts with the MySQL database if needed, and generates a response.
7. The response is sent back to Nginx, which then sends it to the user's browser.
8. The user's browser renders the received HTML, CSS, and JavaScript to display the website.

## Issues:
- Single Point of Failure (SPOF): If the server goes down, the entire website becomes unavailable.
- Downtime during maintenance: When updating the application code or performing server maintenance, the website may experience downtime.
- Limited scalability: If the website receives a high volume of traffic, the single server might not be able to handle the load, leading to slow performance or crashes.
