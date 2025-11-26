#SETS 
alpha = {"ram", "shyam"}
print(type (alpha))

#converting tuple, list and string in set


String_here = "ramesh"
list_here = ["ramesh"]
tuple_here = ("ramesh")


set1 = set(String_here)
set2 = set(list_here)
set3 = set(tuple_here)
print(type(set1), type(set2),type( set3))


##accessing set elements in sets 

for i in alpha:
    print(i)


print(300*"/")
print("yes" if "ram" in alpha else "no")


alpha.add("Ramesh uncle ko xora")

print(alpha)

alpha.remove("shyam")

print(alpha)

print("ram" in alpha)


## common how to take common on 2 sets ??? 

print("*" * 200)

set1  = {1,2,3,4,5,6,8}
set2  = {2,4,1,5,6,2,234,2,1,2,31}
set3 = set1 & set2


print(set3.issubset(set1))

set1 = {4,2,3,1}
set1.add(5)
print(set1)

listed = [10, 1, 99, 2, 45, 7, 3]

set23 = set(listed)
print(set23)

sum1 = sum(set1) 
sum2 = sum(set2)

print(sum1 == sum2)

trail = {2,3,4}
trail.update((2,45))
print(trail)

my_name = {"rama", "kumar"}
her_name = {"sita", "kumar"}
unique = my_name | her_name
print(unique)




