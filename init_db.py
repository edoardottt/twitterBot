#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:41:22 2019

@author: edoardottt
"""

import os
import sqlite3

db_filename = 'database.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

if db_is_new:
    sql_create_users_table = """ CREATE TABLE users (
                                        username text PRIMARY KEY,
                                        password text NOT NULL
                                    ); """
 
    sql_create_analytics_table = """CREATE TABLE analytics (
                                    username text NOT NULL,
                                    date date NOT NULL,
                                    likes integer NOT NULL,
                                    retweets integer NOT NULL,
                                    followers integer NOT NULL,
                                    PRIMARY KEY (username,date)
                                    FOREIGN KEY (username) REFERENCES users (username)
                                );"""
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_analytics_table)
conn.close()
