import sqlite3
import pandas as pd
from webscraper_script import fetch_data_mvp,years_to_scrap, get_url, all_players_html_page, fetch_all_players_data,fetch_standings

def extract_pipeline():
    def create_connection():
        conn = sqlite3.connect('/nba.db')
        return conn

    def mvp_db():
        df = fetch_data_mvp()
        conn = create_connection()
        df.to_sql("mvp", conn, if_exists='replace', index=False)
        conn.commit()

    mvp_db()

    def all_players_db():
        df = fetch_all_players_data()
        conn = create_connection()
        df.to_sql('all_players_stats', conn, if_exists='replace', index=False)
        conn.commit()

    all_players_db()
    def team_record_db():
        df = fetch_standings()
        conn = create_connection()
        df.to_sql('team_record', conn, if_exists='replace', index=False)
        conn.commit()
    team_record_db()
    def nicknames_db():
        df = pd.read_csv("/Users/cameronlooney/Documents/nicknames.csv")
        conn = create_connection()
        df.to_sql('team_nickname', conn, if_exists='replace', index=False)
        conn.commit()
    nicknames_db()

