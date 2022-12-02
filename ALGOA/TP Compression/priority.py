class PQUEUE:
    def __init__(self, comparateur, s):
        self.comparateur = comparateur # fonction de comparaison
        self.tableau = []
        for i in range(s):
            self.tableau.append(None)
        self.size = 0
        self.max_size = s
    
    def insert(self, elt):
        if self.size == self.max_size:
            raise IndexError("heap is full")
        else:
            self.tableau[self.size] = elt
            self.size += 1
            self.heap_fix_up(self.size - 1)

    def heap_fix_up(self, i):
        p = (i - 1) // 2
        while p >= 0 and self.comparateur(self.tableau[i], self.tableau[p]):
            tmp = self.tableau[i]
            self.tableau[i] = self.tableau[p]
            self.tableau[p] = tmp
            i = p
            p = (i - 1) // 2

    def extract_min(self):
        popped = self.tableau[0]
        self.tableau[0] = self.tableau[self.size - 1]
        i = 0
        left = 2 * i + 1
        right = 2 * i + 2
        #on s'assure qu'on ne sort pas du tableau
        if left >= self.size: left = i
        if right >= self.size: right = i
        while (i < self.size) and (left > i and left < self.size and self.comparateur(self.tableau[left], self.tableau[i])) or (right > i and right < right < self.size and self.comparateur(self.tableau[right], self.tableau[i])) :
            if self.tableau[right] == None or self.comparateur(self.tableau[left], self.tableau[right]):
                # on descend à gauche
                tmp = self.tableau[i]
                self.tableau[i] = self.tableau[left]
                self.tableau[left] = tmp
                i = left
                left = 2 * i + 1
                right = 2 * i + 2
            else:                #on descend à droite
                tmp = self.tableau[i]
                self.tableau[i] = self.tableau[right]
                self.tableau[right] = tmp
                i = right
                left = 2 * i + 1
                right = 2 * i + 2
                if left >= self.size: left = i
                if right >= self.size: right = i
        self.tableau[self.size - 1] = None
        self.size -= 1
        return popped