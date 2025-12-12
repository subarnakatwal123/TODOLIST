import random
money = {179543200013 : 20000, 1 : 10000}
corresponds = {"subwrn@gmail.com": [179543200013,"subarna123", "subarna",9839393939,]}
def operations(email):
    while True:
        try:
            process = (input(" press : 1 to view balance \n 2 to transfer balance \n 3 to logout"))
            if process == "1":
                print(f"account balance: {money[corresponds[email][0]]}")
            elif process == "2":
                accno = int (input("enter receivers ac/no: "))
                if accno in money:
                    howmuch = int (input("enter how much ? "))
                    if howmuch <10:
                        print("balance must be greater than 10")
                        break
                    if money[corresponds[email][0]] > howmuch:
                        money[accno] += howmuch
                        money[corresponds[email][0]] -= howmuch
                        print("balance transfer successfull")
                        

                    else:
                        print("Not enough balance")

            elif process == "3":
                print("logout successfully")
                break
        except Exception as e:
            print("error has been identified as :  ", e)



        
while True:
    try:
        inter = int(input("press 1 to sign in to your account : \n press 2 to create an account"))
        if inter == 1: 
            email  = input (print("enter your email"))
            pwd = input("enter your pasword")
            if email in corresponds and pwd == corresponds[email][1]:
                print("login successfull")
                operations(email)
                break # please use break keywords soon
            else:
                print("wrong credentials!")
            
        else:
            #register name & number
            name = input("enter your name")
            phone = input("enter you phone numnber")
            emailaddr = input ("enter you email address")
            accountno = random.randint(10**11, 10**12-1)
            password = input("enter strong password")
            confirmpwd = input("confirm your password")
            if emailaddr in corresponds:
                print("account already exists with the username")
            else: 
                corresponds[emailaddr] = [accountno, password, name, phone]
                money[accountno] = 20000
                print("Account registered successfully")
                operations(emailaddr)
            #registered successfully 
            #home page
            print("registeration successful")
            break

    except ValueError as e:
        print(f"error {e} has occured")
        