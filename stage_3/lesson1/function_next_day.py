def nextDayMy(year, month, day):
	
	yearR, monthR, dayR = year, month, day

	# validate days
	if day == 30:
		dayR   = 1
		monthR = month + 1
	else:
		dayR = day + 1

	# validate year
	if day == 30 and month == 12:
		yearR = year + 1
		monthR = 1

	return yearR, monthR, dayR	


print nextDayMy(1999,12,30)
print nextDayMy(2013,1,30)
print nextDayMy(2012,12,30)

def nextDay(year, month, day):
	"""Warning: this version incorrectly assumes all months have thirty days"""
	if day < 30:
		return year, month, day + 1
	else:
		if month < 12:
			return year, month + 1, 1
		else:
			return year + 1, 1, 1

print nextDay(1999,12,30)
print nextDay(2013,1,30)
print nextDay(2012,12,30)
