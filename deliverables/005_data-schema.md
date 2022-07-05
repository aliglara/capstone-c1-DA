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
| Source | [https://data.census.gov](https://data.census.gov) |
| Direct link | [https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/](https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/) |

### Data Schema

*\~165 rows & 8 columns.* Size 18.7 KB


  Field | Type    |    Description |
  ------|---------|--------------------------------------|
  us_states       |    STRING      | Name of US states |
  states_abbreviation   |STRING      |States abbreviation |
  years                 |INTEGER     |

## Population Database

|||
|-|-|
| File name | project_data.csv (US population indexes) 2010 - 2020|
| Name | US Population and People|
| Size | 3.6 MB|
| Source | [https://data.census.gov](https://data.census.gov)|
| Direct link | [https://data.census.gov/cedsci/table?q=United%20States](https://data.census.gov/cedsci/table?q=United%20States)|

### Data Schema

*\~200 rows & 53 columns.* Size 66.0 KB

| Name | Label | SubLabel   | Predicate Type    |
|------|------ |------------|-------------------|
| S0201_001E | TOTAL NUMBER OF RACES REPORTED | Total population                                                                   | int |
| S0201_038E | RELATIONSHIP | Population in households                                                                             | int               |
| S0201_090E | EDUCATIONAL ATTAINMENT |Population 25 years and over                                                               | int               |
| S0201_091E | EDUCATIONAL ATTAINMENT |Population 25 years and over!!Less than high school diploma                                | float             |
| S0201_092E | EDUCATIONAL ATTAINMENT |Population 25 years and over!!High school graduate (includes equivalency)                  | float             |
| S0201_093E | EDUCATIONAL ATTAINMENT |Population 25 years and over!!Some college or associate's degree                           | float             |
| S0201_094E | EDUCATIONAL ATTAINMENT |Population 25 years and over!!Bachelor's degree                                            | float             |
| S0201_095E | EDUCATIONAL ATTAINMENT |Population 25 years and over!!Graduate or professional degree                              | float             |
| S0201_154E | EMPLOYMENT STATUS |Population 16 years and over                                                                    | int               |
| S0201_155E | EMPLOYMENT STATUS |Population 16 years and over!!In labor force                                                    | float             |
| S0201_157E | EMPLOYMENT STATUS |Population 16 years and over!!In labor force!!Civilian labor force!!Employed                    | float             |
| S0201_158E | EMPLOYMENT STATUS |Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed                  | float             |
| S0201_161E | EMPLOYMENT STATUS |Population 16 years and over!!Not in labor force                                                | float             |
| S0201_213E | INCOME IN THE PAST 12 MONTHS |Households                                      | int               |
| S0201_214E | INCOME IN THE PAST 12 MONTHS | Median household income (dollars)   | int               |
| S0201_226E | INCOME IN THE PAST 12 MONTHS |Families                                        | int               |
| S0201_265E | HOUSING TENURE |Occupied housing units                                                                             | int               |
| S0201_266E | HOUSING TENURE |Owner-occupied housing units                                               | float             |
| S0201_267E | HOUSING TENURE | Renter-occupied housing units                                              | float             |
| S0201_298E | HOUSING TENURE | Median Owner-occupied housing units value (dollars)                                        | int               |
| S0201_304E | GROSS RENT | Occupied units paying rent                                                                             | int               |

STRING = text

INTEGER = number without decimals

FLOAT = number with decimals

DATETIME = date

BOOLEAN = True/False values
