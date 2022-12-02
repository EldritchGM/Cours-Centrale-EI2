from math import ceil

ZRLE_ONE = 257
ZRLE_TWO = 258


CONSTANT = {ZRLE_ONE: 1, ZRLE_TWO: 2}

def bijbin_to_int(bijbin):
    bijbin.reverse()
    res = 0
    for i in range(len(bijbin)):
        res += CONSTANT[bijbin[i]] * 2 ** i
    return res



def int_to_bijbin(entier):
    liste_q = [entier]
    while liste_q[-1] != 0:
        liste_q.append(ceil(liste_q[-1]/2) - 1)
    liste_a = []
    for k in range(len(liste_q) - 1):
        a = liste_q[k] - 2 * liste_q[k+1]
        if a == 1: 
            liste_a.append(ZRLE_ONE)
        elif a == 2: 
            liste_a.append(ZRLE_TWO)
        else:
            raise ValueError("ça marche pas :(")
    liste_a.reverse()
    return liste_a


def zRLE_encode(texte):
    texte = list(texte)
    i = 0
    cpt = 0
    while i < len(texte):
        if texte[i] == 0:
            texte.remove(0)
            cpt += 1
        elif cpt > 0:
            texte = texte[:i] + list(int_to_bijbin(cpt)) + texte[i:]
            cpt = 0
        else:
            i += 1
    if cpt > 0:
        texte = texte[:i] + list(int_to_bijbin(cpt)) + texte[i:]
    return texte


def zRLE_decode(texte): 
    texte = list(texte)
    i = 0
    bijbin = []
    while i < len(texte):
        if texte[i] in [ZRLE_ONE, ZRLE_TWO]:
            bijbin.append(texte[i])
            texte.pop(i)            
        elif len(bijbin) > 0:
            texte = texte[:i] + [0 for i in range(bijbin_to_int(bijbin))] + texte[i:]
            bijbin = []
        else:
            i += 1
    if len(bijbin) > 0:
        texte = texte[:i] + [0 for i in range(bijbin_to_int(bijbin))] + texte[i:]
    return texte

            


if __name__ == "__main__":
    bijb = int_to_bijbin(2)
    print(bijb)
    print(bijbin_to_int(bijb))
    abc = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0]
    code = zRLE_encode(abc)
    print(code) 
    decode = zRLE_decode(code)
    print(abc)
    print(decode)

