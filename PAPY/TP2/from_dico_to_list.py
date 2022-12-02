def dicos_to_list(dicos):
    res = {}
    for dico in dicos:
        for key in dico:
            if key not in res:
                res[key] = []
            res[key].append(dico[key])
    return res

data =  [{'Lea': 'java', 'Bobby': 'python'},
        {'Lea': 'php', 'Bobby': 'java'},
        {'Lea': 'cloud', 'Bobby': 'big-data'}]

def dicos_to_list2(dicos):
    return {key:[dico[key] for dico in dicos] for dico in dicos for key in dico}

print(dicos_to_list2(data))