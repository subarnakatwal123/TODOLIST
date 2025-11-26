## Dictionary in Python
dictionarye = {"alpha" : (234, 234), "beta" : [2342], "rita" : {"sita": 2}}
print(dictionarye)
print(type(dictionarye["rita"]))

print(dictionarye.keys())   # prints out all the keys [ excluding values inside the dictionary]
print(dictionarye.values()) # prints out al the values [ excluding keys inside of the dictionary]
## DICTIONARY BASICS 

storage = {"name": "", "age" :"" , "country" :"" }
print(storage)

storage["subject"] = "python"
print(storage)

storage["age"] = 28
print(storage)
print(type(storage["age"]))
storage["age"] += 28
print(storage)
print(type(storage["age"]))

storage["name"] = "Subarna Katwal"
print(storage)

storage["country"] = "Nepal"


if "ramu" in storage:
    print("exists")
else: 
    print("noexists")

print(storage)
del storage["name"]
print(storage)

for key in storage: 
    print(key)

for value in storage:
    print(value)

for key, value in storage.items(): 
    print(key, value)
   

print(storage)
almo = storage.copy()
print(almo)

##########

details = { "name" : "subarna", "address" : "Kathmandu", "phone": [8342342], "courses" : ['Network', 'python', 'Linux']}

(details["courses"].pop(1))
print(details)


# or use del keyword to delete
del details["phone"]


print(300*"*")

print("how to delete keys")

del details["name"]
print(details)


print(200*"*")


##### how to insert in dictionary 

details["religion"] = "hindu" # simple insertion

print(details)

details["listing"] = [1,2,3,4,"katta"]
print(details) 
details["listing"].insert(0,"surugaru")   #inserting into the list with list techniques.

print(details)



dictiondddd = {1:1}
print(dictiondddd)
print(type(dictiondddd))


dictasdladfa = {"ramesh" :[342,2342], "kalesh" :[234, 5838]}
print( 342 in dictasdladfa["ramesh"])