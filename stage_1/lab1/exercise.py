# 1. Quiz: Programming em Python 1
# Write Python code that prints out the number of hours in 7 weeks.
print "1. Quiz: Programming em Python 1"
print 7 * 7 * 24

# 2. Quiz: Velocidade da Luz
print "2. quiz: Velocidade da Luz"

# Write Python code that stores the distance 
# in meters that light travels in one 
# nanosecond in the variable, nanodistance. 

# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec   = 1000000000. # 1 billion

# After your code, running the following:

# print nanodistance

# should output: 0.2998

# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line

nanodistance = speed_of_light / nano_per_sec

print nanodistance

# 3. Quiz: Strings
print "3. Quiz: Strings"

s = "M"
print ('a' + s)[1:]
print s+''
print s[0] + s[1:]
print s[0:]

# 4. Quiz: Bodacious Udacity
# Write the code Python that print udacious without any caractere de citations in your code
print "4. Quiz: Bodacious Udacity"
s = 'udacity'
t = 'bodacious'
print s[0] + t[2:]

# 5. Quiz: Find One
print "5. Quiz: Find One"
text = "first hoo"
print text.find("hoo")

# 6. Quiz: Find Two
print "6. Quiz: Find Two"
text = "zip files are zipped"
first_zip = text.find("zip")
print text.find('zip', first_zip+1)

# 7. Quiz: round numbers
print "7. Quiz: round numbers"
x = 27.63
num = x + 0.5
text = str(num)
point = text.find(".")
print text[:point]