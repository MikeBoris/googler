# search all channels

from sys import argv

from googler import google_search_to_metrics
from twitter_search import gimme_tweets

def search_all_channels(query, numberOfResults):
	"""
	query
	numberOfResults: only for twitter


	Channels:
		--social media
		Twitter

		--search engines
		Google

		--etc

	TODO:
		Yahoo
		Bing

		Reddit

		Wikipedia


		Facebook
		Instagram
		Amazon
		
		Blogger
		YouTube
		Foursquare
		Flickr
		Imgur
		Indeed
		LinkedIn
		Pinterest
		Technorati
		Tumblr
		Vimeo

	"""
	gimme_tweets(query, numberOfResults)
	google_search_to_metrics(query)
	# 

if __name__ == '__main__':
	search_all_channels(argv[1], argv[2])