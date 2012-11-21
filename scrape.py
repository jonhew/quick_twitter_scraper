import simplejson
import requests
import pymongo
import time
from pymongo import Connection

# query
query = "NerdRapperNames"

# Mongo establish connection & define RDB
connection = Connection()
db = connection.nerds
tweets = db.tweets

def scrape(url):
    for x in range(1,50):
        print x
        try:
            r = requests.get(url + str(x))
            json = simplejson.loads(r.content)
            for tweet in json['results']:
                if tweets.find({'from_user' : tweet['from_user'], 'text' : tweet['text'], 'id' : tweet['id']}).count() != 0:
                    continue
                else:
                  print tweet['text']
                  t = tweets.insert(tweet)

        except:
            print "Lost " + str(x)

while True:
  scrape('http://search.twitter.com/search.json?q=' + query + '&rpp=100&page=')
  time.sleep(500)