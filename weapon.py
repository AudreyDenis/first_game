class Arme:
    def __init__( self,
                  name  = 'weapon',
                  genre  = '',
                  power = 0,
                  ):
        self.name  = name
        self.genre = genre
        self.powe  = power 
    
    def se_detruire(self):
        print(f" l'arme {self.name} a ete detruite ! ")
        self.power = 0 
    
    def ameliorer(self,power):
        self.power += power 