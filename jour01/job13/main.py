val1=int(input("Entrez un premier nombre:"))
val2=int(input("Entrez un deuxieme nombre:"))
val3=int(input("Entrez un troisieme nombre:"))
val4=int(input("Entrez un quatrieme nombre:"))
val5=int(input("Entrez un cinquieme nombre:"))
def order(a,b,c,d,e):
    if int(a) & int(b) & int(c) & int(d) & int(e):
        tab=[a,b,c,d,e]
        tab.sort()
        for i in tab:
            print(i)

order(val1,val2,val3,val4,val5)