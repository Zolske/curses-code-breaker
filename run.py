# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import curses
from curses import wrapper
import menu
import player


def main(screen):
    # color pairs used by 'curses' and accessible over variable below, 1st text, 2nd background
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLUE)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    RED = curses.color_pair(1)
    GREEN = curses.color_pair(2)
    BLUE = curses.color_pair(3)
    YELLOW = curses.color_pair(4)
    BLACK = curses.color_pair(5)  # can be used to return to the original background color
    FEEDB = curses.color_pair(6)  # for feedback-marker
    curses.curs_set(0)  # make cursor invisible

    def player_move():
        user_arrow_input = screen.getkey()
        if user_arrow_input == 'q':
            return 'q'
        current_color = player_object.color_mark_map[player_object.current_position[0]][player_object.current_position[1]]
        current_color = player_object.color_order.index(current_color) + 1
        marker.erase()
        marker.addstr(game_menu.content_marker, curses.color_pair(current_color))
        marker.refresh(*game_menu.position_marker[player_object.current_position[0]][player_object.current_position[1]])

        player_object.arrow_input(user_arrow_input)
        current_color = player_object.color_mark_map[player_object.current_position[0]][player_object.current_position[1]]
        current_color = player_object.color_order.index(current_color) + 1
        marker.erase()
        marker.addstr(game_menu.content_marker, curses.color_pair(current_color))
        marker.refresh(*game_menu.position_select[player_object.current_position[0]][player_object.current_position[1]])

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
    # prints the main game menu on the screen, add '\n' to the loop for terminal but remove it for heroku
    for position in range(44):
        screen.addstr(f"{game_menu.line[position]}\n")
    screen.refresh()

    status_message = curses.newwin(1, 10, 34, 22)
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
