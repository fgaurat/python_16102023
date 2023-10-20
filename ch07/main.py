def main():
    a=2
    b=3
    c=a/b

    # fstring : formated string
    formatted_value = f"{int(c * 100) / 100:.2f}"
    print(formatted_value)
    
    s = f"{a}/{b}={c*100:.2f}%"
    print(s)

    s = f"{a}/{b}={c:.2%}"
    print(s)
    s = f"{a=}/{b=} => {c=:.2%}"
    print(s)
    print(50*'-')
    l = ["Value 01","Value 02","Value 03"]

    # s = "v3={2}, v1 ={0} ,v2={1}".format(l[0],l[1],l[2])
    s = "v1 ={} ,v2={}, v3={}".format(l[0],l[1],l[2])
    s = "v1 ={} ,v2={}, v3={}".format(*l)
    print(s)
    print(50*'-')
    s="nom: {nom}, prénom: {prenom}, age:{age}".format(nom="GAURAT", prenom="Fred",age=47)
    print(s)
    d={
        "nom":"GAURAT", "prenom":"Fred","age":47
    }
    s="nom: {nom}, prénom: {prenom}, age:{age}".format(**d)
    print(s)

    s=f"{d=}"
    print(s)



if __name__ == '__main__':
    main()
