# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:36:32 2019

@author: edoardottt


This file has a method called print_usage that brings as input a number (the error code).
It prints the appropriate error code and error message.
Then It quits.

This file is under MIT License.


"""

import sys

def print_usage(a):
    if a==0:
        print('')
        print('Usage: python twitterbot.py -u [value] {-k [value OR values separated by comma] OR -s OR -m} -i OR -h')
        print('')
        print('-u or --username: ')
        print('')
        print("        It's your twitter username(e-mail)")
        print('')
        print('-k or --keywords:')
        print('')
        print("        It's/They are the keyword[s] you want to crawl")
        print('')
        print('        If you want to insert multiple keywords you have to separated them by comma:')
        print('')
        print('        e.g. -k climatechange,techtips,python')
        print('')
        print('-s or --stat:')
        print('')
        print('        If you want to see your stats account.')
        print('')
        print('        Insert only -u [value] -s')
        print('')
        print('-m or --mine:')
        print('')
        print("        If you want to crawl your feed's tweets.")
        print('')
        print('        Insert only -u [value] -m')
        print('')
        print('-i or --info:')
        print('')
        print("        To see info")
        print('')
        print('        Insert only -i')
        print('')
        print('-h or --help:')
        print('')
        print("        Help doc")
        print('')
        print('        Insert only -h')
        print('')
        print('')
        print('-f or --follow:')
        print('')
        print("        Insert an username. The bot will check for some")
        print("        followers of that username and it tries to follow them.")
        print('')
        print('        Insert -f username')
        print('')
        print('examples:')
        print('')
        print('To start the bot searching for some keywords:')
        print('    python twitterbot.py -u replace_your_email@mail.com -k trend,topics,twitter')
        print('To start the bot with your feed:')
        print('    python twitterbot.py -u replace_your_email@mail.com -m')
        print('To see your account bot statistics:')
        print('    python twitterbot.py -u replace_your_email@mail.com -s')
        print('To see info:')
        print('    python twitterbot.py -i')
        print('Help: ')
        print('    python twitterbot.py -h')
    elif a==1:
        print('Error n.1:')
        print('Invalid Credentials.')
    elif a==2:
        print('Error n.2:')
        print('Make sure that your Firefox window are in Desktop mode.')
    elif a==3:
        print('Error n.3:')
        print('Execute "pip install selenium" on command line.')
    elif a==4:
        print('Error n.4:')
        print('Execute "python -m pip install -U matplotlib" on command line.')
    elif a==5:
        print('Error n.5:')
        print('Noone database detected.')
        print('Execute the initdb.py file by typing in your command line:')
        print('python init_db.py')
    elif a==6:
        print('Error n.6:')
        print('Check if the internet connection is on.')
    elif a==7:
        print('twitterBot v1.3.3')
        print('This project is under MIT License.')
        print('To know about twitterBot: ')
        print('This product is kept on   https://github.com/edoardottt/twitterBot')
        print('Edoardo Ottavianelli')
        print('https://edoardoottavianelli.it')
    elif a==8:
        print('Error 8: ')
        print('Bad input')
        print('See the help documentation')
        print('typing only the -h or --help option.')
    sys.exit()
        