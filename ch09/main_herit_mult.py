
class A:
    def __init__(self) -> None:
        print("Constructeur A")
    
    def methode(self):
        print("methode A")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("Constructeur B")
    
    def methode(self):
        print("methode B")

class C(A):
    def __init__(self) -> None:
        super().__init__()
        print("Constructeur C")
    
    def methode(self):
        print("methode C")

class D(C,B):
    def __init__(self) -> None:
        super().__init__()
        print("Constructeur D")
    
    def methode(self):
        super(B,self).methode()
        print("methode D")


def main():
    d = D()
    d.methode()
    print(D.mro()) # Method Resolution Order

if __name__ == '__main__':
    main()
