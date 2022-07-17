#%%
import pandas as pd
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import markers

#%%
sns.set_style('whitegrid')
all_shapes = list(markers.MarkerStyle.markers.keys())

#%%

# Connect to database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="c11405i.",
    database="c1_capstone_project"
)

cursorObject = database.cursor()
# Data file

#database.close()
# %%
list_states = ['NY', 'CA', 'MA', 'WA', 'PA', 'OH', 'AZ', 'TX', 'OR', 'IL', 'MI', 'CO', 'GA', 'FL']

string_name = ",".join(list_states)

#%% Analizing number of rent housing by income

query = "SELECT rcid.*, sr.Abbreviation " \
        "FROM rent_cost_income_distribution as rcid " \
        "JOIN state_region sr ON rcid.state = sr.state " \
        "WHERE sr.Abbreviation IN " \
        "('NY', 'CA', 'MA', 'WA', 'PA', 'OH', 'AZ', 'TX', 'OR', 'IL', 'MI', 'CO', 'GA', 'FL')"

cursorObject.execute(query)

myresult = cursorObject.fetchall()

database.close()
#%%
column_names = [i[0] for i in cursorObject.description]
rent_cost_income_df = pd.DataFrame(myresult, columns=column_names)
#%%
rent_cost_income_df = rent_cost_income_df.drop(['id', 'state', 'Name'], axis=1)

#%%
rent_cost_income_df.head()
#%%
fig, ax = plt.subplots(figsize=(10,8))

_ = sns.barplot(x='Abbreviation', y='Total Renter occupied - by income',
                data=rent_cost_income_df[rent_cost_income_df['Year'] == 2015],
                ax=ax)
ax.set_xlabel('US State', fontsize=12)
ax.set_ylabel('Total Number of rental houses', fontsize=12)
plt.show()
#%%

#pd.pivot_table(rent_cost_income_df.loc['2015'], index=['Abbreviation'])

#%%
