import string
from math import sqrt

def getParam(line: str , parameter: str , vars : dict = {}) -> str:
    """Returns the FIRST parameter in the G code line with it's value, if the parameter does not exists it returns None"""
    letters = list(string.ascii_uppercase)
    
    for i in range(len(line)):
        
        if line[i] == parameter:
            #if the param is in the line
            remaining = line[i:] #we define the ramining char to identify the param's valur among them
            for j in range(len(remaining)):
                try :
                    #so we loop until we fing a letter, by definition not a value
                    if remaining[j+1] in letters:
                        param = line[i:j+i+1].strip()
                        #if we have a variable
                        if "#" in param and "[" in param:
                            param = param[0] + getValueFromVariableQuery(param[1:], vars)
                        return param
                except :
                    #if we go out of index, it means we are a the end of a line
                    param = line[i:j+i+1].strip()
                    #if we have a variable
                    if "#" in param and "[" in param:
                        param = param[0] + getValueFromVariableQuery(param[1:], vars)
                    return param
                
    return None
                
def getValueFromVariableQuery(line : str, vars : dict = {}) -> str:
    #get a nice format to treat : [element1, element2, element3, ....]
    lineArr = line.replace("[","").replace("]","").split("+")
    #first, we have to raplace all #<VARNAME> with their values in the {vars} dict
    toSum = []
    for element in lineArr:
        if element in list(vars.keys()):
            toSum.append(float(vars[element]))
        else:
            toSum.append(float(element))
            
    #then we add all elements
    return str(sum(toSum))
    
def getVar(line : str) -> tuple :
    """return (varNumber, varValue)if var in line, else returns None"""
    if not "#" in line or "G" in line or "X" in line or "Z" in line: return None
    
    letters = list(string.ascii_uppercase)
    
    for i in range(len(line)):
        
        if line[i] == "#":
            #if the # var marker is in the line
            remaining = line[i:] #we define the ramining char to identify the param's valur among them
            for j in range(len(remaining)):
                try :
                    #so we loop until we fing a letter, by definition not a value
                    if remaining[j+1] == "=":
                        return (line[i:j+i+1].strip(), line[j+i+2:].strip())
                except :
                    #if we go out of index, it means we are a the end of a line
                    return (line[i:j+i+1].strip(), line[j+i+2:].strip())

def magnitude(v : tuple):
    """returns the magnitude of a 2d vector"""
    return sqrt(v[0]**2+v[1]**2)

def dotProduct(u : tuple,v : tuple) -> float:
    """return the dot product of two 2d vector"""
    return u[0] * v[0] + u[1] * v[1]