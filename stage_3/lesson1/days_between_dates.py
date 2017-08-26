
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year & 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 30

def nextDay(year, month, day):
    """Warning: this version incorrectly assumes all months have thirty days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
    if month1 == month2:
        return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    #if not dateIsBefore(year1, month1, day1, year2, month2, day2): raise AssertionError
    #assert not dateIsBefore(year1, month1, day1, year2, month2, day2)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
        if(days == 500):
            break
    return days

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

# def test():
#     test_cases = [((2012,9,30,2012,10,30), 30),
#                   ((2012,1,1,2013,1,1), 362),
#                   ((2012,9,1,2012,9,4), 3)]

#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print "Test with data:", args, "failed"
#             print result
#         else:
#             print "Test case passed!"

def test2():
    # tests with 30-day months!
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,1,1,2013,1,2) == 1
    assert nextDay(2013,1,1) == (2013,1,2)
    assert nextDay(2013,4,30) == (2013,5,1)
    assert nextDay(2012,12,31) == (2013,1,1)
    assert nextDay(2013,2,28) == (2013,3,1)
    assert nextDay(2013,9,30) == (2013,10,1)
    assert daysBetweenDates(2012,1,1,2013,1,1) == 366
    assert daysBetweenDates(2013,1,1,2014,1,1) == 365
    assert daysBetweenDates(2013,1,24,2013,6,29) == 156
    print "Tests Finished!"

# test()
test2()
