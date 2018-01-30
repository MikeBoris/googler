


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
			result1_text = '''
			Rover.com | Background-Checked Cat Sitters | Rover.com
https://www.rover.com/cat-sitting/
Looking for a cat sitter? Book a 5-star cat sitter to feed and play with your cat while you're away or at work.
'''



	
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
	import requests
	import beautifulsoup4 as BeautifulSoup
	from textblob import TextBlob
	#
	# google search
	# ----------------------
	# query formatting
	query = 'cat sitting'
	split_q = query.split(' ')
	formatted_query = '+'.join(split_q) # formatted_query = cat+sitting
	search_string = 'https://www.google.com/search?q={}'
	formatted_search_string = search_string.format(formatted_query)
	# execute search
	def execute_request(formatted_search_string):
		results_thing = requests.get(formatted_search_string)
		html_dump = results_thing.text
		return html_dump

	html_dump = execute_request(formatted_search_string)
	
	# parsed_text <- html_parser(html_dump)
	def html_parser(html_dump, parser='html.parser'):
		soup = BeautifulSoup(html_dump, parser)
		parsed_text = soup.get_text()
		return parsed_text

	parsed_text = html_parser(html_dump)
	# tokenizes
	
	blob = TextBlob(parsed_text)
	# returns word_freq_dist_Object
#**** word_freq_dist = blob.word_counts
	#--- metrics -----------
	# TODO: Need ideas for more metrics - ask John
	# 
	# extract topics
#**** extract topics
	# extract noun_phrases
	print('Noun phrases: {}'.format(', '.join(blob.noun_phrases)))
	# extract polarity
	print('Polarity: {}'.format(blob.sentiment.polarity))
	# extract named entities
#**** extract named entities
	
	

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
