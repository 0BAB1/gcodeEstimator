import string

def getParam(line, parameter):
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
                        return line[i:j+i+1]
                except :
                    #if we go out of index, it means we are a the end of a line
                    return line[i:j+i+1]
                
    return None

def getParamsDict(line, parameter):
    """Returns the FIRST parameter in the G code line with it's value, if the parameter does not exists it returns None"""
    letters = list(string.ascii_uppercase)
    params = {}
    
    for i in range(len(line)):
        
        if line[i] == parameter:
            #if the param is in the line
            remaining = line[i:] #we define the ramining char to identify the param's valur among them
            for j in range(len(remaining)):
                try :
                    #so we loop until we fing a letter, by definition not a value
                    if remaining[j+1] in letters:
                        return line[i:j+i+1]
                except :
                    #if we go out of index, it means we are a the end of a line
                    return line[i:j+i+1]
                
    return params