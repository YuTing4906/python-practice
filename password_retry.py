# [密碼重試程式]
# 題目 : 先在程式碼中 設定好密碼 password = 'a123456'
#       讓使用者[最多輸入3次密碼]
#       不對的話, 就印出'密碼錯誤! 還有_次機會'
#       對的話, 就印出'登入成功!'

password = 'a123456'       # 正確密碼
chance = 3                 # 剩餘輸入密碼次數

while chance > 0:
    chance = chance - 1
    user = input('請輸入密碼: ')
    
    if user == password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!')
        if chance > 0:
            print('還有', chance, '次機會')
        else:
            print('沒機會嘗試了! 要鎖帳號了!')