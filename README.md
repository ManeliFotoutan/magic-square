# Magic Square Generator

A magic square is a square grid of numbers where the sum of the numbers in each row, column, and diagonal is the same. The numbers in a magic square are usually consecutive integers starting from 1, and each number appears exactly once.

Here's an example of a 3x3 magic square:
  8  1  6
  3  5  7
  4  9  2
In this magic square, the sum of each row, column, and diagonal is 15.

This Python script generates a magic square of odd or even order using Pygame library.

## Prerequisites

- Python 3.x
- Pygame library
  
Install the required dependencies:
pip install pygame

Follow the on-screen instructions to enter the desired order of the magic square.

## Features

- Generates both odd and even order magic squares.
- Provides a visual representation of the generated magic square using Pygame.
- Allows user input for specifying the order of the magic square.

## Explanation of the Code

- `generate_odd_magic_square(n)`: This function generates an odd-order magic square using the Siamese method. It fills the square starting from the middle of the first row and moves diagonally up and to the right.

- `generate_even_magic_square(n)`: This function generates an even-order magic square using a specific method explained in the source comment. It constructs the magic square by filling the square in specific patterns in its corners and center.

- `print_magic_square(square)`: This function prints the magic square in a formatted manner.

- `draw_magic_square(screen, magic_square)`: This function draws the magic square on the Pygame screen.

- `get_input()`: This function initializes Pygame, sets up the screen, and gets the user input for the order of the magic square.

- `ask_for_input(screen)`: This function handles the user input interface using Pygame. It displays a text input box and a "Generate" button for the user to input the desired order of the magic square.

- `main()`: The main function of the script. It initializes Pygame, gets user input for the magic square's order, generates the magic square accordingly, and displays it on the Pygame screen. It also handles events like quitting the program or toggling the display.

- `if __name__ == "__main__"`: This conditional block ensures that the `main()` function is executed only when the script is run directly, not when it's imported as a module.

For more information on magic squares, you can refer to [Wikipedia](https://en.wikipedia.org/wiki/Magic_square).
