import pygame
import random
import math
pygame.init()

draw_grid_lines = True


# colours = {
#     (random.randint(1,255),random.randint(1,255),random.randint(1,255)):random.randint(1,10000),
#     (random.randint(1,255),random.randint(1,255),random.randint(1,255)):random.randint(1,10000),
#     (random.randint(1,255),random.randint(1,255),random.randint(1,255)):random.randint(1,10000),
#     (random.randint(1,255),random.randint(1,255),random.randint(1,255)):random.randint(1,20000),
#     (random.randint(1,255),random.randint(1,255),random.randint(1,255)):random.randint(1,10000),

   
# }

colours = {
    (255,0,0) : 1,
    (0,255,0) : 6
}


# ==================================================
# This resizes the window based on number of input colours

pixelTotal = sum(colours.values())

rowsCols = int(math.sqrt(pixelTotal))+1

defaultWidth = 512

PIXEL_SIZE = (defaultWidth//rowsCols) + 1

WIDTH,HEIGHT = PIXEL_SIZE * rowsCols, PIXEL_SIZE * rowsCols

# ==================================================

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("random colour image generator")


BLACK = (0,0,0)
WEIRD_BLUE = (10,255,164)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)

# initialises an unrandomised grid from the colours set
def initBaseGrid(colours,size):
    coloursArray = []
    baseGrid = []
    for i in colours:
        for j in range(colours[i]):
            coloursArray.append(i)

    count = 0
    for i in range(rowsCols):
        baseGrid.append([])
        for _ in range(rowsCols):
            if count < size:#stops once all colours have been added 
                baseGrid[i].append(coloursArray[count])
                count += 1
            else:
                baseGrid[i].append((255,255,255))
                
    return baseGrid
    



def shuffle(array):
    # get 1d array of all colours
    inputArray = []
    shuffledArray1D = []
    for i in range(len(array)):
        for j in range(len(array)):
            inputArray.append(array[i][j])

    array_length = int(math.sqrt(len(inputArray)))
    shuffledArray2D = [[BLACK for i in range(array_length)]for i in range(array_length)]
    
    # get randomised version of base grid as 1d array
    for i in range(len(inputArray) -1, -1,-1):
        randomNumber = random.randint(0,i)
        shuffledArray1D.append(inputArray[randomNumber])
        inputArray.pop(randomNumber)

    # convert random 1d to 2d array for the grid 
    counter = 0
    for i in range(len(array)):
        for j in range(len(array)):
            shuffledArray2D[i][j] = shuffledArray1D[counter]
            counter += 1
    
    return shuffledArray2D


            

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, color in enumerate(row):
            pygame.draw.rect(win,color, ((j * PIXEL_SIZE), (i * PIXEL_SIZE), PIXEL_SIZE, PIXEL_SIZE))
            
    if draw_grid_lines:
        for i in range(rowsCols + 1):
            pygame.draw.line(win, BLACK, (0,(i * PIXEL_SIZE)),
                             (WIDTH, (i * PIXEL_SIZE)))

        for i in range(rowsCols + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),(i * PIXEL_SIZE, HEIGHT))



def draw(win, grid):
    win.fill(WHITE)
    draw_grid(win, grid)
    pygame.display.update()


run = True
baseGrid = initBaseGrid(colours,pixelTotal)
grid = shuffle(baseGrid)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
       
            
    draw(WIN, grid)
    

pygame.quit()
