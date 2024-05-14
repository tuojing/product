import os #operating system

#讀取檔案
def read_file(file_name):
    products = []
    with open(file_name,'r',encoding = 'utf-8') as f:
         for line in f:
            if '商品,價格' in line:
                continue
            name,price = line.strip().split(',')
            products.append([name, price])
    return products  

#讓使用者輸入資料
def input_file(products):
    while True:
        name = input('請輸入商品名稱(輸入q離開): ')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        products.append([name,price])
    print(products)
    return products

#印出所有購買紀錄
def print_file(products):    
    for p in products:
        print(p[0],'的價格為',p[1])

#寫入檔案
def write_file(file_name,products):
    with open (file_name,'w',encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0]+','+p[1]+'\n')            

    #檢查檔案在不在
def main():
    file_name = 'products.csv'    
    if os.path.isfile(file_name):
        print('Yeah! 找到檔案了!')
        products = read_file(file_name)
    else:
        products = []
        print('找不到檔案')

    products = input_file(products)
    print_file(products)
    write_file('products.csv',products)
main()    