from math import sqrt, pi,  acos, asin
from .profile import Profil
from .utils import *
import re

class Biglia():
    """go inside machine.py to configure the lathe to correspond to your lathe's specifications"""
    def __init__(self) -> None:
        self.lineNumber = 0 #the number of the line being interpreted
        
        self.position = (0,0) # mm x,z
        self.cuttingSpeed = 0 #m/min
        self.feed = 0 #mm/tour
        self.perRevolutionFeed = True #IS SPEED ? mm/min si false
        self.maxSpeed = 12500 #mm/min
        self.rotation = 0 #1/min
        self.maxRotation = 99999999#G92
        self.isRotationConstant = False #are we in G97 mode (True) or in G96 (False => we use Vc cuttingSpeed to calculate N - the rotation - to get time)
        self.toolName = ""
        
        self.Profil = Profil()
        
        self.variables = {}
        
        self.currentCycle = ""
        self.cycleTime = 0 #current cycle accumulated time
        self.deadCycleTime = 0 #not machining (fast interpolations)
        
        self.csvData = {} #to return at the end later on
        self.globalTime = 0.0  #to return for testing purpuses
    
    def move_and_get_time(self, X,Z, distance, fast = False) -> float:
        """moves the tool to its new position in a linear trajectory. returns the necessary time"""
        
        #=== distance setter ===
        
        dist = distance
        
        if fast:
            
            time = dist / self.maxSpeed
            
        elif not fast:
            
            #=== speed setter ===
            
            #determine the speed depending on the machinning factors
            if not self.perRevolutionFeed :
                speed = self.feed
            elif self.isRotationConstant:
                speed = self.rotation * self.feed
            elif not fast and not self.isRotationConstant:
                D_moyen = X + self.position[0]
                rot_moyen = 1000 * self.cuttingSpeed / (pi * D_moyen)
                if rot_moyen > self.maxRotation : rot_moyen = self.maxRotation
                speed = rot_moyen * self.feed

            time = dist / speed
            
        self.position = (X,Z)
        self.globalTime += time*60
        return time*60 #return seconds
    
    def determineDistanceFromCurrentPos(self, X : float = 0, Z : float = 0, kind : str = "linear", *args, **kwargs) -> float:
        """determine distance from the current lathe's position to the new point"""
        if kind == "linear":
            return sqrt((X-self.position[0])**2 + (Z-self.position[1])**2)
        
        if kind == "circular":
            I = kwargs["I"]
            J = kwargs["J"]
            R = kwargs["R"]
            
            if not I == 0 or not J == 0:
                if not R == None:
                    #ignonore R by dfault if I or J is set (or both btw)
                    R = None
                    
            if not R: #if we are using I and J to calc our distance
                #then the math begins :
                #determine u and v vectors (to old and new pos)
                u = (-I + self.position[0], -J + self.position[1])
                v = (X - I, Z - J)
                
                #check if valid (determine R and apply 2R > distance)
                if 2 * min(magnitude(u), magnitude(v)) < self.determineDistanceFromCurrentPos(X,Z):
                    raise ValueError("incorrect I and J values in code resulting in an impossible profile, please check yout program or use R")
                
                #determine theta, the angle, always between old and new one
                theta = acos(round(dotProduct(u,v)/(magnitude(u)*magnitude(v)),3))
                dist = theta * magnitude(v) #here, magnitude(u) == magnitude(v) == R, the radius
                return dist
                #determine the distance by multiplying
            elif not R == None:
                #if we using the radius to code the G2/3 interpolation :
                #check if valid (determine R and apply 2R > distance)
                if 2 * R < self.determineDistanceFromCurrentPos(X,Z):
                    print("WARNING ! R was too small and has been adjusted from %.2f to %.2f" % (R, 0.1 + self.determineDistanceFromCurrentPos(X,Z)/2))
                    R = 0.1 + self.determineDistanceFromCurrentPos(X,Z)/2
                #determine theta (cf formula on paper)
                theta = 2 * (asin((self.determineDistanceFromCurrentPos(X,Z)/2)/R))
                dist = theta * R
                return(dist)
    
    def sendDataAndReset(self) -> None:
        """returns all the current cycle data for logging and reset the cycle time"""
        if (self.cycleTime == 0 and self.deadCycleTime == 0) or len(self.toolName) <= 1:
            return
        #print(self.toolName + " => " + str(self.cycleTime + self.deadCycleTime) + " seconds")
        self.cycleTime = 0
        self.deadCycleTime = 0
        return
    
    def interpret(self, line):
        """get a line, interprets it and stores toolname, op type and time for csv indentation in its (the lathe) inernal dataset"""
        
        self.lineNumber +=1
        
        line = re.sub("\(.*?\)","",line)
        var = getVar(line)
        if var:
            self.variables[var[0]] = var[1]
            
        #=====================
        #  FEED SPEED GETTER
        #=====================
        
        F = getParam(line, "F")
        
        if not F == None:
            self.feed = F
        
        #-----------------------------
        #Cutting speeds G getters
        #-----------------------------
        
        #look for G95 or G94 to determine thje state of self.perRevoltionFeed (true id mm/tr and false if mm/min)
        if "G95" in line or "G99" in line:
            self.perRevolutionFeed = True
        if "G94" in line or "G98" in line:
            self.perRevolutionFeed = False
        
        #G97 says we use constant rotation speed, thus using cuuting speed useless
        if "G97" in line:
            #Definition de vitesse de rotation constante
            S = getParam(line, "S")
            if S:
                self.isRotationConstant = True
                self.rotation = S
                
        #G92 here, maximum rotation speed rate
        if "G92" in line:
            S = getParam(line, "S")
            if S:
                self.maxRotation = S
                
        #G96 tells us we use cutting speed to move the  tool
        if "G96" in line:
            S = getParam(line, "S")
            if S:
                self.isRotationConstant = False
                self.cuttingSpeed = S
                
        #G28 tells to return to reference point
            
        #=====================
        # PROFILE DEFINITION
        #=====================
        
        if self.Profil.isDefinitionTakingPlace :
            if "G71" in line: #this means we are in the second G71 line, so we get params from it
                self.Profil.begin = int(getParam(line,"P"))
                self.Profil.end = int(getParam(line, "Q"))
            
            N = getParam(line,"N")
            if not N : #if there is no N in line, getParams returns None so we handle that
                N = int(0)
            else :
                N = int(N)
            
            #if we are at the end of profile def, we determine everything
            if not N == 0 and N == self.Profil.end:
                self.Profil.isDefinitionTakingPlace = False
                dist = self.Profil.get_mean_Z(self.position[1])
                for i in range(self.Profil.get_number_of_passes()):
                    #======PARAMS GETTER==========
                    X = getParam(line,"X", self.variables)
                    Z = getParam(line, "Z", self.variables)
                    
                    if X == None : X = self.Profil.points[-1][0]
                    if Z == None : Z = self.Profil.points[-1][1]
                    
                    print()
                    #move and makes the passes
                    self.cycleTime += self.move_and_get_time(X , Z, dist, fast = False)
                    #also make fasts passes
                    self.cycleTime += self.move_and_get_time(X , Z, dist, fast=True)
                
                
                self.Profil = Profil()
            else:
                #======PARAMS GETTER==========
                X = getParam(line, "X", self.variables)
                Z = getParam(line, "Z", self.variables)
                        
                if X == None :
                    if len(self.Profil.points) >= 1:
                        X = self.Profil.points[-1][0]
                    else:
                        X = self.position[0]
                        
                if Z == None :
                    if len(self.Profil.points) >= 1:
                        Z = self.Profil.points[-1][1]
                    else:
                        Z = self.position[1]
                
                self.Profil.points.append((X,Z))
            
            return #passer a la ligne suivante sans interpreter le reste
            
        #=====================
        #  TOOL NAME GETTER 
        #=====================
        
        try:
            T = "T" + str(getParam(line, "T")) #T0101 for exemple
            if T != None:
                self.toolName = T
        except:
            ... #some times bugged on "GOTO" lines
        #if this is a new tool, we return the tool times and procced to treat the next
        #HERE SHOUL ADD A NEW ENTRY TO THE DATA DICT
        
        #=====================
        # G CODES INTERPRETER
        #=====================
        
        #we get the current cycle so we can spread it across lines
        try :
            G = getParam(line, "G")
            if "G" in line:
                self.currentCycle = "G" + str(int(G))
        except:
            ... #some times bugged on "GOTO" lines
            
        #and now, we cover all G codes possibilities...
        
        #-----------------------------
        # Machinning cycles G getters
        #-----------------------------
        
        X = getParam(line, "X", self.variables)
        Z = getParam(line, "Z", self.variables)
        U = getParam(line, "U", self.variables)
        W = getParam(line, "W", self.variables)
            
        #=====position setter =======
        
        if X == None: X = self.position[0]
        if not U : U = 0
        X += U
        
        if Z == None: Z = self.position[1]
        if not W : W = 0
        Z += W
            
        #G0 : fast linear interpolation
        if self.currentCycle in ["G00", "G0"]:
            dist = self.determineDistanceFromCurrentPos(X,Z,"linear")
            self.deadCycleTime += self.move_and_get_time(X,Z, dist,fast = True) #add the cycle time to the current time cycle
        #G01 : linear mouvement
        if self.currentCycle in ["G01", "G1"]:
            dist = self.determineDistanceFromCurrentPos(X,Z,"linear")
            self.cycleTime += self.move_and_get_time(X,Z, dist,fast = False) #add the cycle time to the current time cycle
            
        #G02 and G03 (time is bascaly the same for either Gs)
        if self.currentCycle in ["G02", "G2", "G03", "G3"]:
            i = getParam(line, "I")
            j = getParam(line, "J")
            r = getParam(line, "R")
            
            if not i : i = 0
            if not j : j = 0
            if not r : r = 0
            
            dist = self.determineDistanceFromCurrentPos(X, Z, "circular", I = i, J = j, R = r)
            if i or j or r:
                self.cycleTime += self.move_and_get_time(X,Z, dist, fast = False)
        
        #G71, G72 Stock removal turning/facing => this is an approx given at +-5seconds
        if self.currentCycle in ["G71", "G72"]:
            if "G71" in line or "G72" in line:
                self.Profil.isDefinitionTakingPlace = True
                self.Profil.deltaPasses = getParam(line, "U")
                print("in", self.cycleTime/60, self.lineNumber)