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

    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)

        self.block_width = round((self.width - self.SIDE_PAD) / len(list))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def generate_list(n, minVal, maxVal):
    list = []
    for _ in range(n):
        value = random.randint(minVal, maxVal)
        list.append(value)
    return list

def main():
    n, minVAL, maxVal = 250, 0, 100

    list = generate_list(n, minVAL, maxVal)


if __name__ == "__main__":
    main()