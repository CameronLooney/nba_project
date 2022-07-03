from data_extraction.webscraper_database import extract_pipeline
from data_loading.load_data_db import load_pipeline
from data_transformation.cleaning import transform_pipeline

def data_pipeline():
    stages = 0
    try:
        extract_pipeline()
        print("Data extraction successful")
        stages += 1
    except:
        print("Error in extracting data")
    try:
        transform_pipeline()
        print("Data transformation successful")
        stages += 1
    except:
        print("Error in transforming data")
    try:
        load_pipeline()
        print("Data loading successful")
        stages += 1
    except:
        print("Error in loading data")
    if stages == 3:
        print("Data pipeline successful")
    else:
        print("Data pipeline failed")
data_pipeline()


