# list are mutable - > we can change the value in list
lists = [2,32,1,42,23,123,24,53,234,2,123,234,234,2,342,23]
lists[4] = 5213 # we can change the value of list

print(lists[4])
 
#Slicing in the Lists 

print(lists[3:7])

#can we concatenate the lists ? 

alpha_list = lists + [23,42,1,34,2]

print(alpha_list)

### METHODS OF LISTS  - > Adding, removing, searching, counting, sorting , reversing, coping and slicing

Test = [1,2,3]
Test.append([     "4","5"])  # APPEND  -- > to add at the end of the list.
print(Test)
Test.insert(0,"RAMA RAMA")

print(Test)

# TO ADD MULTIPLE AT ONCE

Test.extend(["lauda surr", "gauda surr"])

print(Test)
print(Test.count("RAMA RAMA"))

# TO DELETE AT LISTS

del Test[3]  # delets at particular index
print(Test) 

Test.pop()  # removes the end items 

print (Test)
Test.pop(0) # removes at the particular index

print (Test)

imposter = ["Rahul", "Shyam", "radhe", 6, 6,2,5]

print(imposter.count("Rahula")) # returns boolean values true or false ? if available 1 if not 0 
print(imposter.index(6)) # returns the index of first match from the lists. 





### ### SORTING AND REVERSING
Plain = [1,3,52,23,62,123,231,582,123,15,0,2,3,12]
Plain.sort()        # ascending order sort
print(Plain)
Plain.sort(reverse=True) # descending order sort
print(Plain)

Plain.reverse() #reverses the order of the current lists.
print(Plain
      )


# can we copy Plain list ? 
# ABSOLUTELY

COPIED = Plain.copy()

print(COPIED)


# cannot convert list into a list however we can convert a string into a list Like : 
stringhere = "a boy is a male"
print("heres the list of stringhere : ", stringhere.split())


#Alissing
aliasing = ["gandu", 23, 23492, "bandu"]
bliasing = aliasing
aliasing[0] = "pandu"

print(bliasing) # since bliasing is also pointing to the same list that aliasing is pointing once we cahnge the vlaues of any of them the main list changes.


aliasing.extend(["4234"])
print(aliasing)

print(len(aliasing))

print("rama".find("a"))

#print(aliasing.sort(reverse=True)) ## ERROR ( TYPE ERROR )


## FLATTENDING ? ? HARDQEUS

data = [1, [2, [3, 4], 5], 6, [7, 8]]

## print [1,2,3,4,5,6,7,8]



gaddari = [1,2,3]
aadhari = gaddari[:]
gaddari[1] = [0]
print(aadhari)

sumed = [1,2,3]
print(len([sum([1,2,3])]))


EXCEPTION HANDLING learn