

#Parent Class
class User():
    def __init__(self,name,age,gender,sexual_orientation):
        self.name = name
        self.age = age
        self.gender = gender
        self.sexual_orientation = sexual_orientation
    
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)
        print("Sexual Orientation ", self.sexual_orientation)
        
#Child Class
class Bank(User):
    def __init__(self,name,age,gender,sexual_orientation):
        super().__init__(name,age,gender,sexual_orientation)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount        
        self.balance = self.balance + amount
        print("Account balance has been updated : CAD", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print("insufficient Funds| Balance Available : CAD", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : CAD", self.balance)

    def view_balance(self):
        self.show_details()
        print("Your account balance is : CAD", self.balance)
        
        
    
        
