class player:
    def __init__(self,name):
        self.name = name
        self.picked = []
    
    def getPoints(self):
        return self.points

    def addPoints(self,add):
        self.points += add

    def setPoints(self,new_points):
        self.points = new_points

    def getPicked(self):
        return self.picked
    
    def addPicked(self, add):
        self.picked.append(add)
    
    def setPicked(self,new_list):
        self.picked = new_list
    def emptyPicked(self):
        self.picked = []



    points = 0
    