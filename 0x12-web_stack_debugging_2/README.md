# Web Stack Debugging #2

This project is about debugging issues in web stack configurations and ensuring best practices for running services under the correct user permissions.

## Files

- `0-iamsomeoneelse`: Script to run `whoami` as a specified user.
- `1-run_nginx_as_nginx`: Script to configure Nginx to run as the nginx user.
- `100-fix_in_7_lines_or_less`: A concise version of the script to configure Nginx to run as the nginx user, within 7 lines.

## Setup and Usage

1. **Run Software as Another User**
    - Usage: `./0-iamsomeoneelse <user>`
    - Example: `./0-iamsomeoneelse www-data`

2. **Run Nginx as Nginx**
    - Usage: `./1-run_nginx_as_nginx`
    - Verify: `ps aux | grep ngin[x]`

3. **7 Lines or Less**
    - Usage: `./100-fix_in_7_lines_or_less`
    - Verify: `ps aux | grep ngin[x]`

## Testing

Ensure the scripts are executable:
```sh
chmod +x 0-iamsomeoneelse 1-run_nginx_as_nginx 100-fix_in_7_lines_or_less
