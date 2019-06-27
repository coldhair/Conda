# Fibonacci series: 斐波纳契数列
a,b=0,1
while b<100:
    print(a)
    print(b)
    a,b=b,a+b
    print('a=',a)
    print('b=',b-a,'+',a) #解释了b怎么来的

print('结束了！')
