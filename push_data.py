import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()
uri=os.getenv("MONGO_DB_URL")
# print(uri)

import certifi
ca= certifi.where()
from pymongo import MongoClient
import numpy as np
import pandas as pd
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtractor:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def csv_to_json(self, csv_file_path):
        try:
            df = pd.read_csv(csv_file_path)
            df.reset_index(drop=True, inplace=True)
            # Convert DataFrame to JSON records format
            json_data = df.to_dict(orient='records')
            logging.info(f"Converted csv to json. Sample record: {json_data[0] if json_data else 'No data'}")
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def push_data(self, records,database_name, collection_name):
        try:
            self.database_name = database_name
            self.collection_name = collection_name
            self.mongo_client = MongoClient(uri, tlsCAFile=ca)
            self.db = self.mongo_client[database_name]
            self.collection = self.db[collection_name]
            self.collection.insert_many(records)
            logging.info(f"Inserted {len(records)} documents into {database_name}.{collection_name}")
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

if __name__ == "__main__":
    try:
        # Check if MongoDB URI is available
        if uri is None:
            print("MONGO_DB_URL not found in .env file")
            sys.exit(1)
            
        data_extractor = NetworkDataExtractor()
        # Fixed the typo in the file name
        records = data_extractor.csv_to_json("Network_Data/phisingData.csv")
        no_of_records=data_extractor.push_data(records, "network_security", "network_security_data")
        print(no_of_records)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e