#%%

import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime as dt

#%% User-function
def read_dict(dictionary):
    """
    Read all the values from a nested dictionary
    Args:
        dictionary (dict: Dictionary with all variables defined as census.gov

    Yields:
        _type_: yield object with all variables
    """
    for _, values in dictionary.items():
        if type(values) is dict:
            # in case is a children dict
            yield from read_dict(values)
        else:
            yield values

def grab_data(y, api_key):
    """Pull data from census.gov

    Args:
        y (list): years list
        api_key (public api): api key required to scrap info from census

    Yields:
        iterator: iterator object which contains the info from each y
    """
    for year in y:
        url = 'https://api.census.gov/data/{}/acs/acs1?get=NAME{}&for=state:*&key={}'.format(year, feature_string, api_key['API'][0]['key'])
        json_text = requests.request("GET", url).json()
        for row in range(1, len(json_text)):
            json_text[row].insert(0, year)
        yield json_text[1:]

#%%
# Reading api key
f = open('../../apis/api_keys.json', "r")
api_keys = json.load(f)

#%%
# Dictionary of the variables selected for the project
features = {
    "Total population": "B01001_001E",
    "Population in households": "B11001_001E",
    "Educational attainment for the population 25 years and over": {
        "Total" : "B15003_001E",
        "No schooling completed" : "B15003_002E",
        "Bachelor's degree": "B15003_022E"
        "Master's degree" : "B15003_023E",
        "Doctorate degree" : "B15003_023E"
    },
    "Income" : {
        "Total Below poverty level" : "B17001_002E",
        "Total Above poverty level" : "B17001_031E",
        "Total household": "B19001_001E",
        "Median household": "B19019_001E"
    },
    "Earnings" :{
        "Total": "B20001_001E",
        "Median": "B20002_001E",
        "Median Bachelor": "B20004_005E",
        "Median Master or Above": "B20004_006E"
    },
    "Employment status": {
        "Total": "B23025_001E",
        "Total by Educational Attainment 25 years or above": "B23006_001E",
        "Total Bachelor or higher in labor force": "B23006_024E",
        "Total Bachelor or higher not labor force": "B23006_029E"
    },
    "Housing": {
        "Total housing units": "B25001_001E",
        "Total Renter occupied": "B25003_003E",
        "Total by educational attainment of householder": "B25013_001E",
        "Total renter-occupied housing units by educational attainment" : "B25013_007E",
        "Renter occupied with bachelor's degree or higher" : "B25013_011E",
        "Median gross rent": "B25064_001E"
    }
}

#%%
# Read variables from features dict
gen_features = read_dict(features)

# Create variables for scraping the webpage and identify the final
# dataframe

feature_names = ['Year', 'Name']

feature_string = ''
for feature in gen_features:
    feature_string = feature_string + ',' + feature
    feature_names.append(feature)

feature_names.append('state')

#%%

# Years selected
# Year 2020 is not available on the API service
first_year = 2010
last_year = 2019
years = np.arrange(first_year, last_year + 1)

# Grab info from census.gov for each year
gen_data = grab_data(years, api_keys)

# Put all data together, but it's possible to grab a specific year
all_data = []
for x in gen_data:
    all_data.extend(x)

census_df = pd.DataFrame(all_data, columns=feature_names)

#%% Changing type fof variables from object to num, except the state name
census_df = census_df.apply(lambda x: pd.to_numeric(x) if x.name != "Name" else x)
census_df['year'] = census_df["Year"].apply(lambda x: pd.to_datetime(x, format='%Y'))

census_df = census_df.drop('Year', axis=1)

# Reorder dataframe
reordered_name = ['year']
reordered_name.extend(census_df.columns[:-2])
census_df = census_df[reordered_name]
#%%
print(census_df.describe())
#%%
