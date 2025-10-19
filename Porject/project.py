mport os
from prettytable import PrettyTable
import csv
import sys
import time
import re


def main() -> None:
    """
    This a main function that only used to orchestrates the pipeline to run the function written
    I'm trying to build a ETL pipline to extract the data from  csv check the quality ,
    do some transformation & cleaning on the data and check the quality again
    Main Features:

        - File selection and ingestion through CLI
        - Data quality inspection before and after transformation
        - Manual transformation and cleaning routines
        - Optional reporting and runtime metrics
        - Designed as a learning-oriented, extensible ETL framework
    """
    ## reminder: I'm trying to build this ETL tool without using pandas module as it's not mention to CS50P as challange for me
    ## I'm pretty sure it's much much easier to implment this using pandas module!
    print("||==============================================================================||")
    print("||                                                                             ||")
    print("||                                                                             ||")
    print("||                            WELCOME TO THE ETL TOOL ⚙️                         ||")
    print("||                                                                             ||")
    print("||                                                                             ||")
    print("||=============================================================================||")
    ## assign the chosen file name to variable
    chosen_file = terminal_output()
    ## use the checker function to give some info about the given table and it's bad data
    checker(chosen_file)
    ## creating a variable to store the current time of  the process before it starts
    start_time = time.time()
    ## applying transformation & cleaning on the chosen file using our transformation function
    new_file = transformer(chosen_file)
    end_time = time.time()
    ## Calculating the total duration of  transformation process and give it back in reports
    total_dur = end_time - start_time
    while True:
        check_button = input(
        "Now If you press C you will get info about the new table\n"
        "Press C to check: (C) "
    ).lower()

        if check_button == "c":
            break
        else:
            print(" Invalid input! Please press C to continue. ❌")


    checker(new_file)


    while True:
        reports_button = input(
            "Now last but not least if you want generate some report: press the R button (R)"
        ).lower()
        if reports_button == "r":
            break
    reports_generator(total_dur, new_file)
    print("-------------------------------------------")
    print("💖💘💞 ɢᴏᴏᴅʙʏᴇ , sᴇᴇ ʏᴏᴜ sᴏᴏɴ !! 💞💘💖")


def terminal_output():
    ## first terminal table
    menu = PrettyTable()
    menu.field_names = ["#", "Options"] ## column names of the table
    ## adding rows to the table
    ## you can just add more rows if you want by changing the list below
    menu.add_rows([[1, "Show CSV Files"]])
    print(menu)

    while True:
        print("-------------------------------------------------------------------")
        first_option = input("Press 1 to Start the project and see Local Csv Files: 1⃣ '\n' Press 0 Select your own file:  (1,0) ")
        print("-------------------------------------------------------------------")
        option_tuple = ("1" , "0") ## Used tuple in this example so that i don't change it data by mistake : good for constant
        if first_option not in option_tuple:
            print("Usage: pick an option from the menu: ")
            continue
        else:
            break

    if first_option == "1":
        csv_table = PrettyTable()
        ## using os libary to read the CSV files in the current directory and saving it names in a list
        csv_files = [file for file in os.listdir() if file.endswith(".csv")]
        csv_table.field_names = ["#", " LOCAL CSV FILE NAMES"]
        ## iterating through each file exist in the directory and adding index to it :: very cool
        for index, filename in enumerate(csv_files, start=1):
            csv_table.add_row([index, filename])
        print(csv_table)
        while True:
            try:
                file_number = int(
                    input(
                        "You can pick a CSV file from the current directory ( Pick a Number! ):   "
                    )
                )
                if file_number in range(1, index + 1):
                    break
                else:
                    print(f"Please enter a number between 1 and {index}.   ")
            except ValueError:
                print("Invalid input! Please enter a valid number.  ")
        chosen_file = csv_files[file_number - 1]
        return chosen_file
    ## giving the user the option to choose it own file
    if first_option == "0":
        try:
            own_dict = input("⌨ Attach your own file by writing your file full path:  ")
            if own_dict.endswith(".csv") == False:
                raise ValueError
        except ValueError:
            sys.exit("Please Enter a valid CSV file")
        return own_dict


def checker(chosen_file):
   import os
import csv
from prettytable import PrettyTable

