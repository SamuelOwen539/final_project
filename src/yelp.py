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
        self.store_data[location] = 'value'








if __name__ == "__main__":
    yelp = Yelp()
    yelp.call('Detroit')
    print(yelp.store_data)