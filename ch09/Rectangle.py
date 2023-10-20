from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):

    __cpt=0 # static

    def __init__(self,longueur=1,largeur=1) -> None:
        # assert longueur>0 and largeur>0

        if longueur<=0 and largeur<=0:
            raise Exception("longueur<=0 and largeur<0=")
        print(f"def __init__(self,{longueur},{largeur})")

        self.__longueur = 1
        self.__largeur = 1
        Rectangle.__cpt+=1

        if longueur>0 and largeur>0:
            self.__longueur = longueur
            self.__largeur = largeur

    @staticmethod
    def get_cpt():
        return Rectangle.__cpt
    

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur   
    
    @longueur.setter
    def longueur(self,longueur):
        if longueur>0:
            self.__longueur = longueur

    @largeur.setter
    def largeur(self,largeur):
        if largeur>0:
            self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur

    def __del__(self):
        # print(f"__del__(self) => {self.__longueur=}, {self.__largeur=}")
        Rectangle.__cpt-=1
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self, __value: object) -> bool:
        return self.longueur == __value.longueur and self.largeur == __value.largeur
    
