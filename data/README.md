# Content description

This folder contents the raw data files and the final file which it was used during the project

    .
    ├── raw_data                             # Files taken census.gov
    ├── 2007-2021-PIT-Counts-by-State.xlsx   # US homelessness dataset
    ├── geo_data.csv                         # Information de States ID based on census.gov
    ├── project_data.csv                     # Final dataset used in the project
    ├── grab_data.py                         # Python file which creates the dataset file
    ├── grab_data.ipynb                      # Jupiter Notebook file which creates the dataset file
    └── ...

## Population dataset

The raw data was downloaded from [data.census.gov](https://data.census.gov/cedsci/table?q=United%20States), which was filtered by the following topics:

1. Geography > Nation > United States
1. Population and People > Population and People

As a result of the previous filter applied, several tables were presented. Finally, the main table was selected to get a broad view of the features available.

The result was downloaded in a CSV format, and each year created, a file. The set of files was saved in the folder **raw_data**

## Homelessness Dataset

The estimates of homelessness by state from 2007 to 2021 was downloaded from the [HUD Exchange](https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/) website and the resut was stored in the file *2007-2021-PIT-Counts-by-State.xlsx*

## Python code

The estimates of the US population is a quite long dataset. Therefore, a python script was created (*grab_data.py*) to extract the information needed for this project.

The list of features were:

- Name of state
- Year
- Total population
- Population in households
- Education attainment
- Employment status
- Income
- Housing ternure
- Housing cost

The final file is ***project_data.csv***

## Other files

The file *grab_data.ipynb* is a mirror of the grab_data.py but in jupyter notebook format. Meanwhile, *geo_data.csv* is a simple file which the state id is listed based on teh census.gov nomenclature.
