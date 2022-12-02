class ListNode:

    def __init__(self, symbol = None, next = None):
        self.symbol = symbol
        self.next = next

    def insert_front_node(self, node):
        node.self = self
        return node
    
    def insert_front_symbol(self, symbol):
        self_next = self.next
        self_symbol = self.symbol
        new_son = ListNode(self_symbol, self_next)
        self.symbol = symbol
        self.next = new_son

    def delete_next(self):
        if self.next is None:
            pass
        elif self.next.next == None:
            self.next = None
        else:
            tmp = self.next.next
            self.next = tmp
    
    def find_npi(self, elt, parent = None, occ = 0):
        if self.symbol == elt:
            return (self, parent, occ)
        elif self.next == None:
            return None
        else:
            return self.next.find_npi(elt, self, occ + 1)
    
    def find_np(self, indice, parent = None):
        if indice == 0:
            return (self, parent)
        elif self.next is None:
            return None
        else:
            return self.next.find_np(indice - 1, self)

    @classmethod
    def from_liste(cls, liste):
        if liste == []:
            return None
        else:
            return ListNode(liste[0], cls.from_liste(liste[1:]))
    
    def __repr__(self):
        if self.next == None:
            return str(self.symbol)
        else:
            return f"{self.symbol} {str(self.next)}" 
    

def mtf_encode_rec(liste, texte):
    if texte == []:
        return []
    else:
        node, parent, index = liste.find_npi(texte[0])
        front_symbol = node.symbol
        if parent is not None:
            parent.delete_next()
            liste.insert_front_symbol(front_symbol)
        return [index] + mtf_encode_rec(liste, texte[1:])



def mtf_encode(texte, alphabet = range(257)):
    liste = ListNode.from_liste(list(alphabet))
    texte = [ord(lettre) for lettre in texte]
    code = mtf_encode_rec(liste, texte)
    return code

def mtf_decode_rec(liste, code):
    if code == []:
        return ""
    else:
        node, parent = liste.find_np(code[0])
        front_symbol = node.symbol
        if parent is not None:
            parent.delete_next()
            liste.insert_front_symbol(front_symbol)
        return f"{chr(front_symbol)}{mtf_decode_rec(liste, code[1:])}"


def mtf_decode(code, alphabet = range(257)):
    liste = ListNode.from_liste(list(alphabet))
    # code est déjà des chiffres
    texte = mtf_decode_rec(liste, code)
    return texte

if __name__ == "__main__":
    alphabet = [ord(letter) for letter in "abcde"]
    code = mtf_encode("cccdc", alphabet)
    print(code)
    decode = mtf_decode(code, alphabet)
    print(decode)
