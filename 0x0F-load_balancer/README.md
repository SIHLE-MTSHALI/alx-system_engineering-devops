# 0x0F Load Balancer

This project involves configuring load balancing and redundancy for web servers using HAproxy. Custom HTTP headers are added to track which server is responding. Puppet is used to automate some configurations.

## Tasks

### 0. Double the number of webservers
- Configure Nginx on web-01 and web-02 to include custom HTTP header X-Served-By with hostname  
- Script 0-custom_http_response_header configures this

### 1. Install your load balancer 
- Install and configure HAproxy on lb-01 
- Configure roundrobin load balancing for web-01 and web-02
- Manage HAproxy with init script
- Script 1-install_load_balancer automates this setup

### 2. Add a custom HTTP header with Puppet
- Automate adding custom HTTP header X-Served-By using Puppet
- Create manifest 2-puppet_custom_http_response_header.pp
