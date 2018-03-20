#importing dependencies
import pandas as pd
import csv
import os 
import datetime 

#lists to hold new formated info
emp_ids=[]
first_name=[]
last_name=[]
dob=[]
ssn=[]
state=[]
#state abbreviation dictionary for formatting in upcoming loop
states_abv = {"Alabama": "AL","Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",  "California": "CA",
    "Colorado": "CO",    "Connecticut": "CT",    "Delaware": "DE",    "Florida": "FL",    "Georgia": "GA",
    "Hawaii": "HI",    "Idaho": "ID",    "Illinois": "IL",    "Indiana": "IN",    "Iowa": "IA",    "Kansas": "KS",
    "Kentucky": "KY",    "Louisiana": "LA",    "Maine": "ME",    "Maryland": "MD",    "Massachusetts": "MA",    "Michigan": "MI",
    "Minnesota": "MN",    "Mississippi": "MS",    "Missouri": "MO",    "Montana": "MT",    "Nebraska": "NE",    "Nevada": "NV",
    "New Hampshire": "NH",    "New Jersey": "NJ",    "New Mexico": "NM",    "New York": "NY",    "North Carolina": "NC",
    "North Dakota": "ND",    "Ohio": "OH",    "Oklahoma": "OK",    "Oregon": "OR",    "Pennsylvania": "PA",    "Rhode Island": "RI",
    "South Carolina": "SC",    "South Dakota": "SD",    "Tennessee": "TN",    "Texas": "TX",    "Utah": "UT",    "Vermont": "VT",
    "Virginia": "VA",    "Washington": "WA",    "West Virginia": "WV",    "Wisconsin": "WI",    "Wyoming": "WY",}
    #creating a file path for first file
filepath = os.path.join("../raw_data/employee_data1.csv")
#reading through both employee csv files and appending formated data to dictionary
with open(filepath)as employee_data:
    reader= csv.DictReader(employee_data)
    for row in reader:
         #Grab emp_ids and store it into a list
         emp_ids= emp_ids+[row["Emp ID"]]
         # Take name, split them, and store them as variable
         split_name = row["Name"].split(" ")
         # Then save first and last name in separate lists
         first_name = first_name + [split_name[0]]
         last_name = last_name + [split_name[1]]
         # Grab DOB and reformat it
         reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
         reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")
         # Then store it into a list
         dob = dob + [reformatted_dob]
         # Grab SSN and reformat it
         split_ssn = list(row["SSN"])
         split_ssn[0:3] = ("*", "*", "*")
         split_ssn[4:6] = ("*", "*")
         joined_ssn = "".join(split_ssn)
         # Then store it into a list
         ssn = ssn + [joined_ssn]
         # Grab the states and use the dictionary to find the replacement
         em_statesabv = states_abv[row['State']]
         # Then store the abbreviation into a list
         state = state + [em_statesabv]
#creating a file path for the second csvfiel
filepath2 = os.path.join("../raw_data/employee_data2.csv")
#reading through both employee csv files and appending formated data to dictionary
with open(filepath2)as employee_data:
    reader= csv.DictReader(employee_data)
    for row in reader:
            # Grab emp_ids and store it into a list
            emp_ids= emp_ids+[row["Emp ID"]]
            # Take name, split them, and store them as variable
            split_name = row["Name"].split(" ")
            # Then save first and last name in separate lists
            first_name = first_name + [split_name[0]]
            last_name = last_name + [split_name[1]]   
            # Grab DOB and reformat it
            reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
            reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")
            # Then store it into a list
            dob = dob + [reformatted_dob]
            # Grab SSN and reformat it
            split_ssn = list(row["SSN"])
            split_ssn[0:3] = ("*", "*", "*")
            split_ssn[4:6] = ("*", "*")
            joined_ssn = "".join(split_ssn)
            # Then store it into a list
            ssn = ssn + [joined_ssn]
            # Grab the states and use the dictionary to find the replacement
            em_statesabv = states_abv[row['State']]
            # Then store the abbreviation into a list
            state = state + [em_statesabv]
# Zip all of the data from both csv files together
new_employee_data = zip(emp_ids, first_name, last_name, dob, ssn, state)
#creating a variable for csv file
employee_output= "employee_records.csv"
#creating the csv file
with open (employee_output,"w", newline="")as csvfile:
    csvwriter= csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    for row in new_employee_data:
        csvwriter.writerow(row)