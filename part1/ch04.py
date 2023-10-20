# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

l = ["Value 01","Value 02","Value 03","Value 04"]

for v in l:
    print(v)

for i in range(len(l)):
    print(str(i)+" "+l[i])
print(50*'-')
print(range(4)) # [0,1,2,3]
print(list(range(4))) # [0,1,2,3]
print(50*'-')


to_find = 15

for i in range(10):
    print(i)
    if i == to_find:
        print("ok")
        break
else:
    print("KO")


print(50*'-')
to_find = 5

for i in range(10):
    if i == to_find:
        print("ok")
        continue

    print(i)
print(50*'-')

def fib(n:int): 
    """Print a Fibonacci series up to n.""" # docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(10)


def fib2(n=10) -> list:
    """return a Fibonacci series up to n."""
    r = []
    a, b = 0, 1
    while a < n:
        r.append(a)
        a, b = b, a+b

    return r


l = fib2(10) 
print(l) # [0,1,1,2,3,5,8]
 
print(50*'-')


a = 2
def the_function():
    global a
    a = 1234
    print("the_function "+str(a)) # 1234
    
    if True:
        b=12
    print("b : "+str(b))
the_function()
print(a) # 1234

print(50*'-')
l = fib2() 
l = fib2(22) 
print(l)

print(50*'-')

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

print(50*'-')

def f(a, L=[]):
    L.append(a)
    return L
print(f(1)) # [1]
print(f(2)) # [1,2]
print(f(3)) # [1,2,3]

def f(a, L=None):
    if L is None:
        L =[]
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2)) # [1,2]
print(f(3)) # [1,2,3]

print(50*'-')
def hello(name,firstName,age=22,job=None):
    print("name : "+name)
    print("firstName : "+firstName)
    print("age : "+str(age))
    print("job : "+str(job))

# hello(firstName="Frédéric",name="GAURAT",47,"dev")
hello("GAURAT","Frédéric")
print(50*'-')

def add(*the_list): # arguments en nombres variables par position
    r = 0
    for i in the_list:
        r+=i

    return r


l = [1,2,3,4,5]

print(*l) # print(1,2,3,4,5)

a,b,*c = l
print(a,b,c,sep=", ")
r= add(*l)
print(r) # 10
print("toto",12,"tutu",3.4,True,sep="-")
r= add(1,2,3,45,6,7)

print(r) # 10


print(50*'-')
def hello(**kwargs):
    print(kwargs)
    print("name : ",kwargs['name'])
    print("firstName : ",kwargs['firstName'])
    print("age : ",kwargs['age'])
    print("job : ",kwargs['job'])

hello(firstName="Frédéric",name="GAURAT",job="dev",age=47)
print(50*'-')


def the_function(*,a,b,c): # kw only
# def the_function(a,b,c,/): # pos only
    print(a,b,c)

# the_function(a="value a",b="value b",c="value c")
# the_function("value a","value b","value c")


print(50*'-')


def mult2(l)->list:
    r =[]
    for i in l:
        r.append(i*2)
    return r

l =[1,2,3,4]
l2 = mult2(l)

print(l2) # [2,4,6,8]

def mult2_2(i):
    return i*2

l2 = map(mult2_2,l)
for i in l2:
    print(i)

l2 = list(map(mult2_2,l))
print(l2)
l2 = list(map(lambda i:i*2,l))
print(l2)

a =2
a = lambda i: i*2
c = a(3)
print(c)


