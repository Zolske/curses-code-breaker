# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import curses
from curses import wrapper
import menu
import player
from time import *
import threading


def main(screen):
    # color pairs used by 'curses' and accessible over variable below, 1st text, 2nd background
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
    curses.curs_set(0)  # make cursor invisible

    def player_move():
        # waits for the user to press a key on the keyboard
        user_arrow_input = screen.getkey()

        # status_message.erase()  # part of status_message
        # status_message.addstr(' '.join(player_object.secret_code))  # show userinput key for testing
        # status_message.refresh()  # refresh status_message pad

        # if the user presses 'q' the function exits and returns 'q',
        # this will exit the program because it will break the loop and there is nothing left to do for the program
        if user_arrow_input == 'q':
            return 'q'
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
            end_key_message.refresh()
        else:
            end_key_message.erase()
            end_key_message.addstr("press the 'End' key", ORIGINAL)
            end_key_message.refresh()
        # status_message.addstr('KEY_LEFT')
        # if screen.getkey() == 'KEY_LEFT':
        #     # player_object.position[9][]
        #     status_message.addstr('KEY_LEFT')
        #     status_message.refresh()
        #     screen.refresh()
        # elif screen.getkey() == 'KEY_RIGHT':
        #     pass
        # elif screen.getkey() == 'KEY_UP':
        #     pass
        # elif screen.getkey() == 'KEY_DOWN':
        #     pass
    # create the game_menu object which contains data for displaying elements on the screen
    game_menu = menu.Game()
    # create the player_object which contains data for current position, secret code, player code
    player_object = player.PlayerObject()
    # generates the secret code
    player_object.generate_secret_random_number()
    # prints the main game menu on the screen, add '\n' to the loop for terminal but remove it for heroku
    for position in range(44):
        screen.addstr(f"{game_menu.line[position]}\n")
    screen.refresh()

    def timer():
        timer_window = curses.newwin(1, 6, 2, 6)
        seconds_text = '00'
        seconds_int = 0
        minutes_text = '00'
        minutes_int = 0

        while True:
            timer_window.erase()
            timer_window.addstr(f"{minutes_text}:{seconds_text}")
            timer_window.refresh()
            sleep(1)
            seconds_int += 1
            if seconds_int == 60:
                minutes_int += 1
                seconds_int = 0
            seconds_text = str(seconds_int)
            seconds_text = seconds_text.zfill(2)
            minutes_text = str(minutes_int)
            minutes_text = minutes_text.zfill(2)

    timer_thread = threading.Thread(target=timer)  # allows the timer to run in the background
    timer_thread.start()  # starts the timer thread on the side

    status_message = curses.newwin(2, 40, 34, 22)
    # highlights the text 'press the 'End' key' when the user has selected 4 colors
    end_key_message = curses.newwin(1, 20, 41, 24)
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

    # status_message.addstr('KEY_LEFT')
    # status_message.refresh()
    # screen.refresh()
    # if pad should be used for more

    # while True:
    #     if screen.getkey() == 'KEY_LEFT':


    # feedback.addstr(game_menu.content_feedback, FEEDB)
    # screen.refresh()
    # feedback.refresh(*game_menu.position_feedback[0][3])
    # feedback.clear()
    # feedback.refresh(*game_menu.position_feedback_half[0][2])
    # feedback.refresh(*game_menu.position_marker[0][0])



    # marker_10_1.addstr(panel, curses.color_pair(2))
    # def change():
    #     marker_10_1.refresh(0, 0, 40, 5, 42, 7)
    # change()
    # marker_10_1.refresh(0, 6, 40, 5, 42, 7)
    # marker_10_1.refresh(0, 0, 40, 5, 42, 7)


    # select_10_1 = curses.newpad(1, 2)
    # select_10_2 = curses.newpad(1, 2)
    # select_10_1.addstr("↑", curses.color_pair(1))
    # select_10_1.refresh(0, 0, 40, 6, 41, 6)
    # select_10_2.addstr("↓", curses.color_pair(2))
    # select_10_2.refresh(0, 0, 42, 6, 43, 6)
    # marker_10_1.refresh(0, 0, 40, 5, 42, 7)
#     zolsk_pad = curses.newwin(1, 5, 0, 0,)
#     test_pad = curses.newpad(1, 2)
#     # screen.refresh()
#     # zolsk_win.clear()
#     zolsk_pad.addstr("1234", )
#     test_pad.addstr("▉", curses.color_pair(2))
#     zolsk_pad.refresh()
#     test_pad.refresh(0, 0, 0, 4, 1, 5)
#     # del zolsk_pad
#     screen.refresh()
#
#     # del test_pad
#     # screen.touchwin()
#     var_test = test_pad
#     screen.refresh()
#     zolsk_pad.clear()
#     zolsk_pad.addstr("1235", curses.color_pair(1))
#     zolsk_pad.refresh()
#     zolsk_pad.refresh()
#     # test_pad.refresh(0, 0, 0, 4, 1, 5)
#     # test_pad.addstr("Z")
#     test_pad.refresh(0, 0, 0, 4, 1, 5)
#     zolsk_pad.clear()
#     zolsk_pad.addstr("1238", curses.color_pair(1))
#     zolsk_pad.refresh()
#     var_test.refresh(0, 0, 0, 5, 1, 5)
#     # zolsk_pad.clear()
#     # zolsk_pad.addstr("MM")
#     # zolsk_pad.refresh()
#     # screen.refresh()
# #     zolsk_pad.refresh(3,3,0,0,0,0)
# #     screen.refresh()
#     for position in range(20):
#         screen.addstr(position, 0, f"Hello World {position}")
#
#     screen.refresh()
    while True:  # runns a loop till the user presses 'q' to get out
        if player_move() == 'q':
            break


wrapper(main)
