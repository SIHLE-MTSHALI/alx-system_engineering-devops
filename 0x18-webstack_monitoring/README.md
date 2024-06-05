# 0x18. Webstack Monitoring

## Project Overview

This project involves setting up monitoring for web servers using Datadog. The tasks include signing up for Datadog, installing the Datadog agent, monitoring specific system metrics, and creating a dashboard with various widgets.

## Files

- `README.md`: Comprehensive documentation of the project.
- `2-setup_datadog`: File containing the dashboard ID.

## Tasks

### Task 0: Sign up for Datadog and install datadog-agent

1. Sign up for a free Datadog account.
2. Install the Datadog agent on the web-01 server.
3. Create an application key and add the Datadog API key and application key to your Intranet user profile.

### Task 1: Monitor some metrics

1. Set up monitors in Datadog to check the number of read and write requests issued to the device per second.

### Task 2: Create a dashboard

1. Create a new dashboard in Datadog.
2. Add at least 4 widgets to the dashboard.
3. Save the dashboard ID in the file `2-setup_datadog`.

## Installation Guide

1. **Install Datadog Agent:**
   ```sh
   sudo apt-get update
   sudo apt-get install -y apt-transport-https
   sudo sh -c "echo 'deb https://apt.datadoghq.com/ stable 7' > /etc/apt/sources.list.d/datadog.list"
   sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C7A7DA52
   sudo apt-get update
   sudo apt-get install -y datadog-agent
   sudo sh -c "sed -i 's/api_key:.*/api_key: <YOUR_DATADOG_API_KEY>/' /etc/datadog-agent/datadog.yaml"
   sudo systemctl restart datadog-agent

