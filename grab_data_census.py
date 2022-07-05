#%%
### INCOMPLETE - WIP

import pandas as pd
import json
import requests

#%% User-function
def json_to_dataframe(r):
    """This function is to convert the data taken from census.org
    to pandas DataFrame
    Args:
        r (_type_): json file containing census data

    Returns:
        _type_: census data in dataframe format
    """
    return pd.DataFrame(r.json()[1:], columns=r.json()[0])

#%%
# Reading my api keys file
f = open('../../apis/api_keys.json', "r")
api_keys = json.load(f)

#%%
# Pulling data from census.gov
type = 'acs1'
year = '2019'
table = 'S0201'
url_address = 'https://api.census.gov/data/'+ year +'/acs/'+ type +'/spp?get=NAME,group('+ table +')&for=state:*&key={0}'

url = url_address.format(api_keys['API'][0]['key'])

response = requests.request("GET", url)

#%%
# Census data in dataframe
census_df = json_to_dataframe(response)

#%%
print(census_df.head())
#%%
