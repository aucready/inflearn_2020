nums = [1, 2, 3, 4, 5, 6, 7]
re_nums = []
for i in nums:
    sqrt_a = i*i
    re_nums.append(sqrt_a)
nums = re_nums
print(nums)


temp = {}
dict_a = {'메로나': 500, '폴라포': 700, '빵빠레':1000 }

print(dict_a)
print(type(dict_a))
temp = {'죠스바':400,'월드콘':1200}
print(temp)

print('메로나 가격:', dict_a['메로나'])
dict_a['메로나'] = 1200
print('메로나 가격:', dict_a['메로나'])

del dict_a['메로나']


print(dict_a)


