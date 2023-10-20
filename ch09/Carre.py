from Rectangle import Rectangle

class Carre(Rectangle):

    def __init__(self, cote=1) -> None:
        super().__init__(cote, cote)
        self._cote = cote

    @property
    def cote(self):
        return self._cote
    
    @cote.setter
    def cote(self,cote):
        self.longueur = cote
        self.largeur = cote
        self._cote = cote

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.cote=}"


    def __del__(self):
        print(f"__del__(self) {__class__.__name__} {self.cote=}")