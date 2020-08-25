from code_testing import merger
import os 
import csv
from pathlib import Path
from looger import App_Logger


class Automate:
    

      def __init__(self,path):
             self.calling_data=merger(path)
             self.file_object=open("Final_logs/Data_Extraction", 'a+')
             self.log_writer = App_Logger()
        
      def validates(self):
          try:
               self.log_writer.log(self.file_object,"Data Merging Started!!!!!")
               self.calling_data.combine()
               self.log_writer.log(self.file_object,"Data Merging Completed!!!!!")
         
          except Exception as e:
              raise e



if __name__ == "__main__":
   data=Path("Training_Batch_Files")
   tv=Automate(data)
   tv.validates()

    





