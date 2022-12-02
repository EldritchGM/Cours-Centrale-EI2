import reader, priority
import time
NEUTRE = -1 #symbole d'un noeud qui n'est pas une feuille
HUFFMAN_MARKER = 259


class HuffmanTreeNode:
    def __init__(self, symbole, occurence, left = None, right = None):
        self.symbole = symbole
        self.occurence = occurence
        self.left = left
        self.right = right
        self.codemap = [None for i in range(260)]
        
    
    def __mul__(self, other):
        return merge(self, other)
    
    def __lt__(self, other):
        return less(self, other)

    def __repr__(self):
        return f"{self.symbole} : {self.occurence}"
    
    
    def build_codemap_rec(self, current = "", res = [None for i in range(260)]):
        if self.symbole == NEUTRE:
            if self.left != None:
                res = self.left.build_codemap_rec(current + "0", res)
            if self.right != None:
                res = self.right.build_codemap_rec(current + "1", res)
        else:
            res[self.symbole] = current
        return res
    



def merge(N1, N2):
    """
    N1 et N2 sont des Huffman Tree Node
    merge renvoie un noeud ayant pour fils N1 et N2
    On associe à ce nouveau n÷ud la somme des nombres d'occurrences de x et y
    """
    new_node = HuffmanTreeNode(NEUTRE, N1.occurence + N2.occurence)
    new_node.left = N1
    new_node.right = N2
    return new_node

def less(N1, N2):
    return N1.occurence < N2.occurence




class Huffman:
    def __init__(self, tree = None):
        self.tree = tree
        self.codes = self.tree.build_codemap_rec()
    
    @classmethod
    def build_tree(self, file):
        #On construit d'abord la liste des noeuds
        content = reader.contents(file)
        occurences = {}
        for i in range(256):
            occurences[i] = 0
        occurences[HUFFMAN_MARKER] = 1
        for character in content:
            occurences[character] += 1
        trees = priority.PQUEUE(less, 257)
        for character in occurences:
            if occurences[character] > 0:
                trees.insert(HuffmanTreeNode(character, occurences[character]))
        #puis on fusionne
        while trees.size > 1:
            x = trees.extract_min()
            y = trees.extract_min()
            trees.insert(merge(x,y))
        return Huffman(trees.extract_min())
    
    def __repr__(self):
        return str(self.tree)
    
    def encode(self, file):
        with open(file, "rb") as file:
            texte = file.read()
            res = ""
            for letter in texte:
                res += self.codes[letter]
            res += self.codes[HUFFMAN_MARKER]
            res += "0" * (8 - len(res) % 8)
            binary_list = []
            for i in range(0,len(res),8):
                binary_list.append(str_to_bin(res[i:(i+8)]))
            return binary_list
    
    def decode(self, binary_list):
        texte = "".join([bin_to_str(b) for b in binary_list])
        packet_length = 1
        res = []
        while len(texte) > 0:
            packet = texte[0:packet_length]
            if packet in self.codes:
                res.append(self.codes.index(packet))
                if res[-1] == 259:
                    break
                else:
                    texte = texte[packet_length:]
                    packet_length = 1
            else:
                packet_length += 1
        return "".join([chr(c) for c in res[:-1]])
            




def str_to_bin(s):
    """
    s est un string composé d'exactement huit 0 et 1.
    """
    b = 0b00000000
    for i in range(len(s)):
        b = b << 1
        if s[i] == "1":
            b |= 1
    return b

def bin_to_str(b):
    b = bin(b)
    s = f"{'0' * (10 - len(b))}{b[2:]}"
    return s

if __name__ == "__main__":
    texte = reader.contents("test.txt")
    print(texte)
    before = time.time()
    H = Huffman.build_tree("test.txt")
    res = H.encode("test.txt")
    print(res)
    print(H.decode(res)[:1000])
    print(time.time() - before)


