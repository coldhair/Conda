# __init__()方法
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -5.4)
print(x.r, x.i)
