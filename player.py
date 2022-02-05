import random
import curses
import menu

class PlayerObject:
    def __init__(self):
        self.secret_code = [],
        self.player_code = [],
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
                                  ]
        self.has_color = 0
        self.match_color_position = 0
        self.player_code_matches_secret_code = False

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
        if arrow_key == 'KEY_LEFT':
            if self.current_position[1] == 0:  # if position field is outer left
                self.current_position[1] = 3  # then go position field outer right
            else:
                self.current_position[1] -= 1  # change position field to the left
            current_position_color = self.color_mark_map[self.current_position[0]][self.current_position[1]]
            if current_position_color == 'BLACK':  # if color at current position is black
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'RED'  # then change to red
        elif arrow_key == 'KEY_RIGHT':
            if self.current_position[1] == 3:  # if position field is outer right
                self.current_position[1] = 0  # then go position field outer left
            else:
                self.current_position[1] += 1  # change position field to the right
            current_position_color = self.color_mark_map[self.current_position[0]][self.current_position[1]]
            if current_position_color == 'BLACK':  # if color at current position is black
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'RED'  # then change to red
        # change color
        elif arrow_key == 'KEY_UP':
            if index_color_order == 0:  # if current color is at the color index 0
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'YELLOW'  # then change to yellow
            else:
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = self.color_order[index_color_order -1]  # otherwise, change to left color
        elif arrow_key == 'KEY_DOWN':
            if index_color_order == 3:  # if current color is at the color index 3
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = 'RED'  # then change to red
            else:
                self.color_mark_map[self.current_position[0]][self.current_position[1]] = self.color_order[index_color_order +1]  # otherwise, change to right color
        elif arrow_key == 'KEY_END':
            if self.color_mark_map[self.current_position[0]].count('BLACK') == 0:  # only if there is no 'black' fields
                self.update_player_code()  # update before current position is changed
                self.check_secret_code()  # need to update values before feedback message
                self.update_code_feedback_message()  # updates the "code feedback" message
                self.is_the_game_over()  # checks if the game is over
                self.set_feedback_marker()  # sets the feedback marker on the board
                if self.current_position[0] >= 0:  # stop at 0, otherwise it is going out of range
                    self.current_position[0] -= 1  # reduce the row number, go up
                    self.current_position[1] = 0  # go to left field
                    self.color_mark_map[self.current_position[0]][0] = 'RED'  # set the new field in the new row to red

        return [self.current_position, self.color_mark_map[self.current_position[0]][self.current_position[1]]]  # [current-position-row, current-position-field]['color-at-current-position']

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
        feedback_message = curses.newwin(3, 56, 32, 22)
        feedback_message.erase()
        feedback_message.addstr(f" On line {self.current_position[0] + 1} your code matches in color and position {self.match_color_position}\n times and only in color but not in position {self.has_color} times,\n you have {self.current_position[0]} turns left to 'break' the code.")
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

    def is_the_game_over(self):
        game_over_message = curses.newwin(3, 56, 32, 22)
        game_over_message.erase()
        if self.current_position[0] == 0 and self.match_color_position != 4:
            game_over_message.addstr(f" Sorry, but you have not broken the code !!!\n The secret code was: \n {self.secret_code[0]}, {self.secret_code[1]}, {self.secret_code[2]}, {self.secret_code[3]}")
            game_over_message.refresh()
        elif self.match_color_position == 4:
            game_over_message.addstr(f" Congratulations, you have broken the code !!!\n The secret code was: \n {self.secret_code[0]}, {self.secret_code[1]}, {self.secret_code[2]}, {self.secret_code[3]}")
            game_over_message.refresh()
