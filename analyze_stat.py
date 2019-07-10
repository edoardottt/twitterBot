#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:52:08 2019

@author: edoardottt
"""

import os,sys
import sqlite3
import datetime as dt

try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as md
except Exception as ex:
    print('Execute "python -m pip install -U matplotlib"')
    sys.exit()

db_filename = 'database.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

def check_stat(username):
    timestamps = []
    likes = []
    retweets = []
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
                    timestamps += [record[1]]
                    likes += [record[2]]
                    retweets += [record[3]]
                plt.subplots_adjust(bottom=0.2)
                plt.xticks( rotation=25 )
                ax=plt.gca()
                ax.xaxis_date()
                plt.plot(timestamps,likes, '-r', label='likes')
                plt.plot(timestamps,retweets, '-g', label='retweets')
                plt.legend(loc='upper left')
                print('Total likes: '+str(sum(likes)))
                print('Total retweets: '+str(sum(retweets)))
                for a,b in zip(timestamps, likes):
                    plt.text(a, b, str(b))
                for a,b in zip(timestamps, retweets):
                    plt.text(a, b, str(b))
                plt.title('Statistics for '+username)
                plt.show()
            else:
                print('There are no data for that username.')
                
    conn.close()