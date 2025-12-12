# # # # # # '''
# # # # # # Employee Hierarchy

# # # # # # Class Person → name, age

# # # # # # Class Employee inherits Person → salary

# # # # # # Class Manager inherits Employee → department

# # # # # # Create an object of Manager and print all details.

# # # # # # '''

# # # # # # class Person:
# # # # # #     def __init__(self, name, age):
# # # # # #         self.name = name
# # # # # #         self.age = age
    
# # # # # #     def qualified (self):
# # # # # #         if self.age > 18:
# # # # # #             print("you are qualified")
# # # # # #         else:
# # # # # #             print("disqualified")


# # # # # # class Employee(Person):
# # # # # #     def __init__(self,name, age, salary):
# # # # # #         self.salary = salary
# # # # # #         super().__init__(name, age)
# # # # # #     def tax(self):
# # # # # #         print(f"taxable amount is {self.salary} and tax amount = {0.13*self.salary}")
# # # # # # class Manager(Employee):
# # # # # #     def __init__(self, name, age, salary, department):
# # # # # #         super().__init__(name, age, salary)
# # # # # #         self.department = department
# # # # # #         print(f"Name of the employee : {self.name} \n Age of the employee : {self.age} \n Salary of the employee : {self.salary} \n Departmnet of the employee : {self.department}")

# # # # # # emplo1 = Manager("Rahul", 18, 18000, "CX")
# # # # # # emplo1.tax()
# # # # # # emplo1.qualified()


# # # # # '''Q5. Product → Electronic → Smartphone

# # # # # Product: name, price

# # # # # Electronic: warranty_years

# # # # # Smartphone: camera_mp, battery_mah

# # # # # Smartphone method: full_specs() that prints EVERYTHING.
# # # # # '''
# # # # # class Product:
# # # # #     def __init__(self, name, price):
# # # # #         self.name =  name 
# # # # #         self.price = price
    
# # # # # class Electronic(Product):
# # # # #     def __init__(self,name, price, warranty_years):
# # # # #         super().__init__(name, price)
# # # # #         self.warranty_years = warranty_years

# # # # # class Smartphone(Electronic):
# # # # #     def __init__(self,name, price, warranty_years, camera_mp, battery_mah):
# # # # #         super().__init__(name, price, warranty_years)
# # # # #         self.camera_mp = camera_mp
# # # # #         self.battery_mah = battery_mah
    
# # # # #     def Smartphone (self):
# # # # #         print(f"model name : {self.name} \n price : {self.price} \n warranty : {self.warranty_years} \n camera : {self.camera_mp} battery : {self.battery_mah}")


# # # # # moto = Smartphone("poco", 10000, 2, 108, 5000)
# # # # # moto.Smartphone()

# # # # class Bank:
# # # #     def __init__(self, bank_name, branch):
# # # #         self.bank_name = bank_name
# # # #         self.branch = branch

# # # # class Saving(Bank):
# # # #     def __init__ (self, bank_name, branch, accounntno, balance):
# # # #         super().__init__(bank_name, branch)
# # # #         self.accounntno = accounntno
# # # #         self.balance = balance
    
# # # #     def deposit(self, amount):
# # # #         self.amount = amount
# # # #         if balance > 10:
# # # #             try:
# # # #                 self.balance += amount
# # # #                 print(f"successfully deposited rs {self.amount}, new balance is {self.balance}")
            
# # # #             except error as e:
# # # #                 print(f"error has accoured during deposit: {e}")
# # # #     def withdraw(self, amount):
# # # #         self.amount = amount
# # # #         if balance > 100:
# # # #             try:
# # # #                 self.balance -= amount
# # # #                 print(f"amount withdrawn successfull rs {self.amount}, remaining balance {self.balance}")

# # # #             except error as e:
# # # #                 print(f"error has occored during withdraw : {e}")
    
# # # # class FixedDepo(Saving):
# # # #     def __init__(self,bank_name, branch, accounntno, balance):
        
# # # #         super().__init__(bank_name, branch, accounntno, balance)
    
# # # #     def addFD(self, amount, time):
# # # #         try: 
# # # #             fd = self.balance - amount
# # # #             self.balance -= amount
# # # #             print(f"Fixed deposit : {amount}, remaining original balance = {fd}, expected interest : {((0.12*amount) * time )} , maturity days remains : {365}")
            
        
# # # #         except error as e:
# # # #             print(f"error has occured: {e}")
# # # # rajesh = FixedDepo("nmb", "Koteshwor", 110, 100000)
# # # # rajesh.addFD(10000, 2)

# # # # # GST AND DISCOUNT CALCULATOR

# # # # class BasePrice:
# # # #    def __init__(self, price):
# # # #       self.price = price
      

# # # # class Discounts(BasePrice):
# # # #    def __init__ (self, price, discountpercentage):
# # # #       BasePrice.__init__(self, price)
# # # #       self.discountpercentage = discountpercentage

