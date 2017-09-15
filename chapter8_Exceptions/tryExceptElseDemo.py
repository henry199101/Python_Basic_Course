while True:
    try:
        x = input('enter the first number: ')
        y = input('enter the second number: ')
        value = x/y
        print 'x/y is ', value
    except:
        print 'invalid input. please try again.'
    else:
        break
