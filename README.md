# python程式練習
*****

## 1.溫度轉換程式 ([celsius_to_fahrenheit.py](celsius_to_fahrenheit.py "程式碼"))
- 可以將攝氏(°C)轉換成華氏(°F)的程式，讓使用者輸入攝氏溫度，然後印出華氏溫度
- 也可以將華氏(°F)轉換成攝氏(°C)的程式，讓使用者輸入華氏溫度，然後印出攝氏溫度
- 公式 : 

          F = C*(9/5)+32      攝氏溫度轉成華氏溫度

          C = (F-32)*(5/9)    華氏溫度轉成攝氏溫度

## 2.密碼重試程式([password_retry.py](password_retry.py "程式碼"))
- 先在程式碼中 設定好密碼 password = 'a123456'
- 讓使用者**最多輸入3次密碼**
- 不對的話, 就印出'密碼錯誤! 還有_次機會'
- 對的話, 就印出'登入成功!'

## 3.猜數字遊戲([guess_num.py](guess_num.py "程式碼"))
- 產生一個隨機整數 (不要印出來)
- 讓使用者決定要猜的數字範圍 (開始值和結束值) 
- 讓使用者重複輸入數字去猜
- 猜對的話，印出「終於猜對了!」
- 猜錯的話，要告訴他 比答案大/小
- 在猜測的過程中印出目前共猜了幾次
> 要`import random`來產生隨機數

## 4.留言分析程式([reviews_analytics.py](reviews_analytics.py "程式碼"))
- 寫程式碼來讀取留言檔
- 讀取檔案的過程中, 印出len(data)才知道目前讀取的進度
- 計算留言的平均長度
- 篩選有幾筆留言長度小於100
- 篩選有幾筆留言有提到good
> 留言檔下載位置 : [review.txt](https://drive.google.com/file/d/1mb_FeKWcZnJxvWm9UN8-PrcwWvzdM7Gr/view "留言檔")

## 5.記帳程式專案([products.py](products.py "程式碼"))
- 讓使用者讀取舊的記帳檔案(csv檔), 檔案裡面的欄位有 商品 和 價格
- 檢查要讀取的檔案在不在
- 讓使用者輸入新的商品和價格, 紀錄新的花費
- 可以印出所有購買紀錄
- 將使用者新輸入的商品和價格, 寫入檔案中
> 要寫成function的形式(讓function內**盡量**只做一件事)

## 6.文字檔案處理1-格式改寫([facebook_chat.py](facebook_chat.py "程式碼"))
- 改寫input.txt檔案的格式，變成像output.txt的檔案格式
- input.txt檔案 : 從facebook上複製下來的的對話紀錄
- output.txt檔案 : 讓每一行訊息都有顯示人名
![image](https://github.com/YuTing4906/python-practice/assets/89449703/5a4cdd32-3d29-4fad-ba5b-67658eeb01ec "輸入和輸出檔案的內容")
> 檔案下載位置 : [input.txt](https://drive.google.com/file/d/1QmA05N94Z2jb9L7wxNBw_h7rL09sakiZ/view)

## 7.文字檔案處理2-List切割([line_chat.py](line_chat.py "程式碼"))
- LINE-Viki.txt檔案(輸入檔案) : 從LINE上複製下來的的對話紀錄
- 計算Allen和Viki總共講了幾個字
- 計算Allen和Viki傳了幾個貼圖
- 計算Allen和Viki傳了幾張圖片  
![image](https://github.com/YuTing4906/python-practice/assets/89449703/24315208-30f3-4026-961a-9e1006a69301 "輸入檔案的內容")
> [!TIP]
> **可能遇到的問題** : 利用spilt(' ')切割每一行資料時，若是後方訊息資料中有出現空格，也會被切割  
> **作法** : 利用List分割的作法 (比如 : s[2:]可以拿到s[2]後面所有的內容)

## 8.文字檔案處理3-字串切割([chat.py](chat.py "程式碼"))
- 處理當檔案中的時間和人名中間沒有空格時(無法使用spilt去切割)，要如何取出時間和人名
- 關鍵 :  
  (1) 時間的長度是固定的  
  (2) 清單(List)的切割也可以使用在字串上  
![image](https://github.com/YuTing4906/python-practice/assets/89449703/45508ed0-c0e9-42b8-b062-0efb23e08bbc "輸入檔案的內容")

## 9.留言分析程式-增加文字計數功能
- 計算一百萬筆留言中每個字出現的次數
- 印出哪些字是出現超過一百萬次的
- 讓使用者輸入要查的字，印出這個字出現的次數
- 解決空字串出現在字典裡的情況 (作法 : **利用split()即可**，當遇到連續空格時，會當成只有一個空格，**不要用split(' ')**)
> `建立字典`來計算每個字出現的次數







