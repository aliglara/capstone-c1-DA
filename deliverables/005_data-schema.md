# Topic: Rental Rise Cost

## Data Wrangling

Team Number: 120

Group Members: Jenelle Allen, [Nancy Beard](https://www.linkedin.com/in/nancy-beard-96872b37), Orpa Jackson, [Wildo Acosta](linkedin.com/in/wildo-acosta-quiñones-86215484), [Ali Lara](https://www.linkedin.com/in/aliglara)



## Homelessness Database

|||
|-|-|
| File name | 2007-2021-PIT-Counts-by-State (2007 - 2020) |
| Name | PIT and HIC Data Since 2007 |
| Size | 1.1 MB |
| Source | [https://www.hudexchange.info](https://www.hudexchange.info) |
| Direct link | [https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/](https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/) |

### Data Schema

*\~50 rows & 7 columns.* Size 18.7 KB


  Field | Type    |    Description |
  ------|---------|--------------------------------------|
  States          |    STRING      | States abbreviation |
  years           | INTEGER        |

## Population Database

|||
|-|-|
| File name | project_data.csv (US population indexes) 2015 - 2020|
| Name | US Population and People|
| Size | 3.6 MB|
| Source | [https://data.census.gov](https://data.census.gov)|
| Direct link | [https://data.census.gov/cedsci/table?q=United%20States](https://data.census.gov/cedsci/table?q=United%20States)|

### Data Schema

*\~200 rows & 53 columns.* Size 66.0 KB

| Variable Name | Description  | Type |
|---|---|---|
| B01001_001E | Population | int |
| B11001_001E | Population in households | int |
| B17001_002E | Pop. below poverty level | int |
| B17001_031E | Pop. at or Above poverty level | int |
| B23025_002E | Pop. in Labor Force | int |
| B23025_007E | Pop. not in Labor Force | int |
| B23006_024E | Bachelor or higher Pop. in labor force | int |
| B23006_029E | Bachelor or higher Pop. not labor force | int |
| B15003_001E | Total Population 25 years and over - Educ. attainment | int |
| B15003_002E | Population 25 years and over - No schooling completed | int |
| B15003_022E | Population 25 years and over - Bachelor's degree | int |
| B15003_023E | Population 25 years and over - Master's degree | int |
| B15003_023E | Population 25 years and over - Doctorate degree | int |
| B19013_001E | Median household Earnings($) | int |
| B20004_001E | Median Earnings - Educational attainment | int |
| B20004_005E | Median Earnings - Bachelor | int |
| B20004_006E | Median Earnings - Master or Above | int |
| B25001_001E | Total housing units | int |
| B25002_002E | Total Occupied housing units | int |
| B25003_003E | Total Renter occupied - Tenure | int |
| B25118_014E | Total Renter occupied - by income | int |
| B25013_001E | Total housing units - Educational attainment | int |
| B25013_007E | Total Renter-occupied units- Educational attainment | int |
| B25013_008E | Renter-occupied units - Less than high school graduate | int |
| B25013_009E | Renter-occupied units - High school graduate | int |
| B25013_010E | Renter-occupied units - Some college degree | int |
| B25013_011E | Renter-occupied units - Bachelor's degree or higher | int |
| B25064_001E | Median gross rent | int |
| B25063_003E | Renter-occupied housing units with a rent Less than $100 | int |
| B25063_004E | Renter-occupied housing units with a rent $100 to $149 | int |
| B25063_005E | Renter-occupied housing units with a rent $150 to $199 | int |
| B25063_006E | Renter-occupied housing units with a rent $200 to $249 | int |
| B25063_007E | Renter-occupied housing units with a rent $250 to $299 | int |
| B25063_008E | Renter-occupied housing units with a rent $300 to $349 | int |
| B25063_009E | Renter-occupied housing units with a rent $350 to $399 | int |
| B25063_010E | Renter-occupied housing units with a rent $400 to $449 | int |
| B25063_011E | Renter-occupied housing units with a rent $450 to $499 | int |
| B25063_012E | Renter-occupied housing units with a rent $500 to $549 | int |
| B25063_013E | Renter-occupied housing units with a rent $550 to $599 | int |
| B25063_014E | Renter-occupied housing units with a rent $600 to $649 | int |
| B25063_015E | Renter-occupied housing units with a rent $650 to $699 | int |
| B25063_016E | Renter-occupied housing units with a rent $700 to $749 | int |
| B25063_017E | Renter-occupied housing units with a rent $750 to $799 | int |
| B25063_018E | Renter-occupied housing units with a rent $800 to $899 | int |
| B25063_019E | Renter-occupied housing units with a rent $900 to $999 | int |
| B25063_020E | Renter-occupied housing units with a rent $1000 to $1249 | int |
| B25063_021E | Renter-occupied housing units with a rent $1250 to $1499 | int |
| B25063_022E | Renter-occupied housing units with a rent $1500 to $1999 | int |
| B25063_023E | Renter-occupied housing units with a rent $2000 to $2499 | int |
| B25063_024E | Renter-occupied housing units with a rent $2500 to $2999 | int |
| B25063_025E | Renter-occupied housing units with a rent $3000 to $3499 | int |
| B25063_026E | Renter-occupied housing units with a rent $3500 or more | int |
| B25118_015E | Renter-occupied housing units with an income less than $5000 | int |
| B25118_016E | Renter-occupied housing units with an income $5000 to $9999 | int |
| B25118_017E | Renter-occupied housing units with an income $10000 to $14999 | int |
| B25118_018E | Renter-occupied housing units with an income $15000 to $19999 | int |
| B25118_019E | Renter-occupied housing units with an income $20000 to $24999 | int |
| B25118_020E | Renter-occupied housing units with an income $25000 to $34999 | int |
| B25118_021E | Renter-occupied housing units with an income $35000 to $49999 | int |
| B25118_022E | Renter-occupied housing units with an income $50000 to $74999 | int |
| B25118_023E | Renter-occupied housing units with an income $75000 to $99999 | int |
| B25118_024E | Renter-occupied housing units with an income $100000 to $149999 | int |
| B25118_025E | Renter-occupied housing units with an income $150000 or more | int |

STRING = text

INTEGER = number without decimals

FLOAT = number with decimals

DATETIME = date

BOOLEAN = True/False values
