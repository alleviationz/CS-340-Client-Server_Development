import pytest
from Capstone_Milestone4.Project_One import AnimalShelter as AAC

# Configure the plotting routines
import pandas as pd


@pytest.fixture(scope="module")
def DataFrame():
    db = AAC("aacuser", "SNHU1234")

    df = pd.DataFrame.from_records(db.read({}))

    return df

def test_DataFrame_Loads(DataFrame):
    assert DataFrame is not None
    assert not DataFrame.empty
    assert len(DataFrame) >= 1

def test_DataFrame_Columns(DataFrame):
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

    for col in columns:
        assert col in DataFrame.columns

def test_drop_id_column(DataFrame):
    df = DataFrame.drop(columns=["_id"])
    assert "_id" not in df.columns


