import curses
import menu
import player
import spreadsheet
from time import *
import threading
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('code_breaker_global_high_score')

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

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

new_line_character = True
today_date = spreadsheet.get_today_month_year()
temp_date_text = ''
today_year = temp_date_text.join(today_date[0])
today_month = temp_date_text.join(today_date[1])
score_date = temp_date_text.join(today_date[2])
file_name_date = temp_date_text.join(today_date[3])
today_day_name = temp_date_text.join(today_date[4])
today_date_num = temp_date_text.join(today_date[5])
file_name_day_date = temp_date_text.join(today_date[6])


def user_input():
    user_key = screen.getkey()
    return user_key


def player_move():
    """
    Processes the user key input.
    :return: returns True if the user presses the '1' key which will break the loop and end the program
    """
    # waits for the user to press a key on the keyboard
    user_arrow_input = screen.getkey()
    if user_arrow_input == '1':  # ends the program if user presses '1'
        return True
    elif user_arrow_input == '2':  # resets the game if the user presses '2'
        game_menu.start_game(screen)
        player_object.reset_player()
    elif user_arrow_input == '5':  # opens archive page
        player_object.play_game = False
        game_menu.archive_menu(game_menu.archive_list)

    if game_menu.menu_mode == 'archive':
        if user_arrow_input == 'KEY_RIGHT':
            if game_menu.archive_list == 0 or game_menu.archive_list == 55:
                game_menu.archive_list += 55
                game_menu.high_score_list_text(game_menu.archive_list)
            elif game_menu.archive_list == 110:
                game_menu.archive_list = 0
                game_menu.high_score_list_text(game_menu.archive_list)
        elif user_arrow_input == 'KEY_LEFT':
            if game_menu.archive_list == 55 or game_menu.archive_list == 110:
                game_menu.archive_list -= 55
                game_menu.high_score_list_text(game_menu.archive_list)
            elif game_menu.archive_list == 0:
                game_menu.archive_list = 110
                game_menu.high_score_list_text(game_menu.archive_list)

    if user_arrow_input == '4':  # opens help page
        player_object.play_game = False
        game_menu.help_menu()

    if game_menu.menu_mode == 'help':
        if user_arrow_input == 'KEY_DOWN':
            if game_menu.help_scroll < 85:
                game_menu.help_scroll += 5
                game_menu.help_text()
        elif user_arrow_input == 'KEY_UP':
            if game_menu.help_scroll > 5:
                game_menu.help_scroll -= 5
                game_menu.help_text()
            else:
                game_menu.help_scroll = 0
                game_menu.help_text()

    if user_arrow_input == '3':  # opens contact page
        player_object.play_game = False
        game_menu.contact_menu()

    # saves the color of the current location according to the color_mark_map in the player object
    current_color = player_object.color_mark_map[player_object.current_position[0]][player_object.current_position[1]]
    # adds 1 to the index value of the color_order, can be used on the equivalent curses.color_pair()
    current_color = player_object.color_order.index(current_color) + 1
    marker = curses.newpad(3, 10)
    # is needed so the 'addstr' pad can be added
    marker.erase()
    # creates the 'addstr' pad with the color according to the position
    marker.addstr(game_menu.content_marker, curses.color_pair(current_color))
    # draws the pad at the current position according to the player object property 'current_position'
    # uses the 'marker' pad, any 'select' or 'enter' pads at that position are removed
    marker.refresh(*game_menu.position_marker[player_object.current_position[0]][player_object.current_position[1]])
    # processes the user key input and updates the values in the player object properties
    if player_object.arrow_input(user_arrow_input):
        player_object.ask_player_name(screen)
        player_object.set_new_high_score = False
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
    # highlights the text 'press the 'End' key' when the user has selected 4 colors
    end_key_message = curses.newpad(1, 20)
    if player_object.play_game:
        if player_object.color_mark_map[player_object.current_position[0]].count('BLACK') == 0:
            end_key_message.erase()
            end_key_message.addstr("press the '#' key", HIGHLIGHT)
            end_key_message.refresh(0, 0, 41, 24, 41, 41)
            screen.refresh()
        else:
            end_key_message.erase()
            end_key_message.addstr("press the '#' key", ORIGINAL)
            end_key_message.refresh(0, 0, 41, 24, 41, 41)
            screen.refresh()


def timer():
    """
    Increases the seconds and decreases the score in an 1-second interval
    (score is recalculated depending on how many lines are left).
    The loop can be broken when the player_object.stop_time is set to True.
    The time and points can be reset when player_object.reset_time is set to True

    """
    seconds_int = 0
    minutes_int = 0
    player_score = 1800
    while True:
        if player_object.stop_time:
            break
        time.sleep(1)
        seconds_int += 1
        if seconds_int == 60:
            minutes_int += 1
            seconds_int = 0
        seconds_text = str(seconds_int)
        seconds_text = seconds_text.zfill(2)  # .zfill(2) fills the space with 0 if less than 2 digits
        minutes_text = str(minutes_int)
        minutes_text = minutes_text.zfill(2)  # .zfill(2) fills the space with 0 if less than 2 digits
        if player_score > 0:
            player_score = player_object.current_position[0] * 200 - (minutes_int * 60 + seconds_int)
        else:
            player_score = 0
        if player_object.reset_time:
            player_object.reset_time = False
            seconds_int = 0
            seconds_text = '00'
            minutes_int = 0
            minutes_text = '00'
            player_score = 1800
        if player_object.update_timer:
            timer_window = curses.newpad(1, 6)
            timer_window.erase()
            timer_window.addstr(f"{minutes_text}:{seconds_text}")
            timer_window.refresh(0, 0, 2, 6, 2, 11)
            player_object.player_time_seconds_total = (minutes_int * 60) + seconds_int
            player_object.player_time_seconds = seconds_int
            player_object.player_time_minutes = minutes_int
            score_window = curses.newpad(1, 6)
            score_window.erase()
            score_window.addstr(f"{str(player_score).rjust(5)}")
            score_window.refresh(0, 0, 2, 14, 2, 19)
            screen.refresh()


# create the game_menu object which contains data for displaying elements on the screen
game_menu = menu.Game(today_year, today_month, file_name_date, today_day_name, today_date_num, file_name_day_date)
# code institutes browser terminal will raise an error which will switch the new_line_character in the Game object
# to False,
# the start_game() method in the Game object will print the background without the \n character which otherwise would
# raise an error
try:
    curses.curs_set(0)
except:  # making the exception more specific e.g. ValueError, curses the browser-terminal to rais an error!!!!
    game_menu.new_line_character = False  # this line is not needed for the terminal but for the browser-terminal !!!
    new_line_character = False  # this line is not needed for the terminal but for the browser-terminal !!!
# prints the background to the screen and sets the colors
game_menu.start_game(screen)
# create the player_object which contains data for current position, secret code, player code
player_object = player.PlayerObject(score_date, file_name_date, new_line_character, today_month, today_year,
                                    today_day_name, file_name_day_date)
# generates the secret code
player_object.generate_secret_random_number()

timer_thread = threading.Thread(target=timer)  # allows the timer to run in the background
timer_thread.start()  # starts the timer thread on the side
while True:  # runs a loop till the user presses '1' to get out
    if player_move():
        player_object.stop_time = True
        break

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
