import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self):
        # Initializing the MongoClient
        # Initialize Connection
        try:
            self.client = MongoClient(os.getenv("ATLAS_URI"))
            self.database = self.client["AAC"]
            self.collection = self.database["animals"]

        # catch all exceptions
        except Exception as e:
            print(f"Error connecting to database. Error: {e}")

# Create method to insert into database collection (AAC.animals in this case)
    def create(self, insert_data) -> bool:
        # if data, insert into database and return True
        if (insert_data != None):
            try:
                self.collection.insert_one(insert_data)  # data should be dictionary
                return True
            # if there is no data, notify, and return False
            except:
                print("No value was given to insert in database")
                return False

# Read method to general query (AAC.animals in this case)
    def read(self, query) -> list:
        # check if empty data passed
        if (query == None):
            return []
        
        # query for the animal and return each dict in a list
        # will return empty list if animal/s not found
        posts = list(self.collection.find(query))
        # veryify at least 1 result, otherwise return empty list
        if (len(posts) == 0):
            print("No results found.")
            return []
        
        return posts
    
# Update method to update database documents in collection (AAC.animals)
    def update(self, query, update_data) -> int:
        # check if empty data passed
        if (query == None):
            return -1
        
        # call pyMongo update passing the query object, update by setting the update_data, saving the results
        results = self.collection.update_many(query, {"$set": update_data})
        # return the saved results
        return results.modified_count
        
# Delete method to remove a document in collection (AAC.animals)
    def delete(self, query) -> int:
        # check if empty data passed
        if (query == None):
            return -1
        
        # call pyMongo delete, passing in query and saving results
        results = self.collection.delete_many(query)
        # return the saved results
        return results.deleted_count