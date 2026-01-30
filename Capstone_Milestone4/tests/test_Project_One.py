import pytest

from src.Project_One import AnimalShelter

# Constrain the API object and the Client to the testing suite
@pytest.fixture(scope="module")
# Initialize API object
def Client():
    return AnimalShelter()

# Initialize an object with expected format to compare (value will persist while test suite is active)
@pytest.fixture(scope="module")
def test_animal():
    # Force the _id value to a known value to allow comparison
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

# Ensure the client initialized correctly
def test_AAC_Client_Setup(Client):
    # Non-Empty
    assert Client.database != None
    assert Client.collection != None

    # Validate actual values
    assert Client.collection.name == "animals"
    assert Client.collection.database.name == "AAC"

# Test the API's create method using the mocked test_animal values
def test_AAC_create(Client, test_animal):
    # Create using the test animal_values
    Client.create(test_animal)

    # Ensure the document exists
    assert (Client.collection.find_one({"_id": "testing123!@#"}) == test_animal)

# Test the API's read method using the mocked test_animal values
def test_AAC_read(Client, test_animal):
    # Ensure data was received
    assert Client.read({}) != []
    assert len(Client.read({})) >= 1

    # Validate explicit value read
    assert Client.read({"_id": "testing123!@#"}) == [test_animal]

# Test the API's update method using the mocked test_animal values, returns modified document count
def test_AAC_update(Client):
    # Ensure the function returns the correct number of documents altered
    assert Client.update({"_id": "testing123!@#"}, {"name": "Fido"}) == 1
    first_index = 0

    # Ensure the change was made
    assert Client.read({"_id": "testing123!@#"})[first_index]["name"] == "Fido"

# Test the API's delete method, returns number of documents deleted
def test_AAC_delete(Client):
    # Ensure the function returns the correct number of documents altered
    assert Client.delete({"_id": "testing123!@#"}) == 1

    # Ensure the deletion was made
    assert Client.read({"_id": "testing123!@#"}) == []