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
    f = open(filepath, "r")
    credentials = json.load(f)
    f.close()
    conn = psycopg2.connect(
        host=credentials['databases']["heroku"][project]['host'],
        user=credentials['databases']["heroku"][project]['user'],
        password=credentials['databases']["heroku"][project]['password'],
        database=credentials['databases']["heroku"][project]['database'],
        port=credentials['databases']["heroku"][project]['port']
    )
    cursorobject = conn.cursor()
    cursorobject.execute(query_string)
    results = cursorobject.fetchall()
    column_names = [i[0] for i in cursorobject.description]
    cursorobject.close()
    df = pd.DataFrame(results, columns=column_names)
    return df