


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



	