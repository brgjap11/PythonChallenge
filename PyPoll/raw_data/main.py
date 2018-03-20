# dependencies
import csv 
import os
import pandas as pd
#creating new lists for the csv files to be populated
voter_id=[]
candidate= []
county=[]
#creating a file path that the user will input
filepath = os.path.join("../raw_data/election_data_1.csv")
#reading through both election csv files and adding all data together
with open(filepath, newline="")as csvfile:
    filereader= csv.reader(csvfile, delimiter =",")
    next(filereader, None)
    for row in filereader:
        voter_id.append(row[0])
        candidate.append(row[1])
        county.append(row[2])

filepath2=os.path.join("../raw_data/election_data_2.csv")
with open(filepath2, newline="")as csvfile:
    filereader2= csv.reader(csvfile, delimiter =",")
    next(filereader2, None)
    for row in filereader2:
        voter_id.append(row[0])
        candidate.append(row[1])
        county.append(row[2])
#creating a dataframe to view the merged files to ensure all data looks correct
election_results=pd.DataFrame({'Voter_id':voter_id,'Candidate':candidate,'County':county})
#calculations for the results dataframe
gb_candidate= election_results.groupby("Candidate")
#The total number of votes cast
total_votes=len(election_results["Voter_id"])
#The total number of votes each candidate won
candidates_total=gb_candidate["Voter_id"].count()
#The percentage of votes each candidate won
percentage_of_votes= (candidates_total/total_votes)*100
#put results into a new dataframe & format results
final_results = pd.DataFrame({"Percentage":percentage_of_votes,"Total Vote":candidates_total})
final_results=final_results.reset_index()
final_results=final_results.sort_values("Total Vote", ascending=False)
final_results["Percentage"]= final_results["Percentage"].map("{:,.2f}%".format)
final_results["Total Vote"]= final_results["Total Vote"].map("{:,.0f}".format)
#The winner of the election based on popular vote.
winner= final_results.iloc[0,0]
#creating a csv for the results & printing results to the terminal
output_file="Election_Analysis.txt"
with open(output_file, 'w')as txt_file:
    results_output =(
    f"\n\nElection Results\n"
    f"-----------------------------------------\n"
    f"Winner : {winner}\n"
    f"-----------------------------------------\n"
    f"{final_results}\n"
    f"------------------------------------------\n")
    print(results_output, end="")

    txt_file.write(results_output)