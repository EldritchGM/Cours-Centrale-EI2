def moyenne(*args):
    somme = 0
    for note in args:
        if (type(note)==int) or (type(note)==float):
            somme += note
        else:
            raise AssertionError
    return somme/len(args)

def crier(string):
    return string.upper()

def chuchoter(string):
    return string.lower()

text="Bonjour"

def salutations(f):
    return f(text)

print(salutations(crier))
print(salutations(chuchoter))

def log(func):
    name = func.__name__

    def logged_func(*args,**kwargs):
        resultat = func(*args,**kwargs)
        print(f"Fonction {name} appelée avec les arguments positionnels {*args} et les arguments par mot-clé {**kwargs}")
        print(f"Résultat: {resultat}")
        return resultat

    return logged_function

@log
def salutations(f):
    return f(text)

print(salutations(crier))
print(salutations(chuchoter))