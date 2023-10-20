from dataclasses import dataclass


@dataclass
class DataRectangle:
    longueur:int=0
    largeur:int=0
    
    @property
    def surface(self):
        return self.largeur*self.longueur

def main():
    d = DataRectangle(3,4)
    d1 = DataRectangle(3,4)
    print(d.largeur)
    print(d.longueur)
    print(d)
    print(d.surface)
    if d==d1:
        print("ok")
    else:
        print("ko")


if __name__ == '__main__':
    main()
