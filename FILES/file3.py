#Create a file called students.txt and write the names of 5 students into it (one name per line). Then, read the file and print all names.
with open("filetesting.txt", "a+") as test:
    test.seek(0)
    abc = test.read()
    if "1" in abc:
        print(abc.index("3"))
    print(abc)

