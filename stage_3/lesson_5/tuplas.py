def hours2days(hours):
	days = hours / 24
	hours = hours % 24
	return int(days), hours

print(hours2days(25))
