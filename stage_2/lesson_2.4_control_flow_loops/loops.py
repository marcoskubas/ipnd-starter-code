# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4196788670/concepts/50222508420923

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

# Add your own code and notes here

def print_numbers(n):
	i=0
	while i < n:
		i = i + 1
		print i
		if i > 2:
			break
	return i

print print_numbers(3)

def factorial(n):
	i      = 0
	result = 1
	while i < n:
		result = result * (n - i)
		i = i + 1
	return result

print factorial(6)

def get_next_target(page):

	start_link  = page.find('<a href=')
	if start_link == -1:
		return None, 0

	start_quote = page.find('"', start_link)
	end_quote   = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com"></div><br><br><div class="udacity float-left"><a href="http://google.com"></div>')
url, end_quote = get_next_target(page)

def print_all_links(page):
	while page:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

print_all_links(page)
