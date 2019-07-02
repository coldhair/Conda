# 关于集合的操作
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
t = 'orange' in basket
print(t)

a=set('abcdefasdlkfja')
b=set('lkwoufnvsljdflak')
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

if a^b == (a-b)|(b-a):
    print('相等')