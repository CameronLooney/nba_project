# team records
# drop Division
# games behind if they are first you get a weird character, change this to 0
# drop **
# drop numbers in 2022


import sqlite3



import pandas as pd
def transform_pipeline():
    def create_connection():
        conn = sqlite3.connect('/nba.db')
        return conn

    def clean_team_data():
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM team_record", conn)
        df = df[~df["Team"].str.contains("Division")]
        df["Team"] = df["Team"].str.replace("*", "",regex = False)
        df["GB"] = df["GB"].str.replace("—", "0",regex = False)
        df["Team"]= df["Team"].str.split('\\xa0').str[0]


        return df

    def clean_mvp_data():
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM mvp", conn)
        df = df[["Player", "Year", "Pts Won", "Pts Max", "Share"]]
        return df

    def player_total_season_stats(df):
        if df.shape[0] ==1:
            return df
        else:
            row = df[df["Tm"]=="TOT"]
            row["Tm"] = df.iloc[-1,:]["Tm"]
            return row
    def clean_player_data():
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM all_players_stats", conn)
        df = df.drop('Rk',axis =  1)
        df["Player"] = df["Player"].str.replace("*", "",regex = False)
        df = df.groupby(["Player", "Year"]).apply(player_total_season_stats)
        df.index = df.index.droplevel()
        df.index = df.index.droplevel()

        return df

    def get_team_nickname():
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM team_nickname", conn)
        team_nickname_dict = dict(zip(df.Abbreviation, df.Name))
        return team_nickname_dict


    def combine_data():
        player_data = clean_player_data()
        mvp_data = clean_mvp_data()
        team_nickname_dict = get_team_nickname()
        team_data = clean_team_data()
        df = player_data.merge(mvp_data, on=["Player", "Year"], how="outer")
        df[["Pts Won","Pts Max","Share"]]= df[["Pts Won","Pts Max","Share"]].fillna(0)
        df["Team"] = df["Tm"].map(team_nickname_dict)
        combine_with_teams = df.merge(team_data, on=["Team", "Year"], how="outer")
        return combine_with_teams

    def fix_datatypes(df):
        df = df.apply(pd.to_numeric, errors='ignore')
        return df

    df = combine_data()
    df = fix_datatypes(df)
    return df



