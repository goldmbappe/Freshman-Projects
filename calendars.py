"""Functions about calendars
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Xavier Phan
"""

def gregorian(year):
    '''determines if a year is a Gregorian leap year 
    requirements:divisible by 4, century years must be divisible by 400'''
    if year %4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0


def milankovic(year):
    '''Finds Leap years on the milankovic calendar. 
    Requirements are: divisible by 4, century years must have a remainder of 200 or 600
    when divided by 900'''
        
    if year %4 != 0:
        return False
    elif year % 100 == 0:
        remainder = year % 900
        return remainder == 200 or remainder == 600
    else:
        return True
    
        

def gregorian_count(year1, year2):
    '''gives us the number of gregorian leap years in any given interval'''
    count = 0
    for year in range (year1, year2):
        if gregorian(year):
            count += 1
    return count


def milankovic_count(year1, year2):
    '''gives us the number of milankovic leap years in any given interval'''
    count = 0
    for year in range(year1, year2):
        if milankovic(year):
            count += 1
    return count


def fromMiddle(age, year):
    '''converts a Middle Earth Age/Year into the years we use today'''
    # This might be helpful...
    ageLengths = [None, 590, 3441, 3021, 2000, 2000, 2000]
    yearZero = 1971  
    for current_age in range(6, age - 1, -1):
        yearZero -= ageLengths[current_age]
    yearZero += year
    return yearZero

def toMiddle(year):
    '''Converts a year we use today into a Middle Earth Year and Age'''
    # This might be helpful...
    ageLengths = [None, 590, 3441, 3021, 2000, 2000, 2000]
    current_age = 7
    middleYear = year - 1971
    while middleYear < 0 and current_age > 1:
        current_age -= 1
        middleYear += ageLengths[current_age]
    return (current_age, middleYear)

def main():
    # Here is where you can prototype and run some code...
    # Webcat will ignore what's here
    print("main is done")


###############################################################

# Here is where you will write your testing code
import unittest

class TestCalendars(unittest.TestCase):    
    # Tests should FAIL when there is a bug in your code! 
    # Verify this yourself! Add a bug up above and re-run to see it fail.
    # Also double check that the number of tests matches what is printed/run
    # Right now, running the file should output 'Ran 3 tests in ...'  
        
    def testGregorian1(self):
        # Makes sure a typical leap year passes 
        self.assertTrue(gregorian(2004), "gregorian year 1696 should be a leap year")
     
    def testGregorian2(self):
        #typical non leap year does not pass (not divisible by 4, not a century year
        self.assertFalse(gregorian(2023),'gregorian year 2023 should not be a leap year')        
       
    def testGregorian3(self):
       # Makes sure a century year divisible by 100 but not 400 doesn't pass 
        self.assertFalse(gregorian(1900), "gregorian year 1900 should not be a leap year")
       
    def testGregorian4(self): 
       # Makes sure a year not divisible by 4 does not pass
        self.assertFalse(gregorian(1777), 'gregorian year 1777 should not be a leap year')
    
    
    
    def testMilankovic1(self):
        #Typical leap year passes (divisible by 4 & not century year)
        self.assertTrue(milankovic(2004), 'milankovic year 2004 should be a leap year')
        
    def testMilankovic2(self):
        #Century year divisible by 4 but doesn't have a remainder of 200 or 600 
        #when divided by 900 doesn't pass
        self.assertFalse(milankovic(2100), 'milankovic year 2100 should not be a leap year')
        
    def testMilankovic3(self):
        #Century year divisble by 4 and produces a remainder of 200 or 600 
        #when divided by 900 passes
        self.assertTrue(milankovic(2000), 'milankovic year 2000 should be a leap year')
        
    def testMilankovic4(self):
        #Year not divisible by 4 does not pass
        self.assertFalse(milankovic(2025), 'milankovic year 2025 should not be a leap year')
        
        
 
    def testGregorianCount0(self):
        #No leap years in interval
        self.assertEqual(0, gregorian_count(1900, 1901), '1900-1901 should not have any leap years')
        
    def testGregorianCount1(self):
        #One leap year in interval
        self.assertEqual(1, gregorian_count(2000, 2002), '2000-2002 should have exactly 1 leap year')
        
    def testGregorianCount3(self):
        # 3 leap years in interval
        self.assertEqual(3, gregorian_count(2001,2013), "2001 to 2013 should have 3 leap years in greg")
        
    
    
    def testMilankovicCount0(self):
        #checks for No leap years in interval
        self.assertEqual(0, milankovic_count(1800, 1801), '1980-1801 should not have any leap years')
    
    def testMilankovicCount1(self):
        #checks for 2 leap years in interval
        self.assertEqual(1, milankovic_count(2000, 2002), '2000-2002 should have exactly one leap year')
        
    def testMilankovicCount3(self):
        #checks for 3 leap years in interval
        self.assertEqual(3, milankovic_count(2001, 2013), '2001-2013 should have exactly 3 leap years')
    
    
    def testFromMiddleYearZero(self):
        # Tests for beginning of 7th Age (1971)
        self.assertEqual(fromMiddle(7, 0), 1971, 'year zero in the 7th age should be 1971')
    def testFromMiddleEndOf6th(self):
        #tests for the last year of 6th age(1970)
        self.assertEqual(fromMiddle(6,1999), 1970, 'year 1999 in the 6th age should be 1970')
    def testFromMiddleRandomYear(self):
        #tests for the last day of the 5th age (-30)
        self.assertEqual(fromMiddle(5, 1999), -30, 'year 1999 in the thth age should be -30')
        
        
        
        
    def testToMiddleYearZero(self):
        #Tests for when in Middle Earth 1971 was (Year 0 in the 7th age)
        self.assertEqual(toMiddle(1971), (7, 0), "1971 should be 7th Age, year 0")
        
    def testToMiddleEndOf6th(self): 
        #tests for when in Middle Earth 1970 was (year 1999 in the 6th age)
        self.assertEqual(toMiddle(1970), (6, 1999), '1970 should be in the 6th age, year 0')
    def testToMiddle1stAge(self):
        #tests for the year 11000 B.C., year 81 of the first age
        self.assertEqual(toMiddle(-11000), (1, 81), '11000 B.C. should have taken place in the first age, year 81')
        
    

        


# ... repeat for all functions, testing throughly for several different 
# inputs producing expected outputs ...
    
    
###############################################################    
    
if __name__ == "__main__":
    unittest.main() # finds and runs any test methods in our TestCase classes
    main() # needed to actually run the main method
    