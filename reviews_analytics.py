# [留言分析程式]
# 題目 : 寫程式碼來讀取留言檔
#       讀取檔案的過程中, 印出len(data)才知道目前讀取的進度
#       計算留言的平均長度
#       篩選有幾筆留言長度小於100
#       篩選有幾筆留言有提到good

data = []
count = 0    # 用來計算目前讀了幾筆資料

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0              # 用來計算目前留言的總長度
for d in data:
    sum_len += len(d)
print('留言的平均長度為: ', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
# print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
# print(good[0])