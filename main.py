import pygame
from block import Block
from text import Text
from ball import Ball


def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (
            rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False


# Defining the main method
def main():
    # Initialising pygame
    pygame.init()

    # Title of the game
    pygame.display.set_caption("Homework 4")

    fpsClock = pygame.time.Clock()

    isOver = False
    wait = False

    # Dimensions and Colour
    width = 600
    height = 600
    colour = (255, 255, 255)
    gameSurface = pygame.display.set_mode((width, height))
    groundHeight = 500

    # Ball dimensions
    ballSpace = 15
    positionX = 30
    positionY = groundHeight - ballSpace

    # Ball Velocity
    xVelocity = 0
    yVelocity = 0

    # Creating the Ball Object
    ball = Ball(positionX, positionY, ballSpace, (250, 100, 100))
    # Variable tracking whether the ball is moving
    ballIsMoving = False

    # Block number, size and colour
    blockNumber = 9
    blockColour = (100, 0, 255)
    blockSpace = 40

    # List for block objects
    blocks = []

    # Adding all blocks
    for i in range(0, 3):
        for j in range(1, 4):
            blocks.append(Block(400 + i * blockSpace, groundHeight - j * blockSpace, blockSpace, blockColour))

    # Current Score
    score = 0
    strScore = "Score: {}"
    scoreText = Text(0, 0, strScore.format(score))

    # Highscore
    highscore = 0
    strHighscore = "High Score: {}"
    highscoreText = Text(350, 0, strHighscore.format(highscore))

    # Given Game physics Variables
    dt = 0.1
    g = 6.67
    R = 0.7
    eta = 0.5

    # Game Loop
    while True:
        for event in pygame.event.get():
            # Leave the game
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

            # While game is running
            if not isOver:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDownPos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    mouseUpPos = pygame.mouse.get_pos()

                    xv = mouseUpPos[0] - mouseDownPos[0]
                    yv = mouseUpPos[1] - mouseDownPos[1]
                    ballIsMoving = True
                    isOver = True

            # Start a new game or finish
            if wait:
                if (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_y):
                    score = 0
                    isOver = False
                    wait = False

                    ballIsMoving = False
                    ball.setPosition((30, groundHeight - ballSpace))
                    positionX, positionY = ball.getPosition()

                    for block in blocks:
                        block.setVisible(True)

                elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_n:
                    pygame.quit()
                    exit()

        # When the ball starts moving
        if ballIsMoving:

            if positionY > groundHeight - (ballSpace):
                yv = -R * yv
                xv = eta * xv
                positionY = groundHeight - (ballSpace)
                positionX += dt * xv

            else:
                yv = yv + g * dt
                positionY += dt * yv
                positionX += dt * xv

            if yv < 0.0001 and xv < 0.0001:
                ballIsMoving = False

            if (not (0 < positionX < width)) or (not (0 < positionY < height)):
                ballIsMoving = False

            ball.setPosition((int(positionX), int(positionY)))

        # Chech for intersection
        for block in blocks:
            if intersect(block.getRect(), ball.getRect()):
                if block.getVisible():
                    score += 1
                    if score >= highscore:
                        highscore = score
                block.setVisible(False)

        # Fill Screen
        gameSurface.fill(colour)
        # Grund line
        groundLine = pygame.draw.line(gameSurface, (0, 0, 0), (0, groundHeight), (width, groundHeight), 3)
        # Draw the ball
        ball.draw(gameSurface)
        # Draw Blocks
        for block in blocks:
            block.draw(gameSurface)

        # Display Score
        scoreText.setMessage(strScore.format(score))
        scoreText.draw(gameSurface)

        # Display HighScore
        highscoreText.setMessage(strHighscore.format(highscore))
        highscoreText.draw(gameSurface)

        # Show choice text after move
        if not ballIsMoving and isOver:
            myStr = 'New Game? Press [Y] or [N]'
            myTxt = Text(90, 150, myStr)
            myTxt.draw(gameSurface)
            wait = True

        pygame.display.update()
        fpsClock.tick(30)


# Call the main method
if __name__ == "__main__":
    main()
