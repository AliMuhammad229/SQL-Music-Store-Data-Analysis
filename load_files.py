import pandas as pd
from sqlalchemy import create_engine

#create connection string to load files in postgre
conn_string = 'postgresql://postgres:64413@localhost/music_database'
db = create_engine(conn_string)
try:
    
    conn = db.connect()

    files = ['album', 'artist', 'customer', 'employee', 'genre', 'invoice', 'invoice_line', 'media_type', 'playlist', 'playlist_track', 'track']
    for file in files:
        df = pd.read_csv(f'D:/Mine/Portfolio/SQL Projects/SQL_Music_Store_Analysis/music store data/{file}.csv')
        df.to_sql(file, con=conn, if_exists='replace', index = False)
    # Close the connection when done
    conn.close()
    print("Connection closed.")
    
except Exception as e:
    print("Error:", e)