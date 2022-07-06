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

def read_dict(dictionary):
    """
        Read values of variables dictionary
    """
    for key, values in dictionary.items():
        if type(values) is dict:
            yield from read_dict(values)
        else:
            yield values

#%%
# Reading my api keys file
f = open('../../apis/api_keys.json', "r")
api_keys = json.load(f)

#%%
# Pulling data from census.gov
features = {
    "Total population": "B01001_001E",
    "Population in households": "B11001_001E",
    "Educational attainment": {
        "Total" : "B15003_001E",
        "No schooling" : "B15003_002E",
        "Master" : "B15003_023E",
        "Bachelor" : "B15003_022E"
    },
    "Income" : {
        "Total Below poverty level" : "B17001_002E",
        "Total Above poverty level" : "B17001_031E",
        "Total by household": "B19001_001E",
        "Median by household size": "B19019_001E"
    },
    "Earnings" :{
        "Total": "B20001_001E",
        "Median": "B20002_001E",
        "Median less than high school": "B20004_002E",
        "Median Bachelor": "B20004_005E",
        "Median Master or Above": "B20004_006E"
    },
    "Employment status": {
        "Total": "B23025_001E",
        "Total by Educational Attainment": "B23006_001E",
        "Total Bachelor or higher in labor force": "B23006_024E",
        "Total Bachelor or higher not labor force": "B23006_029E",
        "Total in labor force": "B23025_002E",
        "Total in labor force Employed": "B23025_004E",
        "Total in labor force Unemployed": "B23025_0045"
    },
    "Housing": {
        "Total units": "B25001_001E",
        "Total Occupied": "B25002_002E",
        "Total Vacant": "B25002_003E",
        "Total Owner occupied": "B25003_002E",
        "Total Renter occupied": "B25003_003E",
        "Total for rent": "B25004_002E",
        "Total for sale": "B25004_004E",
        "Total for seasonal": "B25004_006E",
        "Total monthly housing costs": "B25104_001E",
        "Median monthly housing costs": "B25105_001E",
        "Median gross rent": "B25064_001E"
    }
}

#%%
# Create a list of variables
gen_features = read_dict(features)

feature_string = ''
for feature in gen_features:
    feature_string = feature_string + ',' + feature

#%%


# 'https://api.census.gov/data/'+year+'/acs/acs1/profile?get=NAME,DP01_0001E&for=state:*&key="534045b915f30c77ac4e6e9775ca6aa4981ce33f"'

year = '2019'
url_address = 'https://api.census.gov/data/'+ year +'/acs/acs1/profile?get=NAME,'+ feature_string[1:] +'&for=state:*&key={0}'

#%%
url = url_address.format(api_keys['API'][0]['key'])

response = requests.request("GET", url)

#%%
# Census data in dataframe
census_df = json_to_dataframe(response)

#%%
print(census_df.head())
#%%
