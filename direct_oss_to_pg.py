import psycopg2
import pandas as pd

# Read CSV
df = pd.read_csv('game_events.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="metabase",
    user="metabase",
    password="password",
    host="localhost",
    port="5432"
)

# Insert data
df.to_sql('game_events', conn, if_exists='replace', index=False)
conn.close()