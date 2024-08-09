# Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :-
# 1.) List the names of all breweries present in the states of Alaska, Maine and New York.
# 2.) What is the count of breweries in each of the states mentioned above?
# 3.) Count the number of types of breweries present in individual cities of the state mentioned above
# 4.) Count and list how many breweries have websites in the states of Alaska, Maine and New York.



import json
import requests

class Brewery_Data:
    def __init__(self,url):    #method to get url
        self.url= url
        self.data=None

    def fetch_data(self):
        response=requests.get(self.url)     #this line gets the url and get response from them
        if response.status_code==200:
            self.data=response.json()
        else:
            print(f"Failed to fetch data from URL: {self.url}")

    def get_breweries_by_state (self,states):
        if not self.data:
            print(f"NO data available")
            return[]

        return[brewery for brewery in self.data if brewery.get('state')in states]

    def list_breweries_in_states(self,states):
        breweries=self.get_breweries_by_state(states)
        return[brewery['name']for brewery in breweries]

    def count_breweries_by_state(self,states):
        breweries = self.get_breweries_by_state(states)
        count={state:0 for state in states}
        for brewery in breweries:
            state=brewery.get('state')
            if state in count:
                count[state]+=1
        return count

    def count_breweries_by_city_and_type(self,states):
        breweries = self.get_breweries_by_state(states)
        city_type_count={}
        for brewery in breweries:
            city = brewery.get('city')
            type_ = brewery.get('brewery_type')
            if city not in city_type_count:
                city_type_count[city] = {}
            if type_ not in city_type_count[city]:
                city_type_count[city][type_] = 0
            city_type_count[city][type_] += 1
        return city_type_count


    def count_breweries_with_websites(self,staes):
        breweries = self.get_breweries_by_state(states)
        count_with_websites=0
        for brewery in breweries:
            if brewery.get('website_url'):
                count_with_websites +=1

        return count_with_websites


if __name__=='__main__':
    url = "https://api.openbrewerydb.org/breweries"
    brewery_data = Brewery_Data(url)

    # Fetch the data from the URL
    brewery_data.fetch_data()

    # Define the states to filter
    states = ['Alaska', 'Maine', 'New York']

    # List the names of all breweries present in the states of Alaska, Maine, and New York
    print("Breweries in Alaska, Maine, and New York:")
    print(brewery_data.list_breweries_in_states(states))

    # Count the number of breweries in each of the states mentioned above
    print("\nCount of breweries in each state:")
    print(brewery_data.count_breweries_by_state(states))

    # Count the number of types of breweries present in individual cities of the states mentioned above
    print("\nCount of brewery types in individual cities:")
    city_type_count = brewery_data.count_breweries_by_city_and_type(states)
    for city, types in city_type_count.items():
        print(f"{city}: {types}")

    # Count and list how many breweries have websites in the states of Alaska, Maine, and New York
    print("\nCount of breweries with websites:")
    print(brewery_data.count_breweries_with_websites(states))