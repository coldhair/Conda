from urllib import request
response=request.urlopen('https://www.baidu.com')

print( response.getcode())
cont=response.read()
print(cont)