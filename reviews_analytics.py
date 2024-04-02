# [留言分析程式]

data = []    # 用來存一百萬筆留言
count = 0    # 用來計算目前讀了幾筆資料
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')


# 計算留言的平均長度
sum_len = 0              
for d in data:
    sum_len += len(d)
print('留言的平均長度為: ', sum_len / len(data))


# 篩選有幾筆留言長度小於100
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')


# 篩選有幾筆留言有提到good
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')


# 文字計數
wc = {}   # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1    # 新增新的key進到word_count字典中

print('---以下為出現超過一百萬次的字---')
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print('字典內共有', len(wc), '個字')

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')
print('感謝您使用本查詢功能!')