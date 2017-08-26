# def is_leap_baby(day,month,year):
    
# 	if year%4==0:
# 		if year%100==0:
# 			if year%400==0:
# 				return True
# 			else:
# 				return False
# 		else:
# 			return True
# 	else:
# 		return False

def is_leap_baby(day, month, year):
	if (year % 400) == 0:
		return True
	elif (year % 100) == 0:
		return False
	elif (year % 4) == 0:
		return True
	else:
		return False


print is_leap_baby(28, 2, 1976)