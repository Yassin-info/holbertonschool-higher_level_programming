# Python - Object-relational mapping

This project explores connecting Python with MySQL databases using two approaches:
1. **MySQLdb**: Direct SQL queries with Python
2. **SQLAlchemy**: Object-Relational Mapping (ORM)

## Learning Objectives

- Connect to a MySQL database from a Python script
- SELECT, INSERT, UPDATE, and DELETE rows in MySQL tables using Python
- Understand Object-Relational Mapping (ORM)
- Map Python Classes to MySQL tables using SQLAlchemy
- Prevent SQL injection attacks

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- pycodestyle 2.7.*
- All files must be executable
- All modules, classes, and functions must have documentation

## Installation

```bash
# Install MySQL 8.0
sudo apt update
sudo apt install mysql-server

# Install MySQLdb
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient==2.0.3

# Install SQLAlchemy
sudo pip3 install SQLAlchemy==1.4.22
```

## Tasks

0. **Get all states** - List all states from database using MySQLdb
1. **Filter states** - List states starting with 'N'
2. **Filter states by user input** - Display states matching user input
3. **SQL Injection...** - Safe version preventing SQL injection
4. **Cities by states** - List all cities with their states
5. **All cities by state** - List cities of a specific state
6. **First state model** - Define State class with SQLAlchemy
7. **All states via SQLAlchemy** - List all State objects using ORM
8. **First state** - Print first State object
9. **Contains `a`** - List states containing letter 'a'
10. **Get a state** - Find state by name
11. **Add a new state** - Insert new State object
12. **Update a state** - Change state name
13. **Delete states** - Remove states containing 'a'
14. **Cities in state** - Define City model and list all cities

## Author

Holberton School Project
