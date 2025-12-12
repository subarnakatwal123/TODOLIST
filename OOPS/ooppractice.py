# class animal:
#     def __init__(self, animal, sound):
#         self.animal = animal
#         self.sound = sound
#     def make_sound(self):
#         print (f"The {self.animal} goes {self.sound}")
# cat = animal("cat", "meow")
# cat.make_sound()


from car import BankAccount

ramesh = BankAccount("ramesh", 3000)
ramesh.deposit(200)
ramesh.withdraw(3200)

from car import book

rabindra = book("the peace of hearts", "rabindra nath tagor", 359)
rabindra.reads()

