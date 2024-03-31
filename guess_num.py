# 猜數字遊戲
# 題目 : 產生一個隨機整數1~100 (不要印出來)
#       讓使用者重複輸入數字去猜
#       猜對的話，印出"終於猜對了!""
#       猜錯的話，要告訴他 比答案大/小
import random

print('+++++++++++++++++++++++++++++++++++')
print('|            猜數字遊戲            |')
print('+++++++++++++++++++++++++++++++++++')

start = int(input('請決定隨機整數範圍的開始值: '))
end = int(input('請決定隨機整數範圍的結束值: '))
answer = random.randint(start, end)

count = 0                             # 計算目前猜測的次數

while True:
    num = int(input('請猜數字: '))
    count = count + 1

    if num == answer:
        print('終於猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > answer:
        print('比答案大')
    else:
        print('比答案小')
    
    print('這是你猜的第', count, '次')