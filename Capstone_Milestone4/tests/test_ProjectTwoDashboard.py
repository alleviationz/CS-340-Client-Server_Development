import pytest
import pandas as pd

from src.Project_One import AnimalShelter

# Constrain this API object and data variable to the testing suite
@pytest.fixture(scope="module")

# Setup API object and load data
def DataFrame():
    db = AnimalShelter()
    df = pd.DataFrame.from_records(db.read({}))
    return df

# Assert that we did in fact receive some data
def test_DataFrame_Loads(DataFrame):
    assert DataFrame is not None
    assert not DataFrame.empty
    assert len(DataFrame) >= 1

def test_DataFrame_Columns(DataFrame):
    # All expected columns
    columns = [
        "_id",
        "age_upon_outcome",
        "animal_id",
        "animal_type",
        "breed",
        "color",
        "date_of_birth",
        "datetime",
        "monthyear",
        "name",
        "outcome_subtype",
        "outcome_type",
        "sex_upon_outcome",
        "location_lat",
        "location_long",
        "age_upon_outcome_in_weeks"
    ]

    # Assert that each column is present in the loaded data
    for col in columns:
        assert col in DataFrame.columns

# Ensure dropping the id column works as expected
def test_drop_id_column(DataFrame):
    df = DataFrame.drop(columns=["_id"])
    assert "_id" not in df.columns


