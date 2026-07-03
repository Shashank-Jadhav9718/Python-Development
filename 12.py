#Create a manual CSV parser that reads a standard CSV file, separates the values by commas while safely handling commas inside quotation marks, and prints each row as a list.

import csv
import pandas as pd

file_name = 'data.csv'

def parse_data(file_name):
    with open(file_name , 'r') as file :
        rows = csv.reader(file)
        for row in rows:
            print(row)
            
parse_data(file_name)

df = pd.read_csv('Data.csv')
