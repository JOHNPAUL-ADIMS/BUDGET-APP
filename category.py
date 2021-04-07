# Build up of categories
class Category:
#Class definition
    def __init__(self, name):
        self.name = name
        self.database = [] #THis contains the database to recieve all  list.
        
# describing the deposit function that request an amouunt from the user with their description for deposit.
    def deposit(self, amount, description = None):
        if description == None:
            self.database.append({"amount": (amount) , "description": ""})
        else:
            self.database.append({"amount": (amount), "description": (description)})

#Intilializing checking fund            
    def checkFunds (self, amount): 
        '''
        #This function checks for whether account is less or 
        # equal than  account balance. This calls the balance function.
        '''
        return  amount <= self.computingBalance()

# building a withdrawal function 
# Inital   
    def withdraw(self, amount, description = None):
        if self.checkFunds(amount) == True: 
            '''
            #This checks if  customers has enough amount to withdraw 
            # and if it is true the desecription runs.
            '''
            if description == None:
                self.database.append({"amount": (amount), "description": ""})
            else:
                self.database.append({"amount": (amount), "description": (description)})
            return True
        else:
            return False

            

# Getting  balance of the account
    def computingBalance(self):
        """[The user of the app is credited with an inital amount of 1000]
        """        
        balance = 1000 
        for items in  self.database:
            balance += items['amount']
        print(f'Your Account Balace is #{balance} ')


# Transfering of balance
    def transfer(self, amount, budgetCategory):
        if self.checkFunds(amount) == True: 
            '''
            #checking if the customer has enough amount in his account for transfer.
            '''
            self.database.append({'amount': -(amount), 'description': f'Transfer to {budgetCategory.name}'})
            budgetCategory.deposit(amount, description = f'Transfer from {self.name})')
            return True
        else:
            return False
        

