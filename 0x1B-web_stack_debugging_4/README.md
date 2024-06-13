# 0x1B. Web stack debugging #4

## Description

This project involves debugging and optimizing a web stack running on an Ubuntu 14.04 LTS server. We are focusing on resolving issues with high failed requests under load and adjusting user limits.

## Requirements

- All files are interpreted on Ubuntu 14.04 LTS
- All files end with a new line
- Puppet manifests pass puppet-lint version 2.1.1 without any errors
- Puppet manifests run without error
- Puppet manifests first line is a comment explaining what the Puppet manifest is about
- Puppet manifests files end with the extension .pp
- Files checked with Puppet v3.4

## Files

### 0-the_sky_is_the_limit_not.pp

- **Description:** Configures Nginx to handle more requests by tuning its settings.
- **Location:** `0x1B-web_stack_debugging_4/0-the_sky_is_the_limit_not.pp`

### 1-user_limit.pp

- **Description:** Increases the open file limit for the user `holberton`.
- **Location:** `0x1B-web_stack_debugging_4/1-user_limit.pp`

## Installation of Required Tools

1. Install Ruby and Puppet-lint:
   ```sh
   apt-get install -y ruby
   gem install puppet-lint -v 2.1.1

