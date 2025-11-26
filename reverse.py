# COOL WAY TO REVERSE A list

listed = ["2", "23", "22", "10", "99"]
## special notes : carefully see what happens to default values when start and is is done in python.

print(listed[::-1]) # start is -1 and end is end of the lists
print(listed[::1])  # start is 0 and end is the end of the list 


Excamples = ['A', 'B', 'C', 'D', 'E', 'F']
'''
Get ['A', 'B', 'C'] using slicing.

Get ['C', 'D', 'E'] using slicing.

Get ['F', 'E', 'D'] using slicing (hint: step is negative).

Get every 2nd element → ['A', 'C', 'E'].

Reverse the list using slicing.

'''
print(Excamples[:3])
print(Excamples[2:5])
print(Excamples[-4::-1])
print(Excamples[::2])




'''
Get [20, 40, 60]

Get [70, 50, 30, 10]

Get [30, 20] (hint: backward slice)

Get the middle three numbers [30, 40, 50]

Get everything except the first and last elements.
'''

nums = [10, 20, 30, 40, 50, 60, 70]

print(nums[1::2])
print(nums[::-2])
print(nums[-5:-7:-1])
print(nums[2:5:])
print(nums[1:6:])

'''
Using slicing, get ['f', 'd', 'b'] (skipping 1 each time backwards).

Using slicing, get every 3rd element in reverse order.

Reverse the list but skip every alternate element → ['g', 'e', 'c', 'a'].

Get the last 3 elements in normal order.

Get the last 3 elements in reverse order.

'''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters[-2::-2])
print(letters[-3::-3])
print(letters[::-2])
print(letters[4::])
print(letters[:-4:-1])

'''
Write a slice that returns only the even numbers (by their positions, not values).

Write a slice that returns the list in reverse order but skips every 3rd element.

Get [7, 6, 5, 4] using slicing only.

Get [3, 4, 5, 6, 7] using slicing (use both positive and negative indexes).

Try to get an empty list using slicing but without using [] (hint: make start and end same but not 0).
'''

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(data[::2])
print(data[::-3])
print(data[3:8:])
print(data[3:3])


