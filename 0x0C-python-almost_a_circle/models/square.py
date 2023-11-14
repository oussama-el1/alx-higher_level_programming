"""Module for the squire"""
from rectangle import Rectangle

class Square(Rectangle):
    """class Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """constructeur"""
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """str function"""
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id, self.x, self.y, self.width)
    @property
    def size(self):
        """getter of size."""
        return self.width
    @size.setter
    def size(self, v):
        self.width = v 
        self.height = v
    def __update(self, id=None, size=None, x=None, y=None):
        """methode to update the value"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    def update(self, *args, **kwargs):
        """update function"""
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)
    def to_dictionary(self):
        return {"id" : self.id, "size":self.width, "x":self.__x, "y":self.__y}