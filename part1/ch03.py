import copy 

a = 17 / 3
print(a)
a = 17 // 3
print(a)
a = 3**2
print(a)

la_chaine = "Python c'est un beau langage"
print(la_chaine)
la_chaine = 'Python c\'est un beau langage'
print(la_chaine)
window_path='c:\\new\\target'
print(window_path)
window_path = r'c:\new\target' # raw = brut
print(window_path)
multi_lines = """Ligne 01
Ligne 02
Ligne 03
"""

print(multi_lines)
multi_lines = '''Ligne 01
Ligne 02
Ligne 03
'''
print(multi_lines)
print(50*'-')

a = 2
la_chaine = "valeur de a : "+str(a) # valeur de a : 2
print(la_chaine)

la_chaine = "valeur de a : " * a
print(la_chaine)
print(50*'-')

word = "Python"

print(word[0])
print(len(word))
print(word[len(word)-1])
print(word[-1])
print(word[-2])
print(word[-6])

s = word[2:5]
print(s)

s = word[2:]
print(s)
print(word[2:])
print(word[:4])
print(word[:])
print(word[-2:])
a=2
a=3
print(50*'-')
word = "Python"
# word[0] = "J" # Jython => Python => JVM
# print(word)

# word = "Toto"
# print(word)
print(50*'-')
a=2
print(hex(id(a)))
# a=3
# print(hex(id(a)))
b=2
print(hex(id(b)))
print(50*'-')
word = "Python"
j = 'J'+word[1]
print(50*'-')
squares = [1, 4, 9, 16, 25]
print(squares)
# squares2 = squares[:]
# squares2 = squares.copy()
squares2 = copy.copy(squares)
squares[0] = 1000
print(squares) # [1000, 4, 9, 16, 25]
print(squares2)# [1, 4, 9, 16, 25] / [1000, 4, 9, 16, 25]
print(50*'-')
l1 = [
    [10,20,30],
    [40,50,60],
    [70,80,90],
]

l2 = copy.deepcopy(l1) # récursive
l1[1][2] = 1000
print(l1)
print(l2)

l1 =["toto","titi"]
l2 =["tata","tutu"] + l1
print(l2)
l2.append("tyty")
print(l2)


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b