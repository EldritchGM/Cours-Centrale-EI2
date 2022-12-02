def main():
    print(len(contents("pg5097.txt")))

def contents(file_name):
    with open(file_name, 'rb') as file:
        text = file.read()
        return list(text)



if __name__ == "__main__":
    main()