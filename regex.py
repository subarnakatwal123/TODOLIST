import re
Store = '''Averyday 1 i login to my laptop LUN just to write a code to gain a limit of boaredom, its hard for me but there isn't another way to conquer Svictory.'''

find = re.findall("college", "alpha male iti college") # find exact matches
print (find)


# Find all digits in:
# "My phone number is 9841234567 and age is 21."
number = " my phone number is 9898989999 and my age is 21"

print (re.findall(r'\d', number))

#  Find all words that start with a capital letter in:
#  "Ram Loves Python And Coding."

name = "Ram Loves Python And Coding."
print(re.findall(r"[A-Z][a-z]*\w", name))

#Find all words that contain only lowercase letters in:
lower = "apple Mango banana Grape orange"
print(re.findall(r"\b[a-z]+\b", lower)) # all lower case

print(re.findall(r"\b[A-Z]+\b", Store)) # all capital words

print(re.findall(r"\b[A-Z]\b|\b[A-Z][a-z]*\b", Store)) # all words that is capital or first letter is capital 

#find all words that contain at least one number (digit).

text = "Ram1 went to room23 and met Sita99 near gate5." 
print(re.findall(r"\b\w*\d\w*\b", text))

#From the given text, find all email addresses 
text1 = "Contact us at ram@gmail.com, info@health.org, or admin123@python.co.in for details."
print(re.findall(r"\b[\w.-]*\@[\w.-]*\b", text1))

datefind = "2024-02-22 and 2024-02-11 are the both dark night days "
pattern = r"\d{4}-\d{2}-\d{2}"

print(re.findall(pattern, datefind))



#search function in regex

patterned = "jadioo"
datea = "l;adoo was a favourite of krish, jadoo i know it was weird english but i am tripped right now"

print(re.search(patterned, datea))

#Find all words that end with “ing” in this text 👇

wordsd = "i in ing ingg inggg ng iing ingg ngg"
print(re.search(r"\bing+\b", wordsd))
print(re.findall(r"\bing+\b", wordsd))

print(datea.find("jadoo"))

