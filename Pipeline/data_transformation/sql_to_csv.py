# sqlite3 -header -csv /Users/cameronlooney/PyCharm/nba/nba.db "select * from mvp;" > /Users/cameronlooney/Documents/mvp.csv

import os
def sql_tables_to_csv():
    check =0
    try:
        os.system("sqlite3 -header -csv /Users/cameronlooney/PyCharm/nba/nba.db \"select * from mvp;\" > /Users/cameronlooney/Documents/mvp.csv")
        print("mvp.csv created successfully")
        check +=1
    except:
        print("mvp.csv creation failed")
    try:
        os.system("sqlite3 -header -csv /Users/cameronlooney/PyCharm/nba/nba.db \"select * from all_players_stats;\" > /Users/cameronlooney/Documents/all_players_stats.csv")
        print("all_players_stats.csv created successfully")
        check +=1
    except:
        print("all_players_stats.csv creation failed")
    try:
        os.system("sqlite3 -header -csv /Users/cameronlooney/PyCharm/nba/nba.db \"select * from team_record;\" > /Users/cameronlooney/Documents/team_record.csv")
        print("team_record.csv created successfully")
        check +=1
    except:
        print("team_record.csv creation failed")
    if check == 3:
        print("All csv files created successfully")
    else:
        print("One or more csv files failed to create")



sql_tables_to_csv()