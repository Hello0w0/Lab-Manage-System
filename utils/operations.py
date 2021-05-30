import os
import pandas as pd
import pymysql

from .basic_pymysql import *


def initialize(db_name = "Lab_Management_System"):
    """
    initialize the system
    """
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
    db.create_table("admins", info = ["name VARCHAR(20)", "id INT NOT NULL", "PRIMARY KEY (id)"])
    #db.insert_into_table("admins", info = "'{}' {} '{}'".format(admin_name, admin_id))

    #create table admin_passwords
    db.create_table("admin_passwords", info = ["id INT NOT NULL", "password VARCHAR(20) NOT NULL", "PRIMARY KEY (id)", "FOREIGN KEY (id) REFERENCES admins(id)"])
    #db.insert_into_table("admins", info = "{} '{}'".format(admin_id, admin_password))

    # create table participants
    db.create_table("participants", info = ["name VARCHAR(20)", "id INT NOT NULL", "PRIMARY KEY (id)"])

    # create table responsible
    db.create_table("responsible", info=["admin_id INT NOT NULL", "participant_id INT NOT NULL", "FOREIGN KEY (admin_id) REFERENCES admins(id)","FOREIGN KEY (participant_id) REFERENCES participants(id)"])

def Check_password(admin_id, password):
    pass

class Account_modify(object):
    def __init__(self, database):
        self.db = Database(db = database)

    def add_admin(self, name, id, password):
        self.db.insert_into_table("admins", info = "'{}' {} '{}'".format(name, id))
        self.db.insert_into_table("admin_passwords", info = "'{}'".format(password))
        


class Admin(object):
    def __init__(self, admin_id):
        
        pass

    def add_participant(self, info):
        pass

    def delete_participant(participant_id):
        pass

    def update_participant(info):
        pass

    def change_password(self, new_password):
        pass

    def observe(self, participant_id):
        pass


class Participant(object):
    def __init__(self, participant_id):
        pass

    def observe(self):
        pass
