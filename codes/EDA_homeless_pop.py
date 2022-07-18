import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import markers
import json
import psycopg2

sns.set_style('whitegrid')
all_shapes = list(markers.MarkerStyle.markers.keys())
f = open('/Users/aliglara/Documents/MyGit/a+pis/credential_keys.json', "r")
keys = json.load(f)


# %% Connect to database function
def connect_database(server, project, credentials):
    conn = psycopg2.connect(
        host=credentials['databases'][server][project]['host'],
        user=credentials['databases'][server][project]['user'],
        password=credentials['databases'][server][project]['password'],
        database=credentials['databases'][server][project]['database'],
        port=credentials['databases'][server][project]['port']
    )
    return conn.cursor()


# %% Grabbing homelessness data
cursor = connect_database("heroku", "c1_capstone", keys)
query = ("select ohr.year, ohr.abbreaviation, ohr.homeless_pop "
         "from overall_homeless as ohr "
         "order by ohr.abbreaviation")
cursor.execute(query)
results = cursor.fetchall()
cursor.close()

# Convert query to pandas datafrme
column_names = [i[0] for i in cursor.description]
homeless_df = pd.DataFrame(results, columns=column_names)

# %%
homeless_df.info()

# There are some null values in the homeless_pop field. Let's see what we have
homeless_df[homeless_df["homeless_pop"].isnull()]

# %%
# There is no information from American Samoa (AS) and Northern Mariana Islands (MP).
# Therefore it's possible to rid of those unincorporated US territories

df_clean = homeless_df[(homeless_df["abbreaviation"] != "AS") & (homeless_df["abbreaviation"] != "MP")]
df_clean.reset_index(inplace=True, drop=True)

# # Visualizations
# 
# The data was taken from [Homelessness Data Exchange](https://www.hudhdx.info/) website where is recorded people
# experiencing homelessness.
# There are several fields reported but this project only is focused on the total homeless population by state per year

# %% What is the reported total homeless population by year

total_hom_pop = df_clean.pivot_table(index="year", aggfunc="sum")
total_hom_pop

fig, ax = plt.subplots(figsize=(10, 8))
p = sns.regplot(x=total_hom_pop.index, y="homeless_pop", data=total_hom_pop)
p.set_ylabel("Total homeless population", fontsize=20)
p.set_xlabel("Years", fontsize=20)
p.tick_params(axis='both', which='major', labelsize=15)

plt.show()

# Based on latter calculation, the homeless population has increased since 2018.
# ## What is its yearly percentage change?

total_hom_pop["Percentage change (%)"] = total_hom_pop["homeless_pop"].pct_change() * 100

print(total_hom_pop.head())

# Since 2018, the total homeless population in the USA has increased in 2.4% yearly
# ## How has the homeless population changed by state?

# What are the set of years
years = np.sort(df_clean["year"].unique())
print(years)

# In[17]:


_, axes = plt.subplots(3, 2, figsize=(20, 18), sharey='col')
for year, ax in zip(years, axes.ravel()):
    df2 = df_clean[df_clean["year"] == year].sort_values(by="homeless_pop", ascending=False)
    g = sns.barplot(x="abbreaviation", y="homeless_pop", data=df2,
                    palette="coolwarm_r", ax=ax)
    g.set_title(year)
    plt.sca(ax)
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ## Top 10 States Overall Homeless population from 2016 - 2020
# 
# Based on those figures, CA is the state with a higher homeless population. Besides,
# there were no massive changes in the states with homeless people during the last four years.
# 
# Let's see what are the top 10 states

# In[18]:


fig, axes = plt.subplots(3, 2, figsize=(18, 16))
for year, ax in zip(years, axes.ravel()):
    df2 = df_clean[df_clean["year"] == year].sort_values(by="homeless_pop", ascending=False)
    g = sns.barplot(y="abbreaviation", x="homeless_pop", data=df2.head(10),
                    palette="coolwarm_r", ax=ax, orient="h")
    g.set_title(year)
    g.tick_params(axis='both', which='major', labelsize=15)
