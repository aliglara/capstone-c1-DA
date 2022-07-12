
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import markers
#%%
sns.set_style('whitegrid')
all_shapes = list(markers.MarkerStyle.markers.keys())

# Grabbing homelessness data

raw_data = pd.read_csv('../data/overall_homelessness.csv', header=None)

## Some Data preprocessing

# Assign state abbreviation as column names
df = raw_data.copy()
df = df.replace(" ", 0, regex=True)
df.columns = df.iloc[0]
df = df.drop(labels=[0, 4, 57], axis=0)
df.reset_index(inplace=True, drop=True)


df.set_index('State', inplace=True)
df = df.rename_axis("Year", axis="columns")

df = df.apply(lambda x: x.astype('int'))
# Visualizations

## How is the distribution of homelessness by state for each year?


fig, axes = plt.subplots(2, 2, figsize=(20, 12))
for year, ax in zip(df.columns[-5:-1], axes.ravel()):
    df2 = df.sort_values(year, ascending=False)
    g = sns.barplot(x=df2.index, y=year, data=df2,
                    palette="coolwarm_r", ax=ax)
    plt.sca(ax)
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Top 10 States Overall Homeless population from 2010 - 2020

n_years = len(df.columns)

if n_years % 2 != 0:
    n_years = n_years + 1

fig, axes = plt.subplots(3, 4, figsize=(20, 12), sharex='col')
for year, ax in zip(df.columns, axes.ravel()):
    df2 = df.sort_values(year, ascending=False).head(10)
    _ = sns.barplot(y=df2.index, x=year, data=df2,
                    palette="coolwarm_r", ax=ax, orient="h")
plt.tight_layout()

## Select the top 10 States with higher overall homelessness in the last 10 years

list_top_states = []
for year in df.columns:
    list_top_states.extend(df.sort_values(by=year, ascending=False).head(10).index.to_list())

top_states = list(set(list_top_states))
#%%
top_states_df = df.loc[top_states]


## How the homelessness population has changed over the time for the selected states

sns.set(font_scale=1.5)
#%%
fig, ax = plt.subplots(figsize=(12, 8))
for i, state in enumerate(top_states_df.index.to_list()):
    _ = sns.lineplot(data=top_states_df.loc[state],
                     palette='tab20',
                     marker=all_shapes[i], markersize=14)

ax.set_ylabel('Overall homeless number')
ax.legend(labels=top_states_df.index.to_list(), title = "State",
           fontsize = 'large',
         bbox_to_anchor=(1.01, 1.01), loc="upper left")

plt.show()

# Removing states with significant homeless population change over the last 10 years
out_state = ['CA', 'NY', 'FL']
new_top_states = [i for i in top_states_df.index.to_list() if i not in out_state]
#%%
fig, ax = plt.subplots(figsize=(12, 8))
for i, state in enumerate(new_top_states):
    _ = sns.lineplot(data=top_states_df.loc[state],
                     palette='tab20',
                     marker=all_shapes[i], markersize=12)

ax.set_ylabel('Overall homeless number')
ax.legend(labels=new_top_states, title = "State",
           fontsize = 'large',
         bbox_to_anchor=(1.01, 1.01), loc="upper left")
plt.show()

# Calculate the percentage change per year
change_perc = top_states_df.pct_change(axis=1)

# Calculate the overall percentage change from 2010
change_perc['Accumulated'] = (top_states_df['2020'] - top_states_df['2010']) / top_states_df['2010']
#%%
change_perc = change_perc.mul(100).sort_values('Accumulated', ascending=False)
#%%

columns = change_perc.columns[1:-1]
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 15))
# First figure
_ = sns.barplot(x=change_perc.index,
                y='Accumulated', data=change_perc,
                palette='tab20', ax=ax1)

# Second figure
for i, state in enumerate(change_perc.index.to_list()):
    _ = sns.lineplot(data=change_perc.loc[state][columns],
                     palette='tab20',
                     marker=all_shapes[i], markersize=12, ax=ax2)

ax1.set_ylabel('Accumulated percentage change from 2010')
ax2.set_ylabel('Annual percentage change')
ax2.legend(labels=change_perc.index, title = "State",
          bbox_to_anchor=(1.01, 1.01), loc="upper left")
plt.tight_layout()
plt.show()
#%%
