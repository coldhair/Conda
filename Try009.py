# 是否能被2和3整除
num=int(input('请输入一个数字：'))
if num%2 == 0:
    if num%3 == 0:
        print('你输入的数字可以被2和3整除')
    else:
        print('你输入的数字能够被2整除，但不能被3整除')
else:
    if num%3 == 0:
        print('你输入的数字能够被3整除，但不能被2整除')
    else:
        print('你输入的数字不能被2或3整除')