plt.tight_layout()
plt.show()

# ## Select the top 10 States with higher overall homeless population
# 
# The top ten states list isn't kept constant during the period study. Let's find out which states were on the list

# ### Identify the index of the top 10 states for each year


list_top_states = []
for year in years:
    list_top_states.extend(df_clean[df_clean["year"] == year].sort_values(by="homeless_pop",
                                                                          ascending=False).head(10).index.to_list())

top_states = list(set(list_top_states))

top_states_df = df_clean.loc[top_states]
top_states_df.reset_index(inplace=True, drop=True)

# This is a dataframe where the top 10 states for each year is shown
print(top_states_df.head())

# ### What are the states with higher homeless population from 2015 to 2020
# 
# Now let's see which states are appeared on the top 10 list at least once


name_top_states = top_states_df["abbreaviation"].unique().tolist()
print("There are {} states that has been reported in the top 10 homeless population between {} and {}".format(
    len(name_top_states), min(years), max(years)
))

# ### What are those states located on the US map

query = ("select sr.abbreviation, sr.name, sr.region "
         "from state_region as sr "
         "where sr.abbreviation in (" + "'" + "','".join(name_top_states) + "')")

# In[24]:


cursor = connect_database("heroku", "c1_capstone", keys)
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
which_states = pd.DataFrame(results, columns=['Abbr', 'State', 'Region'])
print(which_states.head())

fig, ax = plt.subplots(figsize=(10, 8))
_ = sns.countplot(x='Region', data=which_states, palette="Spectral")
ax.set_ylabel('Number of states', fontsize=20)
ax.set_xlabel('Region', fontsize=20)
plt.tick_params(axis='x', which='major', labelsize=15, labelrotation=45)
plt.tick_params(axis='y', which='major', labelsize=15)
plt.show()

# From the last figure, it can be shown the US-region where most high-homeless population states
# are located in the West region.

# ## How has change the homeless population of those states over time?
# 
# In order to show the variation over time, let's do a lineplot.

_, ax = plt.subplots(figsize=(10, 8))
for i, state in enumerate(name_top_states):
    _ = sns.lineplot(x="year", y="homeless_pop",
                     data=top_states_df[top_states_df["abbreaviation"] == state],
                     palette='tab20',
                     marker=all_shapes[i],
                     markersize=12)

ax.set_ylabel('Overall homeless population', fontsize=20)
ax.legend(labels=name_top_states, title="State",
          fontsize='large',
          bbox_to_anchor=(1.01, 1.01), loc="upper left")
ax.set_xlabel('Year', fontsize=20)
plt.tick_params(which='major', labelsize=15)
plt.tight_layout()
plt.show()

# Based on this figure, California (CA) is the state where the homelessness population has increased the most
# from 2018 to 2020. The New York state (NY) has shown a continuous homelessness increase.
# 
# In contrast, Florida (FL) has shown a continuous decrease since 2015. Let's see the behaviour of
# the rest of the states.
# 
# Due the magnitud order, the homeless population for the rest of the states has been shrunk to the plot bottom.
# Because of that, let's split the graph

# In[27]:


out_state = ['CA', 'NY', 'FL']
new_top_states = [i for i in name_top_states if i not in out_state]

fig, ax = plt.subplots(figsize=(10, 8))
for i, state in enumerate(new_top_states):
    _ = sns.lineplot(x="year", y="homeless_pop", data=top_states_df[top_states_df["abbreaviation"] == state],
                     palette='tab20',
                     marker=all_shapes[i], markersize=12)

ax.set_ylabel('Overall homeless population', fontsize=20)
ax.legend(labels=new_top_states, title="State",
          fontsize='large',
          bbox_to_anchor=(1.01, 1.01), loc="upper left")
ax.set_xlabel('Year', fontsize=20)
plt.tick_params(which='major', labelsize=15)
plt.tight_layout()
plt.show()

