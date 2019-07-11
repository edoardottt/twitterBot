#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:36:32 2019

@author: edoardottt
"""

import sys

def print_usage(a):
    if a==0:
        print('')
        print('Usage: python twitterbot.py -u [value] {-h [value OR values separated by comma] OR -s OR -m}')
        print('')
        print('-u or --username: ')
        print('')
        print("        It's your twitter username(e-mail)")
        print('')
        print('-h or --hashtags:')
        print('')
        print("        It's/They are the hashtag[s] you want to 'follow'")
        print('')
        print('        If you want to insert multiple hashtags you have to separated them by comma:')
        print('')
        print('        e.g. -h climatechange,techtips,python')
        print('')
        print('-s or --stat:')
        print('')
        print('        If you want to see your stats account.')
        print('')
        print('        Insert only -u [value] -s')
        print('')
        print('-m or --mine:')
        print('')
        print("        If you want to 'follow' your feed's tweets.")
        print('')
        print('        Insert only -u [value] -m')
        print('')
        print('example:')
        print('')
        print('To start the bot searching for some words:')
        print(' python twitterbot.py -u replace_your_email@mail.com -h trend,topics,twitter')
        print('To start the bot with your feed:')
        print(' python twitterbot.py -u replace_your_email@mail.com -m')
        print('To see your account bot statistics')
        print(' python twitterbot.py -u replace_your_email@mail.com -s')
        print('----------------------------------')
        print('https://www.edoardoottavianelli.it')
        print('----------------------------------')
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
    sys.exit()
        