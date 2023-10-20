import time
import timeit

def use_loop():
    l = []
    for i in range(100):
        l.append(i)

def use_map():
    l = list(map(lambda i:i,range(100)))


def use_comp():
    l= [i for i in range(100)]

def main():
    # start = time.time()
    # use_loop()
    # print(time.time()-start)
    # print(50*'-')

    # start = time.time()
    # use_map()
    # print(time.time()-start)
    # print(50*'-')

    # start = time.time()
    # use_comp()
    # print(time.time()-start)
    # print(50*'-')


    t1 = timeit.timeit("use_loop()",setup="from __main__ import use_loop")
    print(t1)
    t1 = timeit.timeit("use_map()",setup="from __main__ import use_map")
    print(t1)
    t1 = timeit.timeit("use_comp()",setup="from __main__ import use_comp")
    print(t1)
if __name__ == '__main__':
    # python -m timeit -s "import main"
    main()


