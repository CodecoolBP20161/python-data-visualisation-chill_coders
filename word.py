class Word():
    """ Creates Word objects, that are going to be drawn to the picture """

    _name = None
    _size = None
    _color = None

    def __init__(self, name, size, color):
        self._name = name
        self._size = size
        self._color = color
