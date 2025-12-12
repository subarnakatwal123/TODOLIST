# try:
#     g = open("abcd.txt")
#     print("file opened successfully")

# except Exception as e:
#     print(f"error {e} has occured")



#readlines 
try : 
    with open("abc.txt", "r+") as file:
        file.truncate(0)
        content = file.write("i am the new content king")
        file.seek(0)
        bullet = file.read()
        print(type(bullet))
        file.seek(0)
        print(file.read())
        file.write (" this is the end")
        file.seek(0)
        print(file.read())
        file.write("this is the start" + bullet)
        file.seek(0)
        print(file.read())
        with open("abc.txt", "w+") as newopen:
            newopen.write("look whos here")
            newopen.seek(0)
            print(newopen.read())
        file.seek(0)
        print(file.read())
#         ## expected output : "i am the new content king" 

# i am the new content king
# i am the new content king this is the end
# this is the starti am the new content king this is the end

except Exception as e:

    print(f"{e} has occurred")