def checker(chosen_file):
    """This function handle : reading the data from selected CSV file , show the columns , show some info about the picked CSV"""
    with open(chosen_file, "r", newline="", encoding="utf-8") as file:
        csvfile = csv.DictReader(file)
        header = csvfile.fieldnames
        counter = 0 ## creating a counter for each row that iterate through the Dict reader : detect how many rows in the table
        null_counts = {col: 0 for col in header} # creating a null counter dict : the key is : col and value are the count of null
        spaces_counts = {col: 0 for col in header} # creating a spaces counter : the key is : col and the value are the elemnts that has spaaces
        total_null = 0
        total_spaces = 0

        size = os.path.getsize(chosen_file)
        for row in csvfile:
            counter += 1
            ## this process is for the whole table to get total empty elements and extra spaces in each of the element
            for col, value in row.items():
                if value is None or value == "":
                    null_counts[col] += 1
                    total_null += 1
                elif value.strip() != value:
                    spaces_counts[col] += 1
                    total_spaces += 1

        table = PrettyTable()
        table.field_names = ("#", "Column Names", "Nulls Count ", "Spaces Count")
        for inx, col in enumerate(header, start=1):
            table.add_row([inx, col, null_counts[col], spaces_counts[col]])
        print("|----------------------------------------------------------------------- |")
        print("|                  Information about given CSV                           |")
        print("|----------------------------------------------------------------------- |")
        print(f"|☛ This Table Contain: {len(header)}  COLUMNS ☚                                    |")
        print(f"|☛ This Table Contain : {counter}  ROWS ☚                                  |")
        print(f"|☛ This Table Contain : {total_null}  NULL / Empty Values ☚                |")
        print(f"|☛ This Table Contain : {total_spaces} extra Space in the string ☚       |")
        print(f"|☛ This file size : {round(size / 1024 , ndigits= 3)}  KB ☚              |")
        print("|----------------------------------------------------------------------- |")
        print(table)





def transformer(chosen_file):
    """This function transform the data input after reading the file and load it into a new csv"""

    transformation_button = input(
        "Now If You Press T : The data will be Transformed (cleaned) and loaded into a new csv: Τ "
    ).lower()
    if transformation_button == "t":
        ## opening the chosen file to iterate through , changing it values and writing it to a new csv
        with open(chosen_file, "r", newline="", encoding="utf-8") as file, open(
            chosen_file + "_new.csv", "w", newline="", encoding="utf-8"
        ) as new_file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            writer = csv.DictWriter(new_file, fieldnames=header)
            writer.writeheader()
            ## iterating through each row of the dict reader
            for row in reader:
                ## assigning each key , value in the row dict using the items dict method
                for col, value in row.items():
                    if value is None or value == "":
                        row[col] = "N/A"  ## changing the empty or null value to N/A
                    elif value.strip() != value:
                        row[col] = value.strip() ## removing the extra spaces from each element at the start and end of it

                writer.writerow(row) ## writing data to the new csv file after changing it
        print("--------------------------------------------------------------------------------------------")
        print("The data has been transformed & loaded to a new file sucessfully             ✅✅ ")

        return chosen_file + "_new.csv"

    else:
        sys.exit("Invalid Input : Run The ETL tool Again                           ❌❌ ")



def reports_generator(total_time, csv_file):
    """This function generate some reports from the numeric columns as insights for the user"""

    print("|----------------------------------------------------------------------------------------------------|")
    print("|                                   📈 Reported generated from CSV 📈                               |")
    print("|----------------------------------------------------------------------------------------------------|")
    print("---------------------------------------------------------------------------------------------------------------------")
    print(
        f"This Process Took the following time in transforming & loading the data: {round(total_time , ndigits= 3)} seconds 🕐🕐      "
    )
    print("---------------------------------------------------------------------------------------------------------------------")

    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        ## creating a dict with KEY as str and dict as it VALUE so it add each column name as key , to it's aggregation function as value
        ## we create muliplte key and values for each column key so that each column is assoicated with diffrent aggregation (sum ,count , min , max)
        columns_stats = {
            field: {"sum": 0, "count": 0, "min": None, "max": None}
            for field in header
        }

        for row in reader:
            ## this process took me hours to really get it done , i'm sure there is a better solution :))
            for key, value in row.items():
                try:
                    number = float(value) ## trying to convert each element to a float and exclude the not changing one : like str
                    columns_stats[key]["sum"] += number
                    columns_stats[key]["count"] += 1
                    if (
                        columns_stats[key]["min"] is None
                        or number < columns_stats[key]["min"]
                    ):
                        columns_stats[key]["min"] = number
                    if (
                        columns_stats[key]["max"] is None
                        or number > columns_stats[key]["max"]
                    ):
                        columns_stats[key]["max"] = number

                except ValueError:
                    pass

    print("------------------------------------------------------------------------------------------------------")
    print(" AGGREGATION OF NUMERIC COLUMNS:📋")

    for col, total in columns_stats.items():

        if re.search(r"(_dt|_date|date|_id|_key|id|key)", col, re.IGNORECASE):
            continue

        if total["count"] == 0:
            continue

        table = PrettyTable()
        table.field_names = [
            "Numeric Column Names",
            "Total of each column",
            "Total number of rows",
            "Minimum Value of the column",
            "Maximum Value of the column",
        ]
        table.add_row([col, total["sum"], total["count"], total["min"], total["max"]])
        print(table)

if __name__ == "__main__":
    main()
