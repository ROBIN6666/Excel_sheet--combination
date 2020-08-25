import re 
from os import listdir
import pandas as pd
import csv
import os
from pathlib import Path


class merger:

   def __init__(self,path):
            self.raw_path=path
         
   def combine(self):

     if not os.path.exists("Data/Combine_Data"):
         os.makedirs("Data/Combine_Data")
         with open('Data/Combine_Data/'+ 'input_file' + '.csv', 'a') as csvfile:
           wr=csv.writer(csvfile,dialect='excel')
           wr.writerow(["LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE","PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6","BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6","PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6","default payment next month"])

     onlyfiles=[f for f in listdir(self.raw_path)]
     for file in onlyfiles:
        path=str(self.raw_path) + "/" + file
        with open(path, "r") as f:
           next(f)
           reader = csv.reader(f, delimiter="\n")
           with open('Data/Combine_Data/'+ 'input_file' + '.csv', 'a') as csvfile:
             wr=csv.writer(csvfile,dialect='excel') 
             for line in reader:
                  wr.writerow(line)   
            
          