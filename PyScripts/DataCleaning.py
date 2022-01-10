import csv
import pandas as pd
'''
Title: CapStone Project
Author: James Mills
Date: Jan 2022
This script was ran to clean the initial grocery dataset to be used for association rule creation.
'''
df = pd.read_csv('../Data/Groceries_dataset.csv')  # reads in initial dataset
df1 = df.drop(columns=["Date"])  # drops unneeded Date column
df1.sort_values(by=['Member_number'], inplace=True)  # sorts by member number
df1.reset_index(inplace=True)
df1.drop(columns=['index'],inplace=True)  # resets the index to map lowest to highest member numbers
grouped = df1.groupby('Member_number')['itemDescription'].apply(list)  # creates list of items purchased by member
transactions = grouped.to_list()
file = open('../Data/transaction_data.csv', 'w', newline='')  # saves resulting list to csv file for rule creation
with file:
    write = csv.writer(file)
    write.writerows(transactions)
