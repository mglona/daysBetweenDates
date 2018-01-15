# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

number_of_days_in_month = 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    number_of_days_in_month = setDaysInMonth(month, year)
    if day < number_of_days_in_month:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    number_of_days_between_dates = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        number_of_days_between_dates += 1
    return number_of_days_between_dates



def setDaysInMonth(month1, year1):
    if isLeapYear(year1) == False:
        if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
            number_of_days_in_month = 31

        if month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11:
            number_of_days_in_month = 30

        if month1 == 2:
            number_of_days_in_month = 28
        return number_of_days_in_month


    else:
        if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
            number_of_days_in_month = 31
        
        if month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11:
            number_of_days_in_month = 30
        
        if month1 == 2:
            number_of_days_in_month = 29
        return number_of_days_in_month

def isLeapYear(year1):
#third isLeapYear code
#All test cases passed
    if year1 % 400 == 0:
        return True
    if year1 % 4 == 0 and not year1 % 100 == 0:
        return True
    return False




#second isLeapYear code
#result: All test cases passed
#    if year1 % 4 != 0:
#        return False
#    if year1 % 100 != 0:
#        return True
#    if year1 % 400 != 0:
#        return False



   #First isLeapYear code used
    """if year1 % 4 == 0:
                    return True
                return False"""



def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()




