from ctypes import CDLL,c_char_p
import time
def main():
    libc = CDLL("hello.o")
    libc.sayHello()

    name = b"Fred"
    c_name = c_char_p(name)
    libc.hello(c_name)
    for i in range(10):
        time.sleep(1)
        a = libc.randNum()
        print(a)

if __name__ == '__main__':
    main()
