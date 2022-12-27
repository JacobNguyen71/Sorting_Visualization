import pygame, random, math

pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    BLUE = 0, 0, 255
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    FONT = pygame.font.SysFont('arial', 30)
    LARGE_FONT = pygame.font.SysFont('arial', 40)

    SIDE_PAD = 100
    TOP_PAD = 150