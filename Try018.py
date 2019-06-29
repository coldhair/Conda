# 可写函数说明
def pinfo(arg1, *vartuple):
    print('输出：')
    print(arg1)
    for var in vartuple:
        print(var)
    return


#  调用pinfo函数
pinfo(10)
pinfo(70, 60, 50)

