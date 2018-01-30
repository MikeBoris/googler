'''


google search results for:

'cat sitter'

1. Rover.com | Background-Checked Cat Sitters | Rover.com
2. Best Cat Sitters in Boston, MA - Care.com
3. Cat Sitters - Care.com
4. Best Cat sitter in Cambridge, MA - Yelp
5. Best Cat sitter in Somerville, MA - Yelp
6. Reliable Pet Care Services - Dog walking, pet sitting, cat visits
7. The 10 Best Cat Sitters Near Me (with Free Estimates) - Thumbtack


Cat-Sitting Services: 3 tips for better cat sitting & why every other day ...
Fetch! Pet Care Dog Walking, Pet Sitting, Cat Visits, Boarding


run google search for topic
	
	run for topic + synonymns (few, many)
		eg
		'cat sitter'
		'cat sitting'
		'cat board'
		'cat boarding'
		'cat sitter near me'

		etc
	collect top 10, 25, 50 results (w/ and w/o local results)
	
	for each result:

		elements of 1 result record:
			title
			url
			description


			result1:
				T: 'Rover.com | Background-Checked Cat Sitters | Rover.com'
				U: 'https://www.rover.com/cat-sitting/'
				D: 'Looking for a cat sitter? Book a 5-star cat sitter to feed and play with your cat while you're away or at work.'

			processing
			tokenize
				T: 'Rover.com | Background-Checked Cat Sitters | Rover.com'
				T_tokenized = ['Rover.com', '|', 'Background-Checked Cat Sitters', 
				'|', 'Rover.com']
				counter - word distribution
				collections.Counter(T_tokenized)
				{'Rover.com': 2, '|': 2, 'Background-Checked Cat Sitters': 1}
				results_tokens -- which is a Counter object of all results_tokens
				-- figure out how to add tokens + counts to preexissting counter object 
			tf-idf
			a noun-phrase, or topic characterization of each element
				['Rover.com', 'Background-Checked Cat Sitters']
			# count the number of times each word appears in the text. 
			# Different texts can then be compared, based on the keywords they share
			result1_text = '
			Rover.com | Background-Checked Cat Sitters | Rover.com
https://www.rover.com/cat-sitting/
Looking for a cat sitter? Book a 5-star cat sitter to feed and play with your cat while you're away or at work.
''

original query (broad term)

get list of all synonymns (narrower terms)
	lemmatize
	lookup synonymns
		wordnet
	-> enhanced_query

submit enhanced_query to:
	twitter
	google
	Yelp

retrieve results
	min results for twitter
	min results for google
	min results for Yelp

input query
	e.g. cat-sitting

query_class
query processing
takes query

executes enhanced_query
	instance dependent
	eg
'''
from collections import Counter
import sys
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from textblob import TextBlob

#
# google search
# ----------------------
# query formatting
def query_format(query):
	split_q = query.split(' ')
	formatted_query = '+'.join(split_q) # formatted_query = cat+sitting
	search_string = 'https://www.google.com/search?q={}'
	formatted_search_string = search_string.format(formatted_query)
	return formatted_search_string

def execute_request(formatted_search_string):
	"""
	Given search string, execute search
	:param: formatted_search_string
	:return: html_dump string
	"""
	try:
		results_thing = requests.get(formatted_search_string)
		html_dump = results_thing.text
		return html_dump
	except ConnectionError:
		print('Connection timed out :(')
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise


# parsed_text <- html_parser(html_dump)
# try another parser? or api search?
def html_parser(html_dump, parser='html.parser'):
	soup = BeautifulSoup(html_dump, parser)
	parsed_text = soup.get_text()
	return parsed_text



#--- metrics -----------
# TODO: Need ideas for more metrics - ask John
# 
# extract topics
#**** extract topics
# extract noun_phrases
def get_top_n_np(np_list, n=10):
	# count up NPs and print most common
	top_n_np = Counter(np_list).most_common(n)
	intr = list(top_n_np.items())
	print('Noun phrases: {}'.format(str(intr)))

# extract polarity
def get_polarity(blob):
	try:
		print('Polarity: {}'.format(blob.sentiment.polarity))
	except:
		raise 'polarity issue'

# metrics
def text_process(parsed_text):
	try:
		parsed_text
	except NameError:
		print('no parsed_text')
	try:
		#print(parsed_text)
		blob = TextBlob(parsed_text)
		get_top_n_np(blob.noun_phrases)
	except:
		raise 'textblob issue'
	# metrics
	#get_polarity(blob)

# extract named entities
#**** extract named entities


# function: search -> process -> metrics
def search_to_metrics(query):
	# format query
	try:
		formatted_search_string = query_format(query)
	except:
		raise 'query issue'
	# search
	try:
		html_dump = execute_request(formatted_search_string)
	except: 'execution issue'
	# parse
	try:
		parsed_text = html_parser(html_dump)
	except:
		raise 'parsing issue'
	try:
		text_process(parsed_text)
	except:
		raise 'failed to process'
	



if __name__ == '__main__':
	search_to_metrics('cat sitting')


'''

returns results_object

TODO:
generates enhanced_query

parse/preprocess results
preprocessing_class
takes results_object
parses
tokenizes
returns word_freq_dist_Object

compute metrics
metrics_class
	instance dependent
generate list of topics
generate list of noun-phrases
generate list of named entities

	twitter:
		twitter_metrics (instance of metrics_class)
			top 10 keywords/topics <- results for twitter
			top 10 noun-phrases <- results for twitter
			top 10 named entities <- results for twitter
	google:
		google_metrics (instance of metrics_class)
			top 10 keywords/topics <- results for google
			top 10 noun-phrases <- results for google
			top 10 named entities <- results for google
	Yelp:
		Yelp_metrics (instance of metrics_class)
			top 10 keywords/topics <- results for Yelp
			top 10 noun-phrases <- results for Yelp
			top 10 named entities <- results for Yelp



John, Can you help me w/ metrics to gather? I'm a bit clueless on what 
we should be collecting -- 


'''