# 建立記帳程式專案(+二維清單)

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    
    # 建立二維清單
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)
    products.append([name, price])      # 等同於上面那四行

print(products)