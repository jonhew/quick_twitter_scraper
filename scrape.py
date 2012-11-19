import simplejson
import requests
import pymongo
from pymongo import Connection

# Mongo establish connection & define RDB
connection = Connection()
db = connection.etsy_tweets
down_tweets = db.etsy_down
up_tweets = db.etsy_up

def scrape(url, down):
    losers = []
    for x in range(1,50):
        print x
        try:
            r = requests.get(url + str(x))
            json = simplejson.loads(r.content)
            for tweet in json['results']:
                if down == 1:
                    tp = down_tweets.insert(tweet)
                else:
                    tp = up_tweets.insert(tweet)
        except:
            print "Lost " + str(x)
            losers.append(x)

        for x in losers:
            try:
                r = requests.get(url + str(x))
                json = simplejson.loads(r.content)
                for tweet in json['results']:
                    tp = tweets.insert(tweet)
            except:
                print "Lost " + str(x)

scrape('http://search.twitter.com/search.json?q=etsy+down&rpp=100&page=', 1)
scrape('http://search.twitter.com/search.json?q=etsy+back+up&rpp=100&page=', 0)
