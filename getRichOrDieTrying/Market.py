import requests
import pandas as pd


ticker = "GOOGL"
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=full&apikey=GWSOQU64H517LNZ7")

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

# Let's be smart and retrieve the name of the column with our actual data
colname = list(raw_data.keys())[-1]

# We want to extract the corresponding column only
data = raw_data[colname]

# Create a dataframe
df = pd.DataFrame(data).T.apply(pd.to_numeric)

# Next we parse the index to create a datetimeindex
df.index = pd.DatetimeIndex(df.index)

# Let's fix the column names
df.rename(columns=lambda s: s[3:], inplace=True)

print(df.head())


class Market:
    def __init__(self, security_data):
        self.security_data = security_data


    def load(self, directory):
        print("Load data")

    def value(self, fin_products):
        securities_value = 0
        for product_name in fin_products.keys():
            securities_value += self.security_data[product_name] * fin_products[product_name]
        return securities_value

