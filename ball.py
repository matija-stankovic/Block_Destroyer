from drawable import Drawable
import pygame

# Ball Class
class Ball(Drawable):
    # Constructor
    def __init__(self, x=0, y=0, size=1, colour=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__size = size
        self.__colour = colour
        left = x - size
        top = y - size
        self.__rect = pygame.Rect(left, top, size*2, size*2)

    # Used to draw the ball
    def draw(self, surface):
        if self.getVisible():
            pygame.draw.circle(surface, self.__colour, self.getPosition(), self.__size, 0)

    # Rext Getter
    def getRect(self):
        P = self.getPosition()
        size = self.getSize()
        left = P[0] - size
        top = P[1] - size
        self.__rect = pygame.Rect(left, top, size * 2, size * 2)
        return self.__rect

    # Size Getter
    def getSize(self):
        return self.__size

    # Size Setter
    def setSize(self, size):
        self.__size = size

    # Colour getter
    def getColour(self):
        return self.__colour

    # Colour Setter
    def setColour(self, colour):
        self.__colour = colour