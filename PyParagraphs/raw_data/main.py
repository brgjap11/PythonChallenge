# Import all the dependencies, libraries and modules
import pandas as pd
import numpy
import os
import csv
import sys
import re

# Store the source file path to a variable
# ask user to input all of the files names into the code
User_Paragraph_File = os.path.join("..", "raw_data", input ("Please enter the input filename: \n"))

# Create new lists for storing the data from the input file (Letters, words, sentences, paragraphs etc.)
Letter = []
Word = []
Sentence = []
Paragraph = []

Sentence_Length = 0
Letter_Count = 0
Word_Count = 0
Sentence_Count = 0
Paragraph_Count = 0

# Open the text file
with open(User_Paragraph_File) as txtfile:
   paragraph = txtfile.read()
   #split_paragraph = re.split(” “, paragraph)
   #print (len(split_paragraph))
   
   Sentence_1 = paragraph.split(".")
   Sentence_2 = paragraph.split("!")
   Word = paragraph.split(" ")
   


Word_Count = len(Word)
Sentence_Count = len(Sentence_1) - 1 + len(Sentence_2) - 1
Letter_Count = len (paragraph)
   
Average_Letter_Count = Letter_Count / Word_Count
Average_Sentence_Length = Word_Count/Sentence_Count

print ("Paragraph Analysis")
print ("-----------------")
print ("Approximate Word Count is: " + str(Word_Count))
print ("Approximate Sentence Count is: " + str(Sentence_Count))
print ("Approximate Letter Count is: " + str (Letter_Count))
print ("Average Letter Count is: "+ str(Average_Letter_Count))
print ("Average Sentence Length is: " + str(Average_Sentence_Length))


