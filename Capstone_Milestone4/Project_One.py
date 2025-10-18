#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        # Initializing the MongoClient
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        #
        # Connection Variables
        #
        HOST = "localhost"
        PORT = 27017
        DB = "AAC"
        COL = "animals"
        #
        # Initialize Connection
        #
        self.client = MongoClient(HOST, PORT, username=user, password=password)
        self.database = self.client["%s" % (DB)]
        self.collection = self.database["%s" % (COL)]

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


# Module testing
# # create an AnimalShelter object to handle CRUD functions
# aac = AnimalShelter("aacuser", "SNHU1234");

# # test the create function with the test animal
# print(aac.create({
#   "rec_num": "1",
#   "age_upon_outcome": "3 years",
#   "animal_id": "B746874",
#   "animal_type": "Cat",
#   "breed": "Domestic Shorthair Mix",
#   "color": "Black/White",
#   "date_of_birth": "-1",
#   "datetime": "2017-04-11 09:00:00",
#   "monthyear": "2017-04-11T09:00:00",
#   "name": "",
#   "outcome_subtype": "SCRP",
#  "outcome_type": "Transfer",
#   "sex_upon_outcome": "Neutered Male",
#   "location_lat": 30.5066578739455,
#   "location_long": -97.3408780722188,
#   "age_upon_outcome_in_weeks": 156.767857142857
# }));

# # test the read function with the test animal
# testAnimal = aac.read({
#   "rec_num": "1",
#   "age_upon_outcome": "3 years",
#   "animal_id": "B746874",
#   "animal_type": "Cat",
#   "breed": "Domestic Shorthair Mix",
#   "color": "Black/White",
#   "date_of_birth": "-1",
#   "datetime": "2017-04-11 09:00:00",
#   "monthyear": "2017-04-11T09:00:00",
#   "name": "",
#   "outcome_subtype": "SCRP",
#  "outcome_type": "Transfer",
#   "sex_upon_outcome": "Neutered Male",
#   "location_lat": 30.5066578739455,
#   "location_long": -97.3408780722188,
#   "age_upon_outcome_in_weeks": 156.767857142857
# });

# # call update with animal_id "B746874" and an update query to change "animal_type" to "Dog"
# aac.update({"animal_id" : "B746874"}, {"animal_type": "Dog"})

# # read the object again and ensure the change occured
# aac.read({"date_of_birth": "-1"})

# # delete the testAnimal by ObjectId
# aac.delete({"$and" : [{"animal_type" : "Dog"}, {"date_of_birth" : "-1"}]})

# # try to read the object by ObjectId that was deleted
# aac.read({
#   "rec_num": "1",
#   "age_upon_outcome": "3 years",
#   "animal_id": "B746874",
#   "animal_type": "Cat",
#   "breed": "Domestic Shorthair Mix",
#   "color": "Black/White",
#   "date_of_birth": "-1",
#   "datetime": "2017-04-11 09:00:00",
#   "monthyear": "2017-04-11T09:00:00",
#   "name": "",
#   "outcome_subtype": "SCRP",
#  "outcome_type": "Transfer",
#   "sex_upon_outcome": "Neutered Male",
#   "location_lat": 30.5066578739455,
#   "location_long": -97.3408780722188,
#   "age_upon_outcome_in_weeks": 156.767857142857
# })