#user.py

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#You have to make two variables to loop
#through a dictionary this way.
#Also notice that the order returned is
#not the order initialized in. No guarantee.
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
    
