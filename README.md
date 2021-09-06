# Applied Databases project.

This repository contains a collection of files for the Applied Databases project submitted as part of the requirement for the Applied Databases module at GMIT as part of the Higher Diploma in Computing and Data Analytics programme.
The actual project was to be submitted through the college Moodle platform as a zip file. This repository serves as a reference for the project.


The Applied Databases module provided a primer on databases with a focus on data analysis; CRUD ( Creation, Retrieval, Update and Deletion) of both structured and unstructured data for a number of modern database systems and architectures; Topics on Relational databases, NoSQL databases, databases interfaces and database logic.

The final project had four different sections.
1. Working with a relational database and writing MySQL queries
2. Working with a non-relational database and writing MongoDb queries.
3. Writing a Python application that allows a user to perform CRUD operations on both relational and non-relational databases. 
4. A discussion on normalization. 

## Repository Content

- This README file
- A folder named ADBP containing a subfolder for each of the 4 sections of the project
  * 4.1 `project_sql` containing the MySQL queries and some comments in a Markdown file.
  * 4.2 `project_mongo` containing the MongoDb queries together with some comments in a Markdown file
  * 4.3 `normalisation` containing a notebook with my answer to the question on database design and normalisation.
  * 4.4 `py_app` containing the Python code for the Python application in 3 Python files.
    1. `menu.py` contains the main menu for the application to interface with both the MySQL database and the MongoDb database.
    2. `mongo_connect.py` a module for connecting to the MongoDb database using the `pymongo` module.
    3. `mysql_connect.py` a module for connecting to the MySQL database using the `pymysql` module.

- The final project specification in PDF format
- The question relating to database design and normalization in PDF format









