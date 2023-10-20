import traceback


class DivisionPar12Error(ArithmeticError):

    def __init__(self) -> None:
        super().__init__("Division par 12 !!!")

def div(a,b):
    if b==12:
        # e = ArithmeticError("Division par 12 !!!")
        e = DivisionPar12Error()
        raise e
    
    return a/b

def call_div(a,b):
    c = 0
    try:
        print("open log")
        c = div(a,b)
        print("write log",c)
    finally:
        print("close log")
    
    return c


def main():
    try:
        a=2
        # b=int(input("valeur de b : "))
        b = 12
        c = call_div(a,b)
        print(c)

    except DivisionPar12Error as e:
        print(e.__class__.__name__,"erreur",e)

    except Exception as e:
        print("Exception",e.__class__.__name__,"erreur",e)
        traceback.print_exc()        

    else:
        print("pas d'erreur")



    print("--- la suite ---")
if __name__ == '__main__':
    main()
