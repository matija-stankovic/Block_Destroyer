from drawable import Drawable
import pygame

# Text Class
class Text(Drawable):
    # Constructor
    def __init__(self, x=0, y=0, message='', visibility=True):
        super().__init__(x, y, visibility)
        self.__message = message
        fontObj = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 32)
        self.__surface = fontObj.render(message, True, (0, 0, 0))
        size = fontObj.size(message)
        self.__rect = pygame.Rect(x, y, size[0], size[1])

    #Draw the text on screen
    def draw(self, target):
        if self.getVisible():
            target.blit(self.__surface, self.getPosition())

    # Rect Getter
    def getRect(self):
        return self.__rect

    # Message Getter
    def getMessage(self):
        return self.__message

    # Message Setter
    def setMessage(self, message):
        self.__message = message
        fontObj = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 32)
        self.__surface = fontObj.render(message, True, (0, 0, 0))