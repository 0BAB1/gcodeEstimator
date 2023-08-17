from timeEstimator.machines import Biglia

def calc(file_path : str) -> str:
    """give a time estimation  using file path, resturns a string with minutes"""
    lathe = Biglia()

    filename = file_path

    i= 0

    with open(filename, "r") as file:
        for line in file:
            i+=1
            #get data from the line to insert into a csv file
            try:
                data = lathe.interpret(line)
            except:
                raise Exception("FROM POS : (" + str(lathe.position[0]) + "," + str(lathe.position[1]) + ") TO POS :"  +line + "    LINE NUMBER : " + str(i))
        
    return str( ("%.2f") % (lathe.globalTime/60) ) + " min"