"""the medule is here."""
from base import Base
class Rectangle(Base):
    """class rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        "constractor."
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """width this rectamgle."""
        return self.__width
    @width.setter
    def width(self, v):
        self.validate_integer("width", v, False)
        self.__width = v
    @property
    def height(self):
        """height this rectamgle."""
        return self.__height
    @height.setter
    def height(self, v):
        self.validate_integer("height", v, False)
        self.__height = v
    @property
    def x(self):
        """x this rectamgle."""
        return self.__x
    @x.setter
    def x(self, v):
        self.validate_integer("x", v)
        self.__x = v
    @property
    def y(self):
        """Y this rectamgle."""
        return self.__y
    @y.setter
    def y(self, v):
        self.validate_integer("y", v)
        self.__y = v
    def validate_integer(self , name, value, eq = True):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be > 0".format(name))
        if not eq and value <=0:
            raise ValueError("{} must be >= 0".format(name))
    def area(self):
        """area methode."""
        return self.width * self.height
    def display(self):
        """display function."""
        shape = '\n' * self.y + (' ' * self.x + self.width * '#' + '\n') * self.height
        print(shape, end="")
    def __str__(self):
        """str function."""
        return '[{}] ({}) {}/{} - {}/{}' .format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)
    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """methode to update the value"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
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
        return {"id" : self.id, "width":self.__width, "height":self.__height, "x":self.__x, "y":self.__y}
            