# # # #    def discountamount(self):
# # # #       return (self.price*(self.discountpercentage/ 100))
   

# # # # class GST(BasePrice):
# # # #    def __init__ (self, price, gstpercentage):
# # # #       BasePrice.__init__(self, price)
# # # #       self.gstpercentage = gstpercentage
   
# # # #    def gstamount(self):
# # # #       return (self.price * (self.gstpercentage/ 100))


# # # # class calc(Discounts, GST):
# # # #    def __init__(self, price, gstpercentage,discountpercentage):
# # # #       GST.__init__(self, price, gstpercentage)
# # # #       Discounts.__init__(self,price,  discountpercentage)
# # # #       finalprice = self.price + self.gstamount() - self.discountamount()
# # # #       print(f"Final price is : {finalprice}")

# # # # Conichiwa = calc(100,13,13)


# # # # Ecommerce

# # # class Item:
# # #    def __init__(self, item, price):
# # #       self.item  = item 
# # #       self.price = price
   
# # # class Tax(Item):
# # #    def __init__(self):
# # #       super().__init__(price)
# # #    def taxamount(self):
# # #       return self.price*(13/100)

# # # class Discount(Item):
# # #    def __init__(self):
# # #       super().__init__(price)
# # #    def discountamount(self):
# # #       return self.price * (10/100)

# # # class Shippingcharge(Item):
# # #    def __init__(self, weight):
# # #       self.weight = weight
# # #    def calc(self, weight):
# # #       if self.weight >10:
# # #          return 200
# # #       if self.weight <= 10:
# # #          return 100

# # # class finalprice(Discount, Tax, Shippingcharge):
   
# # #    def finale(self, Discount, Tax, weight):
# # #       return self.price - self.discountamount - self.taxamountax - self.calc(weight)


# # # olualo = finalprice()
# # # olualo.finale(10, 13, 100)

# # # class Student:
# # #    def __init__(self, name, roll):
# # #       self.name = name
# # #       self.roll = roll
# # #       print(f"{self.name} {self.roll}")
# # #       super().__init__()

# # # class Graduate(Student):
# # #    def __init__(self, name, roll, degree):
# # #       self.degree = degree
# # #       super().__init__(name, roll)
# # #       print(f"{self.degree}")

# # # class Employee(Graduate):
# # #    def __init__(self, name, roll, degree, salary):
# # #       self.salary = salary
# # #       super().__init__(name, roll, degree)
# # #       print(f"{self.salary}")
   
# # # alprint = Employee("ramesh", 12, "BCA", 20000)




# # # class Account:
# # #    def __init__(self, acc_no, holder):
# # #       self.acc_no = acc_no 
# # #       self.holder = holder
   

# # # class Saving(Account):
# # #    def __init__(self, acc_no, holder, balance):
# # #       super().__init__(acc_no, holder)
# # #       self.balance = balance
# # #       print(f"{self.acc_no} {self.holder} {self.balance}")

# # # class Premium(Saving):
# # #    def __init__(self, acc_no, holder, balance):
# # #       super().__init__(acc_no, holder, balance)
# # #       pr = balance * 0.05
# # #       print(f"bonus given with the premium 5 % :{pr}")

# # # ram = Saving(101, "RAM", 2000)
# # # check = float(input("enter amount"))
# # # almato = Premium(102, "rameshor", check)


# # '''5. Employee + Manager + Department

# # Person → name, age

# # Employee(Person) → salary

# # Manager(Employee) → department

# # Department → dept_name, floor

# # ManagerDept(Manager, Department) → inherits both

# # Task: Create ManagerDept object and print all details.
# # (This is a hybrid inheritance problem.)'''

# # # class Person:
# # #    def __init__(self, name, age):
# # #       self.name = name 
# # #       self.age = age
# # # class Employee(Person):
# # #    def __init__(self, name, age, salary):
# # #       super().__init__(name, age)
# # #       self.salary = salary

# # # class Manager(Employee):  
# # #    def __init__(self, name, age, salary, department):
# # #       super().__init__(name, age, salary)
# # #       self.department = department

# # # class Department: 
# # #    def __init__(self, dept_name, floor):
# # #       self.dept_name = dept_name
# # #       self.floor = floor

# # # class ManagerDept(Manager, Department):
# # #       def __init__(self, name, age, salary, department, dept_name, floor):
# # #          super().__init__(name, age, salary, department)
# # #          Department.__init__(self, dept_name, floor)

# # #          print(f"name of the employee is {self.name} \n Age : {self.age} \n Salary: {self.salary} \n Department : {self.department} \n dept_name : {self.dept_name} \n floor : {self.floor}")

# # # Ragrib =ManagerDept("Ragrib", 18, 18000, "CSR", "CX", "ground")

