val=input("Entrer une chaine de caracteres:")
with open("output.txt", 'w') as f:
    f.write(val)