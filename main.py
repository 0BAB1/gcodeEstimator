from timeEstimator.machines import Biglia
import csv

lathe = Biglia()

filename = "912.g"

i= 0

with open(filename, "r") as file:
    for line in file:
        i+=1
        #get data from the line to insert into a csv file
        try:
            data = lathe.interpret(line)
        except:
            raise Exception("FROM POS : (" + str(lathe.position[0]) + "," + str(lathe.position[1]) + ") TO POS :"  +line + "    LINE NUMBER : " + str(i))
    
print(lathe.globalTime, lathe.csvData)

# Specify the file name you want to save
csv_file = 'data.csv'

# Writing dictionary data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row with keys from the dictionary
    writer.writerow(lathe.csvData.keys())

    # Write the corresponding values for each key
    # Use zip to iterate over each list in the dictionary simultaneously
    writer.writerows(lathe.csvData.values())

print(f"Data has been successfully written to {csv_file}.")