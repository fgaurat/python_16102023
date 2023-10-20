


# this
# me

class Rectangle:
    
    def __init__(self,longueur=1,largeur=1) -> None:
        print(f"def __init__(self,{longueur},{largeur})")
        self.__longueur = 1
        self.__largeur = 1
        if longueur>0 and largeur>0:
            self.__longueur = longueur
            self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur   
    
    def set_longueur(self,longueur):
        if longueur>0:
            self.__longueur = longueur

    def set_largeur(self,largeur):
        if largeur>0:
            self.__largeur = largeur
    
    def get_surface(self):
        return self.__longueur*self.__largeur

    def __del__(self):
        print(f"__del__(self) => {self.__longueur=}, {self.__largeur=}")
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"
    
    longueur = property(get_longueur,set_longueur,doc="Property longueur")
    largeur = property(get_largeur,set_largeur,doc="Property largeur")