from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#This help to interact with the database object
from sqlalchemy.ext.declarative import declarative_base

# URL to create a location of this database on our fastAPI application
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

#Database Engine: It is something that we can use to be able to open up a connection and be able to use our database

#'connect_args' allow connection to the database
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

#We need to create a session local and each instance of the session local will have a database session

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()