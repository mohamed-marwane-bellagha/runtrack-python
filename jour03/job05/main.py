import matplotlib.pyplot as plt
from collections import Counter

file = open("data.txt", "rt")
data = file.read()
datasplit= data.split(" ")
lenwords=[]
for word in datasplit:
    lenword=len(word)
    lenwords.append(lenword)

countlenwords=Counter(lenwords)



fig = plt.figure()
plt.bar(countlenwords.keys(),countlenwords.values())
plt.xlabel("Lettres")
plt.ylabel("Presence dans le fichier")
plt.show()
