# RENTAL COSTS ON THE RISE

## Overview

### Business Problem

Many Americans today have chosen to rent housing vs. buying. Some of their choices are no maintenance costs to cover, no real estate taxes to pay, access to complimentary amenities, or even more flexibility if the renter decides to relocate. Rental properties were forced to lock in on current rental rates during the pandemic. However, now that Americans are returning to normalcy, rental rates have risen.

Typically, the highest rent increase was about 3% in the past. However, America is seeing at least an 11% increase from a year earlier, with some larger cities showing 30-40% increases. Unfortunately, the average renter's income is not increasing at these same rates, causing renters to become homeless. Even though many homeless people might be employed, they just cannot afford housing.

Our goal is to create a data-driven tool that will demonstrate whether there is a link between rising rent and homelessness in the United States.

### Business Impact

Homelessness has a massive impact on the health and well-being of families nationwide. Among numerous health issues, homeless people are exposed to more outside elements -- hot, cold, rain, snow, hurricanes,
tornados, which increase the likelihood of getting sickness, injury, or disease can spread.

Additionally, [Bridges](https://journals.sagepub.com/doi/abs/10.1177/00111287221087957) (2022) has reported a strong correlation between homelessness and crime, which does not necessarily mean that homeless people cause offense. But due to harsh living conditions and a lack of defending themselves, they are vulnerable to hate crime.

Finally, [Ventriglio et al.](https://www.google.com/books/edition/Homelessness_and_Mental_Health/4_hQEAAAQBAJ?hl=en&gbpv=0) (2022) gave an outstanding review of the link between homelessness and mental health illnesses, which is obvious. Social and economic issues such as poverty, migration, unemployment, access to healthcare, and urbanization significantly impact both. As a result, understanding the cultural context is necessary for providing the best care in the community.

### Potential Audience

The general public might be interested in having a tool that can show how changes in rent costs impact the level of homelessness in the USA.

Despite that, several government agencies should be another potential audience because they can develop creative strategies to mitigate the problem. Solutions can cover programs such as temporary housing, career training, financial management, and child care services.

## Scope

The goal of this project was to create a data-driven tool to visualize whether there is a link between rising rent cost and homelessness among people who possesses a bachelor's degree or above in the United States.

## Data Analysis and Manipulation

### Data Source

The data used in this project was obtained from two US-official sources between 2015 to 2020.

First, the estimated US population will be grabbed from the US Census website, filtered by the following topics:

1. Geography > Nation > United States
2. Population and People > Population and People

Besides the broad information that can be obtained, this project was focused on the following features:

- Name of the state
- Year
- Total population
- Population in households
- Educational attainment
- Employment status
- Income
- Housing tenure
- Gross rent cost

Second, The estimate of homelessness population by state was pulled out from the HUD Exchange website

**The dataset was stored on my Heroku server to brush up on SQL coding. However, the original csv files are available in the GitHub repository. Click on -> ([link](https://github.com/aliglara/capstone-c1-DA/tree/main/data))**

### Data Wrangling and Cleaning

Describe how the info was taken from census.gov

## Exploratory Data Analysis

The EDA was split in the following sections:

1. General population and Homeless population data
2. Gross rent increase
3. Income and rent expenses by bachelor's professional or above

## US population and homeless population information

### Grabbing and combining datasets

Let's combine the information from the Census.gov and HUC dataset using a SQL

```python
query = (
    "with ctedata as "
"    ( " # Select data from homeless population and add state name and region
    "    SELECT "
    "    ohr.year, "
    "    ohr.abbreaviation, "
    "    sr.name, "
    "    ohr.homeless_pop, "
    "    sr.region "
    "    FROM overall_homeless AS ohr "
    "    JOIN state_region AS sr ON "
    "       ohr.abbreaviation = sr.abbreviation "
    "    WHERE ohr.abbreaviation is not null "
"    ) "
"    SELECT upop.year, " # Extract data from census.gov and add info from ctedata
"           upop.name_state, "
"           cte.abbreaviation, "
"           upop.population, "
"           cte.homeless_pop, "
"           upop.population_in_households, pop_in_labor_force, "
"           upop.bachelor_or_higher_pop_in_labor_force, "
"           upop.total_population_25_years_and_over_educ_attainment, "
"           upop.population_25_years_and_over_no_schooling_completed, "
"           upop.population_25_years_and_over_bachelor_degree, "
"           upop.population_25_years_and_over_master_degree + "
"           upop.population_25_years_and_over_doctorate_degree AS pop_25y_master_over, "
"           cte.region "
"    FROM us_population as upop "
"    LEFT JOIN ctedata AS cte ON (upop.year = cte.year) AND (upop.name_state = cte.name) "
)

raw_data_df = cheroku.make_query(query, "c1_capstone", credential_file)
```

```python
raw_data_df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>name_state</th>
      <th>abbreaviation</th>
      <th>population</th>
      <th>homeless_pop</th>
      <th>population_in_households</th>
      <th>pop_in_labor_force</th>
      <th>bachelor_or_higher_pop_in_labor_force</th>
      <th>total_population_25_years_and_over_educ_attainment</th>
      <th>population_25_years_and_over_no_schooling_completed</th>
      <th>population_25_years_and_over_bachelor_degree</th>
      <th>pop_25y_master_over</th>
      <th>region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>Mississippi</td>
      <td>MS</td>
      <td>2992333</td>
      <td>1983</td>
      <td>1104371</td>
      <td>1335130</td>
      <td>268930</td>
      <td>1952337</td>
      <td>28332</td>
      <td>253036</td>
      <td>223786</td>
      <td>South</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>Missouri</td>
      <td>MO</td>
      <td>6083672</td>
      <td>6482</td>
      <td>2374180</td>
      <td>3062893</td>
      <td>813903</td>
      <td>4097212</td>
      <td>35703</td>
      <td>706922</td>
      <td>640856</td>
      <td>South</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Montana</td>
      <td>MT</td>
      <td>1032949</td>
      <td>1709</td>
      <td>414804</td>
      <td>516733</td>
      <td>141994</td>
      <td>706329</td>
      <td>3347</td>
      <td>144135</td>
      <td>100088</td>
      <td>West</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>Nebraska</td>
      <td>NE</td>
      <td>1896190</td>
      <td>2744</td>
      <td>744159</td>
      <td>1025079</td>
      <td>275822</td>
      <td>1232583</td>
      <td>12252</td>
      <td>244556</td>
      <td>180058</td>
      <td>Midwest</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>Nevada</td>
      <td>NV</td>
      <td>2890845</td>
      <td>8743</td>
      <td>1042065</td>
      <td>1455305</td>
      <td>297028</td>
      <td>1968167</td>
      <td>32904</td>
      <td>304948</td>
      <td>224390</td>
      <td>West</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>State abbr</th>
      <th>Population</th>
      <th>Homeless pop</th>
      <th>Pop in households</th>
      <th>Pop in labor force</th>
      <th>Bachelor+ in labor force</th>
      <th>Pop. 25year+ educ</th>
      <th>Pop. 25year+ no schooling</th>
      <th>Pop. 25year+ bachelor</th>
      <th>Pop. 25year+ master over</th>
      <th>Region</th>
    </tr>
    <tr>
      <th>Year</th>
      <th>State name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">2015</th>
      <th>Mississippi</th>
      <td>MS</td>
      <td>2992333</td>
      <td>1983</td>
      <td>1104371</td>
      <td>1335130</td>
      <td>268930</td>
      <td>1952337</td>
      <td>28332</td>
      <td>253036</td>
      <td>223786</td>
      <td>South</td>
    </tr>
    <tr>
      <th>Missouri</th>
      <td>MO</td>
      <td>6083672</td>
      <td>6482</td>
      <td>2374180</td>
      <td>3062893</td>
      <td>813903</td>
      <td>4097212</td>
      <td>35703</td>
      <td>706922</td>
      <td>640856</td>
      <td>South</td>
    </tr>
    <tr>
      <th>Montana</th>
      <td>MT</td>
      <td>1032949</td>
      <td>1709</td>
      <td>414804</td>
      <td>516733</td>
      <td>141994</td>
      <td>706329</td>
      <td>3347</td>
      <td>144135</td>
      <td>100088</td>
      <td>West</td>
    </tr>
    <tr>
      <th>Nebraska</th>
      <td>NE</td>
      <td>1896190</td>
      <td>2744</td>
      <td>744159</td>
      <td>1025079</td>
      <td>275822</td>
      <td>1232583</td>
      <td>12252</td>
      <td>244556</td>
      <td>180058</td>
      <td>Midwest</td>
    </tr>
    <tr>
      <th>Nevada</th>
      <td>NV</td>
      <td>2890845</td>
      <td>8743</td>
      <td>1042065</td>
      <td>1455305</td>
      <td>297028</td>
      <td>1968167</td>
      <td>32904</td>
      <td>304948</td>
      <td>224390</td>
      <td>West</td>
    </tr>
  </tbody>
</table>
</div>

### How the US population has changed from 2015 to 2020

Let's add 4 columns to the dataframe:

- Homeless population percentage
- Change of homeless population percentage yearly
- Normalized homeless population
- Normalized total population

$$
\begin{aligned}
 & \text{Homeless pop perc.} = \frac{\text{Homeless pop}}{\text{Population}} \cdot 100 \\
 & \text{Normalized population} = \frac{\text{population(i)} - \min(\text{population})}{\max(\text{population}) - \min(\text{population})}
\end{aligned}
$$

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Homeless pop</th>
      <th>Population</th>
      <th>Homeless pop (%)</th>
      <th>Homeless change (%)</th>
      <th>Homeless adim</th>
      <th>Pop adim</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>559194</td>
      <td>324893003</td>
      <td>0.172116</td>
      <td>NaN</td>
      <td>0.972757</td>
      <td>0.980267</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>544951</td>
      <td>326538822</td>
      <td>0.166887</td>
      <td>-2.547059</td>
      <td>0.947980</td>
      <td>0.985233</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>545690</td>
      <td>329056355</td>
      <td>0.165835</td>
      <td>0.135609</td>
      <td>0.949265</td>
      <td>0.992829</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>547200</td>
      <td>330362592</td>
      <td>0.165636</td>
      <td>0.276714</td>
      <td>0.951892</td>
      <td>0.996770</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>561563</td>
      <td>331433217</td>
      <td>0.169435</td>
      <td>2.624817</td>
      <td>0.976878</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>574855</td>
      <td>329824950</td>
      <td>0.174291</td>
      <td>2.366965</td>
      <td>1.000000</td>
      <td>0.995148</td>
    </tr>
  </tbody>
</table>
</div>

![png](images/EDA_homeless_pop_19_0.png)

Takeaways:

- Since 2018, the total US-homeless population has increased an average of 2.5% yearly
- Based on the Census.gov database, the highest US homeless population was registered in 2020
- The US population registered a 0.5%-decrease between 2019 and 2020
- The homeless population is 0.16% of the total population from 2015 to 2020

### How the homeless population is distributed on the US territories

![png](images/EDA_homeless_pop_23_0.png)

Based on those figures, California is the state with a higher homeless population. Besides, there were no massive changes in the states with homeless people during the last four years.

Let's find out what are the top 10 states for each year

![png](images/EDA_homeless_pop_25_0.png)

What are the states that has been reported on the top 10 list between 2015 to 2020?

The top ten states list isn't kept constant during the period study.
Let's find out which states were on the top 10 list per year

Between 2015 and 2020, these are the 13 states that has been reported in the top 10 homeless population

```python
pd.Series(name_top_states)
```

    0        California
    1          New York
    2           Florida
    3             Texas
    4     Massachusetts
    5        Washington
    6      Pennsylvania
    7           Georgia
    8            Oregon
    9          Illinois
    10         Colorado
    11             Ohio
    12          Arizona

What are the US regions where those states belong to?

![png](images/EDA_homeless_pop_34_0.png)

From the last figure, it can be shown the US-region where most high-homeless population states are located in the West region.

### How has changed the homeless population of those states over time?

In order to show the variation over time, let's create a lineplot.

![png](images/EDA_homeless_pop_38_0.png)

Based on this figure, California (CA) is the state where the homelessness population has increased the most from 2018 to 2020. The New York state (NY) has shown a continuous homelessness increase.

In contrast, Florida (FL) has shown a continuous decrease since 2015. Let's see the behaviour of the rest of the states.

Due the magnitud order, the homeless population for the rest of the states has been shrunk to the plot bottom. Because of that, let's split the graph

![png](images/EDA_homeless_pop_41_0.png)

On the previous graph, it is possible to observe that the homeless population has increased considerably in Texas and Washington states. In contrast, Pennsylvania and  Illinois show that growth slowed down noticeably.
An interesting case is Georgia state, where homelessness has decreased dramatically. Finally, Colorado state shows a steady level, while Ohio appeared on the map in 2019 with a 3%-increase in the homeless population.

## Analyzing the 25 years and over US population

The main project goal is to analyze recent US population data to answer the question:

**Will a rent cost increment increase the risk of people who have been awarded a degree experiencing homelessness?**

Because of that, in the following section, a comparison between the US 25-year-and-over population is shown.

Let's create a pivot table where the 25 year and over population is summed by year

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pop. 25year+ bachelor</th>
      <th>Pop. 25year+ educ</th>
      <th>Pop. 25year+ master over</th>
      <th>Pop. 25year+ no schooling</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>41576643</td>
      <td>218829689</td>
      <td>35944674</td>
      <td>3191717</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>42675515</td>
      <td>220847677</td>
      <td>37397456</td>
      <td>3197250</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>44013586</td>
      <td>223593758</td>
      <td>39171256</td>
      <td>3238045</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>45029878</td>
      <td>225446877</td>
      <td>40358458</td>
      <td>3305133</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>46174068</td>
      <td>227200303</td>
      <td>41359648</td>
      <td>3360924</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>45478307</td>
      <td>225168128</td>
      <td>40665846</td>
      <td>3513496</td>
    </tr>
  </tbody>
</table>
</div>



![png](images/EDA_homeless_pop_46_0.png)

From the left plot, the 25-year population who have earned a formal educational level increased by around 4% from 2015 to 2019. However, in 2020, an almost 1% decrease is shown.

On the left graph, the bachelor's graduate population has kept 30% higher than the master's and above graduates from 2015 to 2020.

Interestingly, the population who haven't finished schooling has risen steadily to 1% of the total 25-year population during the same timespan.

In general, bachelor's graduate population represent a 20% of the population based on educational attainment while the master's one a 15%.

## US Population in labor force and in households

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Bachelor+ in labor force</th>
      <th>Pop in households</th>
      <th>Pop in labor force</th>
      <th>Population</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017</th>
      <td>49486843</td>
      <td>121254123</td>
      <td>165928662</td>
      <td>329056355</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>50702924</td>
      <td>122699817</td>
      <td>167091685</td>
      <td>330362592</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>51941004</td>
      <td>123973834</td>
      <td>168719014</td>
      <td>331433217</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>51234055</td>
      <td>123559968</td>
      <td>167113763</td>
      <td>329824950</td>
    </tr>
  </tbody>
</table>
</div>

![png](images/EDA_homeless_pop_52_0.png)

From this plot, the distribution of population in households, in labor and bachelor's graduate have kept almost the same since 2017

## Selection of the US states for further analysis

In order to visualize the relative change between the homeless population and the total population. Let's create the following ratio

$$ \text{ratio} = \frac{\text{Homeless population}}{\text{Total population}}\cdot 100 $$

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>State name</th>
      <th>Population</th>
      <th>Homeless pop</th>
      <th>% homeless</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>2015</td>
      <td>New York</td>
      <td>19795791</td>
      <td>88250</td>
      <td>0.445802</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2015</td>
      <td>Ohio</td>
      <td>11613423</td>
      <td>11182</td>
      <td>0.096285</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2015</td>
      <td>Oregon</td>
      <td>4028977</td>
      <td>13226</td>
      <td>0.328272</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2015</td>
      <td>Pennsylvania</td>
      <td>12802503</td>
      <td>15421</td>
      <td>0.120453</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2015</td>
      <td>Texas</td>
      <td>27469114</td>
      <td>23678</td>
      <td>0.086199</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>283</th>
      <td>2020</td>
      <td>Massachusetts</td>
      <td>6873003</td>
      <td>17975</td>
      <td>0.261531</td>
    </tr>
    <tr>
      <th>284</th>
      <td>2020</td>
      <td>Texas</td>
      <td>28635442</td>
      <td>27229</td>
      <td>0.095088</td>
    </tr>
    <tr>
      <th>287</th>
      <td>2020</td>
      <td>Ohio</td>
      <td>11675275</td>
      <td>10655</td>
      <td>0.091261</td>
    </tr>
    <tr>
      <th>288</th>
      <td>2020</td>
      <td>Colorado</td>
      <td>5684926</td>
      <td>9846</td>
      <td>0.173195</td>
    </tr>
    <tr>
      <th>295</th>
      <td>2020</td>
      <td>Washington</td>
      <td>7512465</td>
      <td>22923</td>
      <td>0.305133</td>
    </tr>
  </tbody>
</table>
<p>78 rows × 5 columns</p>
</div>

![png](images/EDA_homeless_pop_57_0.png)

From the graph, New York is the state with the highest proportion of people experiencing  homelessness. Along New York, the states with higher ratio homeless/population are: California, Oregon, Washington and Massachusetts.

On the other hand, Colorado, Florida, Arizona have a lower ratio, while Illinois has the lowest ratio in the group of states.

The group top ratio homeless-population states can be split at 0.25% level.

![png](images/EDA_homeless_pop_60_0.png)

These plots are interesting because show which states have had higher variance (change) on the ratio homeless-population in the last 6 years.

Based on those results, a better selection of the states for further study can be done. Let's calculate the mean and std for each feature

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean</th>
      <th>std</th>
    </tr>
    <tr>
      <th>State name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>0.341894</td>
      <td>0.045757</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>0.279207</td>
      <td>0.020963</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>0.343536</td>
      <td>0.019093</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>0.150073</td>
      <td>0.018300</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>0.107287</td>
      <td>0.018175</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>0.457563</td>
      <td>0.014874</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>0.287690</td>
      <td>0.011720</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>0.183129</td>
      <td>0.011054</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>0.140096</td>
      <td>0.008513</td>
    </tr>
    <tr>
      <th>Illinois</th>
      <td>0.087233</td>
      <td>0.008216</td>
    </tr>
    <tr>
      <th>Pennsylvania</th>
      <td>0.110664</td>
      <td>0.007799</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>0.087466</td>
      <td>0.004502</td>
    </tr>
    <tr>
      <th>Ohio</th>
      <td>0.089982</td>
      <td>0.003480</td>
    </tr>
  </tbody>
</table>
</div>

The selection of states will be those whose std % homeless is higher than 0.011

    ['California',
     'Massachusetts',
     'Oregon',
     'Florida',
     'Georgia',
     'New York',
     'Washington',
     'Colorado']

## Number of renter housing units by educational attainment level

The data was taken from the census.gov and it refers to the number of housing units available for rent, and the amount of occupied by people based on their educational level.

Therefore, the total of units by state represents the total number of renter housing units occupied by people based on their instructional level.

### Percentage of the units occupied by Bachelors or above

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total occupied units</th>
      <th>HS graduate</th>
      <th>College degree</th>
      <th>Bachelor degree or higher</th>
      <th>Perc bachelor or higher</th>
    </tr>
    <tr>
      <th>Year</th>
      <th>State name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">2015</th>
      <th>New York</th>
      <td>3394792</td>
      <td>844820</td>
      <td>845166</td>
      <td>1100677</td>
      <td>32.422517</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>604314</td>
      <td>134547</td>
      <td>240163</td>
      <td>161900</td>
      <td>26.790708</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1025304</td>
      <td>230928</td>
      <td>383616</td>
      <td>302918</td>
      <td>29.544213</td>
    </tr>
    <tr>
      <th>California</th>
      <td>5985534</td>
      <td>1200022</td>
      <td>1893017</td>
      <td>1744084</td>
      <td>29.138319</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>752117</td>
      <td>159916</td>
      <td>272185</td>
      <td>237783</td>
      <td>31.615161</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2703113</td>
      <td>746895</td>
      <td>905205</td>
      <td>676010</td>
      <td>25.008573</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1395241</td>
      <td>381047</td>
      <td>462321</td>
      <td>326843</td>
      <td>23.425559</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>979998</td>
      <td>256051</td>
      <td>256315</td>
      <td>324354</td>
      <td>33.097414</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2016</th>
      <th>New York</th>
      <td>3367884</td>
      <td>842587</td>
      <td>832435</td>
      <td>1095468</td>
      <td>32.526892</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>602099</td>
      <td>134741</td>
      <td>232715</td>
      <td>166276</td>
      <td>27.616056</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1038756</td>
      <td>228848</td>
      <td>382716</td>
      <td>313860</td>
      <td>30.214988</td>
    </tr>
    <tr>
      <th>California</th>
      <td>6000750</td>
      <td>1172516</td>
      <td>1895661</td>
      <td>1797156</td>
      <td>29.948856</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>743160</td>
      <td>169862</td>
      <td>264391</td>
      <td>231567</td>
      <td>31.159777</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2716331</td>
      <td>756690</td>
      <td>897648</td>
      <td>682080</td>
      <td>25.110342</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1417529</td>
      <td>374613</td>
      <td>460669</td>
      <td>359201</td>
      <td>25.339940</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>980468</td>
      <td>255927</td>
      <td>247469</td>
      <td>329306</td>
      <td>33.586614</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2017</th>
      <th>New York</th>
      <td>3374299</td>
      <td>868719</td>
      <td>822243</td>
      <td>1105071</td>
      <td>32.749647</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>596620</td>
      <td>138924</td>
      <td>227762</td>
      <td>164438</td>
      <td>27.561597</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1056828</td>
      <td>234076</td>
      <td>393582</td>
      <td>321653</td>
      <td>30.435700</td>
    </tr>
    <tr>
      <th>California</th>
      <td>5880007</td>
      <td>1167700</td>
      <td>1835573</td>
      <td>1818894</td>
      <td>30.933535</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>744383</td>
      <td>162841</td>
      <td>262026</td>
      <td>244313</td>
      <td>32.820873</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2679777</td>
      <td>758775</td>
      <td>893171</td>
      <td>670330</td>
      <td>25.014395</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1390152</td>
      <td>394684</td>
      <td>444283</td>
      <td>342009</td>
      <td>24.602274</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>981439</td>
      <td>267497</td>
      <td>244481</td>
      <td>334467</td>
      <td>34.079245</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2018</th>
      <th>California</th>
      <td>5906458</td>
      <td>1203884</td>
      <td>1823407</td>
      <td>1847783</td>
      <td>31.284113</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>758776</td>
      <td>158898</td>
      <td>264440</td>
      <td>257133</td>
      <td>33.887867</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2661116</td>
      <td>738646</td>
      <td>860756</td>
      <td>721596</td>
      <td>27.116293</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1376577</td>
      <td>384552</td>
      <td>438661</td>
      <td>351760</td>
      <td>25.553238</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>1003582</td>
      <td>243505</td>
      <td>254588</td>
      <td>364827</td>
      <td>36.352485</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>3413230</td>
      <td>863831</td>
      <td>822469</td>
      <td>1143569</td>
      <td>33.504012</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>615117</td>
      <td>139189</td>
      <td>230828</td>
      <td>176328</td>
      <td>28.665766</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1076587</td>
      <td>234401</td>
      <td>390863</td>
      <td>344269</td>
      <td>31.977815</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2019</th>
      <th>Georgia</th>
      <td>1382142</td>
      <td>364332</td>
      <td>451772</td>
      <td>371406</td>
      <td>26.871769</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>1002933</td>
      <td>248245</td>
      <td>245302</td>
      <td>379052</td>
      <td>37.794349</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2668313</td>
      <td>735931</td>
      <td>861242</td>
      <td>726145</td>
      <td>27.213636</td>
    </tr>
    <tr>
      <th>California</th>
      <td>5939131</td>
      <td>1170712</td>
      <td>1795291</td>
      <td>1938650</td>
      <td>32.641981</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>763191</td>
      <td>167779</td>
      <td>257594</td>
      <td>269774</td>
      <td>35.348163</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>3461296</td>
      <td>875810</td>
      <td>834760</td>
      <td>1209542</td>
      <td>34.944772</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>612227</td>
      <td>139477</td>
      <td>235822</td>
      <td>179748</td>
      <td>29.359698</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1082785</td>
      <td>232286</td>
      <td>395085</td>
      <td>350981</td>
      <td>32.414653</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2020</th>
      <th>California</th>
      <td>5861796</td>
      <td>1139471</td>
      <td>1819433</td>
      <td>1894008</td>
      <td>32.311053</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>3402708</td>
      <td>836585</td>
      <td>835974</td>
      <td>1177129</td>
      <td>34.593888</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2680435</td>
      <td>734536</td>
      <td>875359</td>
      <td>726725</td>
      <td>27.112204</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1377105</td>
      <td>370881</td>
      <td>451423</td>
      <td>363727</td>
      <td>26.412438</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>611573</td>
      <td>135147</td>
      <td>232841</td>
      <td>180989</td>
      <td>29.594014</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>992088</td>
      <td>247804</td>
      <td>249190</td>
      <td>363796</td>
      <td>36.669731</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>722078</td>
      <td>155657</td>
      <td>251821</td>
      <td>246568</td>
      <td>34.147004</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1067763</td>
      <td>229626</td>
      <td>391055</td>
      <td>342751</td>
      <td>32.099914</td>
    </tr>
  </tbody>
</table>
</div>

Pivot Table for aggregating the percentage of occupied houses by Bachelors or above

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>State name</th>
      <th>California</th>
      <th>Colorado</th>
      <th>Florida</th>
      <th>Georgia</th>
      <th>Massachusetts</th>
      <th>New York</th>
      <th>Oregon</th>
      <th>Washington</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>29.14</td>
      <td>31.62</td>
      <td>25.01</td>
      <td>23.43</td>
      <td>33.10</td>
      <td>32.42</td>
      <td>26.79</td>
      <td>29.54</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>29.95</td>
      <td>31.16</td>
      <td>25.11</td>
      <td>25.34</td>
      <td>33.59</td>
      <td>32.53</td>
      <td>27.62</td>
      <td>30.21</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>30.93</td>
      <td>32.82</td>
      <td>25.01</td>
      <td>24.60</td>
      <td>34.08</td>
      <td>32.75</td>
      <td>27.56</td>
      <td>30.44</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>31.28</td>
      <td>33.89</td>
      <td>27.12</td>
      <td>25.55</td>
      <td>36.35</td>
      <td>33.50</td>
      <td>28.67</td>
      <td>31.98</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>32.64</td>
      <td>35.35</td>
      <td>27.21</td>
      <td>26.87</td>
      <td>37.79</td>
      <td>34.94</td>
      <td>29.36</td>
      <td>32.41</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>32.31</td>
      <td>34.15</td>
      <td>27.11</td>
      <td>26.41</td>
      <td>36.67</td>
      <td>34.59</td>
      <td>29.59</td>
      <td>32.10</td>
    </tr>
  </tbody>
</table>
</div>

![png](images/EDA_homeless_pop_77_0.png)

## Takeaways

From there, we can say:

- From 2015 to 2020, bachelor's or above has rented between 22% to 35% of the rental housing market in the selected states.
- Oregon had shown around 2%-increment in houses rented by bachelors or above between 2017 and 2020. In contrast, it was about a 1%-decrease between 2019 and 2020 is shown in Massachusetts and Colorado.
- For the rest of the states, the rental rate is slowing down.

## Median income of bachelors or above

In this section, the features related to income and gross rent cost are analyzed focusing on professional householders.

What is the average national of the income for a bachelor and master graduates?

The next pivot table will help to answer that question

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Bachelor earning</th>
      <th>Master or above earning</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>51547.125</td>
      <td>67579.250</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>53728.125</td>
      <td>69625.250</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>55125.375</td>
      <td>71916.625</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>56791.125</td>
      <td>74543.375</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>58474.500</td>
      <td>77522.625</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>58469.625</td>
      <td>76875.375</td>
    </tr>
  </tbody>
</table>
</div>

From the previous results, the average of the median income had been increased yearly from 2015 to 2019 for both professional groups. However, from 2019 to 2020 their income decreased by 5% approx.

![png](images/EDA_homeless_pop_86_0.png)

What it would be maximum the rent cost a graduate professional could afford?

For this estimation, let's assume a professional will have to pay 37% in taxes and a mandatory requirement is that his/her monthly income has to twice higher than the rent cost offered.

$$ \text{max rent cost} = \text{salary}\cdot \left(\frac{100 - \text{tax perc}}{12 \cdot \text{ratio} \cdot 100}\right) $$

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>State name</th>
      <th>Bachelor earning</th>
      <th>Master or above earning</th>
      <th>Gross rent</th>
      <th>Perc diff</th>
      <th>Max rent Bachelor</th>
      <th>Max rent Master</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>New York</td>
      <td>55360</td>
      <td>71684</td>
      <td>1173</td>
      <td>29.49</td>
      <td>968.80</td>
      <td>1254.47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>Oregon</td>
      <td>44049</td>
      <td>61139</td>
      <td>943</td>
      <td>38.80</td>
      <td>770.86</td>
      <td>1069.93</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Washington</td>
      <td>55795</td>
      <td>71123</td>
      <td>1080</td>
      <td>27.47</td>
      <td>976.41</td>
      <td>1244.65</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>California</td>
      <td>57282</td>
      <td>80442</td>
      <td>1311</td>
      <td>40.43</td>
      <td>1002.44</td>
      <td>1407.74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>Colorado</td>
      <td>50196</td>
      <td>63270</td>
      <td>1111</td>
      <td>26.05</td>
      <td>878.43</td>
      <td>1107.22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015</td>
      <td>Florida</td>
      <td>42714</td>
      <td>57128</td>
      <td>1046</td>
      <td>33.75</td>
      <td>747.50</td>
      <td>999.74</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2015</td>
      <td>Georgia</td>
      <td>49696</td>
      <td>61443</td>
      <td>909</td>
      <td>23.64</td>
      <td>869.68</td>
      <td>1075.25</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015</td>
      <td>Massachusetts</td>
      <td>57285</td>
      <td>74405</td>
      <td>1164</td>
      <td>29.89</td>
      <td>1002.49</td>
      <td>1302.09</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>New York</td>
      <td>56868</td>
      <td>73504</td>
      <td>1194</td>
      <td>29.25</td>
      <td>995.19</td>
      <td>1286.32</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Oregon</td>
      <td>46942</td>
      <td>63868</td>
      <td>1015</td>
      <td>36.06</td>
      <td>821.48</td>
      <td>1117.69</td>
    </tr>
  </tbody>
</table>
</div>

**How much a master professional earns over a bachelor one?**

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Year</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
      <th>2018</th>
      <th>2019</th>
      <th>2020</th>
      <th>All</th>
    </tr>
    <tr>
      <th>State name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>40.43</td>
      <td>36.84</td>
      <td>40.39</td>
      <td>44.68</td>
      <td>41.88</td>
      <td>41.93</td>
      <td>41.02</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>26.05</td>
      <td>28.40</td>
      <td>29.73</td>
      <td>24.11</td>
      <td>22.99</td>
      <td>28.08</td>
      <td>26.56</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>33.75</td>
      <td>32.30</td>
      <td>33.53</td>
      <td>33.13</td>
      <td>30.57</td>
      <td>31.32</td>
      <td>32.43</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>23.64</td>
      <td>23.27</td>
      <td>26.13</td>
      <td>23.19</td>
      <td>30.50</td>
      <td>27.31</td>
      <td>25.67</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>29.89</td>
      <td>27.22</td>
      <td>28.67</td>
      <td>31.08</td>
      <td>31.12</td>
      <td>29.47</td>
      <td>29.58</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>29.49</td>
      <td>29.25</td>
      <td>24.96</td>
      <td>27.03</td>
      <td>29.25</td>
      <td>28.61</td>
      <td>28.10</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>38.80</td>
      <td>36.06</td>
      <td>32.56</td>
      <td>34.20</td>
      <td>34.97</td>
      <td>33.29</td>
      <td>34.98</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>27.47</td>
      <td>24.15</td>
      <td>28.07</td>
      <td>31.71</td>
      <td>37.98</td>
      <td>30.95</td>
      <td>30.05</td>
    </tr>
    <tr>
      <th>All</th>
      <td>31.19</td>
      <td>29.69</td>
      <td>30.51</td>
      <td>31.14</td>
      <td>32.41</td>
      <td>31.37</td>
      <td>31.05</td>
    </tr>
  </tbody>
</table>
</div>

A Master's degree holder earns an average of 30% more than a bachelor graduate in the last 6 years. In California, a master graduate earns 40% over a bachelor professional, while in Georgia is only 25% more.

**How much the gross rent has change over time?**

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Year</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
      <th>2018</th>
      <th>2019</th>
      <th>2020</th>
      <th>All</th>
    </tr>
    <tr>
      <th>State name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>1311.00</td>
      <td>1375</td>
      <td>1447.00</td>
      <td>1520.00</td>
      <td>1614.00</td>
      <td>1586.00</td>
      <td>1475.50</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>1111.00</td>
      <td>1171</td>
      <td>1240.00</td>
      <td>1289.00</td>
      <td>1369.00</td>
      <td>1335.00</td>
      <td>1252.50</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>1046.00</td>
      <td>1086</td>
      <td>1128.00</td>
      <td>1182.00</td>
      <td>1238.00</td>
      <td>1218.00</td>
      <td>1149.67</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>909.00</td>
      <td>933</td>
      <td>958.00</td>
      <td>1008.00</td>
      <td>1049.00</td>
      <td>1042.00</td>
      <td>983.17</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>1164.00</td>
      <td>1179</td>
      <td>1208.00</td>
      <td>1295.00</td>
      <td>1360.00</td>
      <td>1336.00</td>
      <td>1257.00</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>1173.00</td>
      <td>1194</td>
      <td>1226.00</td>
      <td>1274.00</td>
      <td>1309.00</td>
      <td>1315.00</td>
      <td>1248.50</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>943.00</td>
      <td>1015</td>
      <td>1079.00</td>
      <td>1130.00</td>
      <td>1185.00</td>
      <td>1173.00</td>
      <td>1087.50</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1080.00</td>
      <td>1135</td>
      <td>1216.00</td>
      <td>1316.00</td>
      <td>1359.00</td>
      <td>1337.00</td>
      <td>1240.50</td>
    </tr>
    <tr>
      <th>All</th>
      <td>1092.12</td>
      <td>1136</td>
      <td>1187.75</td>
      <td>1251.75</td>
      <td>1310.38</td>
      <td>1292.75</td>
      <td>1211.79</td>
    </tr>
  </tbody>
</table>
</div>

The average gross rent cost in the selected states had had a constant increase between 2015 to 2019. Nevertheless, in 2020 showed a slightly decrease.

![png](images/EDA_homeless_pop_97_0.png)

This figure is fascinating. It is shown that the median income for a bachelor's graduate is not enough to rent a house in none of the selected US-States. Florida is the only state where a bachelor's graduate roughly can afford the median gross rental cost.

In contrast, a master's graduate should be able to afford the median gross rent in all the states except Colorado and Florida.

Another thing is the gross rent cost has been increasing steadily in all States. California shows a 25%-increment percentage around %25, which is the higher observed among the selected States. On the other hand, the gross rent cost showed a slight decrease between 2019 and 2020

What is the maximum rent increase a master graduate could be tolerated?

Assuming the rent cost and median earning for master graduated kept constant. What it would be the maximum rental cost increase that can be afford for that population sector?

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State name</th>
      <th>Master or above earning</th>
      <th>Gross rent</th>
      <th>Max rent Master</th>
      <th>Max increase Master</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Georgia</td>
      <td>69501</td>
      <td>1042</td>
      <td>1216.27</td>
      <td>16.72</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Massachusetts</td>
      <td>84800</td>
      <td>1336</td>
      <td>1484.00</td>
      <td>11.08</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Washington</td>
      <td>83120</td>
      <td>1337</td>
      <td>1454.60</td>
      <td>8.80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New York</td>
      <td>80506</td>
      <td>1315</td>
      <td>1408.86</td>
      <td>7.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Oregon</td>
      <td>70453</td>
      <td>1173</td>
      <td>1232.93</td>
      <td>5.11</td>
    </tr>
    <tr>
      <th>0</th>
      <td>California</td>
      <td>91622</td>
      <td>1586</td>
      <td>1603.38</td>
      <td>1.10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florida</td>
      <td>63440</td>
      <td>1218</td>
      <td>1110.20</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Colorado</td>
      <td>71561</td>
      <td>1335</td>
      <td>1252.32</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State name</th>
      <th>Master or above earning</th>
      <th>Gross rent</th>
      <th>Max rent Master</th>
      <th>Max increase Master</th>
      <th>Units for rent available</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Georgia</td>
      <td>69501</td>
      <td>1042</td>
      <td>1216.27</td>
      <td>16.72</td>
      <td>77642</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Massachusetts</td>
      <td>84800</td>
      <td>1336</td>
      <td>1484.00</td>
      <td>11.08</td>
      <td>23804</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Washington</td>
      <td>83120</td>
      <td>1337</td>
      <td>1454.60</td>
      <td>8.80</td>
      <td>29356</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New York</td>
      <td>80506</td>
      <td>1315</td>
      <td>1408.86</td>
      <td>7.14</td>
      <td>104499</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Oregon</td>
      <td>70453</td>
      <td>1173</td>
      <td>1232.93</td>
      <td>5.11</td>
      <td>17695</td>
    </tr>
    <tr>
      <th>5</th>
      <td>California</td>
      <td>91622</td>
      <td>1586</td>
      <td>1603.38</td>
      <td>1.10</td>
      <td>173095</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Florida</td>
      <td>63440</td>
      <td>1218</td>
      <td>1110.20</td>
      <td>0.00</td>
      <td>201301</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Colorado</td>
      <td>71561</td>
      <td>1335</td>
      <td>1252.32</td>
      <td>0.00</td>
      <td>28517</td>
    </tr>
  </tbody>
</table>
</div>

![png](images/EDA_homeless_pop_109_0.png)

## Distribution of renter housing units by income salary

Assuming the rent cost increases higher than the maximum a master graduate can afford, are there cheaper rental options?

Based on our last result, let's focus on Georgia, Massachusetts, Washington, New York and California

list_states = ['Georgia', 'Massachusetts', 'Washington', 'New York', 'California']


![png](images/EDA_homeless_pop_116_0.png)

The average income for a master's graduate is USD75,000 which belongs to range where there are more renter housing units available in the selected states. Below the income range USD 50,000 to USD 74,999 most of the available housing units are rented by people who earn between USD 25,000 to USD50,000.

Therefore, it seems more likely in case of the rent cost increase more than maximum allowed that group of people could find cheaper places.

Based on the figure, the distribution of rented housing is not the same for all states. However, most units are rented by household income between USD 50,000 and 74,999.
Interestingly, the distribution of rented units for household income of USD 35,000 or above in California and New York tends to be uniform. On the other hand, for income range of USD 25,000 or less, the distribution of housing units is almost uniform.

Finally, in California, New York, and Massachusetts, the proportion of rented housing units with an income of USD 150,000 or above is significantly higher than in the rest of the seleted US States.

Let's check is the number of houses rented by people who earn less money than a master's graduate has increased since 2019

<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">$25000-$34999</th>
      <th colspan="2" halign="left">$35000-$49999</th>
      <th colspan="2" halign="left">$50000-$74999</th>
    </tr>
    <tr>
      <th>Year</th>
      <th>2019</th>
      <th>2020</th>
      <th>2019</th>
      <th>2020</th>
      <th>2019</th>
      <th>2020</th>
    </tr>
    <tr>
      <th>State name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>545487</td>
      <td>562032</td>
      <td>751801</td>
      <td>747735</td>
      <td>1035274</td>
      <td>1019318</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>73011</td>
      <td>77651</td>
      <td>110697</td>
      <td>107303</td>
      <td>160864</td>
      <td>147626</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>337616</td>
      <td>352222</td>
      <td>438067</td>
      <td>442012</td>
      <td>516471</td>
      <td>508067</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>178083</td>
      <td>181628</td>
      <td>219840</td>
      <td>212870</td>
      <td>255701</td>
      <td>243544</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>89652</td>
      <td>94697</td>
      <td>119355</td>
      <td>119366</td>
      <td>159921</td>
      <td>153367</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>325378</td>
      <td>335882</td>
      <td>414625</td>
      <td>417316</td>
      <td>534883</td>
      <td>526163</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>68084</td>
      <td>73620</td>
      <td>96298</td>
      <td>93765</td>
      <td>120352</td>
      <td>115913</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>102914</td>
      <td>105126</td>
      <td>153085</td>
      <td>154729</td>
      <td>202341</td>
      <td>202831</td>
    </tr>
  </tbody>
</table>
</div>

The Pivot table shows that the number of rented units increased for the USD 25,000-350000 income range, while for the USD 50,000 to 75,000 range decreased.

At this point, it seems there will have cheaper houses available for renting

## Distribution of renter housing units by rent cost

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>State name</th>
      <th>Less than 100</th>
      <th>$100-$149</th>
      <th>$150-$199</th>
      <th>$200-$249</th>
      <th>$250-$299</th>
      <th>$300-$349</th>
      <th>$350-$399</th>
      <th>$400-$449</th>
      <th>...</th>
      <th>$800-$899</th>
      <th>$900-$999</th>
      <th>$1000-$1249</th>
      <th>$1250-$1499</th>
      <th>$1500-$1999</th>
      <th>$2000-$2499</th>
      <th>$2500-$2999</th>
      <th>$3000-$3499</th>
      <th>$3500 or more</th>
      <th>id_state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>New York</td>
      <td>7166</td>
      <td>10928</td>
      <td>19334</td>
      <td>75748</td>
      <td>61802</td>
      <td>51727</td>
      <td>50293</td>
      <td>52649</td>
      <td>...</td>
      <td>200690</td>
      <td>207601</td>
      <td>518411</td>
      <td>442533</td>
      <td>546433</td>
      <td>229092</td>
      <td>117541</td>
      <td>72060</td>
      <td>65347</td>
      <td>36</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>Oregon</td>
      <td>1217</td>
      <td>1764</td>
      <td>4135</td>
      <td>8490</td>
      <td>5652</td>
      <td>5137</td>
      <td>5589</td>
      <td>9448</td>
      <td>...</td>
      <td>68147</td>
      <td>65774</td>
      <td>113914</td>
      <td>60251</td>
      <td>53955</td>
      <td>14396</td>
      <td>4407</td>
      <td>2519</td>
      <td>1667</td>
      <td>41</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Washington</td>
      <td>2662</td>
      <td>3985</td>
      <td>5918</td>
      <td>16466</td>
      <td>9906</td>
      <td>9940</td>
      <td>11834</td>
      <td>11794</td>
      <td>...</td>
      <td>84372</td>
      <td>90124</td>
      <td>178693</td>
      <td>143812</td>
      <td>151320</td>
      <td>47381</td>
      <td>15203</td>
      <td>7876</td>
      <td>5219</td>
      <td>53</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>California</td>
      <td>8966</td>
      <td>9636</td>
      <td>14664</td>
      <td>39713</td>
      <td>64298</td>
      <td>45813</td>
      <td>36758</td>
      <td>50098</td>
      <td>...</td>
      <td>369169</td>
      <td>411913</td>
      <td>980599</td>
      <td>885260</td>
      <td>1186872</td>
      <td>573041</td>
      <td>263003</td>
      <td>121438</td>
      <td>82590</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>Colorado</td>
      <td>2594</td>
      <td>2570</td>
      <td>3090</td>
      <td>11771</td>
      <td>6278</td>
      <td>3827</td>
      <td>6440</td>
      <td>7382</td>
      <td>...</td>
      <td>60414</td>
      <td>64189</td>
      <td>142587</td>
      <td>116160</td>
      <td>115197</td>
      <td>34901</td>
      <td>9451</td>
      <td>4011</td>
      <td>4792</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Less than 100</th>
      <th>$100-$149</th>
      <th>$150-$199</th>
      <th>$200-$249</th>
      <th>$250-$299</th>
      <th>$300-$349</th>
      <th>$350-$399</th>
      <th>$400-$449</th>
      <th>$450-$449</th>
      <th>$500-$549</th>
      <th>...</th>
      <th>$800-$899</th>
      <th>$900-$999</th>
      <th>$1000-$1249</th>
      <th>$1250-$1499</th>
      <th>$1500-$1999</th>
      <th>$2000-$2499</th>
      <th>$2500-$2999</th>
      <th>$3000-$3499</th>
      <th>$3500 or more</th>
      <th>id_state</th>
    </tr>
    <tr>
      <th>Year</th>
      <th>State name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">2015</th>
      <th>California</th>
      <td>8966</td>
      <td>9636</td>
      <td>14664</td>
      <td>39713</td>
      <td>64298</td>
      <td>45813</td>
      <td>36758</td>
      <td>50098</td>
      <td>49042</td>
      <td>65375</td>
      <td>...</td>
      <td>369169</td>
      <td>411913</td>
      <td>980599</td>
      <td>885260</td>
      <td>1186872</td>
      <td>573041</td>
      <td>263003</td>
      <td>121438</td>
      <td>82590</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>2594</td>
      <td>2570</td>
      <td>3090</td>
      <td>11771</td>
      <td>6278</td>
      <td>3827</td>
      <td>6440</td>
      <td>7382</td>
      <td>7694</td>
      <td>10997</td>
      <td>...</td>
      <td>60414</td>
      <td>64189</td>
      <td>142587</td>
      <td>116160</td>
      <td>115197</td>
      <td>34901</td>
      <td>9451</td>
      <td>4011</td>
      <td>4792</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>3166</td>
      <td>4898</td>
      <td>13553</td>
      <td>25641</td>
      <td>19440</td>
      <td>17761</td>
      <td>19618</td>
      <td>25963</td>
      <td>30279</td>
      <td>41204</td>
      <td>...</td>
      <td>266657</td>
      <td>283884</td>
      <td>574505</td>
      <td>347049</td>
      <td>323370</td>
      <td>90330</td>
      <td>31144</td>
      <td>19153</td>
      <td>11648</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1383</td>
      <td>3167</td>
      <td>8789</td>
      <td>17889</td>
      <td>17513</td>
      <td>16575</td>
      <td>17889</td>
      <td>22538</td>
      <td>25670</td>
      <td>38787</td>
      <td>...</td>
      <td>156099</td>
      <td>150949</td>
      <td>265367</td>
      <td>134682</td>
      <td>90673</td>
      <td>20108</td>
      <td>5541</td>
      <td>2233</td>
      <td>2384</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>5941</td>
      <td>5641</td>
      <td>7505</td>
      <td>22932</td>
      <td>26360</td>
      <td>19974</td>
      <td>17669</td>
      <td>16220</td>
      <td>15996</td>
      <td>14535</td>
      <td>...</td>
      <td>56186</td>
      <td>62896</td>
      <td>152640</td>
      <td>138307</td>
      <td>161366</td>
      <td>65792</td>
      <td>29029</td>
      <td>13678</td>
      <td>10398</td>
      <td>25</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>7166</td>
      <td>10928</td>
      <td>19334</td>
      <td>75748</td>
      <td>61802</td>
      <td>51727</td>
      <td>50293</td>
      <td>52649</td>
      <td>52813</td>
      <td>69286</td>
      <td>...</td>
      <td>200690</td>
      <td>207601</td>
      <td>518411</td>
      <td>442533</td>
      <td>546433</td>
      <td>229092</td>
      <td>117541</td>
      <td>72060</td>
      <td>65347</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>1217</td>
      <td>1764</td>
      <td>4135</td>
      <td>8490</td>
      <td>5652</td>
      <td>5137</td>
      <td>5589</td>
      <td>9448</td>
      <td>11039</td>
      <td>12067</td>
      <td>...</td>
      <td>68147</td>
      <td>65774</td>
      <td>113914</td>
      <td>60251</td>
      <td>53955</td>
      <td>14396</td>
      <td>4407</td>
      <td>2519</td>
      <td>1667</td>
      <td>41</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>2662</td>
      <td>3985</td>
      <td>5918</td>
      <td>16466</td>
      <td>9906</td>
      <td>9940</td>
      <td>11834</td>
      <td>11794</td>
      <td>12474</td>
      <td>16643</td>
      <td>...</td>
      <td>84372</td>
      <td>90124</td>
      <td>178693</td>
      <td>143812</td>
      <td>151320</td>
      <td>47381</td>
      <td>15203</td>
      <td>7876</td>
      <td>5219</td>
      <td>53</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2016</th>
      <th>California</th>
      <td>13093</td>
      <td>7938</td>
      <td>12554</td>
      <td>34644</td>
      <td>67886</td>
      <td>47876</td>
      <td>36728</td>
      <td>46576</td>
      <td>46963</td>
      <td>58610</td>
      <td>...</td>
      <td>309788</td>
      <td>376222</td>
      <td>942644</td>
      <td>865586</td>
      <td>1252782</td>
      <td>642460</td>
      <td>302057</td>
      <td>162518</td>
      <td>113711</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>2330</td>
      <td>1910</td>
      <td>3090</td>
      <td>8790</td>
      <td>5669</td>
      <td>6229</td>
      <td>6143</td>
      <td>8070</td>
      <td>8481</td>
      <td>10180</td>
      <td>...</td>
      <td>53328</td>
      <td>56295</td>
      <td>141062</td>
      <td>115635</td>
      <td>140470</td>
      <td>40988</td>
      <td>9952</td>
      <td>4207</td>
      <td>2563</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>3622</td>
      <td>5089</td>
      <td>14625</td>
      <td>24276</td>
      <td>20923</td>
      <td>21078</td>
      <td>20556</td>
      <td>20505</td>
      <td>24646</td>
      <td>36326</td>
      <td>...</td>
      <td>247825</td>
      <td>274001</td>
      <td>586172</td>
      <td>384395</td>
      <td>358569</td>
      <td>103760</td>
      <td>36529</td>
      <td>14200</td>
      <td>14550</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>3120</td>
      <td>4197</td>
      <td>9482</td>
      <td>16273</td>
      <td>14384</td>
      <td>15737</td>
      <td>18382</td>
      <td>24329</td>
      <td>25515</td>
      <td>41920</td>
      <td>...</td>
      <td>148199</td>
      <td>143102</td>
      <td>283926</td>
      <td>147155</td>
      <td>107276</td>
      <td>24787</td>
      <td>6461</td>
      <td>3422</td>
      <td>3223</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>3937</td>
      <td>4729</td>
      <td>8977</td>
      <td>25135</td>
      <td>27091</td>
      <td>18623</td>
      <td>16801</td>
      <td>16539</td>
      <td>14610</td>
      <td>16670</td>
      <td>...</td>
      <td>58418</td>
      <td>61056</td>
      <td>141698</td>
      <td>126226</td>
      <td>175040</td>
      <td>73770</td>
      <td>31628</td>
      <td>17747</td>
      <td>9117</td>
      <td>25</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>6276</td>
      <td>7381</td>
      <td>18429</td>
      <td>77562</td>
      <td>57835</td>
      <td>49612</td>
      <td>49944</td>
      <td>48420</td>
      <td>52098</td>
      <td>62278</td>
      <td>...</td>
      <td>203440</td>
      <td>203037</td>
      <td>495210</td>
      <td>436326</td>
      <td>549035</td>
      <td>246747</td>
      <td>117310</td>
      <td>86563</td>
      <td>77085</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>664</td>
      <td>1031</td>
      <td>3817</td>
      <td>7797</td>
      <td>4542</td>
      <td>5717</td>
      <td>5329</td>
      <td>6920</td>
      <td>9548</td>
      <td>13056</td>
      <td>...</td>
      <td>55068</td>
      <td>62190</td>
      <td>113167</td>
      <td>78947</td>
      <td>70220</td>
      <td>19669</td>
      <td>6098</td>
      <td>3122</td>
      <td>3569</td>
      <td>41</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>1489</td>
      <td>2618</td>
      <td>4436</td>
      <td>15965</td>
      <td>10495</td>
      <td>11331</td>
      <td>8550</td>
      <td>8926</td>
      <td>11030</td>
      <td>16657</td>
      <td>...</td>
      <td>79841</td>
      <td>93219</td>
      <td>178634</td>
      <td>141985</td>
      <td>174355</td>
      <td>59803</td>
      <td>24676</td>
      <td>9629</td>
      <td>6911</td>
      <td>53</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2017</th>
      <th>California</th>
      <td>9168</td>
      <td>8297</td>
      <td>13556</td>
      <td>32030</td>
      <td>68632</td>
      <td>38775</td>
      <td>38054</td>
      <td>41395</td>
      <td>40196</td>
      <td>54533</td>
      <td>...</td>
      <td>269986</td>
      <td>312074</td>
      <td>873916</td>
      <td>825890</td>
      <td>1279087</td>
      <td>707712</td>
      <td>361227</td>
      <td>186589</td>
      <td>137619</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>2282</td>
      <td>1066</td>
      <td>2434</td>
      <td>11746</td>
      <td>5397</td>
      <td>5488</td>
      <td>6152</td>
      <td>5879</td>
      <td>6572</td>
      <td>7308</td>
      <td>...</td>
      <td>45071</td>
      <td>54695</td>
      <td>131555</td>
      <td>130008</td>
      <td>147715</td>
      <td>48533</td>
      <td>16357</td>
      <td>5864</td>
      <td>5403</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>3147</td>
      <td>4933</td>
      <td>11812</td>
      <td>27775</td>
      <td>17605</td>
      <td>17607</td>
      <td>18856</td>
      <td>18067</td>
      <td>24069</td>
      <td>37530</td>
      <td>...</td>
      <td>228080</td>
      <td>253690</td>
      <td>572690</td>
      <td>416586</td>
      <td>392748</td>
      <td>120552</td>
      <td>40829</td>
      <td>17559</td>
      <td>15561</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1812</td>
      <td>5065</td>
      <td>8930</td>
      <td>19038</td>
      <td>15123</td>
      <td>16723</td>
      <td>16004</td>
      <td>20304</td>
      <td>27582</td>
      <td>38175</td>
      <td>...</td>
      <td>135179</td>
      <td>132634</td>
      <td>270631</td>
      <td>173624</td>
      <td>122705</td>
      <td>23619</td>
      <td>6806</td>
      <td>3972</td>
      <td>3890</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>4768</td>
      <td>6282</td>
      <td>6178</td>
      <td>24233</td>
      <td>25686</td>
      <td>19252</td>
      <td>18950</td>
      <td>16648</td>
      <td>13882</td>
      <td>15873</td>
      <td>...</td>
      <td>52221</td>
      <td>57272</td>
      <td>145539</td>
      <td>128736</td>
      <td>172675</td>
      <td>84338</td>
      <td>33885</td>
      <td>18678</td>
      <td>13297</td>
      <td>25</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>5600</td>
      <td>8020</td>
      <td>18055</td>
      <td>85064</td>
      <td>56882</td>
      <td>52342</td>
      <td>47744</td>
      <td>45736</td>
      <td>45393</td>
      <td>62324</td>
      <td>...</td>
      <td>188402</td>
      <td>197299</td>
      <td>478264</td>
      <td>430708</td>
      <td>594509</td>
      <td>269734</td>
      <td>122948</td>
      <td>86030</td>
      <td>78938</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>646</td>
      <td>1392</td>
      <td>3093</td>
      <td>6775</td>
      <td>4318</td>
      <td>5109</td>
      <td>5801</td>
      <td>7497</td>
      <td>7408</td>
      <td>9908</td>
      <td>...</td>
      <td>51798</td>
      <td>54818</td>
      <td>125995</td>
      <td>82803</td>
      <td>82051</td>
      <td>25159</td>
      <td>5295</td>
      <td>3237</td>
      <td>1909</td>
      <td>41</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>2802</td>
      <td>1943</td>
      <td>5535</td>
      <td>15128</td>
      <td>9642</td>
      <td>9798</td>
      <td>8256</td>
      <td>9900</td>
      <td>11640</td>
      <td>13870</td>
      <td>...</td>
      <td>67196</td>
      <td>72684</td>
      <td>183292</td>
      <td>148509</td>
      <td>210159</td>
      <td>74522</td>
      <td>28627</td>
      <td>12648</td>
      <td>7503</td>
      <td>53</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2018</th>
      <th>California</th>
      <td>9375</td>
      <td>6599</td>
      <td>10145</td>
      <td>32886</td>
      <td>68943</td>
      <td>38907</td>
      <td>33732</td>
      <td>38273</td>
      <td>41806</td>
      <td>53217</td>
      <td>...</td>
      <td>225753</td>
      <td>289258</td>
      <td>807597</td>
      <td>799628</td>
      <td>1359809</td>
      <td>767418</td>
      <td>406688</td>
      <td>213567</td>
      <td>171462</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>3147</td>
      <td>1431</td>
      <td>3413</td>
      <td>10885</td>
      <td>7761</td>
      <td>6008</td>
      <td>5430</td>
      <td>4976</td>
      <td>6625</td>
      <td>9690</td>
      <td>...</td>
      <td>39840</td>
      <td>51027</td>
      <td>130957</td>
      <td>132181</td>
      <td>165748</td>
      <td>64350</td>
      <td>17423</td>
      <td>5951</td>
      <td>3015</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>3190</td>
      <td>3079</td>
      <td>12705</td>
      <td>23588</td>
      <td>20373</td>
      <td>20093</td>
      <td>17711</td>
      <td>15729</td>
      <td>22575</td>
      <td>25223</td>
      <td>...</td>
      <td>195611</td>
      <td>233947</td>
      <td>548689</td>
      <td>446467</td>
      <td>462986</td>
      <td>139264</td>
      <td>45798</td>
      <td>20904</td>
      <td>13367</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>3567</td>
      <td>3927</td>
      <td>9005</td>
      <td>14968</td>
      <td>15021</td>
      <td>15793</td>
      <td>17714</td>
      <td>21534</td>
      <td>26544</td>
      <td>33306</td>
      <td>...</td>
      <td>119704</td>
      <td>124921</td>
      <td>284146</td>
      <td>187041</td>
      <td>145063</td>
      <td>28108</td>
      <td>7085</td>
      <td>3850</td>
      <td>3569</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>4878</td>
      <td>5708</td>
      <td>5948</td>
      <td>19070</td>
      <td>29480</td>
      <td>21472</td>
      <td>18684</td>
      <td>14882</td>
      <td>13194</td>
      <td>15515</td>
      <td>...</td>
      <td>43847</td>
      <td>51999</td>
      <td>133595</td>
      <td>121027</td>
      <td>191404</td>
      <td>104121</td>
      <td>48447</td>
      <td>24100</td>
      <td>16601</td>
      <td>25</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>4850</td>
      <td>9061</td>
      <td>17679</td>
      <td>77901</td>
      <td>59234</td>
      <td>53150</td>
      <td>43667</td>
      <td>45975</td>
      <td>46706</td>
      <td>49964</td>
      <td>...</td>
      <td>187272</td>
      <td>186589</td>
      <td>467056</td>
      <td>422926</td>
      <td>618091</td>
      <td>309805</td>
      <td>151964</td>
      <td>99658</td>
      <td>87205</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>1109</td>
      <td>1250</td>
      <td>2687</td>
      <td>9319</td>
      <td>5852</td>
      <td>5469</td>
      <td>3940</td>
      <td>5847</td>
      <td>8387</td>
      <td>9281</td>
      <td>...</td>
      <td>45942</td>
      <td>51161</td>
      <td>125189</td>
      <td>101751</td>
      <td>89467</td>
      <td>31876</td>
      <td>7602</td>
      <td>2431</td>
      <td>2589</td>
      <td>41</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>2229</td>
      <td>1360</td>
      <td>5107</td>
      <td>12852</td>
      <td>7820</td>
      <td>7919</td>
      <td>9628</td>
      <td>6834</td>
      <td>10723</td>
      <td>13253</td>
      <td>...</td>
      <td>60528</td>
      <td>63649</td>
      <td>166210</td>
      <td>158101</td>
      <td>233050</td>
      <td>98934</td>
      <td>38759</td>
      <td>17706</td>
      <td>12218</td>
      <td>53</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2019</th>
      <th>California</th>
      <td>8841</td>
      <td>9856</td>
      <td>10284</td>
      <td>25581</td>
      <td>76093</td>
      <td>43902</td>
      <td>31143</td>
      <td>37423</td>
      <td>39136</td>
      <td>46069</td>
      <td>...</td>
      <td>200107</td>
      <td>241144</td>
      <td>704349</td>
      <td>775413</td>
      <td>1394796</td>
      <td>860590</td>
      <td>466360</td>
      <td>268700</td>
      <td>209674</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>1933</td>
      <td>1083</td>
      <td>2021</td>
      <td>9015</td>
      <td>6615</td>
      <td>5866</td>
      <td>4561</td>
      <td>6176</td>
      <td>4533</td>
      <td>6372</td>
      <td>...</td>
      <td>34303</td>
      <td>38673</td>
      <td>129680</td>
      <td>135041</td>
      <td>193156</td>
      <td>74276</td>
      <td>21446</td>
      <td>6953</td>
      <td>3568</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2594</td>
      <td>2845</td>
      <td>9914</td>
      <td>28478</td>
      <td>18051</td>
      <td>17526</td>
      <td>14855</td>
      <td>18638</td>
      <td>18774</td>
      <td>30284</td>
      <td>...</td>
      <td>163631</td>
      <td>202693</td>
      <td>535922</td>
      <td>473369</td>
      <td>523816</td>
      <td>163746</td>
      <td>57234</td>
      <td>22094</td>
      <td>14650</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>1980</td>
      <td>3820</td>
      <td>6402</td>
      <td>17147</td>
      <td>13725</td>
      <td>15799</td>
      <td>15634</td>
      <td>16716</td>
      <td>23508</td>
      <td>28739</td>
      <td>...</td>
      <td>112647</td>
      <td>120809</td>
      <td>277620</td>
      <td>194548</td>
      <td>184058</td>
      <td>36113</td>
      <td>8203</td>
      <td>5390</td>
      <td>3765</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>2857</td>
      <td>5237</td>
      <td>6844</td>
      <td>18257</td>
      <td>30299</td>
      <td>20870</td>
      <td>17873</td>
      <td>16489</td>
      <td>13335</td>
      <td>11412</td>
      <td>...</td>
      <td>40643</td>
      <td>48743</td>
      <td>123468</td>
      <td>121706</td>
      <td>196610</td>
      <td>115297</td>
      <td>55512</td>
      <td>29035</td>
      <td>19747</td>
      <td>25</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>4710</td>
      <td>10406</td>
      <td>18684</td>
      <td>69770</td>
      <td>71247</td>
      <td>45363</td>
      <td>43826</td>
      <td>45636</td>
      <td>42456</td>
      <td>57494</td>
      <td>...</td>
      <td>176019</td>
      <td>192401</td>
      <td>451953</td>
      <td>408289</td>
      <td>648853</td>
      <td>332057</td>
      <td>169278</td>
      <td>108660</td>
      <td>99888</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>1066</td>
      <td>993</td>
      <td>3816</td>
      <td>7464</td>
      <td>5792</td>
      <td>4331</td>
      <td>3802</td>
      <td>5271</td>
      <td>5141</td>
      <td>6849</td>
      <td>...</td>
      <td>40865</td>
      <td>45694</td>
      <td>124063</td>
      <td>105484</td>
      <td>107827</td>
      <td>33323</td>
      <td>8791</td>
      <td>2533</td>
      <td>2701</td>
      <td>41</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>2617</td>
      <td>939</td>
      <td>7198</td>
      <td>16305</td>
      <td>9769</td>
      <td>9385</td>
      <td>6333</td>
      <td>6535</td>
      <td>8210</td>
      <td>10370</td>
      <td>...</td>
      <td>54273</td>
      <td>67391</td>
      <td>160142</td>
      <td>155877</td>
      <td>246063</td>
      <td>110099</td>
      <td>43036</td>
      <td>22512</td>
      <td>12216</td>
      <td>53</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2020</th>
      <th>California</th>
      <td>9376</td>
      <td>7595</td>
      <td>10155</td>
      <td>22394</td>
      <td>67290</td>
      <td>40555</td>
      <td>32657</td>
      <td>32936</td>
      <td>40348</td>
      <td>43461</td>
      <td>...</td>
      <td>204642</td>
      <td>256967</td>
      <td>757719</td>
      <td>759311</td>
      <td>1349250</td>
      <td>820826</td>
      <td>434206</td>
      <td>239869</td>
      <td>226691</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>1909</td>
      <td>1272</td>
      <td>1863</td>
      <td>8600</td>
      <td>6163</td>
      <td>5811</td>
      <td>4772</td>
      <td>5804</td>
      <td>5012</td>
      <td>7301</td>
      <td>...</td>
      <td>37412</td>
      <td>42228</td>
      <td>121595</td>
      <td>120686</td>
      <td>173263</td>
      <td>62977</td>
      <td>20498</td>
      <td>6166</td>
      <td>6113</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>2576</td>
      <td>3135</td>
      <td>9967</td>
      <td>25256</td>
      <td>16664</td>
      <td>17456</td>
      <td>15645</td>
      <td>17467</td>
      <td>19292</td>
      <td>26194</td>
      <td>...</td>
      <td>174797</td>
      <td>216151</td>
      <td>558164</td>
      <td>449218</td>
      <td>503829</td>
      <td>159888</td>
      <td>55337</td>
      <td>23098</td>
      <td>21330</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Georgia</th>
      <td>2264</td>
      <td>3112</td>
      <td>6679</td>
      <td>15355</td>
      <td>14040</td>
      <td>15602</td>
      <td>14479</td>
      <td>17091</td>
      <td>20997</td>
      <td>28840</td>
      <td>...</td>
      <td>113413</td>
      <td>124195</td>
      <td>283268</td>
      <td>194123</td>
      <td>167065</td>
      <td>37402</td>
      <td>8986</td>
      <td>4704</td>
      <td>4537</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Massachusetts</th>
      <td>3808</td>
      <td>5051</td>
      <td>5282</td>
      <td>16060</td>
      <td>30742</td>
      <td>18612</td>
      <td>15519</td>
      <td>16562</td>
      <td>12604</td>
      <td>14061</td>
      <td>...</td>
      <td>44469</td>
      <td>49133</td>
      <td>129465</td>
      <td>117421</td>
      <td>193386</td>
      <td>109571</td>
      <td>50966</td>
      <td>26569</td>
      <td>21696</td>
      <td>25</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>5585</td>
      <td>7620</td>
      <td>14953</td>
      <td>58323</td>
      <td>69795</td>
      <td>46480</td>
      <td>44399</td>
      <td>42157</td>
      <td>43135</td>
      <td>50338</td>
      <td>...</td>
      <td>177535</td>
      <td>183087</td>
      <td>454456</td>
      <td>415276</td>
      <td>634290</td>
      <td>322392</td>
      <td>154225</td>
      <td>100918</td>
      <td>124234</td>
      <td>36</td>
    </tr>
    <tr>
      <th>Oregon</th>
      <td>747</td>
      <td>1147</td>
      <td>2413</td>
      <td>7134</td>
      <td>4797</td>
      <td>4565</td>
      <td>4926</td>
      <td>5510</td>
      <td>6607</td>
      <td>7556</td>
      <td>...</td>
      <td>43301</td>
      <td>47691</td>
      <td>122156</td>
      <td>99120</td>
      <td>105866</td>
      <td>33945</td>
      <td>9415</td>
      <td>3303</td>
      <td>3980</td>
      <td>41</td>
    </tr>
    <tr>
      <th>Washington</th>
      <td>2004</td>
      <td>1633</td>
      <td>4960</td>
      <td>13450</td>
      <td>8741</td>
      <td>9879</td>
      <td>7695</td>
      <td>6976</td>
      <td>8218</td>
      <td>10914</td>
      <td>...</td>
      <td>55297</td>
      <td>65720</td>
      <td>167843</td>
      <td>151598</td>
      <td>233368</td>
      <td>108328</td>
      <td>38255</td>
      <td>19829</td>
      <td>14648</td>
      <td>53</td>
    </tr>
  </tbody>
</table>
<p>48 rows × 25 columns</p>
</div>

### Visualization of distribution of renter housing units

A Barplot is requiered a categorical variable on the x-axis, in our case, gross rent prices range. On the y-axis, a numerical value is needed which it will be the number of housing units.

The next figure shows a set of 6 barplots (one for each year) for each state.

![png](images/EDA_homeless_pop_130_0.png)

Based on the picture, the most of the renter housing units are in the range of USD 750 to $2500. However, it is difficult to observe if the number of units has changed over time.

### Cumulative Distribution of renter housing units

Let's plot a cumulative distribution by state by year


![png](images/EDA_homeless_pop_134_0.png)

There are several takeaways from there.

1. In the universe of the 10 top states where there has been a significant change in the homeless population, there are more housing units with rent costs between $750 to $2000.
2. California has the highest number of housing units for rent in the USA.
3. The distribution of housing units for rent is similar in California and New York.  In both states, the homeless population has increased over the last three years.
4. The total of units has decreased since 2015 in all states. However, in 2018-2020 (an increase in the homeless population), rental units have been almost the same in all states.
5. Interestingly, Florida's distribution of renter housing units is similar to California. Still, in Florida, the homeless population has decreased compared to California.

# Dashboard

# Takeaways
