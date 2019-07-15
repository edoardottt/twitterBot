#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:12:13 2019

@author: edoardottt

version = 1.3.2


This is the main file.
This file must be execute from the command line because It have to read the input arguments (via getopt).
It searches for tweet links found in your personal Feed/via search input field.
It can: Put likes on tweets and retweets them.
It defines a class called TwitterBot.
TwitterBot elements are built with 6 elements: username, password,likes,retweets,hashtags,followers.


This file is under MIT License.


"""

#VARIABLES TO CHANGE-----------------------------
email_email = ''
email_password = ''
password_flag = False   # True if the password has been entered
hashtags = []   # the list of words you want to search in the input field
connection = 2  # time to wait
hashtag_flag = False    # True if the -h option has been entered
stat_flag = False   # True if the -s option has been entered
my_flag = False     # True if the -m option has been entered
limit = 50000   # Limit of the links crawled 
#-----------------------------------------------
import time
import getopt
import getpass
import random
import datetime
import check_user
import add_result
import analyze_stat
import sys,usage

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except Exception as ex:
    usage.print_usage(3)
# all the libraries It needs

try:
    options,remainder =getopt.getopt(sys.argv[1:], 'u:h:sm',['username','hashtags','stat','mine'])  # all the options allowed
    for opt, arg in options:
        if opt in ('-u','--username'):
            email_email = arg
        elif opt in ('-h','--hashtags'):
            try:
                hashtag_flag = True
                hashtags = arg.split(',')   # if more than one hashtag has been entered, split them and put into hashtags
            except Exception as ex:
                usage.print_usage(0)
        elif opt in ('-s','--stat'):
            stat_flag = True
        elif opt in ('-m','--mine'):
            my_flag = True
except Exception as ex:
    usage.print_usage(0)

class TwitterBot:
    
    def __init__(self, username, password,likes,retweets,hashtags,followers):
        self.username = username
        self.password = password
        self.likes = 0
        self.retweets = 0
        self.followers = 0
        self.hashtags = hashtags
        self.links = []
        self.bot = webdriver.Firefox()
        
    def generate_random(self):  # It returns a random value between 5 and 8. That number indicates the seconds to be wait 
        rand = random.randint(5,8)
        return rand
    def generate_mid_random(self):  # Like a coin toss. 1/2 True - 1/2 False
        rand = random.randint(1,2)
        if(rand == 1):
            return True
        else:
            return False
    
    # login
    def login(self): 
        bot = self.bot
        bot.get('https://twitter.com/')     # Get the content of https://twitter.com/
        time.sleep(self.generate_random())  # This line of code WHEREVER wait for n [5-8] seconds.
        try:
            email = bot.find_element_by_class_name("email-input")       # Get the email input field.
            password = bot.find_element_by_name('session[password]')    # Get the password input field.
            email.clear()   # clear the email input field
            password.clear()    # clear the password input field
            email.send_keys(self.username)  # confirm
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN) # send the inputs entered
            time.sleep(self.generate_random())  
            auth_flag = None
            try:
                auth_flag = bot.find_element_by_css_selector("h1.Icon.Icon--bird.bird-topbar-etched") # auth_flag = get the bird icon on top of the page if the authentication is Okay
            except Exception as ex:
                usage.print_usage(1)
            if (auth_flag != None):     # if the user is authorized
                follower_elem = bot.find_element_by_css_selector('li.ProfileCardStats-stat:nth-child(3) > a:nth-child(1) > span:nth-child(2)')
                self.followers = follower_elem.get_attribute('data-count') # get the followers count
                return True
        except Exception as ex:
            usage.print_usage(2)
    
    # add tweets links from search input field by typing the hashtags entered
    def add_links(self):
        print('adding links...')
        bot = self.bot
        for hashtag in self.hashtags:
            bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')    # search the i-th hashtag
            time.sleep(connection)
            bot.execute_script('window.scroll(0,document.body.scrollHeight)')   # scroll the page
            time.sleep(connection)
            tweets = bot.find_elements_by_class_name('tweet') # handle all the tweets shown
            self.links += [elem.get_attribute('data-permalink-path') for elem in tweets]    #get all the links of the tweets
        random.shuffle(self.links)
        print(str(len(self.links))+' links added!')
        
    #add tweets links from the personal feed    
    def add_links_my_home(self):
        print('adding links...')
        bot = self.bot
        for i in range(7):
            bot.execute_script('window.scroll(0,document.body.scrollHeight)')   #scroll the page
            time.sleep(connection)
        time.sleep(connection)
        tweets = bot.find_elements_by_class_name('tweet')   # handle all the tweets shown
        self.links = [elem.get_attribute('data-permalink-path') for elem in tweets]    #get all the links of the tweets
        random.shuffle(self.links)
        print(str(len(self.links))+' links added!')

    # put likes and maybe rwtweets all the tweets reached
    def crawl(self):
        print('TwitterBot started at '+str(datetime.datetime.now())[:-7]+" !")
        for link in self.links:
            if((not link is None) and (self.likes<limit)):  # if the tweets reached don't overcome the limit
                self.bot.get('https://twitter.com'+link)    # get the tweet page 
                try:
                    self.bot.find_element_by_class_name('HeartAnimation').click()   # like
                    self.likes += 1
                    time.sleep(1)
                    if(self.generate_mid_random()): # True probability = 0.5
                        # retweet the tweet
                        self.bot.find_element_by_css_selector("button.ProfileTweet-actionButton.js-actionButton.js-actionRetweet").click()
                        time.sleep(2)
                        # confirm the retweet
                        self.bot.find_element_by_class_name('RetweetDialog-retweetActionLabel').click()
                        self.retweets += 1
                    # print the info 
                    result = " | likes: " + str(self.likes)+' | '+"retweets: " + str(self.retweets)
                    print(str(datetime.datetime.now())[:-7] + result,end='\r')
                    time.sleep(self.generate_random())
                except Exception as ex:
                    time.sleep(15)
        print('')
        print('Finished!')

email_password = getpass.getpass('Insert password for ' +email_email +':') # password input via getpass

# if password, username, and ( -m OR -h)
if((email_email!='')and(email_password!='')and(not stat_flag)and((my_flag and (not hashtag_flag))or(hashtag_flag and (not my_flag)))):
    edoBot = TwitterBot(email_email,email_password,0,0,hashtags,0) #create the bot
    authenticated = edoBot.login()  # login
    if(authenticated): 
        if(check_user.check_if_user_exists(edoBot.username,edoBot.password)):
            print('Welcome back, ' + edoBot.username + ' !')
        else:
            print('Logged in as '+edoBot.username+' !')
        if(hashtag_flag and(not my_flag)):
            edoBot.add_links()
        elif(my_flag and(not hashtag_flag)):
            edoBot.add_links_my_home()
        else:
            usage.print_usage(0)
        edoBot.crawl() #here start the bot
        timee = datetime.datetime.now()
        add_result.add_stat(edoBot.username,timee,edoBot.likes,edoBot.retweets,edoBot.followers)
# if password, username and -s 
elif((email_email!='')and(not password_flag)and(not hashtag_flag)and(stat_flag)and(not my_flag)):
    analyze_stat.check_stat(email_email,email_password)
else:
    usage.print_usage(0)