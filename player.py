import random
import curses
from curses.textpad import Textbox
import spreadsheet
import time
import menu


class PlayerObject:
    def __init__(self, score_date, file_name_date, new_line_character, today_month, today_year, today_day_name, file_name_day_date):
        # gets overwritten when secret_code is generated, secret_code generator can be commented out for testing
        self.player_name = ''
        self.secret_code = ['RED', 'RED', 'RED', 'RED']
        self.player_code = [],
        self.player_score = 0
        self.current_position = [9, 0]  # row 10, first left, current position of the marker
        self.color_order = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'BLACK']  # is important to cycle true the colors
        self.color_mark_map = [['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 1 / index 0
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 2 / index 1
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 3 / index 2
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 4 / index 3
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 5 / index 4
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 6 / index 5
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 7 / index 6
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 8 / index 7
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 9 / index 8
                                ['RED', 'BLACK', 'BLACK', 'BLACK']]  # turn / row 10 / index 9 / do not set ',' on the end!
        self.content_feedback = "█▂"  # content for feedback
        self.position_feedback = [[[0, 0, 4, 1, 4, 1], [0, 0, 4, 3, 4, 3], [0, 0, 6, 1, 6, 1], [0, 0, 6, 3, 6, 3]],  # turn / row 1 / index 0
                                  [[0, 0, 8, 1, 8, 1], [0, 0, 8, 3, 8, 3], [0, 0, 10, 1, 10, 1], [0, 0, 10, 3, 10, 3]],  # turn / row 2 / index 1
                                  [[0, 0, 12, 1, 12, 1], [0, 0, 12, 3, 12, 3], [0, 0, 14, 1, 14, 1], [0, 0, 14, 3, 14, 3]],  # turn / row 3 / index 2
                                  [[0, 0, 16, 1, 16, 1], [0, 0, 16, 3, 16, 3], [0, 0, 18, 1, 18, 1], [0, 0, 18, 3, 18, 3]],  # turn / row 4 / index 3
                                  [[0, 0, 20, 1, 20, 1], [0, 0, 20, 3, 20, 3], [0, 0, 22, 1, 22, 1], [0, 0, 22, 3, 22, 3]],  # turn / row 5 / index 4
                                  [[0, 0, 24, 1, 24, 1], [0, 0, 24, 3, 24, 3], [0, 0, 26, 1, 26, 1], [0, 0, 26, 3, 26, 3]],  # turn / row 6 / index 5
                                  [[0, 0, 28, 1, 28, 1], [0, 0, 28, 3, 28, 3], [0, 0, 30, 1, 30, 1], [0, 0, 30, 3, 30, 3]],  # turn / row 7 / index 6
                                  [[0, 0, 32, 1, 32, 1], [0, 0, 32, 3, 32, 3], [0, 0, 34, 1, 34, 1], [0, 0, 34, 3, 34, 3]],  # turn / row 8 / index 7
                                  [[0, 0, 36, 1, 36, 1], [0, 0, 36, 3, 36, 3], [0, 0, 38, 1, 38, 1], [0, 0, 38, 3, 38, 3]],  # turn / row 9 / index 8
                                  [[0, 0, 40, 1, 40, 1], [0, 0, 40, 3, 40, 3], [0, 0, 42, 1, 42, 1], [0, 0, 42, 3, 42, 3]],  # turn / row 10 / index 9
                                  [[0, 0, 32, 46, 32, 46]],  # position in code feedback text out put
                                  ]
        self.position_feedback_half = [[[0, 1, 4, 1, 4, 1], [0, 1, 4, 3, 4, 3], [0, 1, 6, 1, 6, 1], [0, 1, 6, 3, 6, 3]],  # turn / row 1 / index 0
                                  [[0, 1, 8, 1, 8, 1], [0, 1, 8, 3, 8, 3], [0, 1, 10, 1, 10, 1], [0, 1, 10, 3, 10, 3]],  # turn / row 2 / index 1
                                  [[0, 1, 12, 1, 12, 1], [0, 1, 12, 3, 12, 3], [0, 1, 14, 1, 14, 1], [0, 1, 14, 3, 14, 3]],  # turn / row 3 / index 2
                                  [[0, 1, 16, 1, 16, 1], [0, 1, 16, 3, 16, 3], [0, 1, 18, 1, 18, 1], [0, 1, 18, 3, 18, 3]],  # turn / row 4 / index 3
                                  [[0, 1, 20, 1, 20, 1], [0, 1, 20, 3, 20, 3], [0, 1, 22, 1, 22, 1], [0, 1, 22, 3, 22, 3]],  # turn / row 5 / index 4
                                  [[0, 1, 24, 1, 24, 1], [0, 1, 24, 3, 24, 3], [0, 1, 26, 1, 26, 1], [0, 1, 26, 3, 26, 3]],  # turn / row 6 / index 5
                                  [[0, 1, 28, 1, 28, 1], [0, 1, 28, 3, 28, 3], [0, 1, 30, 1, 30, 1], [0, 1, 30, 3, 30, 3]],  # turn / row 7 / index 6
                                  [[0, 1, 32, 1, 32, 1], [0, 1, 32, 3, 32, 3], [0, 1, 34, 1, 34, 1], [0, 1, 34, 3, 34, 3]],  # turn / row 8 / index 7
                                  [[0, 1, 36, 1, 36, 1], [0, 1, 36, 3, 36, 3], [0, 1, 38, 1, 38, 1], [0, 1, 38, 3, 38, 3]],  # turn / row 9 / index 8
                                  [[0, 1, 40, 1, 40, 1], [0, 1, 40, 3, 40, 3], [0, 1, 42, 1, 42, 1], [0, 1, 42, 3, 42, 3]],  # turn / row 10 / index 9
                                  [[0, 1, 33, 58, 33, 58]],  # position in code feedback text out put
                                  ]
        self.has_color = 0
        self.match_color_position = 0
        self.player_code_matches_secret_code = False
        self.stop_time = False  # use to end the timer, loop breaks
        self.reset_time = False  # use to reset the in game display and its values
        self.update_timer = True  # use to pause the in game display update and the value update
        self.player_time_seconds_total = 0
        self.player_time_seconds = 0
        self.player_time_minutes = 0
        self.all_time_high_score = []
        self.all_time_high_score_new_entry = False
        self.this_month_high_score = []
        self.this_month_high_score_new_entry = False
        self.today_high_score = []
        self.today_high_score_new_entry = False
        self.score_date = score_date
        self.file_name_date = file_name_date
        self.today_month = today_month
        self.today_year = today_year
        self.today_day_name = today_day_name
        self.file_name_day_date = file_name_day_date
        self.play_game = True  # turn on the number options on the keyboard
        self.new_line_character = new_line_character
        self.set_new_high_score = False

    def arrow_input(self, arrow_key):
        # TODO tidy up code
        """
        Changes the current position in self.current_position or
        the color of self.color_mark_map.
        :param arrow_key: 'KEY_LEFT' 'KEY_RIGHT' 'KEY_UP' 'KEY_DOWN'
        :return: [current-position-row, current-position-field][current-position-color]
        """
        current_position_color = self.color_mark_map[self.current_position[0]][self.current_position[1]]
        index_color_order = self.color_order.index(current_position_color)
        # change current position
        if arrow_key == 'KEY_LEFT' and self.play_game:
            if self.current_position[1] == 0:  # if position field is outer left
                self.current_position[1] = 3  # then go position field outer right
            else:
                self.current_position[1] -= 1  # change position field to the left
            current_position_color = self.color_mark_map[self.current_position[0]][self.current_position[1]]
            if current_position_color == 'BLACK':  # if color at current position is black
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'RED'  # then change to red
        elif arrow_key == 'KEY_RIGHT' and self.play_game:
            if self.current_position[1] == 3:  # if position field is outer right
                self.current_position[1] = 0  # then go position field outer left
            else:
                self.current_position[1] += 1  # change position field to the right
            current_position_color = self.color_mark_map[self.current_position[0]][self.current_position[1]]
            if current_position_color == 'BLACK':  # if color at current position is black
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'RED'  # then change to red
        # change color
        elif arrow_key == 'KEY_UP' and self.play_game:
            if index_color_order == 0:  # if current color is at the color index 0
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'YELLOW'  # then change to yellow
            else:
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = self.color_order[index_color_order -1]  # otherwise, change to left color
        elif arrow_key == 'KEY_DOWN' and self.play_game:
            if index_color_order == 3:  # if current color is at the color index 3
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'RED'  # then change to red
            else:
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = self.color_order[index_color_order +1]  # otherwise, change to right color
        elif arrow_key == '#' and self.play_game:
            if self.color_mark_map[self.current_position[0]].count('BLACK') == 0:  # only if there is no 'black' fields
                self.update_player_code()  # update before current position is changed
                self.check_secret_code()  # need to update values before feedback message
                self.update_code_feedback_message()  # updates the "code feedback" message
                self.set_feedback_marker()  # sets the feedback marker on the board
                self.is_the_game_over()  # checks if the game is over
                if self.current_position[0] >= 0:  # stop at 0, otherwise it is going out of range
                    self.current_position[0] -= 1  # reduce the row number, go up
                    self.current_position[1] = 0  # go to left field
                    self.color_mark_map[self.current_position[0]][0] = 'RED'  # set the new field in the new row to red

        return self.set_new_high_score
        #return [self.current_position, self.color_mark_map[self.current_position[0]][self.current_position[1]]]  # [current-position-row, current-position-field]['color-at-current-position']

    def generate_secret_random_number(self):
        """
        Generate secret code from the elements "RED", "GREEN", "BLUE", "YELLOW" and saves it to self.secret_code.
        """
        code_elements = ["RED", "GREEN", "BLUE", "YELLOW"]
        self.secret_code = random.choices(code_elements, k=4)

    def update_player_code(self):
        """
        Checks the field values at the current line and updates the player_code property,
        only call if there are no 'black' fields left!
        """
        self.player_code = self.color_mark_map[self.current_position[0]].copy()

    def check_secret_code(self):
        """
        Compares the secret code and the player code and updates the values match_color_position and has_color.
        """
        copy_secret_code = self.secret_code.copy()  # create copy so the original is not altered
        match_color_position = 0
        has_color = 0
        for position in range(4):  # loops 4 times because there are no more than 4 values
            if self.secret_code[position] == self.player_code[position]:  # checks if the element match at the exact same index
                match_color_position += 1  # only if they match exactly, the match_color_position variable gets updated
        for position in range(4):  # loops 4 times because there are no more than 4 values
            try:
                copy_secret_code.index(self.player_code[position])  # checks if on of the player element matches the secret_code
            except:  # if there is no match, an error is raised which is 'passed'
                pass
            else:
                has_color += 1  # increments the has_color variable because there was a match
                copy_secret_code.remove(self.player_code[position])  # the already found element needs to be removed from the copied secred code list

        self.has_color = has_color - match_color_position  # has_color is always bigger or the same as match_color_position
        self.match_color_position = match_color_position

    def update_code_feedback_message(self):
        """
        Checks the values in match_color_position and has_color and updates the message with the line of the last
        submitted code and how many turns are left to play.
        """
        feedback_message = curses.newwin(4, 56, 31, 22)
        feedback_message.erase()
        feedback_message.addstr(f" On line {self.current_position[0] + 1} your code matches:\n> in color and position   {self.match_color_position} times,\n> only in color but not in position   {self.has_color} times,\n> you have {self.current_position[0]} turns left to 'break' the code.")
        feedback_message.refresh()

    def set_feedback_marker(self):
        """
        Sets the code feedback markers on the board.
        """
        curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # defines the color scheme of the marker
        FEEDB = curses.color_pair(6)  # color variable which is used when the pad is refreshed
        feedback_marker_pad = curses.newpad(1, 3)  # creates the pad for the feedback marker 1 row x max 3 cells if needed
        match_count = self.match_color_position  # how many times the color and position matches
        color_count = self.has_color  # how many times the color is correct but not the position
        field = 0  # starts on 0 and gets incremented everytime if the while loop runs, should not go over 3

        while match_count > 0:  # only loops if there is a matching color and position
            feedback_marker_pad.erase()  # is needed to avoid errors
            feedback_marker_pad.addstr(self.content_feedback, FEEDB)  # uses the content from content_feedback property and color variable FEEDB
            feedback_marker_pad.refresh(*self.position_feedback[self.current_position[0]][field])  # sets the marker depending on the value of current position and the field (no more then 3)

            match_count -= 1  # subtracts the match_count because it has already been printed once and to avoid endless loop
            field += 1  # increments the field so on the next loop the position changes (can not be over 3)

        while color_count > 0:  # only loops if there is a matching color but not the right position
            feedback_marker_pad.erase()  # is needed to avoid errors
            feedback_marker_pad.addstr(self.content_feedback, FEEDB)  # uses the content from content_feedback property and color variable FEEDB
            feedback_marker_pad.refresh(*self.position_feedback_half[self.current_position[0]][field])  # sets the marker depending on the value of current position and the field (no more then 3)

            color_count -= 1  # subtracts the match_count because it has already been printed once and to avoid endless loop
            field += 1  # increments the field so on the next loop the position changes (can not be over 3)

        # should be always set even if there are no matches, is for the feedback code box to make it more clrear but not esential
        feedback_marker_pad.erase()  # is needed to avoid errors
        feedback_marker_pad.addstr(self.content_feedback, FEEDB)  # uses the content from content_feedback property and color variable FEEDB
        feedback_marker_pad.refresh(*self.position_feedback[10][0])  # adds a marker in the code feedback section

        feedback_marker_pad.erase()  # is needed to avoid errors
        feedback_marker_pad.addstr(self.content_feedback, FEEDB)  # uses the content from content_feedback property and color variable FEEDB
        feedback_marker_pad.refresh(*self.position_feedback_half[10][0])  # adds a marker in the code feedback section

    def is_the_game_over(self):
        """
        Checks if the game is finished, and outputs a message accordingly to the feedback code section
        """
        game_over_message = curses.newwin(4, 56, 31, 22)
        game_over_message.erase()
        # game is over, player has played last line and there are no 4 perfect matching colors
        if self.current_position[0] == 0 and self.match_color_position != 4:
            self.update_timer = False
            game_over_message.addstr(f" Sorry, but you have not broken the code !!!\n You played {self.player_time_minutes} minute(s) and {self.player_time_seconds} second(s).\n The secret code was: {self.secret_code[0]}, {self.secret_code[1]}, {self.secret_code[2]}, {self.secret_code[3]}")
            game_over_message.refresh()
            self.play_game = False

        # position and color match, player has won the game
        elif self.match_color_position == 4:
            self.update_timer = False
            self.calculate_player_score()
            game_over_message.addstr(f" Congratulations, you have broken the code !!!\n It took you {self.player_time_minutes} minute(s) and {self.player_time_seconds} second(s).\n The secret code was: {self.secret_code[0]}, {self.secret_code[1]}, {self.secret_code[2]}, {self.secret_code[3]}\n Your score is: {self.player_score} (lines left {self.current_position[0]} x 200 - time {self.player_time_seconds_total}s)")
            game_over_message.refresh()
            self.play_game = False
            self.new_high_score()

    def calculate_player_score(self):
        """
        Calculates the player score. lines_left * 200 - time_needed
        """
        self.player_score = (self.current_position[0] * 200) - self.player_time_seconds_total

    def new_high_score(self):
        """
        Checks if the player score is higher than any other score in the all_time_high_score or this_month_high_score
        list. Handles the 'code feedback' message.
        """
        # all_ is for all_time_high_score list
        all_place = 0  # is the position of the score which is lower than the player score
        all_place_ending = ''  # puts the right wording after the number (e.g. 1st, 2nd , ...)
        all_points = 0  # points from the lower score than the players
        all_date = ''  # is the date when the score was created which is lower than the player score
        all_name = ''  # name of the player whose score is pushed down
        # month_ is for this_month_high_score list
        month_place = 0  # is the position of the score which is lower than the player score
        month_place_ending = ''  # puts the right wording after the number (e.g. 1st, 2nd , ...)
        month_points = 0  # points from the lower score than the players
        month_date = ''  # is the date when the score was created which is lower than the player score
        month_name = ''  # name of the player whose score is pushed down
        # today_ is for today_high_score list
        today_place = 0  # is the position of the score which is lower than the player score
        today_place_ending = ''  # puts the right wording after the number (e.g. 1st, 2nd , ...)
        today_points = 0  # points from the lower score than the players
        today_date = ''  # is the date when the score was created which is lower than the player score
        today_name = ''  # name of the player whose score is pushed down

        # calls the function from 'spreadsheet.py' which gets the google sheet data for the all_time_high_score list
        # (starting from the top of the list (is sorted by highest score first)
        self.all_time_high_score = spreadsheet.get_all_time_high_score()
        # loops through the google spread sheet list and compares the score with the player score
        for index in range(len(self.all_time_high_score)):
            # if the player score is higher the google sheet list, than the loop stops
            if self.player_score > self.all_time_high_score[index][2]:
                all_place = index + 1
                all_points = self.all_time_high_score[index][2]
                all_date = self.all_time_high_score[index][1]
                all_name = self.all_time_high_score[index][0]
                self.set_new_high_score = True  # becomes only true if the loop breaks
                self.all_time_high_score_new_entry = True
                if all_place == 1:
                    all_place_ending = 'st'
                elif all_place == 2:
                    all_place_ending = 'nd'
                elif all_place == 3:
                    all_place_ending = 'rd'
                elif all_place > 3:
                    all_place_ending = 'th'
                break

        # calls the function from 'spreadsheet.py' which gets the google sheet data for this_month_time_high_score list
        # (starting from the top of the list (is sorted by highest score first)
        self.this_month_high_score = spreadsheet.get_this_month_high_score(self.file_name_date)
        # loops through the google spread sheet list and compares the score with the player score
        for index in range(len(self.this_month_high_score)):
            # if the player score is higher the google sheet list, than the loop stops
            if self.player_score > self.this_month_high_score[index][2]:
                month_place = index + 1
                month_points = self.this_month_high_score[index][2]
                month_date = self.this_month_high_score[index][1]
                month_name = self.this_month_high_score[index][0]
                self.set_new_high_score = True  # becomes only true if the loop breaks
                self.this_month_high_score_new_entry = True
                if month_place == 1:
                    month_place_ending = 'st'
                elif month_place == 2:
                    month_place_ending = 'nd'
                elif month_place == 3:
                    month_place_ending = 'rd'
                elif month_place > 3:
                    month_place_ending = 'th'
                break

        # calls the function from 'spreadsheet.py' which gets the google sheet data for today_high_score list
        # (starting from the top of the list (is sorted by highest score first)
        self.today_high_score = spreadsheet.get_today_high_score(self.file_name_day_date)
        # loops through the google spread sheet list and compares the score with the player score
        for index in range(len(self.today_high_score)):
            # if the player score is higher the google sheet list, than the loop stops
            if self.player_score > self.today_high_score[index][2]:
                today_place = index + 1
                today_points = self.today_high_score[index][2]
                today_date = self.today_high_score[index][1]
                today_name = self.today_high_score[index][0]
                self.set_new_high_score = True  # becomes only true if the loop breaks
                self.today_high_score_new_entry = True
                if today_place == 1:
                    today_place_ending = 'st'
                elif today_place == 2:
                    today_place_ending = 'nd'
                elif today_place == 3:
                    today_place_ending = 'rd'
                elif today_place > 3:
                    today_place_ending = 'th'
                break

        if self.set_new_high_score:
            new_high_score_window = curses.newwin(21, 60, 15, 21)
            new_high_score_window.erase()
            new_high_score_window.addstr(f"╭━━━YOUR SCORE IS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┠╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┨\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┠╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┨\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"┃                                                         ┃\n"
                                         f"╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
            new_high_score_window.refresh()
            score_message_title = curses.newpad(1, 60)
            score_message_title.erase()
            score_message_title.addstr(f"{self.player_score} points")
            score_message_title.refresh(0, 0, 15, 39, 15, 49)
            score_message = curses.newpad(3, 60)
            score_message.erase()
            score_message.addstr(f"Your score calculation:\n{self.current_position[0]} (lines left) x 200 = {self.current_position[0]*200},\n"
                                 f"{self.current_position[0]*200} - {self.player_time_seconds_total}s (total time) "
                                 f"= {self.current_position[0]*200 - self.player_time_seconds_total} (your score)")
            score_message.refresh(0, 0, 17, 23, 20, 77)

            if today_place:
                last_entry = ''
                if self.today_high_score[19][2]:
                    last_entry = f"Unfortunate for {self.today_high_score[19][0]}'s score from 20{self.today_high_score[19][1]},\nhis\her score has fallen out of the list."
                today_title = f"NEW {self.today_month.upper()} HIGH SCORE"
                today_title_score_message = curses.newpad(1, 60)
                today_title_score_message.erase()
                today_title_score_message.addstr(today_title)
                today_title_score_message.refresh(0, 0, 20, 25, 20, 25+len(today_title)-1)
                today_score_message = curses.newpad(6, 55)
                today_score_message.erase()
                if today_name:
                    today_score_message.addstr(f"Your score is {self.player_score - today_points} points higher than\n"
                                               f"{today_name}'s score at {today_place}{today_place_ending} place from "
                                               f"20{today_date}.\n{last_entry}")
                else:
                    today_score_message.addstr(f"Your score is with {self.player_score} points at {today_place}{today_place_ending} place.")
                today_score_message.refresh(0, 0, 21, 23, 24, 77)

            if month_place:
                last_entry = ''
                if self.this_month_high_score[19][2]:
                    last_entry = f"Unfortunate for {self.this_month_high_score[19][0]}'s score from 20{self.this_month_high_score[19][1]},\nhis\her score has fallen out of the list."
                month_title = f"NEW {self.today_month.upper()} {self.today_year} HIGH SCORE"
                month_title_score_message = curses.newpad(1, 60)
                month_title_score_message.erase()
                month_title_score_message.addstr(month_title)
                month_title_score_message.refresh(0, 0, 25, 25, 25, 25+len(month_title)-1)
                month_score_message = curses.newpad(6, 55)
                month_score_message.erase()
                if month_name:
                    month_score_message.addstr(f"Your score is {self.player_score - month_points} points higher than\n"
                                               f"{month_name}'s score at {month_place}{month_place_ending} place from "
                                               f"20{month_date}.\n{last_entry}")
                else:
                    month_score_message.addstr(
                        f"Your score is with {self.player_score} points at {month_place}{month_place_ending} place.")
                month_score_message.refresh(0, 0, 26, 23, 29, 77)

            if all_place:
                last_entry = ''
                if self.all_time_high_score[19][2]:
                    last_entry = f"Unfortunate for {self.all_time_high_score[19][0]}'s score from 20{self.all_time_high_score[19][1]},\nhis\her score has fallen out of the list."
                all_title_score_message = curses.newpad(1, 60)
                all_title_score_message.erase()
                all_title_score_message.addstr(f"┠╌╌╌NEW ALL TIME HIGH SCORE╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┨")
                all_title_score_message.refresh(0, 0, 30, 21, 30, 79)
                all_score_message = curses.newpad(6, 55)
                all_score_message.erase()
                if all_name:
                    all_score_message.addstr(f"Your score is {self.player_score - all_points} points higher than\n"
                                               f"{all_name}'s score at {all_place}{all_place_ending} place from "
                                               f"20{all_date}.\n{last_entry}")
                else:
                    all_score_message.addstr(
                        f"Your score is with {self.player_score} points at {all_place}{all_place_ending} place.")
                all_score_message.refresh(0, 0, 31, 23, 34, 77)

    def ask_player_name(self, screen):
        """
        Ask player for his name and saves it to self.player_name.
        """
        curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        BORDER = curses.color_pair(9)
        HIGHLIGHT = curses.color_pair(7)
        if self.player_name:
            new_score_has_name = curses.newpad(8, 60)
            new_score_has_name.clear()
            new_score_has_name.addstr(f"╭━━━INSTRUCTIONS━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n"
                                      f"┃ We found the name                                       ┃\n"
                                      f"┃ Is it your name or would you like to change it?         ┃\n"
                                      f"┃ > Press 'y' for yes, if you want to change it.          ┃\n"
                                      f"┃   or                                                    ┃\n"
                                      f"┃ > Press any other key, if you want to keep it.          ┃\n"
                                      f"┃                                                         ┃\n"
                                      f"╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
            new_score_has_name.refresh(0, 0, 36, 21, 43, 79)
            database_name = curses.newpad(1, 40)
            database_name.erase()
            database_name.addstr(f"{self.player_name}", HIGHLIGHT)
            database_name.refresh(0, 0, 37, 41, 37, 54)
            database_name_ending = curses.newpad(1, 40)
            database_name_ending.erase()
            database_name_ending.addstr(f"in our database.")
            database_name_ending.refresh(0, 0, 37, 42+len(self.player_name), 37, 57+len(self.player_name))
            text_highlight = curses.newpad(1, 14)
            text_highlight.erase()
            text_highlight.addstr(f"y", HIGHLIGHT)
            text_highlight.refresh(0, 0, 39, 32, 39, 32)
            text_highlight.erase()
            text_highlight.addstr(f"any other key", HIGHLIGHT)
            text_highlight.refresh(0, 0, 41, 31, 41, 43)
            user_key = screen.getkey()
            if user_key.upper() == 'Y':
                self.player_name = False
            elif user_key.upper() == 'N':
                pass

        if not self.player_name:
            new_score_background = curses.newpad(8, 60)
            new_score_background.clear()
            new_score_background.addstr(f"╭━━━INSTRUCTIONS━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n"
                                        f"┃ We need your name for the high score entry.             ┃\n"
                                        f"┃                                                         ┃\n"
                                        f"┃ > Please, enter your name:   123456789a123              ┃\n"
                                        f"┃                                                         ┃\n"
                                        f'┃ > Confirm your entry with "ENTER".                      ┃\n'
                                        f"┃                                                         ┃\n"
                                        f"╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
            new_score_background.refresh(0, 0, 36, 21, 43, 79)
            highlight_text = curses.newpad(1, 10)
            highlight_text.erase()
            highlight_text.addstr(f"ENTER", HIGHLIGHT)
            highlight_text.refresh(0, 0, 41, 49, 41, 56)
            #highlight_text.erase()
            #highlight_text.addstr(f"G", HIGHLIGHT)
            #highlight_text.refresh(0, 0, 41, 56, 41, 57)
            highlight_name = curses.newpad(3, 20)
            highlight_name.erase()
            highlight_name.addstr(f"╭━━━━━━━━━━━━━━╮\n┃              ┃\n╰━━━━━━━━━━━━━━╯", BORDER)
            highlight_name.refresh(0, 0, 38, 51, 40, 66)
            player_text_input = curses.newwin(1, 14, 39, 52)
            if self.new_line_character:
                curses.curs_set(1)
            box = Textbox(player_text_input)
            box.edit()
            self.player_name = (box.gather()).rstrip(" ")
            if self.new_line_character:
                curses.curs_set(0)

        new_score_confirmation = curses.newpad(8, 60)
        new_score_confirmation.clear()
        new_score_confirmation.addstr(f"╭━━━INSTRUCTIONS━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n"
                                      f"┃ Thank you {self.player_name}                            ┃\n"
                                      f"┃ Your score has been saved.                              ┃\n"
                                      f"┃ Note, that only the first 6 scores are shown above.     ┃\n"
                                      f"┃ > Press 5 (ARCHIVE) to see all scores.                  ┃\n"
                                      f'┃ > Press 2 (RESTART) to start a new game.                ┃\n'
                                      f"┃ > Or any of the other numbers for the other options.    ┃\n"
                                      f"╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
        new_score_confirmation.refresh(0, 0, 36, 21, 43, 78)
        after_player_name = curses.newpad(1, 58)
        after_player_name.erase()
        after_player_name.addstr(f"for playing 'Code Breaker' !")
        after_player_name.refresh(0, 0, 37, 34 + len(self.player_name), 37, 61 + len(self.player_name))
        highlight_text_1 = curses.newpad(1, 2)
        highlight_text_1.erase()
        highlight_text_1.addstr(f"5", HIGHLIGHT)
        highlight_text_1.refresh(0, 0, 40, 31, 40, 31)
        highlight_text_2 = curses.newpad(1, 2)
        highlight_text_2.erase()
        highlight_text_2.addstr(f"2", HIGHLIGHT)
        highlight_text_2.refresh(0, 0, 41, 31, 41, 31)

        if self.all_time_high_score_new_entry:
            self.all_time_high_score.insert(0, [self.player_name, self.score_date, self.player_score, self.current_position[0]+1, self.player_time_seconds_total])
            self.all_time_high_score = self.all_time_high_score[:20]
            spreadsheet.update_high_score_list('all_time_high_score', self.all_time_high_score)
            self.all_time_high_score_new_entry = False

        if self.this_month_high_score_new_entry:
            self.this_month_high_score.insert(0, [self.player_name, self.score_date, self.player_score, self.current_position[0]+1, self.player_time_seconds_total])
            self.this_month_high_score = self.this_month_high_score[:20]
            spreadsheet.update_high_score_list(self.file_name_date, self.this_month_high_score)
            self.this_month_high_score_new_entry = False

        if self.today_high_score_new_entry:
            self.today_high_score.insert(0, [self.player_name, self.score_date, self.player_score, self.current_position[0]+1, self.player_time_seconds_total])
            self.today_high_score = self.today_high_score[:20]
            spreadsheet.update_high_score_list(self.file_name_day_date, self.today_high_score)
            self.today_high_score_new_entry = False


    def reset_player(self):
        """
        Restarts the player attributes in the player Object, restarts the timer, generates a new secret code,
        clears the board from the marker and set it back to the beginning.
        """
        self.player_code = []
        self.player_score = 0
        self.current_position = [9, 0]  # row 10, first left, current position of the marker
        self.color_mark_map = [['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 1 / index 0
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 2 / index 1
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 3 / index 2
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 4 / index 3
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 5 / index 4
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 6 / index 5
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 7 / index 6
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 8 / index 7
                                ['BLACK', 'BLACK', 'BLACK', 'BLACK'],  # turn / row 9 / index 8
                                ['RED', 'BLACK', 'BLACK', 'BLACK']]  # turn / row 10 / index 9 / do not set ',' on the end!
        self.has_color = 0
        self.match_color_position = 0
        self.player_code_matches_secret_code = False
        self.reset_time = True
        self.update_timer = True
        self.player_time_seconds_total = 0
        self.player_time_seconds = 0
        self.player_time_minutes = 0
        self.play_game = True
        self.set_new_high_score = False
        # TODO comment out if no random secret code to be generated, the default for testing is 'RED' for times
        # self.generate_secret_random_number()


