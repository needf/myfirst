#加双下滑线使方法私有
class Secretive:
  
    def __inaccessible(self):
	print "But your can't see me..."
    
    def accessible(self):
	print "The secret message is :"
	self.__inaccessible()
