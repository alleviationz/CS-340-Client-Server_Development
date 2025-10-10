import pytest
from Capstone_Milestone4.Project_One import AnimalShelter as AAC

# fixutre to create AnimalShelter specifically within this module
@pytest.fixture(scope="module")
def Client():
    return AAC("aacuser", "SNHU1234")

@pytest.fixture(scope="module")
def test_animal():
    # force-set the _id value to a known value to allow comparison
    test_animal = ({
    "_id": "testing123!@#",
    "rec_num": "1",
    "age_upon_outcome": "3 years",
    "animal_id": "testing123123",
    "animal_type": "Cat",
    "breed": "Domestic Shorthair Mix",
    "color": "Black/White",
    "date_of_birth": "-1",
    "datetime": "2017-04-11 09:00:00",
    "monthyear": "2017-04-11T09:00:00",
    "name": "",
    "outcome_subtype": "SCRP",
    "outcome_type": "Transfer",
    "sex_upon_outcome": "Neutered Male",
    "location_lat": 30.5066578739455,
    "location_long": -97.3408780722188,
    "age_upon_outcome_in_weeks": 156.767857142857
    })

    return test_animal

# test_example.py
def test_AAC_Client_Setup(Client):
    assert Client.database != None
    assert Client.collection != None
    assert Client.collection.name == "collection"
    assert Client.collection.database.name == "AAC"

def test_AAC_create(Client, test_animal):

    Client.create(test_animal)

    assert (Client.collection.find_one({"_id": "testing123!@#"}) == test_animal)

def test_AAC_read(Client, test_animal):
    assert Client.read({}) != []
    assert len(Client.read({})) >= 1
    assert Client.read({"_id": "testing123!@#"}) == [test_animal]

def test_AAC_update(Client):
    assert Client.update({"_id": "testing123!@#"}, {"name": "Fido"}) >= 1

# read the object again and ensure the change occured
def test_AAC_read_after_update(Client):
    assert Client.read({}) != []
    assert len(Client.read({})) >= 1
    assert Client.read({"_id": "testing123!@#"})[0]["name"] == "Fido"

def test_AAC_delete(Client):
    assert Client.delete({"_id": "testing123!@#"}) == 1

# read the object again and ensure the deletion occured
def test_AAC_read_after_delete(Client):
    assert Client.read({"_id": "testing123!@#"}) == []