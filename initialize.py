import os
import pandas as pd
import pymysql

from utils.basic_pymysql import *
from utils.operations import *


def initialize(db_name = "Lab_Management_System"):
    db = Database()

    #create database
    try:
        db.create_database(db_name)
    except:
        delete = input("Existing database {}, continue? Y/N\n".format(db_name))
        if delete == "Y":
            db.drop_database(db_name)
            db.create_database(db_name)
    
    db.direct_connect(db = db_name)
    
    # create table admins
    db.create_table("admins", info = ["id CHAR(10) NOT NULL", "name VARCHAR(10)", "PRIMARY KEY (id)"])
    #db.insert_into_table("admins", info = "'{}' {} '{}'".format(admin_name, admin_id))

    #create table admin_passwords
    db.create_table("admin_passwords", info = ["id CHAR(10) NOT NULL", "password VARCHAR(20) NOT NULL", "PRIMARY KEY (id)", "FOREIGN KEY (id) REFERENCES admins(id)"])
    #db.insert_into_table("admins", info = "{} '{}'".format(admin_id, admin_password))

    # create table participants
    db.create_table("participants", info = ["id CHAR(10) NOT NULL", "name VARCHAR(10)", "gender CHAR(2)", "age INT", "outcome VARCHAR(20)", "PRIMARY KEY (id)"])

    # create table responsible
    db.create_table("responsible", info=["admin_id CHAR(10) NOT NULL", "participant_id CHAR(10) NOT NULL", "FOREIGN KEY (admin_id) REFERENCES admins(id)","FOREIGN KEY (participant_id) REFERENCES participants(id)"])


initialize()