"""
Yelp Fusion API code sample.
Forked from: https://github.com/Yelp/yelp-fusion/tree/master/fusion/python

Uses Yelp Fusion Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.

Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
import argparse
import json
import pprint
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

from apiKey import YELP_API_KEY

API_KEY = YELP_API_KEY

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Boston, MA'
SEARCH_LIMIT = 3

def request(host, path, api_key, url_params=None):
    """
    Given API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns: JSON (dict) response
    Raises: HTTPError
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {'Authorization': 'Bearer {}'.format(api_key) }
    print(u'Querying {0} ...'.format(url))
    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


def search(api_key, term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(term, location):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location)
    businesses = response.get('businesses')
    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return
    business_id = businesses[0]['id']
    print(u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id))
    response = get_business(API_KEY, business_id)
    print(u'Result for business "{0}" found:'.format(business_id))
    pprint.pprint(response, indent=2)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()



'''
	Response:

	{ 'categories': [{'alias': 'pet_sitting', 'title': 'Pet Sitting'}],
  'coordinates': {'latitude': 42.339904, 'longitude': -71.0898892},
  'display_phone': '(617) 784-7740',
  'hours': [ { 'hours_type': 'REGULAR',
               'is_open_now': False,
               'open': [ { 'day': 0,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'},
                         { 'day': 1,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'},
                         { 'day': 2,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'},
                         { 'day': 3,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'},
                         { 'day': 4,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'},
                         { 'day': 5,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'},
                         { 'day': 6,
                           'end': '1900',
                           'is_overnight': False,
                           'start': '0730'}]}],
  'id': 'just-4-cats-boston',
  'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/RYJy-Zw5dDMhcwLvcCu1-Q/o.jpg',
  'is_claimed': True,
  'is_closed': False,
  'location': { 'address1': '',
                'address2': '',
                'address3': '',
                'city': 'Boston',
                'country': 'US',
                'cross_streets': '',
                'display_address': ['Boston, MA 02115'],
                'state': 'MA',
                'zip_code': '02115'},
  'name': 'Just 4 Cats',
  'phone': '+16177847740',
  'photos': [ 'https://s3-media2.fl.yelpcdn.com/bphoto/RYJy-Zw5dDMhcwLvcCu1-Q/o.jpg',
              'https://s3-media2.fl.yelpcdn.com/bphoto/tb3xLVLoOejw6IMpviW6og/o.jpg',
              'https://s3-media3.fl.yelpcdn.com/bphoto/k7e1cUDPnfCRSRKtMR08SQ/o.jpg'],
  'rating': 5.0,
  'review_count': 25,
  'transactions': [],
  'url': 'https://www.yelp.com/biz/just-4-cats-boston?adjust_creative=Bl3Dlcn4ZvcALtd7OjbgDw&utm_campaign=yelp_api_
v3&utm_medium=api_v3_business_lookup&utm_source=Bl3Dlcn4ZvcALtd7OjbgDw'}




'''