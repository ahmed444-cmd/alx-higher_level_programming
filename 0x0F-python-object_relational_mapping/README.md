0x0F. Python - Object-relational Mapping
Description
This project aims to teach you how to use an Object-relational Mapper (ORM). You'll start by using the MySQLdb module to connect to a MySQL database in Python, then transition to using SQLAlchemy, another popular ORM.

Background Context
In this project, you'll be bridging the gap between two fascinating domains: Databases and Python.

Initially, you'll use the MySQLdb module to connect to a MySQL database and run SQL queries. In the next phase, you'll utilize SQLAlchemy (pronounced "SQL Alchemy"), an ORM that abstracts database storage, allowing you to focus on interacting with objects rather than writing SQL queries.

The primary advantage of using an ORM is that it eliminates the need to write SQL queries. Instead, you will focus on manipulating your objects, not worrying about how and where they are stored. Additionally, your code will be storage type-agnostic, making it easier to switch storage solutions without rewriting your project.

Resources
Object-relational mappers
MySQLdb documentation (ignore references to _mysql)
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy documentation
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet
SQLAlchemy ORM Tutorial for Python Developers (Note: This tutorial uses PostgreSQL, but the concepts are applicable to MySQL)
SQLAlchemy Tutorial

Installation Instructions
MySQLdb Module Version 2.0.x
To install the MySQLdb module, ensure MySQL is installed:

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient


Verify installation:

$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)


SQLAlchemy Module Version 1.4.x
Install SQLAlchemy:

$ sudo pip3 install SQLAlchemy


Verify installation:

$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
