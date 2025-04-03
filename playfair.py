""" 
author: Xavier Phan 
"""

from string import ascii_lowercase
import unittest

def createTable(phrase):
    ''' Given an input string, create a lowercase playfair table.  The
    table includes no spaces, no punctuation, no numbers, and 
    no Qs -- just the letters [a-p]+[r-z] in some order. The input phrase may contain uppercase characters which should 
    be converted to lowercase.
    
    Input:   string:         a passphrase
    Output:  list of lists:  a ciphertable '''
   
  phrase = phrase.lower()
    phrase = ''.join(filter(str.isalpha, phrase))  # Removes non alphabetic characters
    phrase = phrase.replace('q', '')  # Removes 'q'
    
    #cleans phrase to remove duplicate characters
    uniqueChars = []
    [uniqueChars.append(char) for char in phrase if char not in uniqueChars]
   
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remainingLetters = [char for char in alphabet if char not in uniqueChars and char != 'q']
    uniqueChars.extend(remainingLetters) #adds whatever is left from the alphabet to table
    
    table = [uniqueChars[i:i+5] for i in range(0, 25, 5)] #separates string into rows of 5
    return table




def splitString(plaintext):
    ''' Splits a string into a list of two-character pairs.  If the string
    has an odd length, append an 'x' as the last character.  As with
    the previous function, the bigrams should contain no spaces, no
    punctuation, no numbers, and no Qs.  Return the list of bigrams,
    each of which should be lowercase.
    
    Input:   string:  plaintext to be encrypted
    Output:  list:    collection of plaintext bigrams '''
    plaintext = plaintext.lower()
    plaintext = ''.join(filter(str.isalpha, plaintext))  # Remove non-alphabetic characters
    plaintext = ''.join([char for char in plaintext if char != 'q'])
    
    #adds x if text has unever # of characters
    if len(plaintext) % 2 != 0:
      plaintext += 'x' 

    #splits text into bigrams
    bigrams = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    return bigrams



def playfairRuleOne(pair):
    ''' If both letters in the pair are the same, replace the second
    letter with 'x' and return; unless the first letter is also
    'x', in which case replace the second letter with 'z'.
    
    You can assume that any input received by this function will 
    be two characters long and already converted to lowercase.
    
    After this function finishes running, no pair should contain two
    of the same character   
    
    Input:   string:  plaintext bigram
    Output:  string:  potentially modified bigram '''
    if pair[0] == pair[1]:
       # second letter is z if first letter is x
       if pair[0] == 'x':
           return pair[0] + 'z'
       # second letter is x if pair is made of non x dupes
       else:
           return pair[0] + 'x'
   
   
    return pair #returns the original pair if the letters are different




def playfairRuleTwo(pair, table):
    ''' If the letters in the pair appear in the same row of the table, 
    replace them with the letters to their immediate right respectively
    (wrapping around to the left of a row if a letter in the original
    pair was on the right side of the row).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    letterOne, letterTwo = pair  

    for row in table:
        if letterOne in row and letterTwo in row:  #checks if both letters in same row
            col1, col2 = row.index(letterOne), row.index(letterTwo)
            return row[(col1 + 1) % 5] + row[(col2 + 1) % 5] #shifts letter right

    return pair #returns the pair if not in same row




def playfairRuleThree(pair, table):
    ''' If the letters in the pair appear in the same column of the table, 
    replace them with the letters immediately below respectively
    (wrapping around to the top of a column if a letter in the original
    pair was at the bottom of the column).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    letterOne, letterTwo = pair[0], pair[1]

    # Loop through columns
    for col in range(5):
        rowOne = rowTwo = None
        for row in range(5):
            if table[row][col] == letterOne: #finds the row the letters are in
                rowOne = row
            if table[row][col] == letterTwo:
                rowTwo = row
        
        # If both letters are in the same column
        if rowOne is not None and rowTwo is not None:
            # Shift the letters down (wrap around with % 5)
            return table[(rowOne + 1) % 5][col] + table[(rowTwo + 1) % 5][col]
    
    return pair  #returns unchanged pair if not in same column


