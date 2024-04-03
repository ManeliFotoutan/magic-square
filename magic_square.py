import pygame
import sys


def generate_odd_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    row, col = 0, n // 2

    while num <= n * n:
        magic_square[row][col] = num
        num += 1
        new_row, new_col = (row - 1) % n, (col + 1) % n 
        if magic_square[new_row][new_col]:  # if list is non-zero
            row += 1
        else:
            row, col = new_row, new_col

    return magic_square


def generate_even_magic_square(n): 
    magic_square = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
    # Corners of order (n/4)*(n/4) 
    
    # Top left corner 
    for i in range(0,n//4): 
        for j in range(0,n//4): 
            magic_square[i][j] = (n*n + 1) - magic_square[i][j]

      

    # Top right corner 
    for i in range(0,n//4): 
        for j in range(3 * (n//4),n): 
            magic_square[i][j] = (n*n + 1) - magic_square[i][j]

  

    # Bottom Left corner 
    for i in range(3 * (n//4),n): 
        for j in range(0,n//4): 
            magic_square[i][j] = (n*n + 1) - magic_square[i][j]

      
    # Bottom Right corner 
    for i in range(3 * (n//4),n): 
        for j in range(3 * (n//4),n): 
            magic_square[i][j] = (n*n + 1) - magic_square[i][j]

              

    # Centre of matrix,order (n/2)*(n/2) 
    for i in range(n//4,3 * (n//4)): 
        for j in range(n//4,3 * (n//4)): 
            magic_square[i][j] = (n*n + 1) - magic_square[i][j]

    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(str(cell).rjust(5) for cell in row))


def draw_magic_square(screen, magic_square):
    n = len(magic_square)
    cell_size = 50
    margin = 20

    for i in range(n):
        for j in range(n):
            pygame.draw.rect(screen, (70, 170, 190),
                             (j * cell_size + margin, i * cell_size + margin, cell_size, cell_size))
            font = pygame.font.Font(None, 24)
            text = font.render(str(magic_square[i][j]), True, (0, 0, 128))
            text_rect = text.get_rect(
                center=(j * cell_size + margin + cell_size // 2, i * cell_size + margin + cell_size // 2))
            screen.blit(text, text_rect)


def get_input():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))

    while True:
        n = ask_for_input(screen)
        if n is not None:
            return n


def ask_for_input(screen):
    font = pygame.font.Font(None, 32)
    input_value = ""
    input_rect = pygame.Rect(145, 170, 200, 50)
    button_rect = pygame.Rect(170, 220, 150, 50)
    color_inactive = pygame.Color(70, 170, 190)
    color_active = pygame.Color(0, 0, 128)
    color = color_inactive
    button_color = (0, 0, 128)
    button_hover_color = (70, 170, 190)
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        input_value = input_value[:-1]
                    else:
                        input_value += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    try:
                        return int(input_value)
                    except ValueError:
                        pass

        button_hover = button_rect.collidepoint(pygame.mouse.get_pos())

        screen.fill((0, 0, 128))
        pygame.draw.rect(screen, color, input_rect, border_radius=10)

        text_surface = font.render("Enter the length of the desired square", True, pygame.Color('white'))
        screen.blit(text_surface, (65, 130))

        txt_surface = font.render(input_value, True, pygame.Color('white'))
        screen.blit(txt_surface, (input_rect.x + 15, input_rect.y + 15))
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2, border_radius=10)

        button_color = button_hover_color if button_hover else button_color
        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        text_surface_below = font.render("Generate", True, pygame.Color('white'))
        text_rect = text_surface_below.get_rect(center=button_rect.center)
        screen.blit(text_surface_below, text_rect)

        pygame.display.flip()


def main():
    n = get_input()

    pygame.init()
    screen = pygame.display.set_mode((n * 50 + 40, n * 50 + 40))
    pygame.display.set_caption("Magic Square")



    if n % 2 == 0:
        even = generate_even_magic_square(n)
        print_magic_square(even)
    else:
        odd = generate_odd_magic_square(n)
        print_magic_square(odd)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    pygame.display.flip()
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))
        if n % 2 == 0:
            draw_magic_square(screen, even)
        else:
            draw_magic_square(screen, odd)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()