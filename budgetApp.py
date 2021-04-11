import time

# 1. create a class that can instantiate objects based on budget categories
# 		a. food
# 		b. clothing
# 		c. entertainment

# 2. objects should allow for
# 		a. depositing to categories
# 		b. withdrawing from categories
# 		c. computing balances
# 		d. transfering balance amounts between categories


class Budget:

    """
    A BUDGET APP by JohnPaul Adimonyemma
    #This  contains a database for storing the information of the clients
    """

    database = {'food': 2000, 'clothing': 1000, 'entertainment': 3000}

    def __init__(self):

        self.food = Budget.database['food']
        self.clothing = Budget.database['clothing']
        self.entertainment = Budget.database['entertainment']


# Building of the welcoming page in the app.add()


    def displayCurrentBudget(self):

        print('\n\n' + 'Current Budget Status'.center(34, '=').upper() + '\n')
        # PRINTING OUT THE RESULTS FOR THE CUSTOMERS TO SEE

        print(f'NO\t Category \tAmount\n')
        print(f'1.\t Food \t\t#{self.food:#,.2f}')
        print(f'2.\t Clothing \t#{self.clothing:#,.2f}')
        print(f'3.\t Entertainment\t#{self.entertainment:#,.2f}')
        print(''.center(50, '*') + '\n')

        time.sleep(1.0)
        return self.displayCurrentBudget

    def operationSelection(self):

        print(f' \n\nWhat actions will you like to perform?\n\n'.center(
            50, '*').title())
        time.sleep(1.0)

        print(f'Select an Options\n')
        time.sleep(0.5)
        print(f'1. Deposit Funds')
        print(f'2. Withdraw Funds')
        print(f'3. Transfer Funds')
        print(f'4. Check Budget Balance')
        print(f'5. Exit App\n')

        # Collecting my options from the users
        try:
            option = int(input("Enter your options >  "))

        except ValueError:
            print(f' Invalid Option Selected. Try again ')
            return self.operationSelection()

        return self.choiceSelection(option)

    def choiceSelection(self, option):

        if option == 1:
            return self.deposit()
        elif option == 2:
            return self.withdraw()
        elif option == 3:
            return self.transfer()
        elif option == 4:
            return self.checkFunds()
        elif option == 5:
            return self.exitapp()
        else:
            print(f'Invalid Selection ')
        return self.choiceSelection()

    #   Defining my options

    def deposit(self):

        print("YOU ARE ABOUT TO DEPOSIT ".center(50, "="))
        print("Enter the Category you want to deposit into \n")
        print(" 1. Food\n 2. Clothing\n 3. Entertainment\n")
        time.sleep(0.3)

        try:

            depositCategory = int(input(f'Enter category: >> '))
            depositAmount = int(input('Enter the amount \n #'))

            if depositCategory == 1 and depositAmount > 0:
                print(
                    f'You have deposited #{depositAmount:#,.2f} to Food Category')
                self.food += depositAmount

            elif depositCategory == 2 and depositAmount > 0:
                self.clothing += depositAmount
                print(
                    f'You have deposited #{depositAmount:#,.2f} to Clothing Category')

            elif depositCategory == 3 and depositAmount > 0:
                self.entertainment += depositAmount
                print(
                    f'You have deposited #{depositAmount:#,.2f} to Entertainment Category')

            else:
                print(0)
        except ValueError:
            print("You have made an invalid selection. Try again\n")
            return self.deposit()
        #This goes to check for funds. It can be improve by asking the client what next they want to do with next.add()

        return self.exitapp()

    def transfer(self):

        print("\nYou are about to make a transfer\n")
        print("\nSelect the accounts to transfer from and the beneficiary account\n")
        print("1. Food\n2. Clothing\n3. Entertainment\n")

        time.sleep(0.5)

        while True:

            try:
                transfer_from = int(input("Enter  To Transfer From\n> "))
                beneficiary = int(input("Enter Beneficiary Account\n> "))

                transfer_amount = int(input("Enter Transfer Amount\n"))

                if transfer_from in range(1, 4) and beneficiary in range(1, 4) and transfer_amount > 0:

                    if transfer_from == beneficiary:
                        print("You cannot transfer to the same Account. Try again\n")
                        continue

                    elif transfer_amount > Budget.database[list(Budget.database.keys())[transfer_from-1]]:
                        print(
                            f"You have insufficient balance in {list(Budget.database.keys())[transfer_from-1]} account")
                        continue

                    else:
                        return self.operationSelection()
                else:
                    print("You have made an invalid input")
                    continue

            except ValueError:
                print("You have mada an invalid input")
                return self.transfer(transfer_from, beneficiary, transfer_amount)
            return self.exitapp()

    def withdraw(self):

        print("\nYou are about to make a withdrawal\n")
        print("\nEnter the category to withdraw from\n")
        print("1. Food\n2. Clothing\n3. Entertainment\n")

        time.sleep(1.0)
        try:

            Withdrawal_category = int(input(f'Enter category: >> '))
            Withdrawal_amount = int(input('Enter the amount \n #'))

            if Withdrawal_category == 1 and Withdrawal_amount < self.food:
                print(
                    f'You have withdrawn #{Withdrawal_amount:#,.2f} from Food Category')
                self.food -= Withdrawal_amount

            elif Withdrawal_category == 2 and Withdrawal_amount < self.clothing:
                self.clothing -= Withdrawal_amount
                print(
                    f'You have withdrawn #{Withdrawal_amount:#,.2f} from Clothing Category')

            elif Withdrawal_category == 3 and Withdrawal_amount < self.entertainment:
                self.entertainment -= Withdrawal_amount
                print(
                    f'You have withdrawn #{Withdrawal_amount:#,.2f} from Entertainment Category')

            else:
                print(0)
        except ValueError:
            print(
                "You have made an invalid selection or you have insufficient fund, Try again\n")
            return self.deposit()
        #This goes to check for funds. It can be improve by asking the client what next they want to do with next.add()

        return self.exitapp()

    def exitapp(self):
        print(f'Do you want to exit?')
        print(f'If Yes press 1 or No press 2')
        try:
            exitoption = int(input('>>  '))

            if exitoption == 1:
                print("We will love to see you back")
                exit()

            elif exitoption == 2:
                return self.choiceSelection()
            else:
                return self.exitapp()
        except ValueError:
            print('Invalid Selection. Try again')
        return self.choiceSelection()


# INITIALIZATION OF MY CODE
def welcomePage():

    print("\tMY BUDGET APP \t".center(100, '*'))

    budget = Budget()
    budget.operationSelection()


if __name__ == '__welcomePage__':
    welcomePage()

welcomePage()
