# Matija (Matt) Stankovic, ms5273
# Homework 4
# Ball Shooting game
# Objective: Destory as many blocks as possible
# drawable.py file

# Imports
import abc

# My Drawable Class
class Drawable(metaclass=abc.ABCMeta):
    # Constructor
    def __init__(self, x=0, y=0, visibility=True):
        self.__x = x
        self.__y = y
        self.__visible = visibility

    # Position Getter
    def getPosition(self):
        return self.__x, self.__y

    # Position Setter
    def setPosition(self, position):
        self.__x = position[0]
        self.__y = position[1]

    # Visibility Setter
    def setVisible(self, visibility):
        self.__visible = visibility

    # Visibiliity Getter
    def getVisible(self):
        return self.__visible

    # Abstract method Rect Getter
    @abc.abstractmethod
    def getRect(self):
        pass

    # Abstract method draw
    @abc.abstractmethod
    def draw(self, surface):
        pass