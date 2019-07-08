# twitterBot v 1.1 🤖
A Twitter Bot made by me using Python and some its libriaries.

------------------------------------------------------------
REQUIREMENTS 📣
-----------------------------------------------------

- Mozilla Firefox

- Python 

- geckodriver https://github.com/mozilla/geckodriver/releases

- It works only with desktop-type Twitter website window

-------------------------------------------------
DESCRIPTION 🔦
-------------------------------------------------

It uses selenium, time, random, datetime, getopt and sys libraries.

It tries to login with an email and a password on Twitter, then brings the hashtag/hashtags as input and  it looks for
some tweets searching those words in the search input field.
The tweets links listed in the result pages of those words are copied in a unique list X.
The elements of this X list are shuffled and then It starts to search those tweets.
Surely It presses the heart button on all of those, then It maybe retweets them.

Why maybe?

Because It only retweets the ~50% of all tweets reached (but puts likes on all).

Why ~50% and not exactly 50%?

Because for little numbers of hashtags or less trending hashtags or hashtags with low content (so the captured links < 30-40) It retweets about 40-65% of all tweets reached.
Instead for big numbers of hashtags or most trending hashtags or hashtags with high content (so the captured links > 80-90) It's more precise and almost exactly retweets 50% of them (with a low error like 2-3%).

-------------------------------------------------
USAGE 🚀
-------------------------------------------------

Assuming you are in the same folder of the script:

Type on command line:

python twitterbot.py -u your_email -p your_password -h hashtags

You have to insert instead of those values your personal credentials.

For using multiple hashtags, separate them by a comma (no space):

e.g. -h climatechange,p,developer

-------------------------------------------------
DOWNLOAD 📡
-------------------------------------------------

GIT command on prompt: git -clone https://github.com/edoardottt/twitterBot.git

Download by Browser on: https://github.com/edoardottt/twitterBot


----------------------------------------------
VERSIONING
--------------------------------------------

v 1.1:
      Catching some known Exceptions

--------------------------
If you liked it drop a :star:
--------------------------

https://www.edoardoottavianelli.it for contact me.


      Edoardo Ottavianelli