def playfairRuleFour(pair, table):
    ''' If the letters are not on the same row and not in the same column, 
    replace them with the letters on the same row respectively but in 
    the other pair of corners of the rectangle defined by the original 
    pair.  The order is important -- the first letter of the ciphertext
    pair is the one that lies on the same row as the first letter of 
    the plaintext pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.  
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    letterOne, letterTwo = pair
    (row1, col1) = (None, None)
    (row2, col2) = (None, None)
    
    #locates letters on the table
    for r, row in enumerate(table):
        if letterOne in row:
            row1, col1 = r, row.index(letterOne)
        if letterTwo in row:
            row2, col2 = r, row.index(letterTwo) 

    # If in different rows/columns, swap cols
    if row1 != row2 and col1 != col2:
        return table[row1][col2] + table[row2][col1]

    return pair  #returns unchanged pair if not in same row/col

    
    
    

def encrypt(pair, table):
    ''' Given a character pair, run it through all four rules to yield
    the encrypted version!
    
    Input:   string:         plaintext bigram
    Input:   list of lists:  ciphertable
    Output:  string:         ciphertext bigram '''
    pair = playfairRuleOne(pair)
    pair = playfairRuleTwo(pair, table)
    pair = playfairRuleThree(pair, table)
    pair = playfairRuleFour(pair, table)
    return pair



def joinPairs(pairsList):
    ''' Given a list of many encrypted pairs, join them all into the 
    final ciphertext string (and return that string)
    
    Input:   list:    collection of ciphertext bigrams
    Output:  string:  ciphertext '''
    return "".join(pairsList)




def main():
    ''' Example main() function '''
    unittest.main() # runs your tests in the TestPlayfair class
    print("Done with unit tests!")

    table = createTable("i am entering a pass phrase")
    splitMessage = splitString("this is a test message")
    pairsList = []

    print(table) # printed for debugging purposes
    
    for pair in splitMessage:
        # Note: encrypt() should call the four rules
        pairsList.append(encrypt(pair, table))
    cipherText = joinPairs(pairsList)
    
    print(cipherText) #printed as the encrypted output
    #output should be be hjntntirnpginprnpm
    print("Done with main!")


###############################################################

class TestPlayfair(unittest.TestCase):
    # Below are your tests.  Remember structured tests need to named with 'test' in the
    # beginning so that unittest recognizes them and runs them. 
    def testCreateTable(self):
        assert createTable('i am entering a passphrase') == [['i', 'a', 'm', 'e', 'n'],
                                                           ['t', 'r', 'g', 'p', 's'],
                                                           ['h', 'b', 'c', 'd', 'f'],
                                                           ['j', 'k', 'l', 'o', 'u'],
                                                           ['v', 'w', 'x', 'y', 'z']], "Table created for 'i am a passphrase' is incorrect"
        #makes sure a phrase with uppercase letters is correctly converted to lowercase
        assert createTable("pHrAsE") == createTable("phrase"), "Uppercase letters should be converted to lowercase"
        
        #makes sure a phrase containing q is omitted
        assert 'q' not in [letter for row in createTable("quiet") for letter in row], "q should not be included"
        
        #makes sure no duplicates are entered
        assert createTable("hello") == [['h', 'e', 'l', 'o', 'a'],
                                 ['b', 'c', 'd', 'f', 'g'],
                                 ['i', 'j', 'k', 'm', 'n'],
                                 ['p', 'r', 's', 't', 'u'],
                                 ['v', 'w', 'x', 'y', 'z']], "Error:should be no duplicates in table"
        print('createTable tests passed')
    def testSplitString(self):
        assert splitString("this is my plaintext") == ["th", "is", "is", "my", "pl", "ai", "nt", "ex", "tx"], "string was split incorrectly"
        
        
        assert splitString('plaintext') == ['pl', 'ai', 'nt', 'ex', 'tx'], 'odd string was split incorrectly'
        
        assert splitString('quiet') == ['ui', 'et'], 'Qs were not ommitted from string'
        
        assert splitString("HeLLoWORLD") == ["he", "ll", "ow", "or", "ld"], "uppercase letters converted incorrectly"

        print('splitString tests passed!')
        
    def testPlayfairRuleOne(self):
        # Test case where both letters are the same, should replace the second letter with 'x'
        assert playfairRuleOne("aa") == "ax", "duplicates should return with an x"

        # Test case where both letters are the same, first letter is 'x', so replace second with 'z'
        assert playfairRuleOne("xx") == "xz", "xx should be returned as xz"
    
        # Test case where both letters are different, should return as-is
        assert playfairRuleOne("ab") == "ab", "pair 'ab' returned incorrectly"

        
        assert playfairRuleOne("a1") == "a1", "Pairs should not include numbers"
        
        print('playfairruleone tests passed')

    print("All tests passed!")

    def testPlayfairRuleTwo(self):
        #example playfair table for the keyword 'i am entering a pass phrase'
        exampleTable = [
        ['i', 'a', 'm', 'e', 'n'],
        ['t', 'r', 'g', 'p', 's'],
        ['h', 'b', 'c', 'd', 'f'],
        ['j', 'k', 'l', 'o', 'u'],
        ['v', 'w', 'x', 'y', 'z']
        ]
        
       #pairs in same row are converted to the letters to the right of them
        assert playfairRuleTwo("am", exampleTable) == "me", "input 'am' should produce 'me'"
        #pairs not in same row are unchanged
        assert playfairRuleTwo("ed", exampleTable) == "ed", "input 'ed' should not change"
        #bigram in same row with entry at end of row results in changing to first number in row 
        #(f at end of row moves right to h, first term in row)
        assert playfairRuleTwo("cf", exampleTable) == "dh", "'input 'cf' should produce 'dh'"
        #inputs are returned in the order they are entered, not the order of 
        #numbers in the key 
        assert playfairRuleTwo("pt", exampleTable) == "sr", "input 'pt' should produce 'sr'"
        
        print('playfairrule2 tests passed')
        

    def testPlayfairRuleThree(self):
        #transpose of table in  testPlayfairRuleTwo (rows become columns & vice versa)
        exampleTable = [['i', 't', 'h', 'j', 'v'], 
                        ['a', 'r', 'b', 'k', 'w'],  
                        ['m', 'g', 'c', 'l', 'x'],  
                        ['e', 'p', 'd', 'o', 'y'], 
                        ['n', 's', 'f', 'u', 'z']]
       
        #pairs in same column are converted to the letters underneath them
        assert playfairRuleThree("am", exampleTable) == "me", "input 'am' should produce 'me'"
        #pairs not in same column are unchanged
        assert playfairRuleThree("ed", exampleTable) == "ed", "input 'ed' should not change"
        #bigram in same column with entry at end of column results in changing to first number in column 
        #(f at end of column moves down to h, first term in column)
        assert playfairRuleThree("cf", exampleTable) == "dh", "input 'cf' should produce 'dh'"
        #inputs are returned in the order they are entered, not the order of 
        #numbers in the key 
        assert playfairRuleThree("pt", exampleTable) == "sr", "input 'pt' should produce 'sr'"
        
        print('playfairrule3 tests passed')
    def testPlayfairRuleFour(self):
        table = [
        ['i', 'a', 'm', 'e', 'n'],
        ['t', 'r', 'g', 'p', 's'],
        ['h', 'b', 'c', 'd', 'f'],
        ['j', 'k', 'l', 'o', 'u'],
        ['v', 'w', 'x', 'y', 'z']
        ]
        #tests for cases when letters not in same row/col, should switch cols
        assert playfairRuleFour("fm", table) == "cn", "input 'fm' should produce 'cn'"
        assert playfairRuleFour("as", table) == "nr", "input 'as' should produce 'nr'"
        assert playfairRuleFour("jw", table) == "kv", "input'jw' should produce 'kv'"

        #tests for when letters are in same row/column, should not change
        assert playfairRuleFour("do", table) == "do", "Test failed for pair 'do'"
        
        print('playfairrulefour tests passed')

    def testEncrypt(self):
        table = [
        ['i', 'a', 'm', 'e', 'n'],
        ['t', 'r', 'g', 'p', 's'],
        ['h', 'b', 'c', 'd', 'f'],
        ['j', 'k', 'l', 'o', 'u'],
        ['v', 'w', 'x', 'y', 'z']
        ]
        
        #tests to assure bigrams pass through all playfair rules correctly 
        assert encrypt("gg", table) == "cm", "input 'gg' should encrypt to 'cm'"
        assert encrypt("am", table) == "me", "input 'am' should encrypt to 'me'"
        assert encrypt("th", table) == "hj", "input 'th' should encrypt to 'hj'"
        assert encrypt("fm", table) == "cn", "input 'fm' should encrypt to 'cn'"
            
        print('testEncrypt test passed')
    def testJoinPairs(self):
        # Basic test case
        assert joinPairs(["cm", "me", "hj", "cn"]) == "cmmehjcn", "Pairs were joined incorrectly"
        assert joinPairs(['gg', 'gx', 'cm']) == "gggxcm", "Pairs were joined incorrectly"
        
        # Test case for when an empty list is given
        assert joinPairs([]) == "", "Error: should have produced empty list"
        
        # Test case for 
        assert joinPairs(["ab"]) == "ab", "Error: should have returned bigram"
        
        print('joinPairs test passed')

    

###############################################################    

if __name__ == "__main__":
    main()        
