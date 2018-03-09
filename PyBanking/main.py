<<<<<<< HEAD


import pandas as pd
import numpy as np
import os
import csv

# ask user to input all of the files names into the code
print("Please make sure that your input files are present in the Instructions folder")
# ask user to input all of the files names into the code
User_Analysis_File = os.path.join( "Instructions", input ("Please enter the input filename: \n"))

#Creading new lists for formatting data from csv imports
Date= []
Revenue= []
Change_in_Revenue = []
#Defining needed variables
Months = 0
TotalRevenue = 0
RevenueChangeSum = 0
Counter = 0
x=0
Revenue_Change_Total = 0


#importing  csv file 
with open(User_Analysis_File,newline="")as csvfile:
    csvreader= csv.reader(csvfile, delimiter =",")
    
    next(csvreader, None)
    
    for row in csvreader:
        Date.append(row[0])
        Revenue.append(row[1])
        
        TotalRevenue= TotalRevenue + float(row[1])
        Months = len(Date)

for i in range(Months-1):
    Change_in_Revenue.append(float(Revenue[i+1])- float(Revenue[i]))

# Calculating the maximum Revenue Change
Max_Revenue_Change = max(Change_in_Revenue)

# Calculating the minimum Revenue Change
Min_Revenue_Change = min(Change_in_Revenue)

# Calculating the revenue change length 
Revenue_Change_len = len(Change_in_Revenue)

# Calculating the revenue change total 
for i in range (Revenue_Change_len):
    Revenue_Change_Total = Revenue_Change_Total + Change_in_Revenue [i]


# Calculating the average revenue change
Average_Revenue_Change = Revenue_Change_Total/Revenue_Change_len
    
# Calculating the Date for the Minimum Revenue Change   
for i in range (Revenue_Change_len):
    if (Change_in_Revenue[i] == Min_Revenue_Change):
        Min_Revenue_Change_Date = Date[i+1]

# Calculating the Date for the Maximum Revenue Change
for i in range (Revenue_Change_len):
    if (Change_in_Revenue[i] == Max_Revenue_Change):
        Max_Revenue_Change_Date = Date[i+1]
        

# Print calculations to terminal and export to txt file
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: "+ str(Months))
print ("Total Revenue: "+ "$" + str(TotalRevenue))
print ("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
print ("Greatest Increase in Revenue: " + str(Max_Revenue_Change_Date) + "  $"+ str(Max_Revenue_Change))
print ("Greatest Decrease in Revenue: " + str(Min_Revenue_Change_Date) + "  $"+ str(Min_Revenue_Change))

output_file= open("financial_analysis.txt","w+")
output_file.write("Financial Analysis")
output_file.write("----------------------------")
output_file.write("Total Months: "+ str(Months)
output_file.write("Total Revenue: " + "  $" + str(TotalRevenue))
output_file.write("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
output_file.write("Greatest Increase in Revenue: " + str(Max_Revenue_Change_Date) + "  $"+ str(Max_Revenue_Change))
output_file.write("Greatest Decrease in Revenue: " + str(Min_Revenue_Change_Date) + "  $"+ str(Min_Revenue_Change))
=======


import pandas as pd
import numpy as np
import os
import csv

# ask user to input all of the files names into the code
print("Please make sure that your input files are present in the Instructions folder")
# ask user to input all of the files names into the code
User_Analysis_File = os.path.join( "Instructions", input ("Please enter the input filename: \n"))

#Creading new lists for formatting data from csv imports
Date= []
Revenue= []
Change_in_Revenue = []
#Defining needed variables
Months = 0
TotalRevenue = 0
RevenueChangeSum = 0
Counter = 0
x=0
Revenue_Change_Total = 0


#importing  csv file 
with open(User_Analysis_File,newline="")as csvfile:
    csvreader= csv.reader(csvfile, delimiter =",")
    
    next(csvreader, None)
    
    for row in csvreader:
        Date.append(row[0])
        Revenue.append(row[1])
        
        TotalRevenue= TotalRevenue + float(row[1])
        Months = len(Date)

for i in range(Months-1):
    Change_in_Revenue.append(float(Revenue[i+1])- float(Revenue[i]))

# Calculating the maximum Revenue Change
Max_Revenue_Change = max(Change_in_Revenue)

# Calculating the minimum Revenue Change
Min_Revenue_Change = min(Change_in_Revenue)

# Calculating the revenue change length 
Revenue_Change_len = len(Change_in_Revenue)

# Calculating the revenue change total 
for i in range (Revenue_Change_len):
    Revenue_Change_Total = Revenue_Change_Total + Change_in_Revenue [i]


# Calculating the average revenue change
Average_Revenue_Change = Revenue_Change_Total/Revenue_Change_len
    
# Calculating the Date for the Minimum Revenue Change   
for i in range (Revenue_Change_len):
    if (Change_in_Revenue[i] == Min_Revenue_Change):
        Min_Revenue_Change_Date = Date[i+1]

# Calculating the Date for the Maximum Revenue Change
for i in range (Revenue_Change_len):
    if (Change_in_Revenue[i] == Max_Revenue_Change):
        Max_Revenue_Change_Date = Date[i+1]
        

# Print calculations to terminal and export to txt file
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: "+ str(Months))
print ("Total Revenue: "+ "$" + str(TotalRevenue))
print ("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
print ("Greatest Increase in Revenue: " + str(Max_Revenue_Change_Date) + "  $"+ str(Max_Revenue_Change))
print ("Greatest Decrease in Revenue: " + str(Min_Revenue_Change_Date) + "  $"+ str(Min_Revenue_Change))

output_file= open("financial_analysis.txt","w+")
output_file.write("Financial Analysis")
output_file.write("----------------------------")
output_file.write("Total Months: "+ str(Months)
output_file.write("Total Revenue: " + "  $" + str(TotalRevenue))
output_file.write("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
output_file.write("Greatest Increase in Revenue: " + str(Max_Revenue_Change_Date) + "  $"+ str(Max_Revenue_Change))
output_file.write("Greatest Decrease in Revenue: " + str(Min_Revenue_Change_Date) + "  $"+ str(Min_Revenue_Change))
>>>>>>> d9d82336044d77ede43636185551ade14a0d64b5
output_file.close()