import os
import pandas as pd
import pymysql

class Database(object):
    def __init__(self, host='localhost', user = 'root', passwd = '123456', charset = 'utf8', db = None):
        if db is None:
            self.connect = pymysql.connect(host = host, user = user, passwd = passwd, charset = charset)
            print("hostserver connected")
        else:
            try:
                self.connect = pymysql.connect(host = host, user = user, passwd = passwd, charset = charset, db = db)
                print("database connected") 
            except:
                print("cannot connect to target database.")

    def direct_connect(self, host='localhost', user = 'root', passwd = '123456', charset = 'utf8', db = "database"):
        self.connect = pymysql.connect(host = host, user = user, passwd = passwd, charset = charset, db = db)
        print("database {} connected".format(db)) 
    
    def get_cursor(self):
        cur = self.connect.cursor()
        return cur

    def create_database(self, db_name):
        with self.get_cursor() as cur:
            r = cur.execute("create database {} character set utf8;".format(db_name))
            cur.close()
        self.connect.commit()
        print("create database {} finished.".format(db_name))
    
    def drop_database(self, db_name):
        with self.get_cursor() as cur:
            r = cur.execute("drop database {};".format(db_name))
            cur.close()
        self.connect.commit()
        print("database {} dropped.".format(db_name))

    
    def create_table(self, table_name, info):
        """
        create a new tale
        table_name: string, the name of new table
        info: list, the items of the new table. e.g.["name varchar(20)", "id int", ...]
        """
        table_construction = ','.join(info)
        with self.get_cursor() as cur:
            r = cur.execute("create table {} ({}) character set utf8;".format(table_name, table_construction))
            cur.close()
        self.connect.commit()
        print("create table {} finished.".format(table_name))
    

    def insert_into_table(self, table_name, info, show = False):
        """
        insert a new record into a table
        """
        return_table = None
        with self.get_cursor() as cur:
            r = cur.execute("insert into {} values({})".format(table_name, info))
            if show:
                cur.execute("select * from {}".format(table_name))
                return_table = cur.fetchall()
            cur.close()
        self.connect.commit()
        print("insert finished")
        return return_table
    
    def delete_from_table(self, table_name, condition, show = False):
        """
        delete a record from a table
        """
        return_table = None
        with self.get_cursor() as cur:
            r = cur.execute("delete from {} where {}".format(table_name, condition))
            if show:
                cur.execute("select * from {}".format(table_name))
                return_table = cur.fetchall()
            cur.close()
        self.connect.commit()
        print("delete finished")
        return return_table
    
    def update_table(self, table_name, info, condition, show = False):
        """
        update records of a table
        """
        return_table = None
        with self.get_cursor() as cur:
            r = cur.execute("update {} set {} where {}".format(table_name, info, condition))
            if show:
                cur.execute("select * from {}".format(table_name))
                return_table = cur.fetchall()
            cur.close()
        self.connect.commit()
        print("update finished")
        return return_table


    def query(self, query):
        with self.get_cursor() as cur:
            # group_id, user_id, card_id
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
        self.connect.commit()
        return result


    def do_sql(self, command):
        with self.get_cursor() as cur:
            # group_id, user_id, card_id
            cur.execute(command)
            result = cur.fetchall()
            cur.close()
        self.connect.commit()
    
    def disconnect(self):
        self.connect.close()
        print("detached from database")
    
    