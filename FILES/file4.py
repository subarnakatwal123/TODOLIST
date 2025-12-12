#create a file story
#ask user to input story
#stop input where user enters nothing
#return top 3 word count like : {python : 3, rakesh : 2, pamil : 1}
storage = dict()
with open("story.txt", "w+") as file:
    while True:
        ask = input("enter: ")
        file.write(ask + "\n")
        if ask == "":
            break
    file.seek(0)
    listed = file.read().split()

    for i in listed: 
        if i in storage.keys():
            storage[i] +=1
        else:
            storage[i] = 1
    top3 = sorted(storage.items(), key = lambda x : x[1], reverse=True)[:3]
    
    file.truncate(0)
    for keys, values in top3:
        file.write(f"{keys} : {values} \n")
    file.seek(0)
    print(file.read())