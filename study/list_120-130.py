

#126
portfolio = ['하이닉스', '삼성전자', 'LG전자']

for i in portfolio:
    print('{} 보유중'.format(i))
print('*' * 20 + '127')


pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']

for i in pets:
    lenth = len(i)
    print('{} : {}'.format(i, lenth))
print('*' * 20 + '128')

prices = ["129,300", "1,000", "2,300"]

for j in prices:
    j_re = j.replace(',', '')
    print(j_re)

print('*' * 20 + '129')



menu = ["면라", "밥김", "김튀"]

for rmenu in menu[:: -1]:

    print(rmenu)

