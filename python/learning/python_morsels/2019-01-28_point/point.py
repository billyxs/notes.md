# https://www.pythonmorsels.com/exercises/8a614814784b4264b5085ed9b3358ca3/
# https://www.pythonmorsels.com/exercises/8a614814784b4264b5085ed9b3358ca3/solution/


from dataclasses import astuple, dataclass 


class Point__():
    """3D Point object"""

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def __repr__(self):
        return "Point(x={}, y={}, z={})".format(self.x, self.y, self.z)


# Solutions


class Point_1:

    """3D Point"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        """Return True if our point is equal to the other point."""
        return self.x == other.x and self.y == other.y and self.z == other.z


class Point_2:

    """3D Point"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        """Return True if our point is equal to the other point."""
        return tuple(self) == tuple(other)

    def __add__(self, other):
        x1, y1, z1 = self  # unpacking with the iterator now
        x2, y2, z2 = other
        return Point(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar):
        x, y, z = self
        return Point(x*scalar, y*scalar, z*scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # iterables

    def __iter__(self):
        """iterate by creating a iterator"""
        return iter((self.x, self.y, self.z))

    def __iter__2(self):
        """iterate generator"""
        yield self.x
        yield self.y
        yield self.z

    def __iter__3(self):
        """iterate generator with a tuple"""
        yield from (self.x, self.y, self.z)


@dataclass
class Point:

    """3D Point"""

    x: float
    y: float
    z: float

    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar):
        """Return copy of our point, scaled by a given value"""
        x, y, z = self
        return Point(scalar*x, scalar*y, scalar*z)

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)