# # '''
# # Scenario: E-commerce Users
# # Problem

# # We want to model an E-commerce platform with:

# # Person → Customer → PremiumCustomer (multilevel)

# # Person → name, email

# # Customer → cart, order history

# # PremiumCustomer → discount_rate

# # Account → PaymentAccount (another branch)

# # Account → account_id, balance

# # PaymentAccount → card_number, wallet_balance

# # Hybrid / Multiple inheritance

# # Shopper(PremiumCustomer, PaymentAccount)

# # Combines user info + payment info.

# # Can calculate discounted price and check wallet balance.'''

# # class Person: 
# #    def __init__(self, name, email):
# #       self.name = name 
# #       self.email = email
   
# # class Customer(Person):
# #    def __init__(self, name, email, cart=None):
# #       super().__init__(name, email)
# #       self.cart = cart if cart else []

# # class PremiumCustomer(Customer):
# #    def __init__(self, name, email, cart = None, discount_rate= 10):
# #       super().__init__(name, email, cart)
# #       self.discount_rate = discount_rate


# # class Account:
# #    def __init__(self, account_id, balance):
# #       self.account_id = account_id
# #       self.balance = balance

# # class PaymentAccount(Account):
# #    def __init__(self,account_id, balance, card_number, wallet_balance):
# #       super().__init__(account_id, balance)
# #       self.card_number = card_number 
# #       self.wallet_balance = wallet_balance


# # class Shopper(PremiumCustomer, PaymentAccount):
# #    def __init__(self,name, email, cart, discount_rate, account_id, balance, card_number, wallet_balance):
# #       super().__init__(name, email, cart, discount_rate)
# #       PaymentAccount.__init__(self, account_id, balance, card_number, wallet_balance)
# #       prefinal = sum (self.cart)
# #       discounted = prefinal - (prefinal * (discount_rate/100))

# #       print(f"total amount needed to pay : {discounted} with wallet balance : {self.wallet_balance} by {self.name}")

# # # pravu = Shopper("rathod@gmail.com", [10, 20, 30], 5, 1101, 2000, "xxx999", 20000)
# # # rajes = Shopper("rajesh@gmail.com", [20,30, 50], 10, 1102, 2000, "xx9q23", 800)
# # carditem = [10, 101, 10]
# # mukes = Shopper("ramu", "email@gmail.com", carditem, 10, 1002, 200, 10001, 2000)

# # # SMART HOME SYSTEM 

# # class Device: 
# #    def __init__(self, brand, power_status):
# #       self.brand = brand
# #       self.power_status = power_status
   
# # class Voice_control : 
# #    def __init__(self, mic_sensi, voicelang):
# #       self.mic_sensi = mic_sensi
# #       self.voicelang = voicelang

# # class displaypannel :
# #    def __init__(self, screensize, screenreso):
# #       self.screensize = screensize
# #       self.screenreso = screenreso

# # class Smarthub (Device, Voice_control, displaypannel):
# #    def __init__(self, brand, power_status, mic_sensi, voicelang, screensize, screenreso):
# #       super().__init__(brand, power_status)
# #       Voice_control.__init__(self, mic_sensi, voicelang)
# #       displaypannel.__init__(self, screensize, screenreso)
# #    def printreports(self):
# #       print(f"{self.brand} consumes {self.power_status} its mice is : {self.mic_sensi} sensitive, comes with {self.voicelang} ports here support {self.screensize} with {self.screenreso}")


# # rabare = Smarthub("LG", "300 Watt", 300, "eng", "1920 X 1200", "2k")
# # rabare.printreports()

# #Challenge 4: Bank + Credit Card + Rewards

# class Bank: 
#    def __init__(self, account, balance):
#       self.account = account
#       self.balance  = balance

# class Credit(Bank):
#    def __init__(self, account, balance, limit, duebalance):
#       super().__init__(account, balance)
#       self.limit = limit
#       self.duebalance = duebalance

# class Rewards(Credit):
#    def __init__(self, account, balance, limit, duebalance, cashbackrate):
#       super().__init__(account, balance, limit, duebalance)
#       self.cashbackrate = cashbackrate

# class EliteAccount (Rewards):
#    def __init__(self, account, balance, limit, duebalance, cashbackrate):
#       super().__init__(account, balance, limit, duebalance,cashbackrate)
   
#    def finaldue(self):
#       calcdue = self.duebalance - (self.duebalance * self.cashbackrate)
#       print(f"{calcdue}")
   
#    def availablecredit(self):
#       creditavailable = self.limit - self.duebalance 
#       print(f"{creditavailable}")


# Ramesh = EliteAccount(10001, 1000, 4000, 3000, 0.05)
# Ramesh.finaldue()
# Ramesh.availablecredit()


class Sending: 
    def __init__(self, lungi):
        self.lungi = lungi
        pass
    
    def pompodam (self, rames):
        s
