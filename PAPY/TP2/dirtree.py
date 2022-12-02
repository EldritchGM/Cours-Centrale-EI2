import os

space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '

def print_level(dir, cl, islast = False):
    if cl < 0:
        print(dir)
        return
    if cl > 0:
        print(branch + (cl - 1) * space, end = "")
    if not islast:
        print(tee + dir)
    if islast:
        print(last + dir)

def print_dirtree(path, dir_only, level, length_limit = 1000, current_level = 0, islast = False):
    liste = os.listdir(path)
    print_level(path, current_level - 1, islast = islast)
    if current_level > level:
        return 0
    length_limit -= len(liste)
    if length_limit < 0:
        return 0
    for i in range(len(liste)):
        if i == len(liste) - 1:
            islast = True
        if (os.path.isdir(path + liste[i])):
            length_limit -= print_dirtree(path + liste[i] + "/", dir_only, level - 1, length_limit, current_level = current_level + 1, islast = islast)
        elif not dir_only:
            print_level(liste[i], current_level, islast = islast)
    return(len(liste))


if __name__ == "__main__":
    print_dirtree("./../../../", True, 100, 100)

