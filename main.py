import pygame

# Initialize Pygame
pygame.init()



# Set up the game window
width,height = 800, 800
widthBoard,heightBoard = 300, 300
screen = pygame.display.set_mode((width, height))
board = pygame.Surface((widthBoard, heightBoard))

grid_rows, grid_cols = 3, 3
cell_width = widthBoard // grid_cols
cell_height = heightBoard // grid_rows

# Define colors
grid_color = (255, 255, 255)  # White
board.fill(grid_color) 
# Define colors
crossColor = (255, 0, 0) #red

current_screen = board
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the main screen
    screen.fill((0, 0, 0))  # Fill with a black background

    # Clear the board display
    board.fill((0, 0, 0))  # Fill with a black background
        # Handle other events (e.g., key presses, mouse clicks, etc.)
    if current_screen == board:
        pass
    elif current_screen == screen:
        pass
    # Game logic
    # Update the game state, move objects, check for collisions, etc.

    # Rendering
    # Clear the screen
    # screen.fill((0, 0, 0))  # Fill with black or desired background color

    # Draw game objects and elements on the screen
    # Use functions like pygame.draw.rect(), pygame.draw.circle(), and others to draw objects
    # create main frame inside the main widow
    # pygame.draw.rect(screen, rectangle_color, (200, 200, 400, 400))   
    #copy the board into the screen
    


    #Draw the grid of rectangles
    for row in range(grid_rows):
        for col in range(grid_cols):
            x = col * cell_width
            y = row * cell_height
            pygame.draw.rect(board, grid_color, (x, y, cell_width, cell_height),1)  # The last argument (1) is the border width   pygame.draw.rect(screen, rectangle_color, (x, y, rect_width, rect_height))

    screen.blit(board,(200,200)) #200 coordinate is the coordinate of the top left of the surface 
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
