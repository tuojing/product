products = []
while True:
    name = input('請輸入商品名稱(輸入q離開): ')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    products.append([name,price])
print(products)
         