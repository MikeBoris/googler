# search all channels

from sys import argv

from googler import google_search_to_metrics
from twitter_search import gimme_tweets

#--- channels --------------------
def search_all_channels(arg1, arg2):
	# twitter
	gimme_tweets(arg1, arg2)
	# google
	google_search_to_metrics(arg1)
	# 


if __name__ == '__main__':
	search_all_channels(argv[1], argv[2])