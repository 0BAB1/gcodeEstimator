from .timeEstimator.machines import Biglia
import os

def run(file_path : str) -> (float,list):
    """simulate the given file, returns total time and csv data a table that i can turn into csv later on"""
    lathe = Biglia()
    i = 0

    with open(file_path, "r") as file:
        for line in file:
            i+=1
            #get data from the line to insert into a csv file
            try:
                lathe.interpret(line)
            except Exception as e:
                #error handling
                raise e
            
        lathe.save_csv_data() #last csv Data save to put the last cached data into to lathe.csvData variable
        
    return (round(lathe.globalTime,2), lathe.csvData)