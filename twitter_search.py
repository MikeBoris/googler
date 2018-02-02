'''
	search.py

	Given user search query, retrieves relevant twitter data
	(Ideally) returns descriptive stats for data retrieved
	e.g.

	>>> python search.py 'Richard Branson'
	
	Searching twitter for mentions of Richard Branson
	
	Results:		Tweets returned: 4312
					Positive: 1234
					Negative: 2120
					Neutral: 903

'''
from collections import Counter
import re, string
from sys import argv

from twython import Twython
from textblob import TextBlob

# assumes twitter api key/secret in current directory
from apiKey import API_KEY, API_SECRET

#--- Regex parser -----------------------------------------------------------
# source: https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

#--- Authenticate & Search ------------------------------------------------------

def authenticate(key, secret):
	''' given twitter api key and secret
	returns access token for api '''
	twitter = Twython(key, secret, oauth_version=2)
	return twitter.obtain_access_token()

def search(query, key, token, num_results):
	''' given search query, api key, and access token
	returns twitter search results as json object '''
	twitter = Twython(key, access_token=token)
	json = twitter.search(q=query, count=num_results)
	return json

def execute_search(key, secret, query, num_results=5):
	''' given authenticated query
	api key, secret, query string, and optional return_count
	returns search results as json object '''
	access_token = authenticate(key, secret)
	results = search(query, key, access_token, num_results)
	return results
 
#--- Preprocessing tweets ------------------------------------------------------------

def tokenize(s):
	'''
	Get all words from text
	'''
	return tokens_re.findall(s)

def tokenize2(text):
	'''
	Get all words from text again
	'''
	return re.findall('[a-z]+', text.lower())
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def remove_invalid_chr(list_of_tokens):
	"""
	given tokenized tweet as list of strings
	return list w/ invalid strings removed
	"""
	invalid_chars = set(string.punctuation)
	for token in list_of_tokens:
		# if there's a special char in token
		if any(char in invalid_chars for char in token):
			# remove token from list
			list_of_tokens.remove(token)
	return list_of_tokens

def most_common(lst):
	"""
	Get most frequent token in document
	"""
	data = Counter(lst)
	return data.most_common(1)[0][0]

def print_tweets(results):
	"""
	given search results object
	prints tweet text each line
	"""
	for tweet in results['statuses']:
		print('\n')
		print('==================================')
		print('Screen_name: ' + tweet['user']['screen_name'])
		#print('Created_at: ' + tweet['created_at'])
		print(tweet['text'] + '\n')
		print(preprocess(tweet['text']))
		print(' '.join(remove_invalid_chr(preprocess(tweet['text']))))
		print('Most common word: ' + most_common(remove_invalid_chr(preprocess(tweet['text']))))
		#print('Favorite_count: {}'.format(tweet['favorited']))
		#print('Retweet_count: {}'.format(tweet['retweeted']))
		#print('Lang: ' + tweet['lang'])
		#print('Entities: {}'.format(tweet['entities']))

		#blob = TextBlob(tweet['text'])
		#print('Sentiment: {0}'.format(blob.sentiment.polarity))

def bulk_tweet_collection(results):
	"""
	Converts query results object (tweets) into 
		list of lists
	:param results: parsed json results returned
		by query to twitter api
	:return: list of tweets (each a list)
	"""
	list_of_lists = []
	for tweet in results['statuses']:
		list_of_lists.append(list((tweet['id'], tweet['user']['screen_name'], 
			tweet['created_at'], clean_words(tweet['text']), tweet['favorited'],
			tweet['retweeted'])))
	return list_of_lists

def bulk_tweet_text(results):
	"""
	Converts query results object (tweets) into clean tokens
	:param results: parsed json results returned
		by query to twitter api
	:return: list of clean tokens
	"""
	for tweet in results['statuses']:
		print(clean_words(tweet['text']))


# dirty text to list of lemmas
def clean_words(tweet_str):
	"""
	Takes tweet text, gives list of clean tokens
	:param: tweet_str (str)
	:return: clean (list)
	"""
	#tokenize tweet_str
	# tokenize(tweet_str)
	tokens = re.split('[^a-zA-Z]', tweet_str)
	new_tokens = [token for token in tokens if len(token) > 1]
	new_tokens = [token.lower() for token in new_tokens]
	return ' '.join(new_tokens)


# sentiment stats
def gimme_tweets(key, secret, query, num_results):
	data = execute_search(key, secret, query, num_results)
	print_tweets(data)
	tweets = bulk_tweet_collection(data)
	for t in tweets:
		print(t)
	bulk_tweet_text(data)
	

if __name__ == '__main__':
	print('Searching for tweets about: {0}'.format(argv[1]))

	gimme_tweets(API_KEY, API_SECRET, argv[1], num_results=argv[2])