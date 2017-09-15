__metaclass__ = type

class Secretive():

	def __inaccessible(self):
		print "you can't see me."

	def accessible(self):
		print "the secret message is:"
		self.__inaccessible()
