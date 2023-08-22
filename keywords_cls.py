# keywords: Those words whose functionality is already defined with the programming language..

# There are 35 keywords in python

# import keyword
# print(keyword.kwlist)

# print(len(keyword.kwlist))pin = input('Enter your pin number: ')

if pin == '1234':
    account_type = input('Which type of account are you using? Saving/Current: ')
    if account_type == 'saving':
        amount = input('How much amount do you want to withdraw? ')
        if amount == '5000':
            print('5000 rupees debited from your account')
        else:
            print('Invalid amount')
    elif account_type == 'current':
        amount = input('How much amount do you want to withdraw? ')
        if amount == '4000':
            print('4000 rupees debited from your account')
        else:
            print('Invalid amount')
    else:
        print('Invalid account type')
else:
    print('Invalid pin number')

