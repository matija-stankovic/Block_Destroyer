# Matija (Matt) Stankovic, ms5273
# Homework 4
# Ball Shooting game
# Objective: Destory as many blocks as possible
# block.py file

# Imports

from drawable import Drawable
import pygame

# The block class
class Block(Drawable):
    # Constructor
    def __init__(self, x=0, y=0, size=1, colour=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__size = size
        self.__colour = colour
        self.__rect = pygame.Rect(x, y, size, size)

    # Overloading the draw method
    def draw(self, surface):
        if self.getVisible():
            outlineColour = (0, 0, 0)
            outlineWidth = 2
            pygame.draw.rect(surface, self.__colour, self.__rect, 0)
            pygame.draw.rect(surface, outlineColour, self.__rect, outlineWidth)

    # Rect Getter
    def getRect(self):
        P = self.getPosition()
        size = self.getSize()
        self.__rect = pygame.Rect(P[0], P[1], size, size)
        return self.__rect

    #Size Getter
    def getSize(self):
        return self.__size

    # Size Setter
    def setSize(self, size):
        self.__size = size

    # Colour Getter
    def getColour(self):
        return self.__colour

    # Colour Setter
    def setColour(self, colour):
        self.__colour = colour