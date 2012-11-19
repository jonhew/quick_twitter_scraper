import simplejson
import requests
import pymongo
from pymongo import Connection

# Mongo establish connection & define RDB
connection = Connection()
db = connection.nerd_rapper_names
tweets = db.tweets

def scrape(url):
    losers = []
    for x in range(1,50):
        print x
        try:
            r = requests.get(url + str(x))
            json = simplejson.loads(r.content)
            for tweet in json['results']:
                t = tweets.insert(tweet)

        except:
            print "Lost " + str(x)
            losers.append(x)

        for x in losers:
            try:
                r = requests.get(url + str(x))
                json = simplejson.loads(r.content)
                for tweet in json['results']:
                    t = tweets.insert(tweet)
            except:
                print "Lost " + str(x)

scrape('http://search.twitter.com/search.json?q=nerdrappernames&rpp=100&page=')
