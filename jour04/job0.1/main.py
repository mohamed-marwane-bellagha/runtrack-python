def power(base, exponent):
    # Base Case
    if exponent == 0:
        return 1

    # Recursive Case
    else:
        return base * power(base, exponent - 1)


# Driver Code
number=int(input("Entrez la base :"))
exposant=int(input("Entrez l'exposant :"))
result=power(number,exposant)
print(result)