# Using the URL https://restcountries.com/v3.1/all write a Python program which will do the following :-
# 1.) Using the OOPS concept for the following task.
# 2.) Use the Class Constructor for taking input the above mentioned URL for the task.
# 3.) Create a Method that will Fetch all the JSON data from the URL mentioned above.
# 4.) Create a Method that will display the name of countries, currencies & currency symbols.
# 5.) Create a Method that will display all those countries which have DOLLAR as its currency.
# 6.) Create a Method that will display all those countries which have EURO as its currency.


import json
import requests

class CountryData:
    def __init__(self,url):    #method to get url
        self.url= url
        self.data=None

    def fetch_data(self):
        response=requests.get(self.url)     #this line gets the url and get response from them
        if response.status_code==200:
            self.data=response.json()
        else:
            print(f"Failed to fetch data from URL: {self.url}")


    def display_country_info(self):
        if not self.data:
            print(f"NO data available")
            return

        for country in self.data:
            name=country.get('name',{}).get('common','N/A')
            currencies=country.get('currencies',{})
            currency_info = ', '.join([f"{cur} ({details.get('name', 'N/A')} - {details.get('symbol', 'N/A')})"
                                       for cur, details in currencies.items()])

            print(f"Country: {name}, Currencies: {currency_info}")


    def display_countries_with_currency(self,currency_name):
        if not self.data:
            print(f"NO data available")
            return
        countries = [country.get('name', {}).get('common', 'N/A')
                     for country in self.data
                     if any(details.get('name',"").lower()==currency_name.lower()
                            for details in country.get('currencies', {}).values())]
        print(f"Countries using {currency_name}: {', '.join(countries)}")



if __name__ == "__main__":
    # Initialize the CountryData object with the URL

    country_data=CountryData("https://restcountries.com/v3.1/all")

    # Fetch the data from the URL

    country_data.fetch_data()

    # Display the name of countries, currencies & currency symbols
    print("Countries, Currencies, and Currency Symbols:")
    country_data.display_country_info()

    # Display all those countries which have DOLLAR as its currency
    print("\nCountries using DOLLAR as currency:")
    country_data.display_countries_with_currency("Dollar")

    # Display all those countries which have EURO as its currency
    print("\nCountries using EURO as currency:")
    country_data.display_countries_with_currency("Euro")








