def show_balance(balance):
    print(f"Your Balance :${balance:2.2f}")
    return balance

def make_deposit(balance,deposit):
    balance += deposit
    return balance

def make_withdraw(balance,withdraw):
    balance -= withdraw
    return balance

def main():
    balance = 0
    while True:
        try:
            chose = float(input("1 - Show Balance\n2 - Deposit\n3 - Withdraw\n4 - Quit\nYour chose :"))
            if chose == 4:
                print("Bye")
                break
            elif chose == 1:
                    show_balance(balance)
            elif chose == 2:
                deposit = float(input("Enter Your Deposit :"))
                balance = show_balance(make_deposit(balance,deposit))
            elif chose == 3:
                withdraw = float(input("Enter Your Withdraw :"))
                if withdraw <= balance:
                    balance = show_balance(make_withdraw(balance,withdraw))
                else:
                    print("İnvalid Amount!")
            else:
                print("İnvalid Chose!")
        except ValueError:
            print("İnvalid Chose")
if __name__ =='__main__':
    main()
