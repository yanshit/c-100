class Atm:
    def __init__(self,carnumber,pin):
        self.cardnumber = cardnumber
        self.pin=pin

    def balanceinquiry(self):
        print("Your balance is 100000")

    def cashwidthdrawal(self,amount):
        new_amount=100-amount
        print("You withdrawed:"+str(amount)+"Your remaining balance is:"+str(new_amount))

def  main():
    name=input("hello what is your name?")
    print("hello," +name)
    carnumber=input("insert your card number:")
    pin=input("Enter your pin:")
    new_user = Atm(cardnumber, pin)

    print("choose your activity")
    print("1. Balance")
    print("2. cash withdrawal")
    activity=int(input("enter the activity:"))
    
    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        new_user.cashwidthdrawal(amount)
    else:
        print("enter a valid number")

if __name__ == "__main__":
    main()