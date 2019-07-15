#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:02:43 2019

@author: edoardottt

This file is under MIT License.

"""

import os
import sqlite3

db_filename = 'database.db'
db_is_new = not os.path.exists(db_filename)

def create_user(conn, data,username):
 
    sql = ''' INSERT INTO users VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

# check if user in input exists in database.db
def check_if_user_exists(username,password):
    if(db_is_new):
        print('Error n.3')
        print('Noone database detected.')
        print('Execute the initdb.py file by typing in your command line:')
        print('python initdb.py')
    else:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        data=cursor.fetchone()
        if (data==None):
            cred = (username,password)
            create_user(conn,cred,username)
            return False
        else:
            return True
