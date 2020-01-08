#
# time = str(input('time:00:00'))
# retime = []
# retime = time.split(':')
# a, b = retime
#
# if int(b) == 0:
#     print('{}시 정각입니다.'.format(a))
# else:
#     print('{}시 {}분 입니다.'.format(a,b))
#
# --------------------------

fruit = ['사과', '포도', '홍시']

usr_fruit = input('과일을 입력하세요')

if usr_fruit in fruit:
    print('정답입니다.')

print('오답')
