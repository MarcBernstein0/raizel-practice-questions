def fizzbuzz():
    '''
        create a function called fizzbuzz
        rules: loop from 0 to 100
               if the value is a multiple of 3, print "fizz"
               if the value is a multiple of 5, print "buzz"
               if the value is a multiple of 3 and 5, print "fizzbuzz"
               if the value is not a multiple of either numbers then print the number itslef
    '''
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        else:
            print(x)

# fizzbuzz()

def fizzbuzz_abstract(fizz, buzz):
    '''
        create a function called fizzbuzz
        rules: loop from 0 to 100
               if the value is a multiple of fizz, print "fizz"
               if the value is a multiple of buzz, print "buzz"
               if the value is a multiple of fizz and buzz, print "fizzbuzz"
               if the value is not a multiple of either numbers then print the number itslef
    '''
    for x in range(1,101):
        if x % fizz == 0 and x % buzz == 0:
            print('fizzbuzz')
        elif x % fizz == 0:
            print('fizz')
        elif x % buzz == 0:
            print('buzz')
        else:
            print(x)


# fizzbuzz_abstract(2, 3)

def is_palindrome(word):
    ''' Return True if the passed in word is a palindrome, False otherwise
        
        Args:
        word (str) -- word being passed into the function

        Returns:
        bool: if palindrome - True, else - False
    '''
    if word == " " or word == "":
        return False

    for elem in range(len(word)):
        if word[elem] != word[-(elem+1)]:
            return False
    return True

def is_palindrome_better(word):
    ''' Return True if the passed in word is a palindrome, False otherwise
        
        Args:
        word (str) -- word being passed into the function

        Returns:
        bool: if palindrome - True, else - False
    '''
    if word == " " or word == "":
        return False

    reverse_word = word[::-1]
    return word == reverse_word
    

# print(is_palindrome('racecar'))
# print(is_palindrome('i'))
# print(is_palindrome('eye'))
# print(is_palindrome('best'))
# print(is_palindrome(' '))

# print(is_palindrome_better('racecar'))
# print(is_palindrome_better('i'))
# print(is_palindrome_better('eye'))
# print(is_palindrome_better('best'))
# print(is_palindrome_better(' '))






# -elem + 1 where elem == 0
# -0 + 1 == 1
# -1*elem + 1 where elem == 0
# -1*0 + 1 == 1

# -1(0+1) == -1(1)


