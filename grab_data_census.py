#%%

import pandas as pd
import json
import requests
import numpy as np

#%% User-function
def grab_data(y, features_str, api_key):
    """Pull data from census.gov

    Args:
        y (list): years list
        api_key (public api): api key required to scrap info from census

    Yields:
        iterator: iterator object which contains the info from each y
    """

    for year in y:
        url = 'https://api.census.gov/data/{}/acs/acs1?get=NAME,{}&for=state:*&key={}'.format(year, features_str, api_key['API'][0]['key'])
        json_text = requests.request("GET", url).json()
        for row in range(1, len(json_text)):
            json_text[row].insert(0, year)
        yield json_text[1:]

def create_dataframe_data(var_dict, api_census, first_year, last_year=None):
    """
    Extraction the data from Census.gov per year, then consolidate them and create a pandas dataframe

    Args:
        var_dict: {dict} Dictionary of features
        api_censis: {str} API key for gather info from census.gov
        first_year: {int} First year for query
        last_year: {int} Last year for query, by default is equal to first year

    Output:
        df: {pandas dataframe} Dataframe that contains info from Census.gov
    """

    if last_year == None:
        years = first_year
    else:
        years = np.arange(first_year, last_year + 1)

    column_names = ['Year', 'Name']
    column_names = column_names + list(var_dict.keys()) + ['state']

    # Grab info from census.gov for each year
    feature_string = ",".join(var_dict.values())
    gen_data = grab_data(years, feature_string, api_census)

    # Put all data together, but it's possible to grab a specific year
    all_data = []
    for x in gen_data:
        all_data.extend(x)

    df = pd.DataFrame(all_data, columns=column_names)
    df = df.apply(lambda x: pd.to_numeric(x) if x.name != "Name" else x)

    return df


#%%
# Reading api key
f = open('../../apis/api_keys.json', "r")
api_keys = json.load(f)

#%%
# Dictionary of the variables selected for the project
population_features = {
    "Population": "B01001_001E",
    "Population in households": "B11001_001E",
    "Pop. below poverty level" : "B17001_002E",
    "Pop. at or Above poverty level" : "B17001_031E",
    "Pop. in Labor Force" : "B23025_002E",
    "Pop. not in Labor Force" : "B23025_007E",
    "Bachelor or higher Pop. in labor force": "B23006_024E",
    "Bachelor or higher Pop. not labor force": "B23006_029E",
    "Total Population 25 years and over - Educ. attainment" : "B15003_001E",
    "Population 25 years and over - No schooling completed" : "B15003_002E",
    "Population 25 years and over - Bachelor's degree": "B15003_022E",
    "Population 25 years and over - Master's degree" : "B15003_023E",
    "Population 25 years and over - Doctorate degree" : "B15003_023E",
    "Median household Earnings($)": "B19013_001E",
    "Median Earnings - Educational attainment": "B20004_001E",
    "Median Earnings - Bachelor": "B20004_005E",
    "Median Earnings - Master or Above": "B20004_006E",
    "Total housing units": "B25001_001E",
    "Total Occupied housing units": "B25002_002E",
    "Total Renter occupied - Tenure": "B25003_003E",
    "Total Renter occupied - by income": "B25118_014E",
    "Total housing units - Educational attainment": "B25013_001E",
    "Total Renter-occupied units- Educational attainment" : "B25013_007E",
    "Renter-occupied units - Less than high school graduate": "B25013_008E",
    "Renter-occupied units - High school graduate": "B25013_009E",
    "Renter-occupied units - Some college degree": "B25013_010E",
    "Renter-occupied units - Bachelor's degree or higher": "B25013_011E",
    "Median gross rent": "B25064_001E"
    }

gross_rent_features = {
    "Less than $100": "B25063_003E",
    "$100 to $149": "B25063_004E",
    "$150 to $199": "B25063_005E",
    "$200 to $249": "B25063_006E",
    "$250 to $299": "B25063_007E",
    "$300 to $349": "B25063_008E",
    "$350 to $399": "B25063_009E",
    "$400 to $449": "B25063_010E",
    "$450 to $499": "B25063_011E",
    "$500 to $549": "B25063_012E",
    "$550 to $599": "B25063_013E",
    "$600 to $649": "B25063_014E",
    "$650 to $699": "B25063_015E",
    "$700 to $749": "B25063_016E",
    "$750 to $799": "B25063_017E",
    "$800 to $899": "B25063_018E",
    "$900 to $999": "B25063_019E",
    "$1000 to $1249": "B25063_020E",
    "$1250 to $1499": "B25063_021E",
    "$1500 to $1999": "B25063_022E",
    "$2000 to $2499": "B25063_023E",
    "$2500 to $2999": "B25063_024E",
    "$3000 to $3499": "B25063_025E",
    "$3500 or more": "B25063_026E",
    "Median gross rent": "B25064_001E"
    }

rent_occupied_by_income_features = {
    "Total Renter occupied - by income": "B25118_014E",
    "Renter occupied - income less than $5000": "B25118_015E",
    "Renter occupied - income $5000 to $9999": "B25118_016E",
    "Renter occupied - income $10000 to $14999": "B25118_017E",
    "Renter occupied - income $15000 to $19999": "B25118_018E",
    "Renter occupied - income $20000 to $24999": "B25118_019E",
    "Renter occupied - income $25000 to $34999": "B25118_020E",
    "Renter occupied - income $35000 to $49999": "B25118_021E",
    "Renter occupied - income $50000 to $74999": "B25118_022E",
    "Renter occupied - income $75000 to $99999": "B25118_023E",
    "Renter occupied - income $100000 to $149999": "B25118_024E",
    "Renter occupied - income $150000 or more": "B25118_025E"
    }
#%%

# Years selected
# Year 2020 is not available on the API service
first_year = 2015
last_year = 2019

#%% Changing type fof variables from object to num, except the state name
population_df = create_dataframe_data(population_features , \
                                  api_keys, first_year, last_year)
gross_rent_dist_df = create_dataframe_data(gross_rent_features, \
                                      api_keys, first_year, last_year)

rent_income_dist_df = create_dataframe_data(rent_occupied_by_income_features, \
                                      api_keys, first_year, last_year)

# Dump df to csv if it's needed
# population_df.to_csv('data/population_demo.csv', index=False)


# Now info from HIC
our_data = dict()

raw_data = pd.read_excel('data/2007-2021-PIT-Counts-by-State.xlsx', sheet_name=None)
var_name = 'Overall Homeless, '

years = np.arange(2015, 2021)
for y in years:
    y = str(y)
    our_data[y] = raw_data[y][var_name + y].values

our_data['State'] = raw_data[y]['State']

our_data_df = pd.DataFrame(our_data)
# our_data_df.to_csv('data/overall_homelessness.csv', index=False)

