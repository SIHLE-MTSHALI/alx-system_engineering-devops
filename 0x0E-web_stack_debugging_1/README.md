# 0x0E. Web stack debugging #1

This project focuses on debugging a web stack, specifically an issue with Nginx not listening on port 80 in an Ubuntu container.

## Files

- `0-nginx_likes_port_80`: Bash script that configures Nginx to listen on port 80.
- `1-debugging_made_short`: Bash script that provides a shorter version of the fix for Nginx.

## Requirements

- All files are interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck without any error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script does.
- `wget` is not allowed.

## Tasks

### 0. Nginx likes port 80

Using debugging skills, find out what's keeping the Ubuntu container's Nginx installation from listening on port 80. Write a Bash script with the minimum number of commands to automate the fix.

### 1. Make it sweet and short

Using what you did for task #0, make your fix short and sweet. The Bash script must be 5 lines long or less.
