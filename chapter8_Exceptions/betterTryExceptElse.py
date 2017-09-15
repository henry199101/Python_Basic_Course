while True:
    try:
        x = input('enter the first number: ')
        y = input('enter the second number: ')
        value = x/y
        print 'x/y is ', value
    except Exception, e:
        print 'invalid input:', e
        print 'please try again.'
    else:
        break
