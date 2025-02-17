def filereader():
    print("Set a path")
    path = input(">> ").strip()

    print("Set a filename (and .type)")
    filename = input(">> ").strip()

    fullpath = path+filename

    with open(fullpath, "r") as fr:
        content = fr.readlines()
        return content

    