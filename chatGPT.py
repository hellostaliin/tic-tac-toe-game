import pygame

# Initialize Pygame
pygame.init()

# Set up the main game window
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Grid Example")

# Create a display for the board
board_width, board_height = 300, 300
board = pygame.Surface((board_width, board_height))

# Define grid dimensions
grid_rows, grid_cols = 3, 3
cell_width = board_width // grid_cols
cell_height = board_height // grid_rows

# Define colors
grid_color = (255, 255, 255)  # White
cross_color = (255, 0, 0)  # Red

# Create a 2D list to track the state of each grid cell (initially all empty)
grid_state = [[None for _ in range(grid_cols)] for _ in range(grid_rows)]

# Add player logic 
player = 'X'
def nextPlayer(player):
    if player == 'X':
        player = 'O'
    elif player == 'O':
         player = 'X'
    return player

# Function to get the row and column based on the mouse position
def get_grid_pos(mouse_x, mouse_y):
    col = mouse_x // cell_width
    row = mouse_y // cell_height
    return row, col

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                player = nextPlayer(player)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, col = get_grid_pos(mouse_x - 50, mouse_y - 50)  # Adjust for board position

                # Check if the cell is empty and within the grid
                if grid_state[row][col] is None and 0 <= row < grid_rows and 0 <= col < grid_cols:
                    grid_state[row][col] = player  # Mark the cell with an 'X'
               

    # Clear the main screen
    screen.fill((0, 0, 0))  # Fill with a black background

    # Clear the board display
    board.fill((0, 0, 0))  # Fill with a black background

    # Draw the grid of rectangles on the board
    for row in range(grid_rows):
        for col in range(grid_cols):
            x = col * cell_width
            y = row * cell_height
            pygame.draw.rect(board, grid_color, (x, y, cell_width, cell_height), 1)  # The last argument (1) is the border width
            if grid_state[row][col] == 'X' or  grid_state[row][col] == 'O':
                font = pygame.font.Font(None, 36)
                text = font.render(grid_state[row][col], True, cross_color)
                text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
                board.blit(text, text_rect)

    # Blit the board onto the main screen
    screen.blit(board, (50, 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

