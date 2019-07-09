def average(*args):
    sum=0.0
    if len(args)==0:
        return sum
    for x in args:
        sum=sum+x
    return sum/len(args)

a1=average()
a2=average(1,2)
a3=average(1,2,3)
print(a1)
print(a2)
print(a3)


