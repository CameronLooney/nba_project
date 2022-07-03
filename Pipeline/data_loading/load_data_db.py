
from Pipeline.data_transformation.cleaning import clean_pipeline
from sqlalchemy import create_engine
def load_pipeline():
    df = clean_pipeline()
    def to_postgres(df, pg_user, pg_password, pg_host, pg_database,pg_port,pg_tablename):
        try:
            engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(pg_user, pg_password, pg_host,pg_port, pg_database))
            df.to_sql(pg_tablename, engine)
        except:
            print("Error in writing to postgres")

    to_postgres(df,"cameron", "root", "localhost", "nba", 5432,  "nba_data")

