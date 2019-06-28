# 不定长参数
def pinfo(arg1,*vartuple):
    print(arg1)
    print(vartuple)

#调用不定长参数的函数
pinfo(70,60,50,40)