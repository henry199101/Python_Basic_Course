try:
    x = input('enter the first number: ')
    y = input('enter the second number: ')

    print x/y
except (ZeroDivisionError, TypeError, NameError):
    print 'your numbers were bogus...'
