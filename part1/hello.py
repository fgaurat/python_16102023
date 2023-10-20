print('Hello')
# REPL : Read Eval Print Loop

# TheWorldIsFlat => PascalCase, UpperCamelCase
# theWorldIsFlat => camelCase
# the_world_is_flat => snake_case
# the-world-is-flat => train-case, spin-case, kebab-case

# loi de Pareto : 80/20
the_world_is_flat = True  # False
a = 1  # int  inférence
c = "1"  # str
b = "Toto"  # str
d = 1.2
print(type(a))
a = "Toto"
print(type(a))

print(type(c))
print(type(the_world_is_flat))
print(type(d))

if the_world_is_flat:
    print("Be careful not to fall off!")
    print("ligne 2 Be careful not to fall off!")
