# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Xavier Phan
"""
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []
        
        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList

def reduceOne(firstString, secondString, wordList):
    # Here is where you will write your function to determine
    # if the second string can be reduced from the first string
    if firstString not in wordList or secondString not in wordList:
        return False
    for i in range(len(firstString)):
        if firstString[:i] + firstString[i+1:] == secondString:
            return True
    return False


def reduceAll(word, wordList):
    #returns a list of strings that can be created from reducing a string
    reducedWords = []
   
    for i in range(len(word)):
       reducedWord = word[:i] + word[i+1:]
       if reducedWord in wordList:
           reducedWords.append(reducedWord)
   
    return reducedWords
def reduceTwoAll(word, wordList):
    # 
    # reductions = []
    # oneReduction = reduceAll(word, wordList)
    # for oneReduction in oneReduction:
    #     secondReduction = reduceAll(oneReduction, wordList)
    #     reductions.extend(secondReduction)
    # return reductions
    reductions = []
    for i in range(len(word)):
        # Remove the first character
        firstReduction = word[:i] + word[i+1:]
        for j in range(len(firstReduction)):
            # Remove the second character
            secondReduction = firstReduction[:j] + firstReduction[j+1:]
            if secondReduction in wordList:
                reductions.append(secondReduction)
    return reductions

def validateReduction(reduction, wordList):
    #confirms whether or not an input list 'reductions' creates a valid sequence
    for word in reduction:
        if word not in wordList:
            return False
    for i in range(len(reduction) - 1):
        if not reduceOne(reduction[i], reduction[i+1], wordList):
            return False
    return True

    



def main():
    # Here is where you will call your test cases
    wordList = loadWords()
    pass



###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for reduce()
def testReduceOne():
    # This comment explains what test1() is testing for, and is followed by code
    wordList = loadWords()
    assert reduceOne('leave', 'eave', wordList) == True
    assert reduceOne('boats', 'bats', wordList ) == True
    assert reduceOne("apple", "pple", wordList) == False
    assert reduceOne("table", "tbl", wordList) == False

def testReduceAll():
    # Tests the reduceAll function, making sure only valid reductions are accepted
    wordList = loadWords()
    def generalTest(): 
        assert set(reduceAll("boats", wordList)) == {"oats", "bats", "bots", "boas", "boat"}
    
    def testSingleLetter():
        #tests to ensure a single letter has no reductions
        assert reduceAll("a", wordList) == []  
    
    def testZeroReductions():
        #tests for when there are no valid words possible from one reduction
        assert reduceAll("qwertyuiop", wordList) == []  

    generalTest()
    testSingleLetter()
    testZeroReductions()
# Below are the tests for reduce2()
def testReduce2():
    words = loadWords()

    def generalTest():
       assert set(reduceTwoAll("eerie", words)) == {"rie", "ere", "eer"}

    def testSingleLetter():
       assert reduceTwoAll("a", words) == []  # Can't remove two letters from a single-letter word

    def testZeroReductions():
       assert reduceTwoAll("qwertyuiop", words) == []  # Tests for if qwertyuiop has no reductions

    generalTest()
    testSingleLetter()
    testZeroReductions()


def test_validateReduction():
    wordList = loadWords()  # Load the word list from words_alpha.txt

    def testValid(): #tests basic reduction
        reduction = ["turntables", "turntable", "turnable", "tunable", "unable"]
        assert validateReduction(reduction, wordList) == True, "Valid sequence should return True"

    def testInvalid(): #tests for when the reduced words are not in wordlist
        reduction = ["turntables", "turntable", "invalidword", "tunable", "unable"]
        assert validateReduction(reduction, wordList) == False, "Invalid words should return False"

    def testEmpty(): #tests if empty sequences return false
        reduction = []
        assert validateReduction(reduction, wordList) == False, "Test 5 Failed: Empty sequence should return False"

    testValid()
    testInvalid()
    testEmpty()

    print("All test cases passed!")
def testN():
    # This comment explains what testN() is testing for, and is followed by code
    pass
    
    


    
###############################################################    
    
if __name__ == "__main__":
    main()    