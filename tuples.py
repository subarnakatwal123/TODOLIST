## tuples  are immutable like string - > we cannot change the values in the tuples.
 
store = ("sugar", 23, 405)
print(store)
print(type(store))

#slicing in tuple
learn = ("ram", "shyam", 234, 23, 2.223, "234")
print(learn[2:6:2])

# we can do tuple concatenation too. 

concatenated = learn + ("ho", "raicha", "!", "kasto achamma ho")

print ( concatenated)
print("length of the tuple : ", len(concatenated))

## NESTING IN TUPLES 

nesting = (1,2,("ram", "sita"), 2,3, ("Bagi", 12))
print(nesting[5][0])

print(len(nesting))


tuppled = [1,2,52]
print(tuppled[1:3])