def capital(x): 
    x = int(x)
    
    return x*x

userchoice = 40
print(capital(userchoice))


#greet me! 
def greeet (x):
    return "Hello" + x

name = "raina suerseh"
print(greeet(name))


#even or odd checker 

def checker (x):
    x = int (x)
    if x % 2 == 0: 
        return "Even"
    else: 
        return "Odd"

input_number = 30
print(checker(input_number))

#sum of numbers 
def add(list3):
    sum = 0
    for numbers in list3:
        intedval = int(numbers)
        sum+=intedval
    return sum

list3 = [42,3]
print(add(list3))

#average of numbers 

def average (numblis):
    tot = 0
    for num in numblis:
        tot += int(num)
    if tot == 0:
        return None
    else:
        return (tot / len(numblis))


numlis1 = [13,224,2]
print(average(numlis1))

def taxcalc (item, tax):
    return item + (tax/100 )* item

print(taxcalc(200, 13))

#disc cal
def diccal (x, y):
    amount = int (x)
    dic = int (y)
    return amount - (amount/100 *dic)

print("discounted amount is : ", diccal(200, 10))

# grade calc

def grading (marks):
    if marks >= 90 and marks <=100:
        return "Grade A"
    elif marks >=80 and marks<90:
        return "Grade B"
    elif marks >=70 and marks<80:
        return "Grade B"
    elif marks >=60 and marks<70:
        return "Grade B"
    elif marks >=50 and marks<60:
        return "Grade B"
    else:
        return "congratulation failed"
    

print(grading(84))

def formatter1 (num):
    num = str(num)
    return num[0:2] + "-" + num[2:5] +"-" + num[5:8] + "-" + num[8-10]

print(formatter1(9859484848))


#password strength checker

def checker (pwd):
    pwd = str(pwd)
    upper = any(ch.isupper()  for ch in pwd)
    lower = any(ch.islower() for ch in pwd)
    digits = any(ch.isdigit() for ch in pwd)
    special = any(not ch.isalnum() for ch in pwd)

    if upper and lower and digits and special :
        return " strong pwd" 
    else: 
        return " weak as you "

print(checker("ramesh83#"))


#username validator
def giveuser(user):
    user = str(user)
    length = len(user)
    if length <5:
        return "invalid username"
    elif not user[0].isalpha():
        return "username must start with letter"
    elif  all(ch.isalnum() or ch == '_' for ch in user):
        return "valid username"
    else:
        return "invalid username"

print(giveuser("w_alpha"))

#email validator
def twoathderate(email):
    email = str(email)
    lisemail = list(email)
    count = 0
    for i in lisemail:
        if '@' == i:
            count+=1
            
    if count == 1:
        return False
    else:
        return True
    
def dotchecker(email):
    email = str(email)

    store = email.find('@')
    if store == 0 or store == len(email) -1:
        return True
    if email[store+1] == '.' or email[store-1] == '.':
        return True
    bool1 = False
    for i in range (len(email)):
        if  i > store and email[i].isnumeric():
            return True
        if email[i] == '.':
            if i == 0 or i == len(email) -1:
                return True
            if not(i < store and email[i+1].isalnum() and email[i-1].isalnum()):
                bool1 = True
    return bool1
        
    
                


        
            


def validatorforemail(email):
    email = str(email)
    if not email[0].isalpha():
        return "invalid email"
    elif ( not all(ch.isalnum() or ch =='@' or ch == '.' for ch in email)):
        return "invalid email"
    elif(twoathderate(email)):
        return "invalid email"
    elif(dotchecker(email)):
        return "invalid email"
    elif(not('@' in email and '.' in email)):
        return "invalid email"
    else: 
        return "valid email"
    
    

print(validatorforemail("subwrn@newmew.com"))
# false if its ram@.gmail.com or ram.@gmail.com
# false if 69ram@gmail.com 
# false if 2 or more @
# false if no @ and gmail / domain 
# false if no .com / .org 
# true if there is couple : .com.np or .com.in 
# .com @gmail (this part cannot contain any digits)
# false if there is ispaces or any symbols