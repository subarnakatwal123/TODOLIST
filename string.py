## indexing in string

a = "a cat is a domestic animal"
print(a[-2]) # negative indexing gives output "a" negative indexing starts from -1 starting from the last string
print(a[12]) # positive indexing gives output "o" starts from 0 from the start of string
A = "Its all illusion"

#string slicing
print(A[3:10:2]) # expected output " l l" ## slices all the string the starting 3 is where now 0 begins and 10 is the string limits till when the string is calculated, with steps being 2 it only counts from 0+2+2+2 like this

#another string slicing example
B = "this is what it should be"
print(B[::2])  # prints all the elements with just steps 2 expected output from starting to end without any limitation
# expected output -- > ti swa tsol e

#another string slicing example 
# subsequencing the sequence -- > 
actual_String = "MOTI BINDU"
subsecuenced = actual_String[2:6] # only elements starting from 2 index to index 6 is recorded to subsecuenced string
subsecuenced_pro = actual_String[2:] # not giving ending means it will take all string from 2 to the end of the string at actual string
print(subsecuenced)
print(subsecuenced_pro)

print (3*( subsecuenced + subsecuenced_pro)) # string concatenation. ( adding two strings )

d = subsecuenced_pro.lower()
print((d)) # --> string method to convert string into lower case.

print(d.find("z"))

texts = "apple is good for health but not for doctors financial health ?"
replaced = texts.replace("a","b")
print(texts, "\n", replaced)

print(texts.find("doctor")) # as the doctor is present in text it returns the first letter index that means the index of d 

### string interpolation
# recommended way for string format interpolation
name = "Hritik"
City = "kathmandu"
address = "09 sitapur bazar"
phone = 9123129191
phone1 = 2342234222


print(f"my friend name is {name}, he lives in {City}. his exact address is {address}. You can contact him at {phone}")

# another way for string format interpolation
print("my friend name is {}, he lives in {}. his exact address is {}. You can contact him at {}".format(name, City, address, phone))

print(f"the sum of two number {phone} and {phone1} is {phone+phone1}")
print(f"lets do string concatenation {City + address}")  # we can perform operation using the formated string.

normal = "C:\new_tab\file.txt"
raw = r"C:\new_tab\file.txt"
print ("without raw string output of normal is : \n", normal)
print("with raw string method output of raw is :\n ", raw) # gives proper output of the task we are doing.


print(len(normal))
print(len(raw))

# string split -- > seperates string into smaller pieces like : 
# syntax = string.split (seperator , maxsplit) what to keep when seperating and how many times to split
question = "why are you single ?"
answer = question.split(" ", 2)   # What to split and how much to split 
print (answer) 

lists = "apple, banana, carrot, mango, peach, red wine, velvets"
print(lists.split(",", 4))  # heres the comma as a seperator and we need to split it 4 times so 4 is the limit after 4 there is no splittor



#typecasting exmples. 
a = int(2)
ba = float(a)
ca = str(ba) + str(a)
print(a)
print(ca)


# string strip and strip join
alpha = "can you s""trip me ? "
splitted_alpha = alpha.split(" ")
print(splitted_alpha)
print( int(False))
fname = "subarna"
lname = "katwal"
print(fname + " " + lname)

print("python is \"awesome \"")

#slicing revision
estasi = "rameshwor"
print(estasi[3:5])


counted = "strings"

print(len(counted))