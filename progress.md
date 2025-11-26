## progress tracer 
## Helloworld - input output data types
--> integer float double string boolean(0 1 | T F)
## Typecasting 
-- > chainging from integer to float or float to integer
## Float division and integer division
6/3 = 2.0 ( float division )
6//3 = 2 ( integer division ) so double slash is a integer division ( no remainder)
## Expression and Variables 
+ - * / // % is mathemetical expression combined with numbers (A+B) is an expression.
variable are those names given to an expression 

## Output techniques 
\n -- > is a new line when printing 
\t -- > is a tab line when printing 
if we want to print "\" either we have to put two \\ or "r" like : print(r"printing\");

## String ( A powerful one): can be representated by single quotes or double 'a' or "a" both are corect 
# string methods
variable.upper()
variable.replace("a", "b")

# string indexing 
indexing of string is done starting 0 to n number of words in the string like : 
string = S U B A R N A K A T W A L 
         0 1 2 3 4 5 6 7 8 9 10 11 12 :
         OR you can also use negative indexing which is new to me : 
         -13 -12 -11 -10 -9 -8 -7 -6 -4 -3 -2 -1 ( negative indexing )

# in python we can do negative indexing ( last element is -1 and first element is -1-(+n)) as shown above example ( negative indexing)

# string slicing
slicing refers to extraction of a portion or subsequence from a string. 
format to extract string is : string[starting index : ending index : steps] ex: 
A = "Its all illusion"
print(A[3:7:2]) # string stride
string slicing [start : end]
string stride [start : end : steps]

String slicing and stride are same concepts with steps being extra at string slicing.

# string concatenation 
joining 2 string is called string concatenation here we add one string with another 
A = "subarna" 
B = "katwal" 
C = A + B ( subarn katwal ) string added A and B

# strings are immutable 
once a string is created we cannnot change its values. like : 
A = "subarna" 
we cannot change A[0] = "S" --> it will throw an error. 

# strings : Escape sequences 
\n -- > new line 
\t -- > gives a tab when printing 
to use \ escape sequence you can use double backslash when printing like "\\"

# string methods
String methods are build in functions in python to perform specific operation or manipulation on strings. some are : 
string.upper(); --> chagnes the values of string into upper case.
string.lower(); --> changes the values of string into lower case.
string.strip(); --> removes unnecessary spaces from string.(right left side not from the middle)
string.find (); --> gives output if its avialable ( returns index of the first found string) 
string.replace("a", "b"); --> changes the string a with b. 

# string interpolation
its a process of inserting variable and expressions inside the string, so you can create dynamic messages or formatted text easily.
syntax : 
name = "radhe"
print(f"my name is {name}")
We can do basic operation on Name : the name is executed like name + name 

# raw string 
when using escape sequences we might face issues of using "\" we cannot always do double back slashes. so we can use raw string to solve this problem. 
like if we are working with drives in computer we need to add backslashes too many time so something it may use \n or \t certainly with some operation to solve this we are using raw string. Example : - 
normal = C:\new_tab\file.txt
print (normal)

gives output : 
C:
ew_tab
ile.txt
Raw_string example = r"C:\new_tab\file.txt"
print (Raw_string)
output : C:\new_tab\file.txt

So in raw string we don't face any issues with back slash or escape sequences.

# string split

string.split (seperator, maxsplit)

# string joined


## REGEX

Regex (regular expression) is a pattern matching language used to search, find, and manipulate text based on specific patterns. We can find it as a smart search tool that lets us find words or characters that match rule, replace splits or validate string. 
# regex functions : 
Object in regex : 
- re.findall ("what to search" , " where to search" ) # findall function matches exact match and returns if its available in the targeted search.
- re.split ()
- re.match ()
- re.finditer ()
- re.search () -- > returns the index of pattern start to end for the first match element. "none" if not found.

keys to search : 
\d == digits 
\w == words
\s == tab / whitesapces
+  == one or more repeats
\b == boundary of a word like if it has a sentence and we need to find a lower case words in the sentence we use boudndar \b mango \b to take whole word as a boundary which is lower case in the sentence.

Note : even space in regex / raw data will mess your contitional / And or Not statement

