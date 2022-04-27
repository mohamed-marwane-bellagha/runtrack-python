import matplotlib.pyplot as plt

file = open("data.txt", "rt")
data = file.read()
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
countalphabet=[]
for i in alphabet:
    datacount=data.count(i)
    countalphabet.append(datacount)


fig = plt.figure()
plt.bar(alphabet,countalphabet)
plt.xlabel("Lettres")
plt.ylabel("Presence dans le fichier")
plt.show()