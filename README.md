# Moto

# Project Description
[UML class and package diagram of code design]()

# Install Instruction

### Install required packages
Go to the directory and install the required packages
  ```python
  pip install -r requirements.txt
  ```
### Create the database and table schema and add initial data
Go to the directory and create "sample.db" using schema commands in a file
  ```python
  sqlite3 moto.db < moto.schema
  ```
Open the database file with the sqlite command line utility
  ```python
  sqlite3 moto.db
  ```
Import the data from csv to the database file
  ```python
  sqlite> .mode csv
  sqlite> .import data/Users.csv users
  sqlite> .import data/Moto.csv moto
  ```
### Configure and run the application
Run the application
  ```python
  python main.py
  ```
