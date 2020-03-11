#Citation - www.stackoverflow.com

import os
os.chdir("C:/Users/Sujatha Sivakumar")
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# The four variables below require your own personal access data which can be retrieved from twitter.

access_token = " "            
access_token_secret = " "
consumer_key = " "
consumer_secret = " "


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l,language='en')
    stream.filter(locations=[-122.761230,37.986422,-120.080566,41.794864])     # These are just sample location coordinates
    
'To run this code without interruptions'
#Reference - https://dev.twitter.com/streaming/overview/request-parameters#track
#locations=[-122.761230,37.986422,-120.080566,41.794864] - California
#locations=[-103.381348,29.333101,-94.240723,33.237539] - Texas
