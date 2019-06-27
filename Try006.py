# 字典
dict={'name': 'Runoob', 'Age':7, 'class':2}
print("dict['name']:", dict['name'])
print("dict['Age']:", dict['Age'])
dict['school']='SDU'
if 'school'in dict:
    print('school在里面')

print(dict)
del dict['Age'] #删除字典中的Age键及键值
print(dict)
dict.clear() #清空字典
print('清空后的长度:',len(dict))
print(dict)
del dict #删除整个字典
print(dict)
#字典也是非常实用的东西，类似数组。
