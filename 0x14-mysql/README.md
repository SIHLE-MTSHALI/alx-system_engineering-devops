# MySQL Primary-Replica Setup and Backup Strategy

## Overview
This project involves setting up a MySQL primary-replica infrastructure, creating a database and user for replication, and implementing a backup strategy using a Bash script.

## Files and Directories
- **4-mysql_configuration_primary**: Configuration file for the primary MySQL server.
- **4-mysql_configuration_replica**: Configuration file for the replica MySQL server.
- **5-mysql_backup**: Bash script to back up MySQL databases.

## Setup Instructions
1. **Install MySQL**: Install MySQL 5.7 on both `web-01` and `web-02`.
2. **Create MySQL User**: Create a user `holberton_user` with replication privileges on both servers.
3. **Create Database and Table**: On `web-01`, create a database `tyrell_corp` and a table `nexus6` with sample data.
4. **Create Replica User**: On `web-01`, create a `replica_user` with replication privileges.
5. **Configure Primary-Replica**: Configure `web-01` as the primary server and `web-02` as the replica server.
6. **Backup MySQL Databases**: Use the `5-mysql_backup` script to back up and compress the MySQL databases.

## Usage
- **Backup Script**: Run `./5-mysql_backup <password>` to create a backup of all MySQL databases.

## Verification
- Check the status of the primary and replica servers using MySQL commands.
- Verify the backup file creation in the project directory.
