# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import curses
from curses import wrapper
import menu
import player
from time import *
import threading
import time


#def main(screen):

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
if screen.getkey():
    try:
        curses.curs_set(0)  # make cursor invisible
    except:
        pass

# color pairs used by 'curses' and accessible over variable below, 1st text, 2nd background
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLUE)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_YELLOW)
curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)
RED = curses.color_pair(1)
GREEN = curses.color_pair(2)
BLUE = curses.color_pair(3)
YELLOW = curses.color_pair(4)
BLACK = curses.color_pair(5)  # can be used to return to the original background color
FEEDB = curses.color_pair(6)  # for feedback-marker
HIGHLIGHT = curses.color_pair(7)
ORIGINAL = curses.color_pair(8)


def player_move():
    # waits for the user to press a key on the keyboard
    user_arrow_input = screen.getkey()
    # if the user presses 'q' the function exits and returns 'q',
    # this will exit the program because it will break the loop and there is nothing left to do for the program
    if user_arrow_input == 'KEY_SEND':
        return 'KEY_SEND'
    # saves the color of the current location according to the color_mark_map in the player object
    current_color = player_object.color_mark_map[player_object.current_position[0]][player_object.current_position[1]]
    # adds 1 to the index value of the color_order, can be used on the equivalent curses.color_pair()
    current_color = player_object.color_order.index(current_color) + 1
    # is needed so the 'addstr' pad can be added
    marker.erase()
    # creates the 'addstr' pad with the color according to the position
    marker.addstr(game_menu.content_marker, curses.color_pair(current_color))
    # draws the pad at the current position according to the player object property 'current_position'
    # uses the 'marker' pad, any 'select' or 'enter' pads at that position are removed
    marker.refresh(*game_menu.position_marker[player_object.current_position[0]][player_object.current_position[1]])
    # processes the user key input and updates the values in the player object properties
    player_object.arrow_input(user_arrow_input)
    # updates the current color according to the user input in the player object color_mark_map
    current_color = player_object.color_mark_map[player_object.current_position[0]][player_object.current_position[1]]
    # adds 1, so it can be used for the equivalent curses.color_pair()
    current_color = player_object.color_order.index(current_color) + 1
    # is needed so the 'addstr' pad can be added
    marker.erase()
    # creates the marker pad with the updated color
    marker.addstr(game_menu.content_marker, curses.color_pair(current_color))
    # positions the 'select' pad at the current position
    marker.refresh(*game_menu.position_select[player_object.current_position[0]][player_object.current_position[1]])
    if player_object.color_mark_map[player_object.current_position[0]].count('BLACK') == 0:
        end_key_message.erase()
        end_key_message.addstr("press the 'End' key", HIGHLIGHT)
        end_key_message.refresh(0, 0, 41, 24, 41, 53)
        screen.refresh()
    else:
        end_key_message.erase()
        end_key_message.addstr("press the 'End' key", ORIGINAL)
        end_key_message.refresh(0, 0, 41, 24, 41, 53)
        screen.refresh()


# create the game_menu object which contains data for displaying elements on the screen
game_menu = menu.Game()
# create the player_object which contains data for current position, secret code, player code
player_object = player.PlayerObject()
# generates the secret code
# TODO nex line of code disabled for testing, player_object.generate_secret_random_number()
# player_object.generate_secret_random_number()
# prints the main game menu on the screen, add '\n' to the loop for terminal but remove it for heroku
for position in range(44):
    screen.addstr(f"{game_menu.line[position]}")
screen.refresh()


def timer():
    seconds_text = '00'
    seconds_int = 0
    minutes_text = '00'
    minutes_int = 0
    while True:
        if player_object.stop_time:
            break
        time.sleep(1)
        seconds_int += 1
        if seconds_int == 60:
            minutes_int += 1
            seconds_int = 0
        seconds_text = str(seconds_int)
        seconds_text = seconds_text.zfill(2)
        minutes_text = str(minutes_int)
        minutes_text = minutes_text.zfill(2)
        timer_window = curses.newpad(1, 6)
        timer_window.erase()
        timer_window.addstr(f"{minutes_text}:{seconds_text}")
        timer_window.refresh(0, 0, 2, 6, 2, 11)
        player_object.player_time_seconds_total = (minutes_int * 60) + seconds_int
        player_object.player_time_seconds = seconds_int
        player_object.player_time_minutes = minutes_int


# highlights the text 'press the 'End' key' when the user has selected 4 colors
end_key_message = curses.newpad(1, 20)
# create the 'pad' for the player code-marker (3 row, 10 columns)
marker = curses.newpad(3, 10)
# create the 'pad' for the feedback-marker, after turn (1 row, 3 columns)
feedback = curses.newpad(1, 3)
# write first content into pad
marker.addstr(game_menu.content_marker, RED)
# screen needs to be refreshed after writing content into pad
screen.refresh()
# refreshes the pad screen and sets pad to location
marker.refresh(*game_menu.position_select[9][0])
timer_thread = threading.Thread(target=timer)  # allows the timer to run in the background
timer_thread.start()  # starts the timer thread on the side
while True:  # runs a loop till the user presses 'q' to get out
    if player_move() == 'KEY_SEND':
        player_object.stop_time = True
        # curses.nocbreak()
        # screen.keypad(False)
        # curses.echo()
        # curses.endwin()
        break


# wrapper(main)
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
