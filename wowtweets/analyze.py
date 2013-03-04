import os, os.path
import sys
import pickle

alltweets = set()
for root, _, files in os.walk(os.getcwd()):
  for f in files:
    if f == "analyze.py":
      continue
    with open(os.path.join(root, f), 'r') as lines:
      p = pickle.load(lines)
      for tweet in p:
        if tweet['text'].find('Wow. ') == -1:
          continue
        alltweets.add(tweet['text'])

print alltweets
