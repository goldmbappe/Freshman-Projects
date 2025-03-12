"""Practice with writing test cases and performing test-driven development using a
Guess-My-Number game as a problem statement.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Xavier Phan
"""

import random


def computerNumber():
    ''' This function SHOULD generate a random number in the 1-100 range 
    (inclusive), and return it'''
    return random.randint(1,100)
    # TODO: when testing this function, it can fails sometimes. Investigate why 
    # and fix the code to match the documentation of what the function should do.
    #changed from random.randint(1,101) to random.randint(1, 100) as it is inclusive of both parameters





def makeSmartGuess(lowest, highest, lastFeedback=None):
    ''' This function should make a smart guess within the given range and return it'''
    assert lowest <= highest, "Error: lowest must be less than or equal to highest"
    return (lowest + highest) // 2
    # TODO: code here AFTER making some tests (use Test-Driven Development)
    

def provideFeedback(guess, theNum):
    ''' This function should take as inputs the guess and the number from the computer,
    and will provide feedback as to whether the guess is too low, too high, or correct. 
    It should print the guess and feedback and then return the feedback'''
    # TODO: code here AFTER making some tests (use Test-Driven Development)
    if guess < theNum: 
        return 'too low'
    elif guess > theNum:
        return 'too high'
    else:
        return 'correct!'


def gameLoop(targetNum=None):
    ''' This function handles the main game loop, repeatedly calling the makeSmartGuess() and
    provideFeedback() functions until the guess is correct. When the guess is finally correct,
    it will return the number of guesses it took to find the answer. '''
    # theNum = computerNumber()
    if targetNum is None:
        theNum = computerNumber()
    else: theNum = targetNum
    theNum = targetNum if targetNum is not None else computerNumber()
    lowest = 1
    highest = 100
    numGuesses = 0
    guess = None
    lastFeedback = None
    
    
    while guess != theNum:
        guess = makeSmartGuess(lowest, highest, lastFeedback)
        numGuesses += 1
        lastFeedback = provideFeedback(guess, theNum)
       
        if lastFeedback == 'too high':
            highest = guess - 1
        if lastFeedback == 'too low':
            lowest = guess + 1
    
    
    
    print(f"It took {numGuesses} guesses to get the target number!")
    return numGuesses
    



    # TODO: code here AFTER making some tests (use Test-Driven Development)


###############################################################
# Here is where you will write your basic test case functions
# Do NOT test provideFeedback here. That must go in the structured test further below
# If you wish, you can make all your tests here int the structured form.  

def testGeneratedNumber():
    for i in range(1000):
        aNum = computerNumber() ## calls the function we are testing
        # now verify that the function did as we expected:
        assert 1 <= aNum and aNum <= 100, "The computer generated a number out of valid range"
        # Often, we want to have very simple and direct tests
        # To improve the testing above, we might be do this instead:
        assert type(aNum) == type(1), "computerNumber() didn't generate an integer!"
        assert 1 <= aNum, "The computer generated a number that's too low"
        assert aNum <= 100, "The computer generated a number that's too high"
    # Why no output or return? Because we want fails to be loud, success is silent

### TODO: ADD MORE TEST FUNCTIONS HERE
# to fully test a function, we often need more than one test.  

def guessWithinRange():
    #check 1
    for i in range (9999):
        guess = makeSmartGuess(1, 100)
        assert 1 <= guess <= 100, "Guess is out of range!"
        
def confirmGuessInt():
    #check 3
    guess = makeSmartGuess(1, 100)
    assert isinstance(guess, int), "Guess is not an integer!"
    
def testMakeSmartGuess(): 
    #check 2
    assert makeSmartGuess(1, 100) == 50  #First guess should be the midpoint of 1 and 100

    # #check 5
    # assert makeSmartGuess(51, 100, "too low") == 75  # New guess should be 75

    # #check 6
    # assert makeSmartGuess(51, 74, "too high") == 62  # New guess should be 62
    
def gameEnded():
    tries  = gameLoop()
    
    assert tries > 0, 'Game was ended incorrectly'
    assert tries <= 7, 'game took too many tries!' 
    #a maximum of 7 tries are able to be made in the range (1, 100) using our methods
    
    

    
        
        

        

        


###############################################################
# For large projects, structured testing like this is *necessary*

import unittest

class TestGuessMyNumber(unittest.TestCase):
    
    # Here is where you will write your structured tests for the provideFeedback function
    def testDemonstrationOfUnittesting(self):
        self.assertEqual(1, 1) # Placeholder example assertion which passes
        hasMessage = True
        self.assertTrue(hasMessage, "Here's the message if this test fails")
        # Actual tests should call a function, then assert/verify the results 
        # and changes from that function are what you expected
        
        # TODO: comment these out, they just demonstrate what test failures look like:
        # self.assertEqual(3, 7, "Demonstration purposes: test fails because 3 != 7")
        # self.fail("Here's a way to immediately fail a test!")
        
    # Here is where you will write your structured tests:
    def testGameLoopFeedback(self):
        target_number = computerNumber()  
        tries = gameLoop(targetNum=target_number)
        # makes sure number of tries is greater than 0
        self.assertGreater(tries, 0, 'Game should take at least one guess')
        # makes sure the number of tries is less than or equal to 7
        self.assertLessEqual(tries, 7, 'Game took too many tries')

      
        
            
        
    def testProvideFeedbackLow(self):
        # TODO: make this test!
        self.assertEqual(provideFeedback(25, 50), 'too low')
        

    def testProvideFeedbackHigh(self):
        # TODO: make this test!
        self.assertEqual(provideFeedback(75, 50), 'too high')
        
    def testProvideFeedbackCorrect(self):
        #check 7
        self.assertEqual(provideFeedback(50,50), 'correct!')

    ### TODO: CREATE MORE TESTS HERE

    def aUtilityFunction(self, param):
        # This is a utility function which unittest.main() will NOT run automatically.
        # Your test functions could still use it though:  self.aUtilityFunction("hello")
        print("Utility function runs! Has parameter:", param)


###############################################################    

def main():
    print("Started basic testing...")
    # Call each one of your basic test functions first:
    testGeneratedNumber()
    # TODO: CALL MORE TEST FUNCTIONS
    print("Basic tests done and passed!")
    # Remember, if a basic assertion fails, no other tests will run.  
    # But for structured tests, every test is run and made into one big report
    
    print("Beginning structured tests...", flush=True)
    # This runs all methods in the TestGuessMyNumber that are named 'test...':
    unittest.main()
    print("Structured tests done (look above for report)")


if __name__ == "__main__":
    main()
