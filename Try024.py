'''
如果26个英文字母 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
分别等于:1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26。
那么：Knowlege (知识)： K+N+O+W+L+E+D+G+E＝ 11+14+15+23+12+5+4+7+5=96%。
Workhard (努力工作）：W+O+R+K+H+A+R+D＝ 23+15+18+11+8+1+18+4 =98%。

'''

while True:
    word = input('请输入一个单词：').lower()
    if word == 'exit':
        break
    sum = 0
    for i in word:
        sum = sum + ord(i) - 96
    print('您输入的单词是：{},值为：{}'.format(word, sum))

'''
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
'''
