# -*- coding: utf-8 -*- 
"""
Created on Mon Sep 30 14:42:29 2024

@author: andre
"""

import os
import altair as alt
import numpy as np
import pandas as pd 

##Read in one percent sample (15 Points)
#Question 1

#upload the data
raw_debt = r"C:/Users/andre/Documents/GitHub/ppha30538_fall2024/problem_sets/ps1/data"
path_debt = os.path.join(raw_debt, "parking_tickets_one_percent.csv")
tickets = pd.read_csv(path_debt)

#test the speed of the upload command
import pyspeedtest  #using: https://www.geeksforgeeks.org/application-for-internet-speed-test-using-pyspeedtest-in-python/

my_test = pyspeedtest.SpeedTest(tickets)

my_test.upload()

#use an assert statement to view the length of tickets dataframe

#I'm using this article as a guide: https://www.geeksforgeeks.org/python-assert-keyword/

#First I'll make an assert statement designed to fail.

assert len(tickets) == 2 #using: https://saturncloud.io/blog/5-easy-ways-to-get-pandas-dataframe-row-count/#:~:text=The%20simplest%20and%20most%20straightforward,pandas%20as%20pd%20df%20%3D%20pd.
print("Debt jubilee for everyone.")

#Then I'll make an assert statement designed to succeed.

assert len(tickets) == 287458
print("Since this worked, let's have a debt jubilee :). ")


#Question 2

#using this article: https://docs.python.org/3/library/os.html  to find os.stat
#And this as well: https://www.geeksforgeeks.org/python-os-stat-method/

csv_path = "C:\\Users\\andre\\Documents\\GitHub\\ppha30538_fall2024\\problem_sets\\ps1\\data\\parking_tickets_one_percent.csv"

os.stat(csv_path) #returns a lot of different information 
#about a given file, including st_size, which is in bytes. A st_size of
# 83942807 bytes will be 83942.807 megabytes.

#Question 3

#Which column is being used, by default, as the basis for sorting?

# I believe it is issue date.

#subsetting the data to the first 500 rows

sub_tickets = tickets.iloc[0:500, :]

#writing a function to test if the column is ordered


##Cleaning the data and benchmarking (15 Points)
#Question 1

#Use python datetime to allow python to know which tickets were issued in 
#

sub_tickets




