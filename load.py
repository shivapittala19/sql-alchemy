import csv
from sqlalchemy.orm import sessionmaker
from models import Match, Delivery, Umpire,engine
    
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to load data from a CSV file into the database
def load_csv_data_to_db(csv_path, model_class, sample_session):
    """ load data"""
    with open(csv_path, 'r',encoding='latin-1') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data = {key.strip(): value for key, value in row.items()}
            sample_session.add(model_class(**data))
    sample_session.commit()

matches_csv_path = '/var/lib/postgresql/matches.csv'
umpires_csv_path = '/home/shivapittala/Desktop/IPL_dataset_analysis/umpires.csv'
deliveries_csv_path = '/var/lib/postgresql/deliveries.csv'

load_csv_data_to_db(matches_csv_path, Match, session)
load_csv_data_to_db(umpires_csv_path, Umpire, session)
load_csv_data_to_db(deliveries_csv_path, Delivery, session)

# Close the session
session.close()