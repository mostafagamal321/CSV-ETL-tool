import pytest
import os
import csv
import builtins
from project import checker , reports_generator , transformer


def create_sample_csv(file_path):
    """this function creates a dummpy csv and write some data into it to test my output """
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", "25", "New York"])
        writer.writerow(["Bob", "", " Los Angeles "])
        writer.writerow(["", "30", "Chicago"])


def test_checker_runs(tmp_path):
    """this function takes the dummpy csv that created above and make sure it does exists"""
    csv_file = tmp_path / "test.csv"
    create_sample_csv(csv_file)  
    checker(str(csv_file))  
    assert os.path.exists(csv_file)

def create_numeric_csv(file_path):
    """ This function create a sample csv file to use it in our test"""
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "value1", "value2"])
        writer.writerow([1, 10, 100])
        writer.writerow([2, 20, 200])
        writer.writerow([3, 30, 300])

def test_reports_generator_runs(tmp_path):
    """now checking the function calling is done without any issue and the file is still exists"""
    csv_file = tmp_path / "numeric.csv"
    create_numeric_csv(csv_file)

    
    reports_generator(2.345, str(csv_file))

    
    assert os.path.exists(csv_file)

def create_sample_csv(file_path):
    """this function create a sample csv file to use in our unit test """
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", "25", " New York "])
        writer.writerow(["Bob", "", "Los Angeles"])
        writer.writerow(["", "30", "Chicago"])


def test_transformer_creates_new_csv(tmp_path):
    """tihs function take the dummpy csv file and use it in the unit test"""
   
    csv_file = tmp_path / "test.csv"
    create_sample_csv(csv_file)

    inputs = iter(["t"])
    def mock_input(_):  ## a dummpy input or call it a internal input to use to test the function
        return next(inputs)
    """So the idea for mock input is that to test our function we can't ask the user for input because not how pytest work
        so we create what called mock input just to pretends that there is a actual input """
    builtins.input = mock_input

    
    new_file_path = transformer(str(csv_file))

  
    assert os.path.exists(new_file_path)

    
    with open(new_file_path, "r") as f:
        ## Now we are opening the transformed csv and checking that rows actually changened 
        reader = csv.DictReader(f)
        rows = list(reader)

        assert rows[0]["Name"] == "Alice"
        assert rows[0]["Age"] == "25"
        assert rows[0]["City"] == "New York" 

        
        assert rows[1]["Name"] == "Bob"
        assert rows[1]["Age"] == "N/A"        
        assert rows[1]["City"] == "Los Angeles"

        
        assert rows[2]["Name"] == "N/A"
        assert rows[2]["Age"] == "30"
        assert rows[2]["City"] == "Chicago"


def test_transformer_invalid_input(tmp_path):
   
    csv_file = tmp_path / "test.csv"
    create_sample_csv(csv_file)

    
    inputs = iter(["x"])
    def mock_input(_):
        return next(inputs)

    builtins.input = mock_input

    
    with pytest.raises(SystemExit): ## checking user invalid input 
        transformer(str(csv_file))
