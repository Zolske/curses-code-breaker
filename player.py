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
                                ['RED', 'BLACK', 'BLACK', 'BLACK']]  # turn / row 10 / index 9

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
        return [self.current_position, self.color_mark_map[self.current_position[0]][self.current_position[1]]]  # [current-position-row, current-position-field]['color-at-current-position']
