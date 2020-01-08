



inventory = {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '콜라': 700,  '사이다': 700}


# inventory = set()
dustom_key = inventory['메로나']
print(dustom_key)
inventory['월드콘'] = 1000

usrkey = list(inventory.keys())
usrvalue = list(inventory.values())
print(usrvalue)
print(usrkey)


print(sum(inventory.values()))




keys = ('apple', 'pear', 'peach')
valuess = (300, 250, 400)

result = dict(zip(keys, valuess))

print(result)
usr_input = int(input('number:'))
i = 0
test = 0
if 0 < usr_input < 255:
    print(usr_input + 20)

elif usr_input >= 255:

    print(255)



print(test)












