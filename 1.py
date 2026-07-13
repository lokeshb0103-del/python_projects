
pin = '123'
balance = 100000
attempts = 0
max_attempts = 3
trasactions = []

#login functionality

while True:
    enterd_pin=input('enter your pin:')
    if enterd_pin==pin:
        print('PIN verified successfully')
        break
    else:
        attempts=attempts+1
        print('incorrect pin,attempts left:',(max_attempts-attempts))
        if attempts>max_attempts:
            print('your ATM card is blocked due to limit is exceed')
            exit()
#core functionality : Menu

while True:
    print('----main menu---')
    print('press 1 for balance')
    print('press 2 for deposit money')
    print('press 3 for withdraw money')
    print('press 4 for trasactions(last 4)')
    print('press 5 for exit')

    choice=int(input('enter your choice:'))
    if choice==1:
        print('current balance:',balance)
        input('\npress enter for main menu....')
    elif choice==2:
        deposit_amount=int(input('enter amount for deposit:'))
        if deposit_amount>0:
            balance=balance+deposit_amount
            trasactions.append(f'deposited is {deposit_amount}')
            if len(trasactions)>5:
                trasactions.pop(0)
            print('deposit is successfull,new balance is:',balance)
            input('\npress enter for main menu....')
        else:
            print('invalid amount!')
            input('\npress enter for main menu....')

    elif choice==3:
        withdraw_money=int(input('enter amount to withdraw:'))
        if withdraw_money<=balance and withdraw_money>0:
            balance=balance-withdraw_money
            trasactions.append(f'withdraw:{withdraw_money}')
            if len(trasactions)>5:
                trasactions.pop(0)
            print('withdraw is successfull,new balance is:',balance)
            input('\npress enter for main menu....')
        else:
            print('insufficient balance or invalid amount')
            input('\npress enter for main menu....')
    elif choice==4:
        print('current transactions are:')
        if len(trasactions)==0:
            print('no transactions done upto now')
            input('\npress enter for main menu....')
        else:
            for t in trasactions:
                print(t)
            input('\npress enter for main menu....')
    elif choice==5:
        print('thank you for using this ATM.....')
        break
    else:
        print('invalid options')


