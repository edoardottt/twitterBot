# twitterBot v 1.3 🤖
A Twitter Bot made by me using Python and some its libriaries.

-------------------------------------------------
DOES IT REALLY WORKS? :bar_chart:
-------------------------------------------------
**Take a look**
With 3 days of usage:

![general analytics](https://github.com/edoardottt/twitterBot/blob/master/images/1.JPG)

![followers analytics](https://github.com/edoardottt/twitterBot/blob/master/images/2.JPG)

-------------------------------------------------
DESCRIPTION 🔦 
-------------------------------------------------

It uses selenium, time, random, datetime, getopt, sqlite3, os and sys libraries.

It tries to login with an email and a password on Twitter. If credentials are correct, It looks into the database if that user logged in yet and so if There is a record with that username id.
If there isn't that record, It creates it.
If the credentials aren't correct, throws an error.
You can decide if search for some hashtag/hashtags as input and It will looks for
some tweets searching those words in the search input field.
Instead you can crawl the tweets present in your Home.
The tweets links listed in the result pages are copied in a unique list X.
The elements of this X list are shuffled and then It starts to search those tweets.
Surely It presses the heart button on all of those, then It maybe retweets them.

Why maybe?

Because It only retweets the ~50% of all tweets reached (but puts likes on all).

Why ~50% and not exactly 50%?

Because for little numbers of hashtags or less trending hashtags or hashtags with low content (so the captured links < 30-40) It retweets about 40-65% of all tweets reached.
Instead for big numbers of hashtags or most trending hashtags or hashtags with high content (so the captured links > 80-90) It's more precise and almost exactly retweets 50% of them (with a low error like 2-3%).

When It finish, It stores all the likes and retweets count in a SQLite3 database called database.db

With the -s option, It displays with a graphic the trend of likes and retweets that It made.

-----------------------------------------------------
REQUIREMENTS 📣
-----------------------------------------------------

- Mozilla Firefox

- Python >= 3.6

- selenium (pip install selenium) OR geckodriver https://github.com/mozilla/geckodriver/releases

- matplotlib (python -m pip install -U matplotlib)

- It works only with desktop-type Twitter website window

-------------------------------------------------
USAGE 🚀
-------------------------------------------------

Assuming you are in the same folder of the script:

Usage: python twitterbot.py -u [value] -p [value] {-h [values separated by comma] OR -s OR -m}

-u or --username: 

        It's your twitter username(e-mail)

-p or --password:

        It's your twitter account password.

        **It's needed only if -h is present.**

-h or --hashtags:

        It's/They are the hashtag[s] you want to 'follow'

        If you want to insert multiple hashtags you have to separated them by comma:

        e.g. -h climatechange,techtips,python

-s or --stat:

        If you want to see your stats account.

        Insert only -u [value] -s

-m or --mine:

        If you want to 'follow' your feed's tweets.

        Insert only -u [value] -p [value] -m

Some examples:

To start the bot searching for some words:

 python twitterbot.py -u replace_your_email@mail.com -p replace_your_password -h trend,topics,twitter
 
To start the bot with your feed:

 python twitterbot.py -u replace_your_email@mail.com -p replace_your_password -m
 
To see your account bot statistics

 python twitterbot.py -u replace_your_email@mail.com -s


-------------------------------------------------
DOWNLOAD 📡
-------------------------------------------------

GIT command on prompt: git -clone https://github.com/edoardottt/twitterBot.git

Download by Browser on: https://github.com/edoardottt/twitterBot


----------------------------------------------
VERSIONING :books:
--------------------------------------------

**v 1.3:**

        - Added a better visualization of statistics for every user with matplotlib
        - With -s option now It shows a graphic that shows likes and retweets for each performance performed

**v 1.2.1:**

        - Now It prints the links crawled in your home/search input field  

**v 1.2:**

      - Added some files that create an SQLite3 database and stores users and bot sessions
      
            table Users
            It contains all the users authenticated by twitter
            
            table analytics
            It contains all the likes and retweets count of all bot sessions
            
      - Fixed some known bugs (invalid credentials, bad usage..)
      - More readable usage printer

**v 1.1:**

      - Catching some known Exceptions

--------------------------
If you liked it drop a :star:
--------------------------

https://www.edoardoottavianelli.it for contact me.


      Edoardo Ottavianelli
