alist = ['aaa',['bbb','222'],'ccc']

blist = ['aaa','bbb','ccc','ddd','eee']

if ((blist[3] and blist[3]) in alist) == False:
	print(alist)
	print("nah")
	alist.insert(3,blist[3])
	alist.insert(4,blist[4])

if ((blist[3] and blist[4]) in alist) == True:
	print(alist)
	print("yey")
