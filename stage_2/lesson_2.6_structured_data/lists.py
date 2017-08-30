# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4152219158/concepts/50376191640923

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

# Add your own code and notes here
stooges = ['Moe','Larry','Curly']
print stooges

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month):
	return days_in_month[month-1]

print how_many_days(1)
print how_many_days(9)

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]      

romenia_in_china = countries[0][2] / countries[2][2]
print romenia_in_china

# mutation
p = ['H','e','l','l','o']
p[0] = 'Y'

stooges = ['Moe','Larry','Curly']
stooges[2] = 'Shemp'

spy = [0,0,7]
agent = spy
spy[2] = agent[2]+1
print agent[2]

spy = [0,0,7]

def replace_spy(spy):
	spy[2] = spy[2]+1

replace_spy(spy)
print spy

p = [1,2]
p.append(3)
p = p + [4,5]
print len(p)

p = [1,2]
q = [3,4]
p.append(q)
print len(p)
print p


