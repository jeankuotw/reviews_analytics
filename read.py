#讀取amazone的一百萬筆資料
#先將amazone的留言儲存在跟python執行檔同一個資料夾中

data = [] #建立空清單
count = 0 #記數，for迴圈每執行一次時會記數一次


#=== 求總共有幾筆資料 ===
with open('reviews.txt', 'r') as file: #讀取檔案,將檔案命名為file暫時變數
	for line in file: #for loop,讀取每筆留言資料,並將每筆資料命名為line暫時變數
		data.append(line.strip()) #將每筆資料加到清單data中,並去除掉(.strip())前後空格&換行資料
		count += 1 # 每執行一次時,記數+1。 #此寫法是count = count + 1 的速寫。

		#=== 印出目前計算出來的留言數量(萬的倍數印出) === 
		if count % 10000 == 0: #當count為10000的倍數時。%：求餘數的意思
			print(len(data)) #印出目前的data數量

print('總共有', len(data), '筆資料') #印出data的總數量
print('第一筆留言：', data[0]) #印出第一筆資料


#=== 求平均留言長度 ===
sum_len = 0 #留言長度

for d in data: #d暫時變數,只在此for迴圈中使用,代表每一筆留言
	sum_len += len(d) #sum_len = sum_len + len(d)。計算每一筆留言的長度,並且加總

print('平均留言長度為:', sum_len/len(data))


#=== 求留言長度低於100的數量 ===
message = [] #建立空清單,放文字數量低於100的評語
for m in data: #m暫時變數
	if len(m) < 100: #當留言長度低於100時
		message.append(m) #將內容加到清單message中

print('總共有', len(message), '筆留言長度低於100字')
print('第一筆留言資料為：', message[0])


#==== 求留言中出現good文字的留言數量 ===
good = [] #建立空清單,放含有good文字的評語
for g in data: #g暫時變數
	if 'good' in g: #如果留言中含有'good'文字
		good.append(g) #將此留言內容加到清單good中

print('總共有', len(good), '篇留言提到good文字')
print('第一筆留言資料為：', good[0])