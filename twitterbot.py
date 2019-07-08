#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:12:13 2019

@author: edoardottt

version = 1.2
"""

#VARIABLES TO CHANGE-----------------------------
email_email = ''
email_password = ''
password_flag = False
hashtags = []
connection = 2
hashtag_flag = False
stat_flag = False
my_flag = False
limit = 50000
#-----------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime
import getopt,sys
import check_user
import add_result
import analyze_stat
import usage


options,remainder =getopt.getopt(sys.argv[1:], 'u:p:h:sml',['username','password','hashtags','stat','mine'])
for opt, arg in options:
    if opt in ('-u','--username'):
        email_email = arg
    elif opt in ('-p','--password'):
        email_password = arg
        password_flag = True
    elif opt in ('-h','--hashtags'):
        try:
            hashtag_flag = True
            hashtags = arg.split(',')
        except Exception as ex:
            usage.print_usage()
            sys.exit()
    elif opt in ('-s','--stat'):
        stat_flag = True
    elif opt in ('-m','--mine'):
        my_flag = True

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
        try:
            email = bot.find_element_by_class_name("email-input")
            password = bot.find_element_by_name('session[password]')
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(self.generate_random())
            try:
                auth_flag = bot.find_element_by_css_selector("h1.Icon.Icon--bird.bird-topbar-etched")
                if (auth_flag != None):
                    print('Logged in as '+self.username+' !')
                    return True
            except Exception as ex:
                print('Error n.1:')
                print('Invalid Credentials.')
                sys.exit()
            
        except Exception as ex:
            print('Error n.2:')
            print('Make sure that your Firefox window are in Desktop mode')
            sys.exit()
        
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
        
    def add_links_my_home(self):
        print('adding links...')
        bot = self.bot
        for i in range(6):
            bot.execute_script('window.scroll(0,document.body.scrollHeight)')
            time.sleep(connection)
        time.sleep(connection)
        tweets = bot.find_elements_by_class_name('tweet')
        self.links = [elem.get_attribute('data-permalink-path') for elem in tweets]
        random.shuffle(self.links)
        print('links added!')
        
    def crawl(self):
        print('TwitterBot started!')
        for link in self.links:
            if((not link is None) and (self.likes<limit)):
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
                    time.sleep(20)
        print('Finished!')

if((email_email!='')and(email_password!='')and(not stat_flag)and((my_flag and (not hashtag_flag))or(hashtag_flag and (not my_flag)))):
    edoBot = TwitterBot(email_email,email_password,0,0,hashtags)
    authenticated = edoBot.login()
    if(authenticated):
        check_user.check_if_user_exists(edoBot.username,edoBot.password)
        if(hashtag_flag and(not my_flag)):
            edoBot.add_links()
        elif(my_flag and(not hashtag_flag)):
            edoBot.add_links_my_home()
        else:
            usage.print_usage()
        edoBot.crawl()
        timee = datetime.datetime.now()
        add_result.add_stat(edoBot.username,timee,edoBot.likes,edoBot.retweets)
elif((email_email!='')and(not password_flag)and(not hashtag_flag)and(stat_flag)and(not my_flag)):
    analyze_stat.check_stat(email_email)
else:
    usage.print_usage()