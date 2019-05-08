# This class can be used for any situation where you'd want a flexible object whose attributes you could set 
# In the constructor
class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self
