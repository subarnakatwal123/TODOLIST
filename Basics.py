## conditioning and branching

#comparision operators ==, !=, >, <, >=, <=
a = 3 
b = 4 
if (a !=b ): 
    print(False)

else : 
    print(True)

# logic operators : AND OR NOT
age = 18
limit = 20
nationality = "Nepali"

print(age >= limit and nationality == "Nepali")
print(age >= limit or nationality == "Nepali")
print(not( age >= limit and nationality == "Nepali"))
    
print(30*"*", " LOOP FROM HERE " ,40*"*")

for x in range(4, 20,4) : 
    print(x)


listing = ["red", "yellow", "green"]

for i, values in enumerate(listing):
    print(i, values)


print(30*"*", "WHILE LOOP ", 30*"*")
i = 0
listsingd = [1,2,3,4,5,6,7,8,9,10]
even =[]
while  i<len(listsingd):

    if (listsingd[i] % 2 == 0):
        even.append(listsingd[i])
    i+=1

print(even)
    
print(30*"**", "start of question", 30* "**")

#1 print all even numbers from 1 to 50 
listed = []
for i in range (1,50):
    if i % 2 == 0:
        listed.append(i) 
        print(i)

#2 print the sum of all numbers in a list without using sum ().
# we have listed list to take to solve this question.
print(listed)
# using sum () 

print(sum(listed))
add = 0
#without using sum()
for value in listed:
    add += value

print(add)

#3 Reverse a list using only loop no slicing
print("normal list : ", listed)
rev_listed = []
for value in listed:
    rev_listed.insert(0,value)

print(rev_listed, "\n \n")

#4 count how many numebrs are greater than 10 in list : using loop
nums = [3, 12, 9, 18, 7, 21, 5]
count2 = 0
for value in nums:
    if value > 10 : 
        count2+=1
    
print(count2)

#Take a list of names and print only those names with more than 4 letters.
names = ["rahul", "binod", "simesh", "ritesh", "rewanta", "prajwol", "ram", "sam"]

for value in names:
    if len(value) <= 3:
        print(value)


#convert data into tuple and again list print (type each time) 
data = [1, 2, 3, 4, 5]
tupled = tuple(data)
print(type(tupled ), " finally tuppled")

retupled = list(tupled)
print(type(retupled), "finally re listed")

##  Find common and unique elements from the list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)
unique = set(list1).difference(list2)

print(common, "\n", unique)


#remove duplicates using sets 
nums = [1, 2, 2, 3, 4, 4, 5]
print(nums, "original list")
print(set(nums), " removed duplicates")



#create a set of all unique letters

text = "python programming"
unique_sets = set()

for values in text:
    unique_sets.add(values)

print(unique_sets)


##
print("****" *30, "LEVEL MEDIOCORE ", 30*"****")


###Frequency Counter (Dictionary + Loop)

#👉 Given a list of numbers, count how many times each number appears and store it in a dictionary.
nums = [1, 2, 2, 3, 3, 3, 4, 1]
# Output: {1: 2, 2: 2, 3: 3, 4: 1}
dicted = {}


for key in nums:
     if key in dicted:
         dicted[key] +=1
     else : 
         dicted[key] = 1


print(dicted)

#Given a string, count how many times each letter appears (ignore spaces and make everything lowercase).
text1233 = "Python Programming"
text123 = text1233.replace(" ", "")
# Output: {'p':2, 'y':1, 't':1, 'h':1, 'o':2, 'n':2, 'r':2, 'g':2, 'a':1, 'm':2, 'i':1}
diction = {}

for value in text123:
    if value in diction:
        diction[value] += 1
    else: 
        diction[value] = 1

print(diction)




#3 challenge : take 2 sentences and find out common words from 2 sentence 

sentence1 = "i love my wife"
sentence2 = "i love my girlfriend"

set_1 = set(sentence1.split())
set_2 = set(sentence2.split())

common_worlds = set_1 & set_2

print(common_worlds)


#4 remove duplicates and sort alphabetically

names12= ["ram", "shyam", "hari", "ram", "sita", "hari", "gita", "shyam"]

setednames12 = set(names12)

listeeee = list(setednames12)
listeeee.sort()
print((listeeee))



#5 challegne levl : mediocre 
# merge 2 dictionary 
dict9 = {'a': 2, 'b': 3, 'c': 1}
dict10 = {'a': 5, 'b': 1, 'd': 7}

for keys in dict9: 
    if keys in dict10:
        dict10[keys] += dict9[keys]
    else : 
        dict10[keys] = dict9[keys]

print(dict10)


 

 #merge 2 tuple into dictionarly

tople1 = ("ramesh", "uncle", "ko", "choro")
tople2 = (22,44,11,33)

dictionary9u23 = {}

for i in range(len(tople1)):
    dictionary9u23[tople1[i]] = tople2[i]

print (540* "*")
print(dictionary9u23)

# another way to connect / merge two list into a tuple
# using zip 
dictionary03 = dict(zip(tople2,tople1))
print(dictionary03)



#7 challenge 7 here we go again

'''Challenge 7: Find the Most Frequent Number
You’ll take a list of numbers and find which 
number appears the most times — without using a
ny fancy built-in like max(dict, key=dict.get) 
(we’ll do that later for pro version 😉).
'''

challenge7 ={}
numse = [2, 3, 2, 5, 3, 2, 5, 5, 5]

for i in numse:
    if i in challenge7:
        challenge7[i]+= 1
    else:
        challenge7[i] = 1
    
max = 0
set420 = set(numse)
list420 = list(set420)
print(challenge7)
for i in (challenge7):
    if challenge7[i] > max :
        max = challenge7[i]
        count3 = i
    
print(f"maximum number of repeteated is {count3} with {max} repetation")




## shortcut method : to find out the most highest values in list : 
'''

mostfreqnt = max(nums1, key =nums1.count)
print(mostfreqnt)
'''

# long cut revision
erosenge = [1,2,3,4,5,6,7,8,9,0,2,2,3,4,4,4,4]
# how to count the largest repeteative in list ? erosenge ??? 
#we go dictionary 🤣🤣

erosenge_dic = {}  # initialize empty dictionary
highest = 0
repeat = 0
for value in erosenge:
    if value in erosenge_dic:
        erosenge_dic[value] +=1
        if erosenge_dic[value] > repeat:
            repeat = erosenge_dic[value]
            highest = value
    else : 
        erosenge_dic[value] = 1

print(erosenge_dic)

print(f"the highest repeated is {highest} and the number of repeat is {repeat}")


list = ['apple', 'banana','kerry', 'cherry']
sorted_list = sorted(list, key =len, reverse = False)
print(sorted_list)































































































































































