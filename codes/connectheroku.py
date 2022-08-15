import json

import pandas as pd
import psycopg2


def connect_database(project, filepath):
    f = open(filepath, "r")
    credentials = json.load(f)
    conn = psycopg2.connect(
        host=credentials['databases']["heroku"][project]['host'],
        user=credentials['databases']["heroku"][project]['user'],
        password=credentials['databases']["heroku"][project]['password'],
        database=credentials['databases']["heroku"][project]['database'],
        port=credentials['databases']["heroku"][project]['port']
    )
    return conn.cursor()


def make_query(query_string, project, filepath):
    # open credential file and read api key
    f = open(filepath, "r")
    credentials = json.load(f)
    f.close()

    # make the connection to Heroku server
    conn = psycopg2.connect(
        host=credentials['databases']["heroku"][project]['host'],
        user=credentials['databases']["heroku"][project]['user'],
        password=credentials['databases']["heroku"][project]['password'],
        database=credentials['databases']["heroku"][project]['database'],
        port=credentials['databases']["heroku"][project]['port']
    )
    cursor_object = conn.cursor()

    # query the info requested
    cursor_object.execute(query_string)
    results = cursor_object.fetchall()
    column_names = [i[0] for i in cursor_object.description]
    cursor_object.close()

    # return info as pandas dataframe
    return pd.DataFrame(results, columns=column_names)