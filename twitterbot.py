#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:12:13 2019

@author: edoardottt
"""

#VARIABLES TO CHANGE-----------------------------
email_email = ''
email_password = ''
hashtags = []
connection = 2
#-----------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime
import getopt,sys

version = '1.0'

options,remainder =getopt.getopt(sys.argv[1:], 'u:p:h:',['username','password','hashtags'])
for opt, arg in options:
    if opt in ('-u','--username'):
        email_email = arg
    elif opt in ('-p','--password'):
        email_password = arg
    elif opt in ('-h','--hashtags'):
        hashtags = arg.split(',')
        
        
def print_usage():
    print('Usage: python twitterbot.py -u [value] -p [value] -h [values separated by comma]')
    print('-u or --username is your twitter username(e-mail)')
    print('-p or --password is your twitter account password')
    print('-h or --hashtags is/are the hashtag[s] you want to "follow"')
    print('If you want to insert multiple hashtags you have to separated them by comma:')
    print('e.g. -h climatechange,techtips,python')
    print('----------------------------------')
    print('https://www.edoardoottavianelli.it')
    print('----------------------------------')

class TwitterBot:
    
    def __init__(self, username, password,likes,retweets,hashtags):
        self.username = username
        self.password = password
        self.likes = 0
        self.retweets = 0
        self.hashtags = hashtags
        self.links = []
        self.bot = webdriver.Firefox()
        
    def generate_random(self):
        rand = random.randint(6,13)
        return rand
    def generate_mid_random(self):
        rand = random.randint(1,2)
        if(rand == 1):
            return True
        else:
            return False
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(self.generate_random())
        email = bot.find_element_by_class_name("email-input")
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(self.generate_random())
        print('Logged in as '+self.username+' !')
        
    def add_links(self):
        print('adding links...')
        bot = self.bot
        for hashtag in self.hashtags:
            bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
            time.sleep(connection)
            bot.execute_script('window.scroll(0,document.body.scrollHeight)')
            time.sleep(connection)
            tweets = bot.find_elements_by_class_name('tweet')
            self.links += [elem.get_attribute('data-permalink-path') for elem in tweets]
        random.shuffle(self.links)
        print('links added!')
        
    def crawl(self):
        print('TwitterBot started!')
        for link in self.links:
            if(not link is None):
                self.bot.get('https://twitter.com'+link)
                try:
                    self.bot.find_element_by_class_name('HeartAnimation').click()
                    self.likes += 1
                    time.sleep(1)
                    if(self.generate_mid_random()):
                        self.bot.find_element_by_css_selector("button.ProfileTweet-actionButton.js-actionButton.js-actionRetweet").click()
                        time.sleep(2)
                        self.bot.find_element_by_class_name('RetweetDialog-retweetActionLabel').click()
                        self.retweets += 1
                    result = "likes: " + str(self.likes)+' | '+"retweets: " + str(self.retweets)
                    print(datetime.datetime.now())
                    print(result)
                    time.sleep(self.generate_random())
                except Exception as ex:
                    time.sleep(50)
        print('Finished!')

if((email_email!='')and(email_password!='')and(len(hashtags)!=0)):
    edoBot = TwitterBot(email_email,email_password,0,0,hashtags)
    edoBot.login()
    edoBot.add_links()
    edoBot.crawl()
else:
    print_usage()