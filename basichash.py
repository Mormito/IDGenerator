from filereader import *

def main():
    print('''
1 - Turn in hash (One Name)
2 - Turn in hash (A list)
''')
    
    option = int(input(">> ").strip())
    if option == 1:
        global name
        print("Insert name")
        name = input(">> ").strip()
        turnInHash()
    elif option == 2:
        turnListInHash()


def turnInHash():
    array_name = list(name)

    i = 0
    for letter in array_name:
        i += ord(letter)

    print("Name: " + name)
    print("ID: " + str(i))

def turnListInHash():
    global name
    content = filereader()

    for line in content:
        name = line.strip() 
        if name:
            turnInHash()
        
main()

    