#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:52:08 2019

@author: edoardottt
"""

import os
import sys
import usage
import sqlite3

try:
    import matplotlib.pyplot as plt
except Exception as ex:
    usage.print_usage(4)

db_filename = 'database.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

def check_stat(username,password):
    timestamps = []
    likes = []
    retweets = []
    d_likes = {}
    d_retweets = {}
    if(db_is_new):
        usage.print_usage(5)
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? and password = ?", (username,password))
        data = cursor.fetchone()
        if(data==None):
            print('There are no data for that username.')
            sys.exit()
        cursor.execute("SELECT * FROM analytics WHERE username = ?", (username,))
        data=cursor.fetchall()
        if (data!=None):
            if(len(data)!=0):
                for record in data:
                    timestamps += [record[1]]
                    likes += [int(record[2])]
                    retweets += [int(record[3])]
                for i in range(len(timestamps)):
                    if (not(timestamps[i][:-16] in d_likes)):
                        for j in range(len(timestamps)):
                            if timestamps[i][:-16]==timestamps[j][:-16]:
                                if timestamps[i][:-16] in d_likes:
                                    d_likes[timestamps[i][:-16]] += likes[j]
                                else:
                                    d_likes[timestamps[i][:-16]] = likes[j]
                                if timestamps[i][:-16] in d_retweets:
                                    d_retweets[timestamps[i][:-16]] += retweets[j]
                                else:
                                    d_retweets[timestamps[i][:-16]] = retweets[j]
                plt.subplots_adjust(bottom=0.2)
                plt.xticks( rotation=45 )
                ax=plt.gca()
                ax.xaxis_date()
                date = [i for i in d_likes.keys()]
                likes_vector = [d_likes[i] for i in date]
                retweets_vector = [d_retweets[i] for i in date]
                plt.plot(date,likes_vector, '-r', label='likes')
                plt.plot(date,retweets_vector, '-g', label='retweets')
                plt.legend(loc='upper center')
                print('Total likes: '+str(sum(likes)))
                print('Total retweets: '+str(sum(retweets)))
                for a,b in zip(date, likes_vector):
                    plt.text(a, b, str(b))
                for a,b in zip(date, retweets_vector):
                    plt.text(a, b, str(b))
                plt.title('Statistics for '+username)
                plt.subplots_adjust(left=None, bottom=0.13, right=0.98, top=0.94, wspace=None, hspace=None)
                plt.show()
            else:
                print('There are no data for that username.')
                
    conn.close()