from sqlalchemy import create_engine
import pandas as pd

# Read CSV
df = pd.read_csv('/root/game_events.csv')

engine = create_engine('postgresql://metabase:password@localhost:5432/metabase')

# Insert data
df.to_sql('game_events', engine, if_exists='replace', index=False)
