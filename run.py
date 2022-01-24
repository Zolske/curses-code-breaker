# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import curses
from curses import wrapper


def main(screen):
    for position in range(10):
        screen.addstr(f"Hello World {position}")

    screen.getkey()


wrapper(main)
