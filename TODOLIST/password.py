import hashlib

class Verify:
    def __init__(self, user, password):
        self.user = user
        self.password = password
  
    def encrypt(self):
        hashed = hashlib.sha256(self.password.encode()).hexdigest()
        
        with open("password.txt", "a+") as file:
            file.seek(0)
            temp = file.read()
            if (self.user in temp):
                print("user already exists, change your username")
            else:
                file.write(f"{self.user}:{hashed}\n")
                print("user successfully added")
                user_active = open(f"{self.user}_active.txt", "a+")
                user_done = open(f"{self.user}_done.txt", "a+")
                user_done.close()
                user_active.close()
                
        main()
            
    


def login():
        userid = input("input the user id: ")
        pwd = input("input the password: ")
        password =hashlib.sha256((pwd).encode()).hexdigest()
        with open("password.txt", "a+") as file:
            file.seek(0)
            check = file.readlines()
            Found = False
            for lines in check:
                a, b = lines.strip().split(":",1)
                print(a)
                if a == userid:
                    if password == b:
                        print("Successfully login")
                        dash = dashboardoperation(userid)
                        dash.dashboard()
                    #I NEEED ACCESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
                    #fileoperation here ()
                        #give access to the file the user will be assigned towards.
                    else:
                        print("incorrect password")
                        #give retry password page
                    Found = True
                    break
                
            if not Found:
                print("username not identified")
def register():
    user = input("enter your new userid: ")
    password = input("enter a strong password: ")
    C = Verify(user, password)
    C.encrypt()



class dashboardoperation:
    def __init__(self, userid):
        self.userid = userid
        
    def dashboard(self):
            action = int(input("### DASH ### \n 1.View tasks \n 2. Add task \n 3. Remove task \n 4. logout"))
            if action == 1:
                self.read() # create a read class
            elif action ==2:
                #will work on numbering later
                self.add_task()
            elif action == 3:
                self.remove()
            elif action == 4:
                self.logout()
            else:
                print("please input a valid actions")
    
    def read(self):
        with open(f"{self.userid}_active.txt", "r") as file:
            file.seek(0)
            print(file.read())
            file.close()
        self.dashboard()
    
    def add_task(self):
        with open(f"{self.userid}_active.txt", "a+") as file:
            file.seek(0)
            lines = file.readlines()
            task_num = len(lines)
            while True:
                new_task = input("enter a task to add: ")
                file.write(f"{task_num}-"+ new_task+ "\n")
                task_num+=1
                decide =int( input("Press 1 to add another task\n Press 2 to display dashboard"))
                if decide == 2:
                    break
        self.dashboard()
    
    def remove(self):
        with open(f"{self.userid}_active.txt", "r") as file:
            abc = file.readlines()
            for line in abc:
                print(line)
        
        
        with open(f"{self.userid}_active.txt", "w") as file:
            deleteindex = int(input("which one is completed"))
            newindex = 1
            for line in abc:
                i, j = line.strip().split("-", 1)
                if deleteindex == int(i): 
                    continue
                else:
                    file.write(f"{newindex}-"+ j + "\n")
                    newindex+=1

    def logout(self):
        main()


def main():
    login_register = int(input("1. Login \n 2. Register"))
    if login_register == 1:
        login()
    elif login_register == 2:
        register()
            
if __name__ == "__main__":
    main()



                


            
             
