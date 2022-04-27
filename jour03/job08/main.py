from collections import Counter
import matplotlib.pyplot as plt

file = open("data.txt", "rt")
data = file.read()
datasplit= data.split(" ")
firstletters=[]
for words in datasplit:
    if len(words)>0:
        firstletter=words[0]
        firstletters.append(firstletter)

loweredletters=[]
for letters in firstletters:
    loweredletter=letters.lower()
    loweredletters.append(loweredletter)

res = Counter(loweredletters)

fig = plt.figure()
plt.bar(res.keys(),res.values())
plt.xlabel("Lettres")
plt.ylabel("Presence dans le fichier")
plt.show()


