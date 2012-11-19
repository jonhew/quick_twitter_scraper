import simplejson
import requests
import pymongo
import time
from pymongo import Connection

# Mongo establish connection & define RDB
connection = Connection()
db = connection.nerd_rapper_names
tweets = db.tweets

def scrape(url):
    for x in range(1,50):
        print x
        try:
            r = requests.get(url + str(x))
            json = simplejson.loads(r.content)
            for tweet in json['results']:
                if tweets.find({'from_user' : tweet['from_user'], 'text' : tweet['text'], 'id' : tweet['id']}):
                    continue
                else:
                  print "inserting"
                  t = tweets.insert(tweet)

        except:
            print "Lost " + str(x)

while True:
  scrape('http://search.twitter.com/search.json?q=nerdrappernames&rpp=100&page=')
  time.sleep(500)