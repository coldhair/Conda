# 遍历技巧
knight = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knight.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("What's your {0}? It's {1}.".format(q, a))

# reversed() 函数
for i in reversed(range(1,10,2)):
    print(i)

basket=['apple','orange','apple','pear','orange','banana']
print(basket)
print(set(basket))
for f in sorted(basket):
    print(f)

print('-----------------------')
for f in sorted(set(basket)):
    print(f)
