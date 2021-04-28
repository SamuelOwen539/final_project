
class MapQuest():
    def __init__(self):
        self.store_data = {}
        self.yelp_data = []
    def call(self, loc):
        '''
        Receives a call requests accesses API
        Saves relevant data as self.store data
        Storing local restaurants near loc

        Parameters
        ----
        loc (location): string

        Returns
        -----
        None
        '''
        print(type(self.yelp_data))
        restaurant_data = self.yelp_data[loc]
        city = restaurant_data[0]
        name = restaurant_data[1]
        return city+name













if __name__ == "__main__":
    pass
