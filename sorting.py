## learn to sort in different ways using sorted specially

list = [1,3,2,2,4,5,34,4]
slist = sorted(list)
print(slist)
# sort this list by string length

names = ["ram", "shyam", "hari", "sita", "krishna"]

snames = sorted(names, key = len, reverse= False)

print(snames)

#sort this list of tuples by second value
pairs = [(1, 3), (2, 1), (4, 2)]

sparis = sorted(pairs, key = lambda x:x[1], reverse=False)
print(sparis)

# sort them by age 
people = [
    {"name": "ram", "age": 22},
    {"name": "shyam", "age": 19},
    {"name": "hari", "age": 25}
]
speople = sorted(people, key = lambda x:x['age'])
print(speople)

#sort this list by their last letters
words = ["apple", "ball", "cat", "dog", "mango"]
swords = sorted(words, key = lambda x:x[-1], reverse=False)
print(swords)

#sort it by its absolute value 
nums = [-10, 5, -2, 3, -7]
snums = sorted(nums, key = abs)
print(snums)

#sort this list based on the numbers of words present
sentences = [
    "I love python",
    "This is easy",
    "Sorting with lambda is fun",
    "Hi"
]

ssengtence = sorted(sentences, key= lambda x:len( x.split()), reverse= False)
print(ssengtence)

