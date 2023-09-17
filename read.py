#讀取amazone的一百萬筆資料
#先將amazone的留言儲存在跟python執行檔同一個資料夾中

data = [] #建立空清單
count = 0 #記數，for迴圈每執行一次時會記數一次

with open('reviews.txt', 'r') as file: #讀取檔案,將檔案命名為file暫時變數
	for line in file: #for loop,讀取每筆留言資料,並將每筆資料命名為line暫時變數
		data.append(line) #將每筆資料加到清單data中
		count += 1 # 每執行一次時,記數+1。 此寫法是count = count + 1 的速寫。
	
		if count % 10000 == 0 : #當記數的餘數為10000的倍數時，執行下方內容
		# count % 1000 → 求餘數。 計算第1次的時候,除以10000,餘數為1→不符合,不會印出；計算10000次的時候,除以10000，餘數為0→符合,會印出data目前的計算的長度
			print(len(data)) #印出清單目前計算到的數量


print(len(data)) #想知道清單總長度(總留言筆數)→100萬筆
print(data[0]) #想知道第一筆留言的內容

