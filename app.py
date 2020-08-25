import os
import csv
from os import listdir


path = "C://Users//rahul//Desktop//Excel_Automation//Training_Batch_Files"

if not os.path.exists("Data/Combine_Data"):
     os.makedirs("Data/Combine_Data")
     with open('Data/Combine_Data/'+ 'input_file' + '.csv', 'a') as csvfile:
         wr=csv.writer(csvfile,dialect='excel')
         wr.writerow(["LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE","PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6","BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6","PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6","default payment next month"])



onlyfiles=[f for f in listdir(path)]

for file in onlyfiles:
   with open(path+'/'+ file, "r") as f:
        next(f)
        reader = csv.reader(f, delimiter="\n")
        with open('Data/Combine_Data/'+ 'input_file' + '.csv', 'a') as csvfile:
            wr=csv.writer(csvfile,dialect='excel') 
            for line in reader:
                 wr.writerow(line)