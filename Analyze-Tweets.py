import requests
import json
import urllib.parse
from textblob import TextBlob

searchTerm = "Cats and Dogs!"
searchTerm = urllib.parse.quote(searchTerm)

getInfo = requests.get('https://api.twitter.com/1.1/search/tweets.json?q='+ searchTerm +'&result_type=recent&count=50', headers={"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAA"})
parsedInfo = json.loads(getInfo.text)['statuses']

pubTweets = []
for x in range(len(parsedInfo)):
	pubTweets.append(parsedInfo[x]['text'])

def clean_tweets(tweet):
	tweet_words = str(tweet).split(' ')
	clean_words = [word for word in tweet_words if not word.startswith('#')]
	return ' '.join(clean_words)

def analyze(Topic):
	positive_tweets, negative_tweets = [], []

	for tweet in range(len(pubTweets)):
		cleanedTweet = clean_tweets(pubTweets[tweet])
		tweet_polarity = TextBlob(cleanedTweet).sentiment.polarity
		if tweet_polarity<0:
			negative_tweets.append(cleanedTweet)
			continue
		positive_tweets.append(cleanedTweet)
	return positive_tweets, negative_tweets
positive, negative = analyze('Magufuli')
print(positive , '\n\n', negative)
print('Positive:',len(positive), ' VS  ', 'Negative:',len(negative))
