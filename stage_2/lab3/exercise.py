# 1. Quiz: Selos
def stamps(n):
	p5   = 0
	p2   = 0
	p1   = 0
	rest = n
	i    = 0
	while True:
		if p5 == 0:
			p5 = rest / 5
			rest = rest % 5
		if p2 == 0:
			p2 = rest / 2
			rest = rest % 2
		if p1 == 0:
			p1 = rest / 1
			rest = rest % 1

		i = i + 1
		if i == 3:
			break

	return p5,p2,p1


print stamps(0)

# 1. Quiz: Weekend

def weekend(day):
	return day == 'Saturday' or day == 'Sunday'

print weekend('Sunday')