from math import sqrt
from utils import getParam

class Lathe():
    """go inside machine.py to configure the lathe to correspond to your lathe's specifications"""
    def __init__(self) -> None:
        self.position = (0,0) # mm x,z
        self.cuttingSpeed = 0 #m/min
        self.feed = 0 #mm/tour
        self.maxSpeed = 12500 #mm/min
        self.rotation = 0 #1/min
        self.isRotationConstant = False #are we in G97 mode (True) or in G96 (False => we use Vc cuttingSpeed to calculate N - the rotation - to get time)
        self.toolName = ""
        
        self.cycle = "" # stores currrent G cycle
        self.cycleTime = 0 #current cycle accumulated time
        self.deadCycleTime = 0 #not machining (fast interpolations)
    
    def move_and_get_time_linear(self, new_pos, fast = False):
        """moves the tool to its new position in a linear trajectory. returns the necessary time"""
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
    
    def sendDataAndReset(self):
        """returns all the current cycle data for logging and reset the cycle time"""
        if (self.cycleTime == 0 and self.deadCycleTime == 0) or len(self.toolName) <= 1:
            return
        #print(self.toolName + " => " + str(self.cycleTime + self.deadCycleTime) + " seconds")
        self.cycleTime = 0
        self.deadCycleTime = 0
        return

    
    def interpret(self, line):
        """get a line, interprets it and returns toolname, op type and time for csv indentation if the machine did not finished current cycle, returns nothing"""
        
        # \/ \/ \/ \/  here, should add a return if the line is a comment so it doesn't get interpreted \/ \/ \/ \/
        if "(" in line or "[" in line :
            return
        
        #\/ \/ \/ \/ to treat variables : should add a dict "self.varibles" stocking vars id "[]" is detected in a non G line and then self.readVar() is called if a "[]" is detected in a G line\/ \/ \/ \/ 
            
        #=====================
        #   TOOL NAME GETTER 
        #=====================
        
        T = getParam(line, "T")
        
        if T != None:
            self.toolName = T
            #if this is a new tool, we return the tool times and procced to treat the next
            return self.sendDataAndReset()
        
        #=====================
        #  FEED SPEED GETTER
        #=====================
        
        F = getParam(line, "F")
        
        if F != None and F != "":
            self.feed = F
        
        #=====================
        # G CODES INTERPRETER
        #=====================
        
        #DEFINIE G CYCLE
        G = getParam(line, "G") #get the G
        if G != None and G != self.cycle: #if the G changes, then we return the cycle data to the asker
            self.cycle = G
            
            
        #and now, we cover all G codes possibilities...
        
        #-----------------------------
        #Cutting speeds G getters
        #-----------------------------
        
        if self.cycle in ["G97"]:
            #Definition de vitesse de rotation constante
            S = getParam(line, "S")
            if S:
                self.isRotationConstant = True
                self.rotation = float(S[1:])
                
        #G92 here
                
        if self.cycle in ["G96"]:
            S = getParam(line, "S")
            if S:
                self.isRotationConstant = False
                self.cuttingSpeed = float(S[1:])
        
        #-----------------------------
        #Machinning cycles G getters
        #-----------------------------
        
        #G0 : fast linear interpolation
        if self.cycle in ["G00", "G0"]:
            self.inCycle = True
            
            #get X and Z, we do all the data treatment in the moving methods
            X = getParam(line, "X")
            Z = getParam(line, "Z")
            
            self.deadCycleTime += self.move_and_get_time_linear((X,Z), fast = True) #add the cycle time to the current time cycle
        
        