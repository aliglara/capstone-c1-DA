# %%
import json

import pandas as pd
import requests


# %% User-function
def grab_data(year_list, features_str, api_key):
    """Pull data from census.gov

    Args:
        year_list (list): years list
        api_key (public api): api key required to scrap info from census
        features_str (string): string of variables to be read through API

    Yields:
        iterator: iterator object which contains the info from each y
    """
    acs_string = 'acs1'

    for year in year_list:
        if year == 2020:
            acs_string = 'acs5'
        url_string = 'https://api.census.gov/data/{}/acs/' + acs_string + '?get=NAME,{}&for=state:*&key={}'
        url = url_string.format(year, features_str, api_key['apis']['uscensus']['key'])
        json_text = requests.request("GET", url).json()
        for row in range(1, len(json_text)):
            json_text[row].insert(0, year)
        yield json_text[1:]


def create_dataframe_data(var_dict, api_census, ini_year, end_year=None):
    """
    Extraction the data from Census.gov per year, then consolidate them and create a pandas dataframe

    Args:
        var_dict: {dict} Dictionary of features
        api_census: {str} API key for gather info from census.gov
        ini_year: {int} First year for query
        end_year: {int} Last year for query, by default is equal to first year

    Output:
        df: {pandas dataframe} Dataframe that contains info from Census.gov
    """

    if end_year is not None:
        year_spam = [i for i in range(ini_year, end_year + 1)]
    else:
        year_spam = ini_year

    column_names = ['Year', 'Name']
    column_names = column_names + list(var_dict.keys()) + ['state']

    # Grab info from census.gov for each year
    feature_string = ",".join(var_dict.values())
    gen_data = grab_data(year_spam, feature_string, api_census)

    # Put all data together, but it's possible to grab a specific year
    all_data = []
    for x in gen_data:
        all_data.extend(x)

    return pd.DataFrame(all_data, columns=column_names)


# %%
# Reading api key
f = open('/Users/aliglara/Documents/MyGit/apis/credential_keys.json', "r")
api_keys = json.load(f)

# %%
# Dictionary of the variables selected for the project

population = {
    "Population": "B01001_001E",
    "Population in households": "B11001_001E",
    "Pop. below poverty level": "B17001_002E",
    "Pop. at or Above poverty level": "B17001_031E",
    "Pop. in Labor Force": "B23025_002E",
    "Pop. not in Labor Force": "B23025_007E",
    "Bachelor or higher Pop. in labor force": "B23006_024E",
    "Bachelor or higher Pop. not labor force": "B23006_029E",
    "Total Population 25 years and over - Educ. attainment": "B15003_001E",
    "Population 25 years and over - No schooling completed": "B15003_002E",
    "Population 25 years and over - Bachelor's degree": "B15003_022E",
    "Population 25 years and over - Master's degree": "B15003_023E",
    "Population 25 years and over - Doctorate degree": "B15003_023E",
    "Median household Earnings($)": "B19013_001E",
    "Median Earnings - Educational attainment": "B20004_001E",
    "Median Earnings - Bachelor": "B20004_005E",
    "Median Earnings - Master or Above": "B20004_006E",
    "Total housing units": "B25001_001E",
    "Total Occupied housing units": "B25003_001E",
    "Total Renter occupied - Tenure": "B25003_003E",
    "Total vacant housing units" : "B25004_001E",
    "Total vacant housing units for seasonal" : "B25004_006E",
    "Total vacant housing units for rent" : "B25004_002E",
    "Vacant housing units rented, not occupied" : "B25004_003E",
    "Total Renter occupied - by income": "B25118_014E",
    "Total housing units - Educational attainment": "B25013_001E",
    "Total Renter-occupied units- Educational attainment": "B25013_007E",
    "Renter-occupied units - Less than high school graduate": "B25013_008E",
    "Renter-occupied units - High school graduate": "B25013_009E",
    "Renter-occupied units - Some college degree": "B25013_010E",
    "Renter-occupied units - Bachelor's degree or higher": "B25013_011E",
    "Median gross rent": "B25064_001E"
}

# Number of renter housing by rent cost distribution
gross_rent = {
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
    "$3500 or more": "B25063_026E"
}

# Number of rented-housing units by income distribution
rent_occupied_by_income = {
    "less than $5000": "B25118_015E",
    "$5000 to $9999": "B25118_016E",
    "$10000 to $14999": "B25118_017E",
    "$15000 to $19999": "B25118_018E",
    "$20000 to $24999": "B25118_019E",
    "$25000 to $34999": "B25118_020E",
    "$35000 to $49999": "B25118_021E",
    "$50000 to $74999": "B25118_022E",
    "$75000 to $99999": "B25118_023E",
    "$100000 to $149999": "B25118_024E",
    "$150000 or more": "B25118_025E"
}
# %%

# Years selected
first_year = 2015
last_year = 2020

# %% Changing type fof variables from object to num, except the state name

var_files = [population, gross_rent, rent_occupied_by_income]
name_files = ['population', 'gross_rent', 'rent_occupied_by_income']

for variable, name in zip(var_files, name_files):
    df = create_dataframe_data(variable, api_keys, first_year, last_year)
    df.to_csv('../data/' + name + '.csv', index=False)

# %%
# Now info from HIC

raw_data = pd.read_excel('../data/2007-2021-PIT-Counts-by-State.xlsx', sheet_name=None)
var_name = 'Overall Homeless, '

years = [i for i in range(first_year, last_year + 1)]
our_data = []
for year in years:
    home_slicing = raw_data[str(year)][['State', var_name + str(year)]][:-1]
    home_slicing["Year"] = year
    our_data.extend(home_slicing.values.tolist())

homelessness_df = pd.DataFrame(our_data,
                               columns=['abbreaviation', 'homeless_pop', 'year'])
homelessness_df.set_index('year', inplace=True)

homelessness_df.to_csv('../data/overall_homelessness.csv')

# %%