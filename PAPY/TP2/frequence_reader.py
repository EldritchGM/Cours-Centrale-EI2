zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

zen.replace("'"," ")
lines = zen.split("\n") # on se débarasse des passages à la ligne
for i in range(len(lines)): 
    lines[i] = lines[i].split(" ") # on se débarasse des espaces
mots = []
for line in lines:
    mots += line
to_delete = []
for i in range(len(mots)):
    mots[i] = mots[i].lower().replace(".","").replace(",","").replace("--","").replace("!","").replace("*","")
    if not mots[i].isalnum() and "'" not in mots[i]:
        to_delete.append(i)
to_delete.reverse()
for i in to_delete:
    mots.pop(i)

print(mots)

compteur = {}
for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

pourcentage = {key: (compteur[key] * 100 / len(compteur)) for key in compteur}
values = [(key,pourcentage[key]) for key in pourcentage]

values.sort(key = lambda tuple: tuple[1])

print("Percentage share of the words")
forma = "{0:.2f}"

for i in range(-1,-11,-1):
    print(f"{values[i][0]}\t\t\t{(forma.format(values[i][1]))}%")
print(len(compteur),len(mots))
