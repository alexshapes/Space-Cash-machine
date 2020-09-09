shutdown = False
shutdown1 = False
balance = 800
withdraw = input
format (balance,)

def printbalance ():
    return (balance)

def withdrawbalance ():
    deposit = int(input("Please insert the amount of credits you would like to deposit into your electronic wallet"))
    balance = 800
    balance -= deposit
    print ("Your new balance is {}".format (balance))
    shutdown2 = False
    while (shutdown2 == False):
                print ("What would you like to do next")
                print ("1 = Make a deposit")
                print ("2 = Make a withdrawal")
                print ("3 = Go back to main menu")
                print ("4 = Check balance")
                userchoice1 = int(input ("What would you like to do next?: "))
                if (userchoice1 == 1):
                    deposit = int(input("Please insert the amount of credits you would like to deposit into your electronic wallet"))
                    balance += deposit
                    print ("Your new balance is {}".format (balance))
                elif (userchoice1 ==2):
                    withdraw = int(input ("Please insert the amount of credits you would like to withdraw"))
                    if withdraw < balance:
                        print ("Success, please check your electronic wallet for confirmation!")
                        balance -= withdraw
                        print ("Your remaining credits are {} ".format (balance))
                elif withdraw > balance:
                    print ("Don't we all wish that? Insufficient Credits. Try again")
                    withdraw = int(input ("Please insert the amount of credits you would like to withdraw"))
                elif (userchoice1 ==4):
                    print ("Your Balance is : {}".format (balance))
                elif (userchoice1 ==3):
                    print ("Thank you for being a SpaceBank member, have a lovely space travel!")
                    quit
                    shutdown2 = True



def deposit ():
    deposit = int(input("Please insert the amount of credits you would like to deposit into your electronic wallet"))
    balance = 800
    balance += deposit
    print ("Your new balance is {}".format (balance))
    shutdown1 = False
    while (shutdown1 == False):
                print ("What would you like to do next")
                print ("1 = Make a deposit")
                print ("2 = Make a withdrawal")
                print ("3 = Go back to main menu")
                print ("4 = Check balance")
                userchoice1 = int(input ("What would you like to do next?: "))
                if (userchoice1 == 1):
                    deposit = int(input("Please insert the amount of credits you would like to deposit into your electronic wallet"))
                    balance += deposit
                    print ("Your new balance is {}".format (balance))
                elif (userchoice1 ==2):
                    withdraw = int(input ("Please insert the amount of credits you would like to withdraw"))
                    if withdraw < balance:
                        print ("Success, please check your electronic wallet for confirmation!")
                        balance -= withdraw
                        print ("Your remaining credits are {} ".format (balance))
                elif (userchoice1 ==4):
                    print ("Your Balance is : {}".format (balance))
                elif (userchoice1 ==3):
                    print ("Thank you for being a SpaceBank member, have a lovely space travel!")
                    quit
                    shutdown1 = True



    
menu1 = False
while (menu1 == False):
    print ("Hello and welcome to SpaceBank")
    pin = (input("Please insert your 7 digit pin number"))
    if len(pin) > 7:
        print ("your pin number is too long, please insert your 7 digit pin number again")
        pin = (input("Please insert your 7 digit pin number"))
        if len(pin) > 7:
            print ("your pin number is too short, please insert your 7 digit pin number again")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) > 7:
            print ("your pin number is stil too long, please try again")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) != 7:
            print ("Ok. You have one more try left")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) != 7:
            print ("Last Try, I promise.")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) != 7:
            print ("Ok. Space Police have been alerted. Please mind the Asteroids!")
            quit
            menu1 = True
            shutdown = True
            break

    if len(pin) < 7:
        print ("your pin number is too short, please insert your 7 digit pin number again")
        pin = (input("Please insert your 7 digit pin number"))
        if len(pin) > 7:
            print ("your pin number is too long, please insert your 7 digit pin number again")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) > 7:
            print ("your pin number is stil too long, please try again")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) != 7:
            print ("Ok. You have one more try left")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) != 7:
            print ("Last Try, I promise.")
            pin = (input("Please insert your 7 digit pin number"))
        if len(pin) != 7:
            print ("Ok. Space Police have been alerted. Please mind the Asteroids!")
            quit
            menu1 = True
            shutdown = True


        if len(pin) == 7:
            print ("Success! Your pin has been accepted. Your balance is {} credits".format (balance))
        else:
            print ("Have a lovely space travel! Mind the asteroids! ")
            quit
            menu1 = True
            shutdown = True


    while (shutdown == False):
        print ("Welcome. Please select one of the following 4 options")
        print ("1 = Make a deposit")
        print ("2 = Make a withdrawal")
        print ("3 = Quit SpaceATM")
        print ("4 = Check balance")
        userchoice = int(input ("What would you like to do?: "))

        if (userchoice == 1):
            deposit ()
        elif (userchoice ==2):
            withdrawbalance ()
        elif (userchoice ==4):
            print ("Your new Balance is : {}".format (balance))
        elif (userchoice ==3):
            print ("Thanks you for your membership, have a lovely space travel! Mind the Asteroids.")
            quit
            shutdown = True
            menu1 = True
        else:
            print ("Please select an option")

