# 0x13. Firewall Project

## Overview
This project involves configuring a firewall on a web server to block all incoming traffic except for specific ports and setting up port forwarding. We will use `ufw` (Uncomplicated Firewall) to manage our firewall rules.

## Files

### 0-block_all_incoming_traffic_but
This script installs `ufw` and configures it to block all incoming traffic except for TCP ports 22 (SSH), 443 (HTTPS), and 80 (HTTP).

### 100-port_forwarding
This configuration file sets up port forwarding on `web-01` so that traffic on port 8080/TCP is redirected to port 80/TCP.

## Installation and Usage

### Task 0: Block All Incoming Traffic But
1. Install UFW:
    ```sh
    sudo apt-get update
    sudo apt-get install ufw
    ```
2. Allow specific ports:
    ```sh
    sudo ufw allow 22/tcp
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    ```
3. Block all other incoming traffic:
    ```sh
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    ```
4. Enable UFW:
    ```sh
    sudo ufw enable
    ```
5. Verify UFW status:
    ```sh
    sudo ufw status verbose
    ```

### Task 1: Port Forwarding
1. Open the UFW configuration file:
    ```sh
    sudo vim /etc/ufw/before.rules
    ```
2. Add port forwarding rules before the `*filter` line:
    ```sh
    *nat
    :PREROUTING ACCEPT [0:0]
    :INPUT ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    :POSTROUTING ACCEPT [0:0]

    # Port forwarding rule
    -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80

    COMMIT
    ```
3. Enable UFW:
    ```sh
    sudo ufw reload
    ```
4. Verify the port forwarding:
    ```sh
    sudo ufw status verbose
    ```

## Testing
To test the configuration, use the following commands:
1. Check the status of the firewall:
    ```sh
    sudo ufw status verbose
    ```
2. Use `curl` to verify port forwarding:
    ```sh
    curl -sI http://web-01.holberton.online:80
    curl -sI http://web-01.holberton.online:8080
    ```

## Conclusion
This project demonstrates how to configure `ufw` to manage firewall rules and set up port forwarding on a web server. By following the steps provided, you can secure your server and ensure that only specific ports are accessible.

