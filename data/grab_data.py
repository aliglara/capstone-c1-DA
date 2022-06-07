# %%
# List of modules used
import pandas as pd
import os
import re

# %% [markdown]
# # Selection of the files
# 
# Inside of the folder there is a file for each year. Thus in this part of the code working files are selected based on their name

# %%
folder_path = 'raw_data/population'
pattern_name = '.*S0201_data_with_overlays_*'

# %%
files_data = [(int(x.split('.')[0][-4:]), x) for x in os.listdir(folder_path) if re.match(pattern_name, x)]

# %%
# Let'see what we got
print(files_data)

# %% [markdown]
# # Ordering files
# 
# The order of the files is made based on the year (Ascending)
# 
# ## Extract years and sort them

# %%
year_sorted = [year[0] for year in files_data]
year_sorted.sort()

# %% [markdown]
# ## Sorting files
# Based on the sorted year list, the files were sorted

# %%
files_data_sorted = [i for j in year_sorted for i in filter(lambda k: k[0] == j, files_data)]

# %%
files_data_sorted 

# %% [markdown]
# # Extract info for each file
# 
# A prior selection of the features was made and store in the variable features

# %%
features = {
    "id": "GEO_ID",
    "State": "NAME",
    "Total population": "S0201_001E",
    "Population in households": "S0201_038E",
    "Educational attainment": ["S0201_090E", "S0201_091E", "S0201_092E","S0201_093E", "S0201_094E", "S0201_095E"],
    "Employment status": ["S0201_154E", "S0201_155E","S0201_157E", "S0201_158E",  "S0201_161E"],
    "Income": ["S0201_213E", "S0201_214E", "S0201_226E", "S0201_227E"],
    "Housing tenure": ["S0201_265E", "S0201_266E", "S0201_267E"],
    "Housing cost": ["S0201_298E", "S0201_299E", "S0201_304E"]    
}

# %% [markdown]
# From the previous selection, a list was created to extract the info for each file using the pandas module

list_features = []
for key, value in features.items():
    if isinstance(value, list):
        # In case the value field is a list of codes
        list_features.extend(value)
    else:
        # Id the value field is only one string
        list_features.append(value)

# %% [markdown]
# Extraction the information
# This piece of code extracts the info of selected features from each file, and put all together in a master cvs file

list_dataframes = []
for file_tuple in files_data_sorted:
    # Extract the year and name of file
    
    year, file_name = file_tuple
    df = pd.read_csv(folder_path + '/' + file_name)
    try:
        for feature in list_features:
            # Extract features
            if feature not in df.columns:
                df[feature] = None
        df = df[list_features]
        
        #set state id as index
        df.set_index('GEO_ID', inplace=True)
        
        # Cleaning unnecessary fields
        if '0400000US72' in df.index:
            df = df.drop(['id', '0400000US72'])
        else:
            df = df.drop('id')
        df = df.drop('NAME', axis=1)
        
        # Reshape
        df = df.transpose()
        
        # Added year of the data
        df['Year'] = year
        list_dataframes.append(df)
    except:
        print(file_name)

# Put all together    
data = pd.concat(list_dataframes)

# Save to a csv file
data.to_csv('project_data.csv')    

# %%
print(data.head())
