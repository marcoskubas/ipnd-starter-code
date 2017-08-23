# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4141089439/concepts/50282994840923

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# Add your own code and notes here
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

def next_target_page(page):
	start_link  = page.find('<a href=')
	start_quote = page.find('"', start_link)
	end_quote   = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

url = next_target_page(page)
print url

def sum(a, b):
	a = a + b
	return a

print sum(1, 5)	

def square(n):
	return n*n

print square(5)	

def sum3(a, b, c):
	return a+b+c

print sum3(1,2,3)

def abbaize(a, b):
	return a+b+b+a

print abbaize('dog', 'cat')	

def find_second(a, b):
    position = a.find(b)
    position = a.find(b, position+1)
    return position

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')	

def bigger(n1, n2):
	if n2 > n1:
		return n2
	else:
		return n1

print bigger(3, 7)	

print 2 < 3

def is_friend(friend):
	if friend[:1] == 'D' or friend[:1] == 'N':
	    return True
	
	return False

print is_friend('Diane')
print is_friend('Fred')

def biggest(a,b,c):
	big = a
	if b > big:
		big = b
	if c > big:
		big = c
	return big


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9



