import curses


class Game:
    def __init__(self):
        #  alignment "0123456789a123456789b123456789c123456789d123456789e123456789f123456789g123456789h"
        self.line = ["                                                                                ", #00
                     "    ╓━TIME━━╥━TIMER━╖   ╭┈┈┈┈┈┈╮ ╭┈┈┈┈┈┈┈┈┈╮ ╭┈┈┈┈┈┈┈┈┈┈╮ ╭┈┈┈┈┈┈╮ ╭┈┈┈┈┈┈┈┈┈╮  ", #01
                     "    ║ 00:00 ║ 00:00 ║   ╞1═EXIT╡ ╞2═RESTART╡ ╞3═SETTINGS╡ ╞4═HELP╡ ╞5═CONTACT╡  ", #02
                     "╔═╤═╬═══╦═══╬═══╦═══╣   ╰┈┈┈┈┈┈╯ ╰┈┈┈┈┈┈┈┈┈╯ ╰┈┈┈┈┈┈┈┈┈┈╯ ╰┈┈┈┈┈┈╯ ╰┈┈┈┈┈┈┈┈┈╯  ", #03
                     "║ ┃ ║1  ║   ║   ║   ║                              __                           ", #04
                     "╟━╋━╢   ║   ║   ║   ║           _____  ____   ____/ / ___                       ", #05
                     "║ ┃ ║   ║   ║   ║   ║          / ___/ / __ \ / __  / / _ \                      ", #06
                     "╠═╪═╬═══╬═══╬═══╬═══╣         / /__  / /_/ // /_/ / /  __/                      ", #07
                     "║ ┃ ║2  ║   ║   ║   ║         \___/  \____/ \__,_/  \___/                       ", #08
                     "╟━╋━╢   ║   ║   ║   ║       __                          __                      ", #09
                     "║ ┃ ║   ║   ║   ║   ║      / /_    ____  ___   ____ _  / /__  ___    ____       ", #10
                     "╠═╪═╬═══╬═══╬═══╬═══╣     / __ \  / __/ / _ \ / __ `/ / //_/ / _ \  / __/       ", #11
                     "║ ┃ ║3  ║   ║   ║   ║    / /_/ / / /   /  __// /_/ / / ,<   /  __/ / /          ", #12
                     "╟━╋━╢   ║   ║   ║   ║   /_.___/ /_/    \___/ \__,_/ /_/|_|  \___/ /_/           ", #13
                     "║ ┃ ║   ║   ║   ║   ║                                                           ", #14
                     "╠═╪═╬═══╬═══╬═══╬═══╣╭━━━━━━GLOBAL━HIGHSCORE━━━━━━┰━━━━━━LOCAL━━HIGHSCORE━━━━━━╮", #15
                     "║ ┃ ║4  ║   ║   ║   ║╞NAME══════════╤DATE══╤SCORE═╪NAME══════════╤DATE══╤SCORE═╡", #16
                     "╟━╋━╢   ║   ║   ║   ║┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #17
                     "║ ┃ ║   ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #18
                     "╠═╪═╬═══╬═══╬═══╬═══╣┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #19
                     "║ ┃ ║5  ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #20
                     "╟━╋━╢   ║   ║   ║   ║┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #21
                     "║ ┃ ║   ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #22
                     "╠═╪═╬═══╬═══╬═══╬═══╣┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #23
                     "║ ┃ ║6  ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #24
                     "╟━╋━╢   ║   ║   ║   ║┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #25
                     "║ ┃ ║   ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #26
                     "╠═╪═╬═══╬═══╬═══╬═══╣┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #27
                     "║ ┃ ║7  ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #28
                     "╟━╋━╢   ║   ║   ║   ║╰━━━━━━━━━━━━━━┷━━━━━━┷━━━━━━╨━━━━━━━━━━━━━━┷━━━━━━┷━━━━━━╯", #29
                     "║ ┃ ║   ║   ║   ║   ║╭━━━CODE FEEDBACK━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮", #30
                     "╠═╪═╬═══╬═══╬═══╬═══╣┃ After you have set 4 colors in one line, you can press  ┃", #31
                     "║ ┃ ║8  ║   ║   ║   ║┃ the 'End' key to confirm your code. Your code will be   ┃", #32
                     "╟━╋━╢   ║   ║   ║   ║┃ compared to the secret code, the feedback appears here. ┃", #33
                     "║ ┃ ║   ║   ║   ║   ║┃                                                         ┃", #34
                     "╠═╪═╬═══╬═══╬═══╬═══╣╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯", #35
                     "║ ┃ ║9  ║   ║   ║   ║╭━━━INSTRUCTIONS━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮", #36
                     "╟━╋━╢   ║   ║   ║   ║┃> use the left ← & right → arrow keys to move            ┃", #37
                     "║ ┃ ║   ║   ║   ║   ║┃  left or right on the board                             ┃", #38
                     "╠═╪═╬═══╬═══╬═══╬═══╣┃> use the up ↑ & down ↓ arrow keys to change             ┃", #39
                     "║ ┃ ║10 ║   ║   ║   ║┃  the color of your code                                 ┃", #40
                     "╟━╋━╢   ║   ║   ║   ║┃> press the '#' key to confirm your turn                 ┃", #41
         # alignment "123456789a123456789b123456789c123456789d123456789e123456789f123456789g123456789h"
                     "║ ┃ ║   ║   ║   ║   ║┃> press the marked number to get into the menu (4 help)  ┃", #42
                     "╚═╧═╩═══╩═══╩═══╩═══╝╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯"  #43
                     ]
        self.content_marker = "    ↑  ↑ \n   ← →←↲→\n    ↓  ↓ "  # content of the pad / player-marker
        self.position_marker = [[[0, 0, 4, 5, 6, 7], [0, 0, 4, 9, 6, 11], [0, 0, 4, 13, 6, 15], [0, 0, 4, 17, 6, 19]],  # turn / row 1 / index 0
                                [[0, 0, 8, 5, 10, 7], [0, 0, 8, 9, 10, 11], [0, 0, 8, 13, 10, 15], [0, 0, 8, 17, 10, 19]],  # turn / row 2 / index 1
                                [[0, 0, 12, 5, 14, 7], [0, 0, 12, 9, 14, 11], [0, 0, 12, 13, 14, 15], [0, 0, 12, 17, 14, 19]],  # turn / row 3 / index 2
                                [[0, 0, 16, 5, 18, 7], [0, 0, 16, 9, 18, 11], [0, 0, 16, 13, 18, 15], [0, 0, 16, 17, 18, 19]],  # turn / row 4 / index 3
                                [[0, 0, 20, 5, 22, 7], [0, 0, 20, 9, 22, 11], [0, 0, 20, 13, 22, 15], [0, 0, 20, 17, 22, 19]],  # turn / row 5 / index 4
                                [[0, 0, 24, 5, 26, 7], [0, 0, 24, 9, 26, 11], [0, 0, 24, 13, 26, 15], [0, 0, 24, 17, 26, 19]],  # turn / row 6 / index 5
                                [[0, 0, 28, 5, 30, 7], [0, 0, 28, 9, 30, 11], [0, 0, 28, 13, 30, 15], [0, 0, 28, 17, 30, 19]],  # turn / row 7 / index 6
                                [[0, 0, 32, 5, 34, 7], [0, 0, 32, 9, 34, 11], [0, 0, 32, 13, 34, 15], [0, 0, 32, 17, 34, 19]],  # turn / row 8 / index 7
                                [[0, 0, 36, 5, 38, 7], [0, 0, 36, 9, 38, 11], [0, 0, 36, 13, 38, 15], [0, 0, 36, 17, 38, 19]],  # turn / row 9 / index 8
                                [[0, 0, 40, 5, 42, 7], [0, 0, 40, 9, 42, 11], [0, 0, 40, 13, 42, 15], [0, 0, 40, 17, 42, 19]],  # turn / row 10 / index 9
                                ]
        self.position_select = [[[0, 3, 4, 5, 6, 7], [0, 3, 4, 9, 6, 11], [0, 3, 4, 13, 6, 15], [0, 3, 4, 17, 6, 19]],  # turn / row 1 / index 0
                                [[0, 3, 8, 5, 10, 7], [0, 3, 8, 9, 10, 11], [0, 3, 8, 13, 10, 15], [0, 3, 8, 17, 10, 19]],  # turn / row 2 / index 1
                                [[0, 3, 12, 5, 14, 7], [0, 3, 12, 9, 14, 11], [0, 3, 12, 13, 14, 15], [0, 3, 12, 17, 14, 19]],  # turn / row 3 / index 2
                                [[0, 3, 16, 5, 18, 7], [0, 3, 16, 9, 18, 11], [0, 3, 16, 13, 18, 15], [0, 3, 16, 17, 18, 19]],  # turn / row 4 / index 3
                                [[0, 3, 20, 5, 22, 7], [0, 3, 20, 9, 22, 11], [0, 3, 20, 13, 22, 15], [0, 3, 20, 17, 22, 19]],  # turn / row 5 / index 4
                                [[0, 3, 24, 5, 26, 7], [0, 3, 24, 9, 26, 11], [0, 3, 24, 13, 26, 15], [0, 3, 24, 17, 26, 19]],  # turn / row 6 / index 5
                                [[0, 3, 28, 5, 30, 7], [0, 3, 28, 9, 30, 11], [0, 3, 28, 13, 30, 15], [0, 3, 28, 17, 30, 19]],  # turn / row 7 / index 6
                                [[0, 3, 32, 5, 34, 7], [0, 3, 32, 9, 34, 11], [0, 3, 32, 13, 34, 15], [0, 3, 32, 17, 34, 19]],  # turn / row 8 / index 7
                                [[0, 3, 36, 5, 38, 7], [0, 3, 36, 9, 38, 11], [0, 3, 36, 13, 38, 15], [0, 3, 36, 17, 38, 19]],  # turn / row 9 / index 8
                                [[0, 3, 40, 5, 42, 7], [0, 3, 40, 9, 42, 11], [0, 3, 40, 13, 42, 15], [0, 3, 40, 17, 42, 19]],  # turn / row 10 / index 9
                                ]
        self.position_enter = [[[0, 6, 4, 5, 6, 7], [0, 6, 4, 9, 6, 11], [0, 6, 4, 13, 6, 15], [0, 6, 4, 17, 6, 19]],  # turn / row 1 / index 0
                                [[0, 6, 8, 5, 10, 7], [0, 6, 8, 9, 10, 11], [0, 6, 8, 13, 10, 15], [0, 6, 8, 17, 10, 19]],  # turn / row 2 / index 1
                                [[0, 6, 12, 5, 14, 7], [0, 6, 12, 9, 14, 11], [0, 6, 12, 13, 14, 15], [0, 6, 12, 17, 14, 19]],  # turn / row 3 / index 2
                                [[0, 6, 16, 5, 18, 7], [0, 6, 16, 9, 18, 11], [0, 6, 16, 13, 18, 15], [0, 6, 16, 17, 18, 19]],  # turn / row 4 / index 3
                                [[0, 6, 20, 5, 22, 7], [0, 6, 20, 9, 22, 11], [0, 6, 20, 13, 22, 15], [0, 6, 20, 17, 22, 19]],  # turn / row 5 / index 4
                                [[0, 6, 24, 5, 26, 7], [0, 6, 24, 9, 26, 11], [0, 6, 24, 13, 26, 15], [0, 6, 24, 17, 26, 19]],  # turn / row 6 / index 5
                                [[0, 6, 28, 5, 30, 7], [0, 6, 28, 9, 30, 11], [0, 6, 28, 13, 30, 15], [0, 6, 28, 17, 30, 19]],  # turn / row 7 / index 6
                                [[0, 6, 32, 5, 34, 7], [0, 6, 32, 9, 34, 11], [0, 6, 32, 13, 34, 15], [0, 6, 32, 17, 34, 19]],  # turn / row 8 / index 7
                                [[0, 6, 36, 5, 38, 7], [0, 6, 36, 9, 38, 11], [0, 6, 36, 13, 38, 15], [0, 6, 36, 17, 38, 19]],  # turn / row 9 / index 8
                                [[0, 6, 40, 5, 42, 7], [0, 6, 40, 9, 42, 11], [0, 6, 40, 13, 42, 15], [0, 6, 40, 17, 42, 19]],  # turn / row 10 / index 9
                                ]
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
                                  ]

    def set_colors(self):
        """
        Highlights important text on the game screen
        """
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)
        RED = curses.color_pair(1)
        HIGHLIGHT = curses.color_pair(7)
        ORIGINAL = curses.color_pair(8)
        text_highlight_pad = curses.newpad(1, 10)
        # top navigation bar
        text_highlight_pad.erase()
        text_highlight_pad.addstr("1", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 2, 25, 2, 25)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("EXIT", HIGHLIGHT | curses.A_REVERSE)
        text_highlight_pad.refresh(0, 0, 2, 27, 2, 30)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("2", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 2, 34, 2, 34)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("RESTART", HIGHLIGHT | curses.A_REVERSE)
        text_highlight_pad.refresh(0, 0, 2, 36, 2, 42)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("3", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 2, 46, 2, 46)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("SETTINGS", HIGHLIGHT | curses.A_REVERSE)
        text_highlight_pad.refresh(0, 0, 2, 48, 2, 55)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("4", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 2, 59, 2, 59)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("HELP", HIGHLIGHT | curses.A_REVERSE)
        text_highlight_pad.refresh(0, 0, 2, 61, 2, 64)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("5", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 2, 68, 2, 68)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("CONTACT", HIGHLIGHT | curses.A_REVERSE)
        text_highlight_pad.refresh(0, 0, 2, 70, 2, 76)
        # arrows in Instructions
        text_highlight_pad.erase()
        text_highlight_pad.addstr("←", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 37, 37, 37, 37)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("→", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 37, 47, 37, 47)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("↑", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 39, 35, 39, 35)
        text_highlight_pad.erase()
        text_highlight_pad.addstr("↓", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 39, 44, 39, 44)
        # number marker for help menu example
        text_highlight_pad.erase()
        text_highlight_pad.addstr("4", HIGHLIGHT)
        text_highlight_pad.refresh(0, 0, 42, 70, 42, 70)
        # add initial marker
        marker = curses.newpad(3, 10)
        marker.erase()
        marker.addstr(self.content_marker, RED)
        marker.refresh(0, 3, 40, 5, 42, 7)
