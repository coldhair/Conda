import urllib.request
with urllib.request.urlopen('http://www.piyas.com/a/2693.html') as f:
    print(f.read(30000).decode('utf8')) # 加上网页的编码，不然会显示乱码
