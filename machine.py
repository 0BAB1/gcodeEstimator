from math import sqrt
from utils import getParam

class Lathe():
    """go inside machine.py to configure the lathe to correspond to your lathe's specifications"""
    def __init__(self) -> None:
        self.position = (0,0) # mm x,z
        self.speed = 0 # mm/min
        self.maxSpeed = 15000 #mm/min
        self.toolName = ""
        
        self.cycle = "" # stores currrent G cycle
        self.cycleTime = 0 #current cycle accumulated time
    
    def move_and_get_time(self, new_pos, fast = False):
        """moves the tool to its new position"""
        X = new_pos[0]
        Z = new_pos[1]
    
        if not X :
            X = self.position[0]
        else :
            print(X)
            X = float(X[1:].replace(",",""))
            
        if not Z :
            Z = self.position[0]
        else :
            print(Z)
            Z = float(Z[1:].replace(",",""))
            
        dist = sqrt((X-self.position[0])**2 + (Z-self.position[1])**2)
        
        if fast:
            time = dist / self.maxSpeed
        elif not fast:
            time = dist / self.speed
            
        self.position = (X,Z)
        return time
    
    def treatLine(self, line):
        """get a line, interprets it and returns toolname, op type and time for csv indentation if the machine did not finished current cycle, returns nothing"""
        G = getParam(line, "G") #get the G
        if G != None: #if the G exists, then we have a new cycle
            self.cycle = G
        #and now, we cover all G codes possibilities...
        
        if self.cycle in ["G00", "G0"] and not "(" in line and not "[" in line: #we check for parenthethis as they show a comment line which should not be treated also for [ as it is varible and i don't want to do that rn!
            self.inCycle = True
            
            #get X and Z, we do all the data treatment in the moving methods
            X = getParam(line, "X")
            Z = getParam(line, "Z")
            
            print(line)
            print(60*self.move_and_get_time((X,Z), fast = True))