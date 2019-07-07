import urllib.request


Url_IP = 'https://httpbin.org/ip'


def use_simple_urllib():
    response = urllib.request.urlopen(Url_IP)
    print(response.info())
    print(response.readlines())


if __name__ == '__main__':
    print('use_simple_urllib')
    use_simple_urllib()

