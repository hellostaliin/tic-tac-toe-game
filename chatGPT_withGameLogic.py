import pygame

# Initialize Pygame
pygame.init()

# Set up the main game window
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe Game")

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
grid_state = [['' for _ in range(grid_cols)] for _ in range(grid_rows)]

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

# Function to check for a win
def check_win():
    for row in range(grid_rows):
        if grid_state[row][0] == grid_state[row][1] == grid_state[row][2] != '':
            return True
    for col in range(grid_cols):
        if grid_state[0][col] == grid_state[1][col] == grid_state[2][col] != '':
            return True
    if grid_state[0][0] == grid_state[1][1] == grid_state[2][2] != '':
        return True
    if grid_state[0][2] == grid_state[1][1] == grid_state[2][0] != '':
        return True
    return False

# Function to check for a draw
def check_draw():
    for row in range(grid_rows):
        for col in range(grid_cols):
            if grid_state[row][col] == '':
                return False
    return True

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                player = nextPlayer(player)
                mouse_x, mouse_y = pygame.mouse.get_pos()

                row, col = get_grid_pos(mouse_x - 50, mouse_y - 50)

                if 0 <= row < grid_rows and 0 <= col < grid_cols and grid_state[row][col] == '':
                    grid_state[row][col] = player

    screen.fill((0, 0, 0))
    board.fill((0, 0, 0))

    for row in range(grid_rows):
        for col in range(grid_cols):
            x = col * cell_width
            y = row * cell_height
            pygame.draw.rect(board, grid_color, (x, y, cell_width, cell_height), 1)
            if grid_state[row][col] in ['X', 'O']:
                font = pygame.font.Font(None, 36)
                text = font.render(grid_state[row][col], True, cross_color)
                text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
                board.blit(text, text_rect)

    screen.blit(board, (50, 50))
    pygame.display.flip()

    if check_win():
        print(f"Player {player} wins!")
        pygame.time.delay(2000)  # Delay for 2 seconds
        running = False
    elif check_draw():
        print("It's a draw!")
        pygame.time.delay(2000)  # Delay for 2 seconds
        running = False

pygame.quit()
