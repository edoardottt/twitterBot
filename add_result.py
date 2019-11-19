#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:19:23 2019

@author: edoardottt

This file stores the final result of a crawling session in the database.

This file is under MIT License.

"""

import os
import sqlite3
import usage

db_filename = 'database.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

def create_stat(conn, data):
 
    sql = ''' INSERT INTO analytics VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

def add_stat(username,timestamp,likes,retweets,followers):
    if db_is_new:
        usage.print_usage(5)
    else:
        data = (username,timestamp,likes,retweets,followers)
        create_stat(conn,data)