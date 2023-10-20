from collections import deque

l = [40, 50, 60, 70]
print(l)
l.append(80)
print(l)
last = l.pop()
print(l)
print(last)
l2 = [80, 90, 100]
# l.extend(l2)
l = l+l2
print(l)
l.remove(90)
print(l)

l.insert(0, 30)
print(l)
first_value = l.pop(0)
print(first_value)
print(l)

# Deque
q = deque(l)
print(q)
q.appendleft(30)
print(q)
l = q.popleft()

print(50*"-")


l = []

for i in range(0, 100, 10):
    l.append(i)

print(l)

l = list(map(lambda i: i*10, range(10)))
print(l)

# Liste par intention / comprehension list

l = [i for i in range(0, 100, 10)]
print(l)

values = ["   Ligne 01   ", "   Ligne 02", "Ligne 03   ", "  Ligne 04"]

clean_values = [value.strip() for value in values]

print(clean_values)

# Liste par intention / comprehension list

l = [i for i in range(0, 100, 10) if i > 50]
print(l)
del l[1]
print(l)

# a =2
# print(a)
# del a
# print(a)
print(50*'-')
t = 10, "la valeur 20", 30
print(t)

a, b, *c = 0, 1, 2, 3, 4
print(a, b, c)

# def get_values():
#     return 12,34

# a = get_values()
# print(a)

print(50*'-')

s = {10, 20, 30, 10, 30, 40}
print(s)
s.add(50)
s.add(10)
print(s)

l = [10, 20, 30, 10, 30, 40]
print(l)
l = list(set(l))
l.sort()
print(l)
print(50*'-')


d = {
    "name": "GAURAT",
    "firstName": "Fred",
    "age": 47,
    "projects": [
        "Project 01",
        "Project 02",
        "Project 03",
        "Project 04",
    ]
}

print(d['name'])
print(d['firstName'])

l = list(d)
print(l)

for k in d:
    print(k, d[k])

l = [("name", "GAURAT"), ("firstName", "Fred"), ("age", 47)]
d = dict(l)
print(d)

print(50*'-')

l = [10, 20, 30]
t = 10, 20, 30
s = {10, 20, 30}
d = {
    "value 01": 10,
    "value 02": 20,
    "value 03": 30,
}

# for i in range(len(l)):
for i,value in enumerate(l):
    # print(i,l[i])
    # print(i[0],i[1])
    print(i,value)

for i,value in enumerate(t):
    print(i,value)

for i in enumerate(s):
    print(i)

for k,v in d.items():
    print(k,v)