import math
from ICalcGeo import ICalcGeo

class Cercle(ICalcGeo): # Cercle implémente l'interface ICalcGeo

    def __init__(self,rayon) -> None:
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self,rayon):
        self._rayon=rayon

    @property
    def surface(self):
        return math.pi*self._rayon**2


    def __str__(self) -> str:
        return f"{__class__.__name__} {self.rayon=}"