# 對話紀錄處理-格式改寫
# 處理當檔案中的時間和人名中間沒有空格時(無法使用spilt去切割)，要如何取出時間和人名
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print('時間', time)
    print('名字', name)