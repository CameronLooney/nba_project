from webscraper_database import create_connection,create_cursor

conn = create_connection()
curr = create_cursor(conn)
curr.execute("SELECT * FROM mvp")
rows = curr.fetchall()

for row in rows:
    print(row)