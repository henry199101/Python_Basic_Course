try:
    1/0
except NameError:
    print "Unknown variable"
else:
    print "that went well!"
finally:
    print "cleaning up"
