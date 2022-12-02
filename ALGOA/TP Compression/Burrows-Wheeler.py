BLOCKSIZE = 500000
BWT_MARKER = 256


###############################################################
#####################Counting-sort-simple######################
###############################################################

def counter(arr):
    dic = {}
    for i in arr:
        keys = dic.keys()
        if i in keys:
            dic[i] += 1
        else:
            dic[i] = 1
    keys = list(dic.keys())
    keys.sort()
    index = 0
    for key in keys:
        tmp = dic[key]
        dic[key] = range(index, index+tmp)
        index += tmp
    return dic

def sorting(arr,c):
    for i in range(len(arr)):
        while i not in c[arr[i]]:
            supposed_range = c[arr[i]]
            flag = True
            for j in supposed_range:
                if flag and arr[j] != arr[i]: # le je élément du tableau est déjà dans le bon range 
                    print(f"swap {i}&{j}")
                    tmp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp
                    flag = False
    return arr



def counting_sort(arr, btw_marker = None):
    if btw_marker is None: btw_marker = len(arr)
    arr_to_sort = arr[:btw_marker]
    c = counter(arr_to_sort)
    print(c)
    sorted_arr = sorting(arr_to_sort, c)
    return sorted_arr + arr[btw_marker:]




###############################################################
#####################Counting-sort-arrays######################
###############################################################

def counter__Double(arrs, n):
    dic = {}
    for arr in arrs:
        i = arr[n]
        keys = dic.keys()
        if i in keys:
            dic[i] += 1
        else:
            dic[i] = 1
    keys = list(dic.keys())
    keys.sort()
    index = 0
    for key in keys:
        tmp = dic[key]
        dic[key] = range(index, index+tmp)
        index += tmp
    return dic

def sorting__Double(arrs,c,n):
    for arr in range(len(arrs)):
        i = arrs[arr][n]
        while arr not in c[i]:
            supposed_range = c[i]
            flag = True
            for j in supposed_range:
                if flag and arrs[j][n] != i: # le je élément du tableau est déjà dans le bon range 
                    tmp = arrs[arr]
                    arrs[arr] = arrs[j]
                    arrs[j] = tmp
                    flag = False
            i = arrs[arr][n]
    return arrs



def counting_sort__Double(arrs, btw_marker = None, n = 0):
    if btw_marker is None: btw_marker = len(arrs)
    arrs_to_sort = arrs[:btw_marker]
    c = counter__Double(arrs_to_sort, n)
    sorted_arrs = sorting__Double(arrs_to_sort, c, n)
    return sorted_arrs + arrs[btw_marker:]


###############################################################
#####################Counting-sort-rotate######################
###############################################################






def counting_sort__rotate(arr, texte, n = 0):
    arrs = [[i] + list(texte[i:]) + list(texte[:i]) for i in arr]
    sorted_arrs = counting_sort__Double(arrs, None, n + 1)
    sorted_arr = [arr[0] for arr in sorted_arrs]
    c = counter__Double(arrs, n+1)
    return sorted_arr, c


def radix_sort_rec(arr, texte, n = 0):
    if len(arr) <= 1:
        return arr
    else:
        sorted, c = counting_sort__rotate(arr, texte, n)
        keys = list(c.keys())
        keys.sort()
        res = []
        for key in keys:
            range_key = c[key]
            min_ind = range_key[0]
            max_ind = range_key[-1] + 1
            res += radix_sort_rec(sorted[min_ind:max_ind], texte, n+1)
        return res


class frame:
    def __init__(self, array, resultat, super, n, grow):
        self.array = array
        self.resultat = resultat
        self.super = super
        self.n = n
        self.grow = grow
    
    def __repr__(self):
        s = f"{self.array=}\t{self.resultat=}\t{self.n=}\t{self.grow=}"
        try: s+= "\t" + str(self.super.resultat)
        except:
            s += "\t" + f"{self.super=}"
        finally: return s

def radix_sort(arr, texte):
    res = []
    pile = []
    pile.append(frame(arr, [], [], 0, True))
    while len(pile) > 0:
        if pile[0].grow:
            if len(pile[0].array) <= 1:
                if len(pile) == 1: res = pile[0].resultat
                if pile[0].super == []:
                    res = pile[0].resultat
                    break
                else:
                    pile[0].super.resultat = pile[0].array + pile[0].super.resultat
                pile = pile[1:]
            else:
                pile[0].grow = False
                sorted, c = counting_sort__rotate(pile[0].array, texte, pile[0].n)
                keys = list(c.keys())
                keys.sort()
                top = pile[0]
                for key in keys:
                    range_key = c[key]
                    min_ind = range_key[0]
                    max_ind = range_key[-1] + 1
                    pile = [frame(sorted[min_ind:max_ind], [], top, top.n+1, True)] + pile
        else:
            if pile[0].super == []: return pile[0].resultat
            pile[0].super.resultat = pile[0].resultat + pile[0].super.resultat
            pile = pile[1:]
    return res

def bwt_encode_single(texte):
    arr = [i for i in range(len(texte))]
    sorted_arr = radix_sort(arr, texte)
    return "".join([texte[i-1] for i in sorted_arr])

def bwt_encode(texte):
    textes = [texte[i:(i+BLOCKSIZE-1)] for i in range(0, len(texte), BLOCKSIZE - 1)]
    res = []
    for texte in textes:
        res += [chr(BWT_MARKER)]
        res.append(bwt_encode_single(texte))
    return "".join(res)

def Finder(texte):
    res = {}
    for i in range(len(texte)):
        if texte[i] in res.keys():
            res[texte[i]].append(i)
        else:
            res[texte[i]] = [i]
    return res

def find_nth(elt, n, finder):
    """
    finder est un dictionnaire qui a été créé auparavant par la fonction finder qui prend le texte en entrée
    On cherche la nième occurence de elt dans un texte.
    """
    return finder[elt][n - 1]

def find_rank(sorted_texte, index, finder):
    elt = sorted_texte[index]
    rank = finder[elt].index(index) + 1
    return rank



def bwt_decode_block(texte):
    code = [texte[i] for i in range(len(texte))]
    sorted_code = sorted(code)
    finder_code = Finder(code)
    finder_sorted = Finder(sorted_code)

    res = ""

    letter = sorted_code[find_nth(chr(BWT_MARKER), 1, finder_sorted) - 1]
    res += letter
    print(letter)
    rank = find_rank(sorted_code, len(sorted_code)-1, finder_sorted)

    while len(res) < len(code):
        index = find_nth(letter, rank, finder_code)
        letter = sorted_code[index]
        res += letter
        rank = find_rank(sorted_code, index, finder_sorted)
    return res

def bwt_decode(texte):
    codes = [texte[i:i+BLOCKSIZE] for i in range(0, len(texte), BLOCKSIZE - 1)]
    res = ""
    for code in codes:
        if code != "":
            res += bwt_decode_block(code)
    return res








if __name__ == "__main__":
    texte = "simili."
    arr = [i for i in range(len(texte))]
    print(radix_sort_rec(arr, texte))
    sorted_arr = radix_sort(arr, texte)
    print(sorted_arr)
    print("".join([texte[i-1] for i in sorted_arr]))
    code = bwt_encode(texte)
    print(code)
    print(bwt_decode(code))

