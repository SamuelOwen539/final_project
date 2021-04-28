import requests
import json
import sys
from secrets import key



class Yelp():
    def __init__(self):
        self.store_data = {}
        pass

    def call(self, location):
        '''
        Receives a call requests accesses API
        Saves relevant data as self.store data

        Parameters
        ----
        None

        Returns
        -----
        None
        '''
        # Check the db to see if location has already been searched for, and if so, use the
        # the data from the db

        #else:

        URL = 'https://api.yelp.com/v3/businesses/search'
        HEADERS = {'Authorization': 'bearer %s' % key}
        PARAM = {'term': 'sushi',
         'limit': 50,
         'radius': 5000,
         'offset': 0,
         'location': location}

        response = requests.get(url = URL, params = PARAM, headers = HEADERS)
        data = []
        for place in response.json()['businesses']:
            data.append([
                place['location'].get('city'),
                place.get('name'),
                place.get('rating'),
                place.get('price')
            ])
        return data
# Put repsonse into json and parse for necessary data

# Insert data into db

# Return data from






if __name__ == "__main__":
    yelp = Yelp()
    yelp.call('Detroit')
    print(yelp.store_data)