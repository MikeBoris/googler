# text2data

'''
TODO

turn into module
ie:
text2data/
	__init__.py
	get.py
		get1, get2, ...
	clean.py
	metrics.py

'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

# function to get html
url = 'http://www.indeed.com/jobs?q=data+scientist&l=MA'
html = requests.get(url)

# function to parse html, extract text
	# input html as str
	# tree = fromstring(html)
	#	   = tree.elements
	# NEED TO IDENTIFY RELEVANT ELEMENTS (CLASSES/IDS)
	# 
	# search engine:		indeed:
	# Title Link			job title
	# snippet				company name
	#						job descr
	#						company rating, etc
	#
	# (supposing we've identified our elements)
	# blobs = CssSelector(tree.elements)
	# concat blobs
	# output blobs as str
	# 

soup = BeautifulSoup(html.text, 'html.parser')

def extract_job(soup):
	jobs = []
	for div in soup.find_all(name='div', attrs={'class':'row'}):
		for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
			jobs.append(a['title'])
	return jobs

def extract_sum(soup):
	summaries = []
	spans = soup.findAll('span', attrs={'class':'summary'})
	for span in spans:
		summaries.append(span.text.strip())
	return summaries

def extract_company_from_result(soup): 
	companies = []
	for div in soup.find_all(name='div', attrs={'class':'row'}):
	company = div.find_all(name='span', attrs={'class':'company'})
	if len(company) > 0:
	  for b in company:
	    companies.append(b.text.strip())
	else:
	  sec_try = div.find_all(name='span', attrs={'class':'result-link-source'})
	    for span in sec_try:
	      companies.append(span.text.strip())
	return(companies)
 
extract_company_from_result(soup)

jobs = extract_job(soup)
summaries = extract_sum(soup)

for i, j in zip(jobs, summaries):
	print(i, j)


# function to normalize text

# function to structure text

# function to build metrics


