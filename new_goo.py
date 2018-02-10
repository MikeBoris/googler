import pandas as pd
import numpy as np
import re
import nltk

from lxml.html import fromstring
import requests

html = requests.get('https://www.google.com/search?q=cat+sitting')
tree = fromstring(html.text)

link_text = tree.cssselect('h3.r')
n = len(link_text)
corpus = [link_text[j].text_content() for j in range(n)]

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

labels = ['cat sitting']*n
corpus = np.array(corpus)
corpus_df = pd.DataFrame({'Document': corpus, 'Category': labels})
corpus_df = corpus_df[['Document', 'Category']]

def normalize_doc(doc):
	# lowercase and remove special chars
	doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I)
	doc = doc.lower()
	doc = doc.strip()
	# tokenize doc
	tokens = wpt.tokenize(doc)
	# remove stopwords
	filtered_tokens = [token for token in tokens if token not in stop_words]
	# re-assemble doc from filtered tokens
	doc = ' '.join(filtered_tokens)
	return doc

normalize_corpus = np.vectorize(normalize_doc)

norm_corpus = normalize_corpus(corpus)

print(norm_corpus)