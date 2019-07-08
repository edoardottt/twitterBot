#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:36:32 2019

@author: edoardottt
"""

def print_usage():
    print('')
    print('Usage: python twitterbot.py -u [value] -p [value] {-h [values separated by comma] OR -s OR -m}')
    print('')
    print('-u or --username: ')
    print('')
    print("        It's your twitter username(e-mail)")
    print('')
    print('-p or --password:')
    print('')
    print("        It's your twitter account password.")
    print('')
    print("        It's needed only if -h is present.")
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
    print('        Insert only -u [value] -p [value] -m')
    print('')
    print('example:')
    print('')
    print('To start the bot searching for some words:')
    print(' python twitterbot.py -u replace_your_email@mail.com -p replace_your_password -h trend,topics,twitter')
    print('To start the bot with your feed:')
    print(' python twitterbot.py -u replace_your_email@mail.com -p replace_your_password -m')
    print('To see your account bot statistics')
    print(' python twitterbot.py -u replace_your_email@mail.com -s')
    print('----------------------------------')
    print('https://www.edoardoottavianelli.it')
    print('----------------------------------')