Meta characters in Regex
+ : shows words with at least one repeat
* : shows words with matches one or none

### DATA STRUCTURES

## TUPLES
Syntax : first_tuple = (1,2,2,2,2,2,,32,32,,324,2,3) or ("ram", "shyam","sita", "hari", "bishnu")
they can be accessed through index each elements.

#we can keep any kind of value in tuple like string float or integer anything. ex : tuple = ("ram", 1, 2.3232) ✅

# Concatenating in Tuples
RAM = ("apc", 0, 23.32) + ("holley", 23) == > RAM = ("apc", 0, 23.32, "holley", 23)

# Slicing in tuples - we can do slicing in tuples too. [start:end:steps] same as in string, 
we can convert tuples into string with no problem but can't convert it to int or float as it gives typeerror

## LISTS
Syntax : first_lists = [1,2,3,4,5] or ["alpha", "beta", 123,43]

# Concatenating in Lists ? _ > yes its possible to concatenate the lists :: Syntax - concatenated list = first_lists + [23,234,123]

# Slicing in lists ? _ > yes same way as tuples we can do concatenatiing like we did in tuples or string.

METHODS OF LISTS  - > Adding, removing, searching, counting, ing , reversing, coping and slicing
# APPEND  -- > to add at the end of the list. lists.append("allu")
# INSERT  -- > adds to particular index. syntax :  ( 1, "allu")
METHODS OF TUPLES - > Accessing values, counting, finding, slicing, tuple unpacking, joining tuples. 


# REFERENCING #### ALIASING
If we do, 
A = ["alpha", 4, 343, "unchanged"] // defining a lists
B = A                              // assigning a complete list to B
A[0] = "GANDU"                     // # to be noted : B is pointing to the list stored in A (its the same list both are pointing)

print(B) // will print same thing as print A // both are changed since both are referencing same list.


### DICTIONARY 
Dictionary in python are a group representated by curly braces {}
dictionary = {}

how are values stroed inside dictionary ? ?? 
There are two elements in dictionary : 
Keys : Values 
Keys are immutable and always unique 
Values can be immutable, mutable and duplicates too. 

syntax : 
# dictionary = {"alpha" : 234, "beta" : 2342, "rita" : "sita"}
To print keys : use key keywrod 
Syntax : 
For key int dictionary: 
print ( key ) 

To print values : use value keyword 
syntax:
for value int dictionary : 
print ( values ) 

if you want to print both key and values use items () : 
syntax : 
for key, value in dictionary.items():
    print(key, value)

## How to delete keys ? or values ?

To delete values use : 
del dictionary ["keys"][index if its list(optional)]

dictionary[key].remove("values") # deletes by values in dictionary

dictionary[key].pop(index) # to delete by indexing on certain lists 

To delete keys : 
del dictionary[key] // deletes keys + stored values in this key.

## how to insert ? values or keys ?
dictionary[key] = "alparam"
dictorny[key].append(values) or insert(index, "values") ## if its to insert in lists.


## SETS 
sets don't store duplicates values 
like i said its denoted by : syntax -- > sets = {"alpha", "beta", "gama"}
if we do a duplicate values multiple times then set will ignore the duplicates and removes duplicates automaticallly. 

Syntax is similar to dictionary but there is not keys and values as though in dictionary   

how to  insert in sets ? 
set.add(123) ## if you want to enter a single values
set.update([1,2,4,2])   # if you want to enter a list or multiple values you should enter it into a set.

funcations in sets :: 
set1.issubset(set2) # checks if its subset of set2
set1.issuperset(set2) # checks if set1 is superset of set2
set3 = set1.union(set2) # addds nonrepeatable values to the set3 combining both set1 and set2

# SORTED ? 
how do sorted function works ? 
sorted takes at least one variables or at max 3 variables 
## SORTED (what to sort, key = on what basis ? like length of string, reverse= true or false)
Syntax : 
list = ['apple', 'banana','kerry', 'cherry']
sorted_list = sorted(list, key = len, reverse = false) it reverses on the basis of length of the string



# EXCEPTION HANDLING

Value Error : caused due to wrong value enters like if we assign string into an integer variable 

Type Error : 
