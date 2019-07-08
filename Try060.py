from urllib import request
with request.urlopen('https://httpbin.org/ip') as f:
    data= f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('{}:{}'.format(k,v))
    print('Data:',data.decode('utf-8'))
