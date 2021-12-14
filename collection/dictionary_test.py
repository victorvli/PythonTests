dic = {'username': 'admin', 'password': 'admin123'}
dic.pop('address', None)
dic.pop('username', None)
dic['address'] = 'nanjing'
print(dic)
