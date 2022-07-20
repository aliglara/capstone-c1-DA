import json
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