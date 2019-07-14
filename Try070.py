import urllib.request
with urllib.request.urlopen('http://www.piyas.com') as f:
    print(f.read(3000))
