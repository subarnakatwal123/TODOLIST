''' 
Q1: Smart Integer Input (Hidden Trap)

Write a program that asks the user for 10 numbers.

But here’s the trick:

Accept integers like 10

Accept floats like 10.5

Reject strings like "abc"

Reject scientific notation like "1e3"

"""storage = []
limits = 10
while limits > 0:
    num = input  ("enter anumber")
    if 'e' in num.lower():
        print("scientific notation not allowed lodu")
        continue
    
    try : 
        zum = int(num)
        storage.append(zum)
        limits-=1
        
    except  ValueError:
        try:
            zum = float(num)
            storage.append(zum)
            limits-=1
        except ValueError:
            print("abey lodu only integer and float")

print(storage)"""


########
lst = [10, 20, 30, 40]
condi = True
while condi:
    try : 
        inde = int (input ( "enter an index from 0 -4 "))
        print(lst[inde])
        condi = False
    
    except ValueError as e :
        print(f"please enter right inputs only integers are allowed, {e}")
    
    except IndexError as e :
        print(f"enter a valid range 0-4, {e}")



print("*" * 30 ," # " * 40 )

logs = [33333,45242,55134,64431,53666]

while True:
    try : 
        inde = int ( input ("etnter a number in range 0-4"))
        prin = logs[inde]
        print(f"the value for the given index is : {prin}")
        break
    except IndexError as e :
        print(f"The index is out of range, {e}")
    except ValueError as e : 
        print(f"only integers are allowed for index searcha {e}")

# dictionary - > key error and value error

loggged = {"ramesh" : 3, "sita " : 4, "pawan" : 5}

while True: 
    try : 
        keyeed =(input("enter anumber"))
        valueeed = loggged [keyeed]
        print(f"the value for the key {keyeed} is : {valueeed}")
        break
    except KeyError as e:
        print(f"the key is invalid as {e}")
    except ValueError as e: 
        print(f"value error at : {e}")
'''


# (2) Safe division (ZeroDivisionError + ValueError)
while True:
    
    try : 
        nozero = int(input ( "enter neumerator ") )
        print(4/ nozero)
        break
    except ZeroDivisionError as e:
        print(f"0 division error {e}")
    except ValueError as e:
        print(f"value you enter is not numeric {e}")

               