# ## Ratio Homeless population vs Total population in Top States
# 
# Let's see who the homeless population has changed respect the total population

# ## Grab info from population, homeless and state_region database


query = ("select upop.year, sr.abbreviation, upop.population, ovh.homeless_pop "
         "from us_population as upop "
         "join state_region as sr "
         " on upop.id_state = sr.state "
         "join overall_homeless ovh "
         " on (upop.year = ovh.year) and (sr.abbreviation = ovh.abbreaviation) "
         "where ovh.abbreaviation in (" + "'" + "','".join(name_top_states) + "') "
         "order by upop.year, upop.id_state ")

cursor = connect_database("heroku", "c1_capstone", keys)
cursor.execute(query)
results = cursor.fetchall()
column_names = [i[0] for i in cursor.description]
cursor.close()

df = pd.DataFrame(results, columns=column_names)
df["% homeless"] = df["homeless_pop"] / df["population"] * 100

# Let's plot the % homeless by state over time

# In[34]:


fig, ax = plt.subplots(figsize=(10, 8))
for i, state in enumerate(name_top_states):
    _ = sns.lineplot(x="year", y="% homeless", data=df[df["abbreviation"] == state],
                     palette='tab20',
                     marker=all_shapes[i], markersize=12)

ax.set_ylabel('Percentage Homelessness', fontsize=20)
ax.legend(labels=name_top_states, title="State",
          fontsize='large',
          bbox_to_anchor=(1.01, 1.01), loc="upper left")
ax.set_xlabel('Year', fontsize=20)
plt.tick_params(which='major', labelsize=15)
plt.tight_layout()
plt.show()

# From the graph, the set of top homeless population states can be split at 0.25% level.

# In[35]:


df1 = df[df["% homeless"] > 0.25]
df2 = df[df["% homeless"] < 0.25]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
for i, state in enumerate(df1["abbreviation"].unique().tolist()):
    _ = sns.lineplot(x="year", y="% homeless", data=df1[df1["abbreviation"] == state],
                     palette='tab20',
                     marker=all_shapes[i], markersize=12, ax=ax1)

ax1.set_ylabel('Homelessness Percentage (%)', fontsize=20)
ax1.legend(labels=df1["abbreviation"].unique().tolist(), title="State",
           fontsize='large',
           bbox_to_anchor=(1.01, 1.01),
           loc="upper left")
ax1.set_xlabel('Year', fontsize=20)
ax1.tick_params(which='major', labelsize=15)

for i, state in enumerate(df2["abbreviation"].unique().tolist()):
    _ = sns.lineplot(x="year", y="% homeless", data=df2[df2["abbreviation"] == state],
                     palette='tab20',
                     marker=all_shapes[i], markersize=12, ax=ax2)

ax2.set_ylabel('Homelessness Percentage (%)', fontsize=20)
ax2.legend(labels=df2["abbreviation"].unique().tolist(), title="State",
           fontsize='large',
           bbox_to_anchor=(1.01, 1.01), loc="upper left")
ax2.set_xlabel('Year', fontsize=20)
ax2.tick_params(which='major', labelsize=15)

plt.tight_layout()
plt.show()

df.groupby(["abbreviation"])["% homeless"].agg(['mean', 'std']).sort_values(by="std", ascending=False)

# From the latter result, the state with high % homeless variation is California.
# In contrast, the state of Georgia, New York, and Washington has showed low variation,
# while the rest of the states have the same variation level during the study timespan.
# 
# The state of NY shows a high % homeless and low variation over time.
# 
# ### State of New York


print(df[df["abbreviation"] == 'NY'])

# ### State of Florida

print(df[df["abbreviation"] == 'FL'])

# # Selection the states for the study
# 
# The selection of states will be those whose average % homeless is higher than 0.1%


df_final = df.groupby(["abbreviation"])["% homeless"].agg(['mean', 'std']).sort_values(by="mean",
                                                                                       ascending=False)

print("The selected states are \n")
print(df_final[df_final["mean"] > 0.1].index.tolist())