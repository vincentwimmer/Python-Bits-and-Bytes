import datetime

waitWeek = datetime.datetime.today()

while True:
	todayDate = datetime.datetime.today()
	currentWeekday = datetime.datetime.today().weekday()

	if todayDate > waitWeek and currentWeekday == 2:
		print("yey it's wednesday!")

		waitWeek = datetime.datetime.today() + datetime.timedelta(days=1)

		print(waitWeek)
