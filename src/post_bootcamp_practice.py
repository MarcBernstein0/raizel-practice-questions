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



fizzbuzz()