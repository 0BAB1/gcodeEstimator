import string

def getParam(line, parameter):
    """Returns the parameter in the G code line with it's value, if the parameter does not exists it returns None"""
    letters = list(string.ascii_uppercase)
    
    for i in range(len(line)):
        if line[i] == parameter:
            remaining = line[i:]
            for j in range(len(remaining)):
                try :
                    if remaining[j+1] in letters:
                        return line[i:j+i+1]
                except :
                    return line[i:j+i+1]
                
    return None