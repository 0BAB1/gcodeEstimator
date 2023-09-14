from math import floor

class Profil():
    def __init__(self) -> None:
        self.isDefinitionTakingPlace : bool = False
        self.points = [] 
        # [(0, 0), (20.0, 0), (20.0, -20.0), (15.0, -20.0), (15.0, -10.0), (10.0, -10.0), (5.0, -5.0)]
        self.begin : int
        self.end : int
        self.deltaPasses : float # is used to get the number of passes
        
    def get_mean_Z(self, initialZ : float) -> float:
        """returns the means ponderated Z"""
        totalX, totalZ = 0 , 0
        for i in range(len(self.points)-1):
            DX = abs(self.points[i+1][0] - self.points[i][0])
            DZ = abs(self.points[i+1][2] - initialZ)
            totalX += abs(DX)
            totalZ += abs(DZ*DX)
            
        #after verification : function looks good and problem comes from initalZ and is interprestation
        return abs(totalZ/totalX)
                        
    def get_number_of_passes(self) -> int:
        """divides total height by delata passes, returns the floore number of passes for G71"""
        #get the total Z thckness
        lowest = 99999999
        highest = -999999
        for point in self.points :
            if point[0] < lowest : lowest = point[0]
            if point[0] > highest : highest = point[0]
        
        return floor((highest - lowest)/self.deltaPasses)