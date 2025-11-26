'''Step 1: Basic Loops – Repetition & Simple Counting
Problem 1: Print Sales Report

Description:
You have daily sales for a week: [200, 150, 300, 250, 400, 500, 450]

Print each day’s sale with day number: Day 1: 200

Calculate total and average sales using a loop.

Concepts Learned:

for loops, indexing, running totals'''
Sales = [200, 150, 300, 250, 400, 500, 450]

average = 0
total = 0 

for i in range(len(Sales)):
    print(f"Day {i} : {Sales[i]} ")
    total += Sales[i]

average = total / len(Sales)
print(total, f" is the total & avearge is {average}")

o= 5
for i in range (1, o+1):
    spaces = o - i
    uppe_stars = 2 * i - 1
    print(" "* spaces + "*" * uppe_stars)

# print start pyramid
n = 5 # number of rows to print
for i in range(0, n+1):
    spaces = i
    stars = 2 * (n - i) - 1
    
    print(" " * spaces + "*" * stars )


'''
Problem 2: Even/Odd Categorizer

Description:

Input a list of numbers from user.

Print separately the even and odd numbers.

Count how many even and odd numbers are present.

Concepts Learned:

if inside loop, counting, lists

'''

# take inputs from user
user_inputs = []
while True:
    a = input("enter into a list ")
    if a == "":
        break
    user_inputs.append(a)
print(user_inputs)


#another one : 
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
score = PlayListRatings[0]
i = 0
while score > 6:
    if PlayListRatings[i] < 6 and i < len(PlayListRatings):
        break
    else:
        print(PlayListRatings[i])
        i+=1

"""
Problem 10: Voting Counter

Description:

You have a list of votes: ["A", "B", "A", "C", "B", "A"]

Count votes for each candidate using dictionary

Print winner (highest votes)

Concepts Learned:

Loops + dictionaries + comparison + max

"""
votes = ["A", "B", "A", "C", "B", "A"]
count = {}
for i in votes:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
winner = sorted(count.items(), key = lambda x: x[1], reverse=True)
print(winner[0][0])






