import  requests

while True:
    msg = input('')
    if msg=='退出':
        print('拜拜')
        break
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}.format(msg)"
    a= requests.get(url).json()['content']
    print(a)
