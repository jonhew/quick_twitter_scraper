import simplejson
import requests
#import pymongo
import time
import pickle
#from pymongo import Connection

# query
query = "Wow. https://twitter.com/"

# Mongo establish connection & define RDB
#connection = Connection()
#db = connection.nerds
#tweets = db.tweets

tweets = []

def scrape(url):
    for x in range(1,50):
        print x
        try:
            r = requests.get(url + str(x))
            json = simplejson.loads(r.content)
            for tweet in json['results']:
              #  if tweets.find({'from_user' : tweet['from_user'], 'text' : tweet['text'], 'id' : tweet['id']}).count() != 0:
              #      continue
              #  else:
                  tweets.append(tweet)
                  #t = tweets.insert(tweet)

        except:
            print "Lost " + str(x)

run = 0
while True:
  scrape('http://search.twitter.com/search.json?q=' + query + '&rpp=100&page=')
  output = open('tweets' + str(run), 'wb')
  pickle.dump(tweets, output)
  output.close()
  run += 1
  tweets[:] = []
  time.sleep(500)
