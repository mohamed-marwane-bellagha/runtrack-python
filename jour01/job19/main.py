width = int(input("Entrez une width pour votre rectangle: "))
height = int(input("Entre une height pour votre rectangle: "))
def draw_rectangle(width, height):
    i=0
    while i<height :
        if i==0:
            print("|")
            while i<width:
                print("-")
    print("|")

draw_rectangle(width,height)