from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo


def afficheSurface(o:ICalcGeo):
    print(o.surface)


def main():
    c =Carre(2)
    # print(c.surface)
    # c.cote =12
    # print(c.surface)
    # print(c)
    # print(50*'-')
    ce = Cercle(4)
    # print(ce)
    # print(ce.surface)
    print(50*'-')
    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
    r2 = Rectangle(2,3)
    # Rectangle.cpt = 1000
    print("Rectangle cpt",Rectangle.get_cpt())
    print("r cpt",r.get_cpt())
    print(50*'-')
    
    afficheSurface(c) # Carre
    afficheSurface(ce) # Cercle 
    afficheSurface(r) # Rectangle



def main_rectangle():
    r= Rectangle(2,4)
    r1= Rectangle(21,45)
    # r.set_longueur(-12)
    r.longueur = -12
    print(r.longueur)

    r1.longueur = -2
    print(r1.longueur)
    # r.surface = 34
    print(r.surface)
    
    print(50*'-')
    
    r= Rectangle(2,4)
    r1= Rectangle(2,4)
    

    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")

def old_main():
    r = Rectangle(2,5) # __init__
    
    print(r.get_longueur()) # 2
    print(r.get_largeur()) # 5

    r.set_longueur(12)
    print(r.get_longueur()) # 12
    r.set_longueur(-3)
    print(r.get_longueur()) # 12
    # del r
    r1 = Rectangle()
    print(r1.get_largeur()) # 1
    print(r1.get_longueur()) # 1


    print("surfaces")
    # print(r.get_surface())
    print(r1.get_surface())

    s = str(r)
    print(s)

    r2 = Rectangle()
    r2.longueur = 12
    r2.largeur = 2
    print(r2.longueur)
    print(r2.largeur)
    
    r2.longueur = -12
    print(r2.longueur) # 12
if __name__ == '__main__':
    main()
