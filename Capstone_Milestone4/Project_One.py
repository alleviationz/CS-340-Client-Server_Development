import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

class AnimalShelter():
    # Client object allowing CRUD operations for the animals collection in the AAC database (MongoAtlas)
    def __init__(self):
        # Initializing the MongoClient and Atlas connection
        try:
            self.client = MongoClient(os.getenv("ATLAS_URI"))
            self.database = self.client["AAC"]
            self.collection = self.database["animals"]

        # catch all exceptions
        except Exception as e:
            print(f"Error connecting to database. Error: {e}")

# Create method to insert a JSON animal record into the database collection (AAC.animals), returning True/False depicting success/failure
    def create(self, insert_data) -> bool:
        # if given empty an empty data record, notify the user and return False
        if (insert_data == None):
            print("No value was given to insert in database")
            return False
        
        # if the data isn't null, attempt to insert it into the database and return True
        try:
            self.collection.insert_one(insert_data)
            return True
        
        # if the insertion fails, print the error and return False
        except Exception as e:
            print(f"Error inserting data with create: {e}")
            return False
            

# Read all data records from the collection (AAC.animals), returns retrieved documents as a list
    def read(self, query) -> list:
        # if the query is empty, return an empty list
        if (query == None):
            return []
        
        # query the collection for records, will return empty list if animal/s not found
        try:
            posts = list(self.collection.find(query))
        except Exception as e:
            print(f"Error reading collection using query {query}: {e}")

        # verify at least 1 result was returned, otherwise return empty list
        if (len(posts) == 0):
            print("No results found.")
            return []
        
        return posts
    
# Update database documents in the collection (AAC.animals), returns the number of documents affected or -1 upon failure
    def update(self, query, update_data) -> int:
        # return -1 if empty data or an indifferent change is passed
        if (query == None or update_data == None):
            return -1
        
        # call pyMongo update passing the query, update by setting the update_data, saving the results
        try:
            results = self.collection.update_many(query, {"$set": update_data})
        except Exception as e:
            print(f"Error updating collection using the query {query}: {e}")

        # return the number of documents changed
        return results.modified_count
        
# Delete method to remove a document in the collection (AAC.animals), returns the number of documents deleted or -1 upon failure
    def delete(self, query) -> int:
        # check if an empty query passed
        if (query == None):
            return -1
        
        # call pyMongo delete, passing in query and saving results
        try:
            results = self.collection.delete_many(query)
        except Exception as e:
            print(f"Error deleting documents from the collection using query {query}: {e}")

        # return the number of documents deleted
        return results.deleted_count