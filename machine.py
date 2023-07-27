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
    
    def move_and_get_time_linear(self, new_pos, fast = False):
        """moves the tool to its new position"""
        X = new_pos[0]
        Z = new_pos[1]
    
        if not X :
            X = self.position[0]
        else :
            X = float(X[1:].replace(",",""))
            
        if not Z :
            Z = self.position[0]
        else :
            Z = float(Z[1:].replace(",",""))
            
        dist = sqrt((X-self.position[0])**2 + (Z-self.position[1])**2)
        
        if fast:
            time = dist / self.maxSpeed
        elif not fast:
            time = dist / self.speed
            
        self.position = (X,Z)
        return time*60 #return seconds
    
    def interpret(self, line):
        """get a line, interprets it and returns toolname, op type and time for csv indentation if the machine did not finished current cycle, returns nothing"""
        
        # \/ \/ \/ \/  here, should add a return if the line is a comment so it doesn't get interpreted \/ \/ \/ \/
        if "(" in line or "[" in line :
            return print("comment or variable")
        
        #\/ \/ \/ \/ to treat variables : should add a dict "self.varibles" stocking vars id "[]" is detected in a non G line and then self.readVar() is called if a "[]" is detected in a G line\/ \/ \/ \/ 
            
        #===================
        #  TOOL NAME GETTER 
        #===================
        
        T = getParam(line, "T")
        
        if T != None:
            self.toolName = T
        
        #===================
        #G CODES INTERPRETER
        #===================
        
        #DEFINIE G CYCLE
        G = getParam(line, "G") #get the G
        if G != None: #if the G exists, then we have a new cycle
            self.cycle = G
            
            
        #and now, we cover all G codes possibilities...
        
        #G0 : fast linear interpolation
        if self.cycle in ["G00", "G0"]:
            self.inCycle = True
            
            #get X and Z, we do all the data treatment in the moving methods
            X = getParam(line, "X")
            Z = getParam(line, "Z")
            
            print(self.toolName + " => " + self.move_and_get_time_linear((X,Z), fast = True) + "seconds")
        
        