from timeEstimator.machines import Biglia

lathe = Biglia()

filename = "G.g"

i= 0

with open(filename, "r") as file:
    for line in file:
        i+=1
        #get data from the line to insert into a csv file
        try:
            data = lathe.interpret(line)
        except:
            raise Exception("FROM POS : (" + str(lathe.position[0]) + "," + str(lathe.position[1]) + ") TO POS :"  +line + "    LINE NUMBER : " + str(i))

print(lathe.globalTime/60 , " minutes")