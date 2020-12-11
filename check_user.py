#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:02:43 2019

@author: edoardottt

This file is under MIT License.

"""

import os
import sqlite3
import usage
import hashlib

db_filename = "database.db"
db_is_new = not os.path.exists(db_filename)


def create_user(conn, data, username):

    sql = """ INSERT INTO users VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


# check if user in input exists in database.db
def check_if_user_exists(username, password):
    if db_is_new:
        usage.print_usage(5)
    else:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        p = hashlib.sha256(password.encode("utf-8")).hexdigest()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? and password= ?", (username, p)
        )
        data = cursor.fetchone()
        if data is None:
            cred = (username, p)
            create_user(conn, cred, username)
            return False
        else:
            return True
