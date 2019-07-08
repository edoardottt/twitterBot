#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:52:08 2019

@author: edoardottt
"""

import os
import sqlite3

db_filename = 'database.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

def check_stat(username):
    if(db_is_new):
        print('Error n.3')
        print('Noone database detected.')
        print('Execute the initdb.py file by typing in your command line:')
        print('python initdb.py')
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM analytics WHERE username = ?", (username,))
        data=cursor.fetchall()
        if (data!=None):
            if(len(data)!=0):
                for record in data:
                    print(record)
            else:
                print('There are no data for that username.')
                
    conn.close()