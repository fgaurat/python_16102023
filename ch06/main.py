# import lib.fibo as fb
# from fibo import fib as fi
# from fibo import *
# import fibo

import sys
# sys.path.append('/Users/fgaurat/local_dev/formations/python_16102023/lib')
sys.path.append('../lib')

import fibo as fb
from fibo import fib,fib2

def main():
    print(20*'-',"start",20*'-')
    print(sys.argv) # python main.py 10 ['main.py','10'] 
    v = int(sys.argv[-1])
    print("main",__name__)


    # import fibo
    # fibo.fib(100)
    # l = fibo.fib2(100)

    # def fib(a):
    #     print("fib",a)


    fb.fib(v)
    l = fb.fib2(v)
    print(l)

    print(50*'-')
    fib(100)
    l = fib2(v)
    print(l)
    print(fb.a)

if __name__ == '__main__':
    main()
