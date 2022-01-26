class Game:
    def __init__(self):
        #  alignment "0123456789a123456789b123456789c123456789d123456789e123456789f123456789g123456789h"
        self.line = ["                      ╭┈┈┈┈┈┈┈┈┈╮     ╭┈┈┈┈┈┈┈┈┈┈╮     ╭┈┈┈┈┈┈╮     ╭┈┈┈┈┈┈┈┈┈╮ ", #00
                     "    ╓━TIME━━╥━TIMER━╖ ╞1═RESTART╡     ╞2═SETTINGS╡     ╞3═HELP╡     ╞4═CONTACT╡ ", #01
                     "    ║ 00:00 ║ 00:00 ║ ╰┈┈┈┈┈┈┈┈┈╯     ╰┈┈┈┈┈┈┈┈┈┈╯ __  ╰┈┈┈┈┈┈╯     ╰┈┈┈┈┈┈┈┈┈╯ ", #02
                     "╔═╤═╬═══╦═══╬═══╦═══╣           _____  ____   ____/ / ___                       ", #03
                     "║ ┃ ║1  ║   ║   ║   ║          / ___/ / __ \ / __  / / _ \                      ", #04
                     "╟━╋━╢   ║   ║   ║   ║         / /__  / /_/ // /_/ / /  __/                      ", #05
                     "║ ┃ ║   ║   ║   ║   ║         \___/  \____/ \__,_/  \___/                       ", #06
                     "╠═╪═╬═══╬═══╬═══╬═══╣       __                          __                      ", #07
                     "║ ┃ ║2  ║   ║   ║   ║      / /_    ____  ___   ____ _  / /__  ___    ____       ", #08
                     "╟━╋━╢   ║   ║   ║   ║     / __ \  / __/ / _ \ / __ `/ / //_/ / _ \  / __/       ", #09
                     "║ ┃ ║   ║   ║   ║   ║    / /_/ / / /   /  __// /_/ / / ,<   /  __/ / /          ", #10
                     "╠═╪═╬═══╬═══╬═══╬═══╣   /_.___/ /_/    \___/ \__,_/ /_/|_|  \___/ /_/           ", #11
                     "║ ┃ ║3  ║   ║   ║   ║                                                           ", #12
                     "╟━╋━╢   ║   ║   ║   ║╭━━━━━━GLOBAL━HIGHSCORE━━━━━━┰━━━━━━LOCAL━━HIGHSCORE━━━━━━╮", #13
                     "║ ┃ ║   ║   ║   ║   ║╞NAME══════════╤DATE══╤SCORE═╪NAME══════════╤DATE══╤SCORE═╡", #14
                     "╠═╪═╬═══╬═══╬═══╬═══╣┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #15
                     "║ ┃ ║4  ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #16
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
                     "╟━╋━╢   ║   ║   ║   ║┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #29
                     "║ ┃ ║   ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #30
                     "╠═╪═╬═══╬═══╬═══╬═══╣┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #31
                     "║ ┃ ║8  ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #32
                     "╟━╋━╢   ║   ║   ║   ║┠━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━╫━━━━━━━━━━━━━━╂━━━━━━╂━━━━━━┤", #33
                     "║ ┃ ║   ║   ║   ║   ║┠JOHN DOE      ┠YYMMDD┠000000╟              ┠      ┠      ┃", #34
                     "╠═╪═╬═══╬═══╬═══╬═══╣╰━━━━━━━━━━━━━━┷━━━━━━┷━━━━━━╨━━━━━━━━━━━━━━┷━━━━━━┷━━━━━━╯", #35
                     "║ ┃ ║9  ║   ║   ║   ║╭━━━INSTRUCTIONS━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮", #36
                     "╟━╋━╢   ║   ║   ║   ║┃> use the left ← & right → arrow keys to move            ┃", #37
                     "║ ┃ ║   ║   ║   ║   ║┃  left or right on the board                             ┃", #38
                     "╠═╪═╬═══╬═══╬═══╬═══╣┃> use the up ↑ & down ↓ arrow keys to change             ┃", #39
                     "║ ┃ ║10 ║   ║   ║   ║┃  the color of your code                                 ┃", #40
                     "╟━╋━╢   ║   ║   ║   ║┃> press enter ↲ to confirm your turn                     ┃", #41
         # alignment "123456789a123456789b123456789c123456789d123456789e123456789f123456789g123456789h"
                     "║ ┃ ║   ║   ║   ║   ║┃> press the marked number to get into the menu (3 help)  ┃", #42
                     "╚═╧═╩═══╩═══╩═══╩═══╝╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯"  #43
                     ]
        self.content_marker = "    ↑  ↑ \n   ← →←↲→\n    ↓  ↓ "  # content of the panel / player-marker
        self.position_marker = [[[0, 0, 4, 5, 6, 7], [0, 0, 4, 9, 6, 11], [0, 0, 4, 13, 6, 15], [0, 0, 4, 17, 6, 19]], # turn / row 1
                                [[0, 0, 8, 5, 10, 7], [0, 0, 8, 9, 10, 11], [0, 0, 8, 13, 10, 15], [0, 0, 8, 17, 10, 19]],  # turn / row 2
                                [[0, 0, 12, 5, 14, 7], [0, 0, 12, 9, 14, 11], [0, 0, 12, 13, 14, 15], [0, 0, 12, 17, 14, 19]],  # turn / row 3
                                [[0, 0, 16, 5, 18, 7], [0, 0, 16, 9, 18, 11], [0, 0, 16, 13, 18, 15], [0, 0, 16, 17, 18, 19]],  # turn / row 4
                                [[0, 0, 20, 5, 22, 7], [0, 0, 20, 9, 22, 11], [0, 0, 20, 13, 22, 15], [0, 0, 20, 17, 22, 19]],  # turn / row 5
                                [[0, 0, 24, 5, 26, 7], [0, 0, 24, 9, 26, 11], [0, 0, 24, 13, 26, 15], [0, 0, 24, 17, 26, 19]],  # turn / row 6
                                [[0, 0, 28, 5, 30, 7], [0, 0, 28, 9, 30, 11], [0, 0, 28, 13, 30, 15], [0, 0, 28, 17, 30, 19]],  # turn / row 7
                                [[0, 0, 32, 5, 34, 7], [0, 0, 32, 9, 34, 11], [0, 0, 32, 13, 34, 15], [0, 0, 32, 17, 34, 19]],  # turn / row 8
                                [[0, 0, 36, 5, 38, 7], [0, 0, 36, 9, 38, 11], [0, 0, 36, 13, 38, 15], [0, 0, 36, 17, 38, 19]],  # turn / row 9
                                [[0, 0, 40, 5, 42, 7], [0, 0, 40, 9, 42, 11], [0, 0, 40, 13, 42, 15], [0, 0, 40, 17, 42, 19]],  # turn / row 10
                                ]
        self.position_select = [[[0, 3, 4, 5, 6, 7], [0, 3, 4, 9, 6, 11], [0, 3, 4, 13, 6, 15], [0, 3, 4, 17, 6, 19]], # turn / row 1
                                [[0, 3, 8, 5, 10, 7], [0, 3, 8, 9, 10, 11], [0, 3, 8, 13, 10, 15], [0, 3, 8, 17, 10, 19]],  # turn / row 2
                                [[0, 3, 12, 5, 14, 7], [0, 3, 12, 9, 14, 11], [0, 3, 12, 13, 14, 15], [0, 3, 12, 17, 14, 19]],  # turn / row 3
                                [[0, 3, 16, 5, 18, 7], [0, 3, 16, 9, 18, 11], [0, 3, 16, 13, 18, 15], [0, 3, 16, 17, 18, 19]],  # turn / row 4
                                [[0, 3, 20, 5, 22, 7], [0, 3, 20, 9, 22, 11], [0, 3, 20, 13, 22, 15], [0, 3, 20, 17, 22, 19]],  # turn / row 5
                                [[0, 3, 24, 5, 26, 7], [0, 3, 24, 9, 26, 11], [0, 3, 24, 13, 26, 15], [0, 3, 24, 17, 26, 19]],  # turn / row 6
                                [[0, 3, 28, 5, 30, 7], [0, 3, 28, 9, 30, 11], [0, 3, 28, 13, 30, 15], [0, 3, 28, 17, 30, 19]],  # turn / row 7
                                [[0, 3, 32, 5, 34, 7], [0, 3, 32, 9, 34, 11], [0, 3, 32, 13, 34, 15], [0, 3, 32, 17, 34, 19]],  # turn / row 8
                                [[0, 3, 36, 5, 38, 7], [0, 3, 36, 9, 38, 11], [0, 3, 36, 13, 38, 15], [0, 3, 36, 17, 38, 19]],  # turn / row 9
                                [[0, 3, 40, 5, 42, 7], [0, 3, 40, 9, 42, 11], [0, 3, 40, 13, 42, 15], [0, 3, 40, 17, 42, 19]],  # turn / row 10
                                ]
        self.position_enter = [[[0, 6, 4, 5, 6, 7], [0, 6, 4, 9, 6, 11], [0, 6, 4, 13, 6, 15], [0, 6, 4, 17, 6, 19]], # turn / row 1
                                [[0, 6, 8, 5, 10, 7], [0, 6, 8, 9, 10, 11], [0, 6, 8, 13, 10, 15], [0, 6, 8, 17, 10, 19]],  # turn / row 2
                                [[0, 6, 12, 5, 14, 7], [0, 6, 12, 9, 14, 11], [0, 6, 12, 13, 14, 15], [0, 6, 12, 17, 14, 19]],  # turn / row 3
                                [[0, 6, 16, 5, 18, 7], [0, 6, 16, 9, 18, 11], [0, 6, 16, 13, 18, 15], [0, 6, 16, 17, 18, 19]],  # turn / row 4
                                [[0, 6, 20, 5, 22, 7], [0, 6, 20, 9, 22, 11], [0, 6, 20, 13, 22, 15], [0, 6, 20, 17, 22, 19]],  # turn / row 5
                                [[0, 6, 24, 5, 26, 7], [0, 6, 24, 9, 26, 11], [0, 6, 24, 13, 26, 15], [0, 6, 24, 17, 26, 19]],  # turn / row 6
                                [[0, 6, 28, 5, 30, 7], [0, 6, 28, 9, 30, 11], [0, 6, 28, 13, 30, 15], [0, 6, 28, 17, 30, 19]],  # turn / row 7
                                [[0, 6, 32, 5, 34, 7], [0, 6, 32, 9, 34, 11], [0, 6, 32, 13, 34, 15], [0, 6, 32, 17, 34, 19]],  # turn / row 8
                                [[0, 6, 36, 5, 38, 7], [0, 6, 36, 9, 38, 11], [0, 6, 36, 13, 38, 15], [0, 6, 36, 17, 38, 19]],  # turn / row 9
                                [[0, 6, 40, 5, 42, 7], [0, 6, 40, 9, 42, 11], [0, 6, 40, 13, 42, 15], [0, 6, 40, 17, 42, 19]],  # turn / row 10
                                ]
        self.content_feedback = "█▂"
        self.position_feedback = [[[0, 0, 4, 1, 4, 1], [0, 0, 4, 3, 4, 3], [0, 0, 6, 1, 6, 1], [0, 0, 6, 3, 6, 3]],  # turn / row 1
                                  [[0, 0, 8, 1, 8, 1], [0, 0, 8, 3, 8, 3], [0, 0, 10, 1, 10, 1], [0, 0, 10, 3, 10, 3]],  # turn / row 2
                                  [[0, 0, 12, 1, 12, 1], [0, 0, 12, 3, 12, 3], [0, 0, 14, 1, 14, 1], [0, 0, 14, 3, 14, 3]],  # turn / row 3
                                  [[0, 0, 16, 1, 16, 1], [0, 0, 16, 3, 16, 3], [0, 0, 18, 1, 18, 1], [0, 0, 18, 3, 18, 3]],  # turn / row 4
                                  [[0, 0, 20, 1, 20, 1], [0, 0, 20, 3, 20, 3], [0, 0, 22, 1, 22, 1], [0, 0, 22, 3, 22, 3]],  # turn / row 5
                                  [[0, 0, 24, 1, 24, 1], [0, 0, 24, 3, 24, 3], [0, 0, 26, 1, 26, 1], [0, 0, 26, 3, 26, 3]],  # turn / row 6
                                  [[0, 0, 28, 1, 28, 1], [0, 0, 28, 3, 28, 3], [0, 0, 30, 1, 30, 1], [0, 0, 30, 3, 30, 3]],  # turn / row 7
                                  [[0, 0, 32, 1, 32, 1], [0, 0, 32, 3, 32, 3], [0, 0, 34, 1, 34, 1], [0, 0, 34, 3, 34, 3]],  # turn / row 8
                                  [[0, 0, 36, 1, 36, 1], [0, 0, 36, 3, 36, 3], [0, 0, 38, 1, 38, 1], [0, 0, 38, 3, 38, 3]],  # turn / row 9
                                  [[0, 0, 40, 1, 40, 1], [0, 0, 40, 3, 40, 3], [0, 0, 42, 1, 42, 1], [0, 0, 42, 3, 42, 3]],  # turn / row 10
                                  ]
        self.position_feedback_half = [[[0, 1, 4, 1, 4, 1], [0, 1, 4, 3, 4, 3], [0, 1, 6, 1, 6, 1], [0, 1, 6, 3, 6, 3]],  # turn / row 1
                                  [[0, 1, 8, 1, 8, 1], [0, 1, 8, 3, 8, 3], [0, 1, 10, 1, 10, 1], [0, 1, 10, 3, 10, 3]],  # turn / row 2
                                  [[0, 1, 12, 1, 12, 1], [0, 1, 12, 3, 12, 3], [0, 1, 14, 1, 14, 1], [0, 1, 14, 3, 14, 3]],  # turn / row 3
                                  [[0, 1, 16, 1, 16, 1], [0, 1, 16, 3, 16, 3], [0, 1, 18, 1, 18, 1], [0, 1, 18, 3, 18, 3]],  # turn / row 4
                                  [[0, 1, 20, 1, 20, 1], [0, 1, 20, 3, 20, 3], [0, 1, 22, 1, 22, 1], [0, 1, 22, 3, 22, 3]],  # turn / row 5
                                  [[0, 1, 24, 1, 24, 1], [0, 1, 24, 3, 24, 3], [0, 1, 26, 1, 26, 1], [0, 1, 26, 3, 26, 3]],  # turn / row 6
                                  [[0, 1, 28, 1, 28, 1], [0, 1, 28, 3, 28, 3], [0, 1, 30, 1, 30, 1], [0, 1, 30, 3, 30, 3]],  # turn / row 7
                                  [[0, 1, 32, 1, 32, 1], [0, 1, 32, 3, 32, 3], [0, 1, 34, 1, 34, 1], [0, 1, 34, 3, 34, 3]],  # turn / row 8
                                  [[0, 1, 36, 1, 36, 1], [0, 1, 36, 3, 36, 3], [0, 1, 38, 1, 38, 1], [0, 1, 38, 3, 38, 3]],  # turn / row 9
                                  [[0, 1, 40, 1, 40, 1], [0, 1, 40, 3, 40, 3], [0, 1, 42, 1, 42, 1], [0, 1, 42, 3, 42, 3]],  # turn / row 10
                                  ]




#         self.red = "\033[48;5;9m \033[0;0m"
#         self.green = "\033[48;5;10m \033[0;0m"
#         self.blue = "\033[48;5;39m \033[0;0m"
#         self.yellow = "\033[48;5;11m \033[0;0m"
#         self.full = "\033[38;5;13m▉\033[0;0m"
#         self.half = "\033[48;5;13m\033[38;5;14m▅\033[0;0m"
#         self.selected = "\033[48;5;208m\033[38;5;0m \033[0;0m"
#         self.selected_enter = "\033[48;5;208m\033[38;5;0m↲\033[0;0m"
#         self.selected_up = "\033[48;5;208m\033[38;5;0m↑\033[0;0m"
#         self.selected_down = "\033[48;5;208m\033[38;5;0m↓\033[0;0m"
#         self.selected_left = "\033[48;5;208m\033[38;5;0m←\033[0;0m"
#         self.selected_right = "\033[48;5;208m\033[38;5;0m→\033[0;0m"
#         self.arrow_left_right = "\033[48;5;208m\033[38;5;0mleft ← & right → arrow\033[0;0m"
#         self.arrow_up_down =  "\033[48;5;208m\033[38;5;0mup ↑ & down ↓ arrow\033[0;0m"
#         self.enter = "\033[48;5;208m\033[38;5;0menter ↲\033[0;0m"
#
# # update enter text
#     def highlight_enter(self):
#         start = self.line[41][:30]
#         end = self.line[41][37:]
#         self.line[41] = f"{start}{self.enter}{end}"
#
#     def original_enter(self):
#         start = self.line[41][:30]
#         self.line[41] = f"{start}enter ↲ to confirm your turn                     ┃"
#
# # update arrow text
#     def highlight_arrows(self):
#         start = self.line[37][:32]
#         end = self.line[37][54:]
#         self.line[37] = f"{start}{self.arrow_left_right}{end}"
#         start = self.line[39][:32]
#         end = self.line[39][51:]
#         self.line[39] = f"{start}{self.arrow_up_down}{end}"
#
#     def original_arrow(self):
#         start = self.line[37][:32]
#         self.line[37] = f"{start}left ← & right → arrow keys to move            ┃"
#         start = self.line[39][:32]
#         self.line[39] = f"{start}up ↑ & down ↓ arrow keys to change             ┃"
#
# # set color for 10_1
#     def red_update_10_1(self):
#         start = self.line[40][0:5]
#         end = self.line[40][8:]
#         self.line[40] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[41][0:5]
#         end = self.line[41][8:]
#         self.line[41] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[42][0:5]
#         end = self.line[42][8:]
#         self.line[42] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_10_1(self):
#         start = self.line[40][0:5]
#         end = self.line[40][8:]
#         self.line[40] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[41][0:5]
#         end = self.line[41][8:]
#         self.line[41] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[42][0:5]
#         end = self.line[42][8:]
#         self.line[42] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_10_1(self):
#         start = self.line[40][0:5]
#         end = self.line[40][8:]
#         self.line[40] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[41][0:5]
#         end = self.line[41][8:]
#         self.line[41] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[42][0:5]
#         end = self.line[42][8:]
#         self.line[42] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_10_1(self):
#         start = self.line[40][0:5]
#         end = self.line[40][8:]
#         self.line[40] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[41][0:5]
#         end = self.line[41][8:]
#         self.line[41] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[42][0:5]
#         end = self.line[42][8:]
#         self.line[42] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_10_1(self):
#         start = self.line[40][0:5]
#         end = self.line[40][8:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:5]
#         end = self.line[41][8:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[42][0:5]
#         end = self.line[42][8:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_10_1(self):
#         start = self.line[40][0:6]
#         end = self.line[40][7:]
#         self.line[40] = f"{start}{self.selected_up}{end}"
#         start = self.line[41][0:5]
#         end = self.line[41][8:]
#         middle = self.line[41][6:7]
#         self.line[41] = f"{start}{self.selected_left}{self.middle}{self.selected_right}{end}"
#         start = self.line[42][0:6]
#         end = self.line[42][7:]
#         self.line[42] = f"{start}{self.selected_down}{end}"
#
# # set color for 10_2  // move values +4
#     def red_update_10_2(self):
#         start = self.line[40][0:9]
#         end = self.line[40][12:]
#         self.line[40] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[41][0:9]
#         end = self.line[41][12:]
#         self.line[41] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[42][0:9]
#         end = self.line[42][12:]
#         self.line[42] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_10_2(self):
#         start = self.line[40][0:9]
#         end = self.line[40][12:]
#         self.line[40] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[41][0:9]
#         end = self.line[41][12:]
#         self.line[41] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[42][0:9]
#         end = self.line[42][12:]
#         self.line[42] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_10_2(self):
#         start = self.line[40][0:9]
#         end = self.line[40][12:]
#         self.line[40] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[41][0:9]
#         end = self.line[41][12:]
#         self.line[41] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[42][0:9]
#         end = self.line[42][12:]
#         self.line[42] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_10_2(self):
#         start = self.line[40][0:9]
#         end = self.line[40][12:]
#         self.line[40] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[41][0:9]
#         end = self.line[41][12:]
#         self.line[41] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[42][0:9]
#         end = self.line[42][12:]
#         self.line[42] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_10_2(self):
#         start = self.line[40][0:9]
#         end = self.line[40][12:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:9]
#         end = self.line[41][12:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[42][0:9]
#         end = self.line[42][12:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_10_2(self):
#         start = self.line[40][0:9]
#         end = self.line[40][12:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:9]
#         end = self.line[41][12:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[42][0:9]
#         end = self.line[42][12:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 10_3  // move values +8
#     def red_update_10_3(self):
#         start = self.line[40][0:13]
#         end = self.line[40][16:]
#         self.line[40] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[41][0:13]
#         end = self.line[41][16:]
#         self.line[41] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[42][0:13]
#         end = self.line[42][16:]
#         self.line[42] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_10_3(self):
#         start = self.line[40][0:13]
#         end = self.line[40][16:]
#         self.line[40] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[41][0:13]
#         end = self.line[41][16:]
#         self.line[41] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[42][0:13]
#         end = self.line[42][16:]
#         self.line[42] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_10_3(self):
#         start = self.line[40][0:13]
#         end = self.line[40][16:]
#         self.line[40] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[41][0:13]
#         end = self.line[41][16:]
#         self.line[41] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[42][0:13]
#         end = self.line[42][16:]
#         self.line[42] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_10_3(self):
#         start = self.line[40][0:13]
#         end = self.line[40][16:]
#         self.line[40] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[41][0:13]
#         end = self.line[41][16:]
#         self.line[41] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[42][0:13]
#         end = self.line[42][16:]
#         self.line[42] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_10_3(self):
#         start = self.line[40][0:13]
#         end = self.line[40][16:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:13]
#         end = self.line[41][16:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[42][0:13]
#         end = self.line[42][16:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_10_3(self):
#         start = self.line[40][0:13]
#         end = self.line[40][16:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:13]
#         end = self.line[41][16:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[42][0:13]
#         end = self.line[42][16:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 10_4  // move values +12
#     def red_update_10_4(self):
#         start = self.line[40][0:17]
#         end = self.line[40][20:]
#         self.line[40] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[41][0:17]
#         end = self.line[41][20:]
#         self.line[41] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[42][0:17]
#         end = self.line[42][20:]
#         self.line[42] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_10_4(self):
#         start = self.line[40][0:17]
#         end = self.line[40][20:]
#         self.line[40] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[41][0:17]
#         end = self.line[41][20:]
#         self.line[41] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[42][0:17]
#         end = self.line[42][20:]
#         self.line[42] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_10_4(self):
#         start = self.line[40][0:17]
#         end = self.line[40][20:]
#         self.line[40] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[41][0:17]
#         end = self.line[41][20:]
#         self.line[41] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[42][0:17]
#         end = self.line[42][20:]
#         self.line[42] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_10_4(self):
#         start = self.line[40][0:17]
#         end = self.line[40][20:]
#         self.line[40] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[41][0:17]
#         end = self.line[41][20:]
#         self.line[41] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[42][0:17]
#         end = self.line[42][20:]
#         self.line[42] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_10_4(self):
#         start = self.line[40][0:17]
#         end = self.line[40][20:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:17]
#         end = self.line[41][20:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[42][0:17]
#         end = self.line[42][20:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_10_4(self):
#         start = self.line[40][0:17]
#         end = self.line[40][20:]
#         self.line[40] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[41][0:17]
#         end = self.line[41][20:]
#         self.line[41] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[42][0:17]
#         end = self.line[42][20:]
#         self.line[42] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 10_A //
#     def full_update_10_A(self):
#         start = self.line[40][:1]
#         end = self.line[40][2:]
#         self.line[40] = f"{start}{self.full}{end}"
#
#     def half_update_10_A(self):
#         start = self.line[40][:1]
#         end = self.line[40][2:]
#         self.line[40] = f"{start}{self.half}{end}"
#
# # set color for 10_B // move values +2
#     def full_update_10_B(self):
#         start = self.line[40][:3]
#         end = self.line[40][4:]
#         self.line[40] = f"{start}{self.full}{end}"
#
#     def half_update_10_B(self):
#         start = self.line[40][:3]
#         end = self.line[40][4:]
#         self.line[40] = f"{start}{self.half}{end}"
#
# # set color for 10_C // move lines +2
#     def full_update_10_C(self):
#         start = self.line[42][:1]
#         end = self.line[42][2:]
#         self.line[42] = f"{start}{self.full}{end}"
#
#     def half_update_10_C(self):
#         start = self.line[42][:1]
#         end = self.line[42][2:]
#         self.line[42] = f"{start}{self.half}{end}"
#
# # set color for 10_D // move values +2, move lines +2
#     def full_update_10_D(self):
#         start = self.line[42][:3]
#         end = self.line[42][4:]
#         self.line[42] = f"{start}{self.full}{end}"
#
#     def half_update_10_D(self):
#         start = self.line[42][:3]
#         end = self.line[42][4:]
#         self.line[42] = f"{start}{self.half}{end}"
#
# # new line
# # set color for 9_1
#     def red_update_9_1(self):
#         start = self.line[36][0:5]
#         end = self.line[36][8:]
#         self.line[36] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[37][0:5]
#         end = self.line[37][8:]
#         self.line[37] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[38][0:5]
#         end = self.line[38][8:]
#         self.line[38] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_9_1(self):
#         start = self.line[36][0:5]
#         end = self.line[36][8:]
#         self.line[36] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[37][0:5]
#         end = self.line[37][8:]
#         self.line[37] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[38][0:5]
#         end = self.line[38][8:]
#         self.line[38] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_9_1(self):
#         start = self.line[36][0:5]
#         end = self.line[36][8:]
#         self.line[36] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[37][0:5]
#         end = self.line[37][8:]
#         self.line[37] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[38][0:5]
#         end = self.line[38][8:]
#         self.line[38] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_9_1(self):
#         start = self.line[36][0:5]
#         end = self.line[36][8:]
#         self.line[36] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[37][0:5]
#         end = self.line[37][8:]
#         self.line[37] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[38][0:5]
#         end = self.line[38][8:]
#         self.line[38] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_9_1(self):
#         start = self.line[36][0:5]
#         end = self.line[36][8:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:5]
#         end = self.line[37][8:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[38][0:5]
#         end = self.line[38][8:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_9_1(self):
#         start = self.line[36][0:5]
#         end = self.line[36][8:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:5]
#         end = self.line[37][8:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[38][0:5]
#         end = self.line[38][8:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 9_2  // move values +4
#     def red_update_9_2(self):
#         start = self.line[36][0:9]
#         end = self.line[36][12:]
#         self.line[36] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[37][0:9]
#         end = self.line[37][12:]
#         self.line[37] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[38][0:9]
#         end = self.line[38][12:]
#         self.line[38] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_9_2(self):
#         start = self.line[36][0:9]
#         end = self.line[36][12:]
#         self.line[36] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[37][0:9]
#         end = self.line[37][12:]
#         self.line[37] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[38][0:9]
#         end = self.line[38][12:]
#         self.line[38] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_9_2(self):
#         start = self.line[36][0:9]
#         end = self.line[36][12:]
#         self.line[36] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[37][0:9]
#         end = self.line[37][12:]
#         self.line[37] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[38][0:9]
#         end = self.line[38][12:]
#         self.line[38] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_9_2(self):
#         start = self.line[36][0:9]
#         end = self.line[36][12:]
#         self.line[36] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[37][0:9]
#         end = self.line[37][12:]
#         self.line[37] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[38][0:9]
#         end = self.line[38][12:]
#         self.line[38] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_9_2(self):
#         start = self.line[36][0:9]
#         end = self.line[36][12:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:9]
#         end = self.line[37][12:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[38][0:9]
#         end = self.line[38][12:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_9_2(self):
#         start = self.line[36][0:9]
#         end = self.line[36][12:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:9]
#         end = self.line[37][12:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[38][0:9]
#         end = self.line[38][12:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 9_3  // move values +8
#     def red_update_9_3(self):
#         start = self.line[36][0:13]
#         end = self.line[36][16:]
#         self.line[36] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[37][0:13]
#         end = self.line[37][16:]
#         self.line[37] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[38][0:13]
#         end = self.line[38][16:]
#         self.line[38] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_9_3(self):
#         start = self.line[36][0:13]
#         end = self.line[36][16:]
#         self.line[36] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[37][0:13]
#         end = self.line[37][16:]
#         self.line[37] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[38][0:13]
#         end = self.line[38][16:]
#         self.line[38] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_9_3(self):
#         start = self.line[36][0:13]
#         end = self.line[36][16:]
#         self.line[36] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[37][0:13]
#         end = self.line[37][16:]
#         self.line[37] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[38][0:13]
#         end = self.line[38][16:]
#         self.line[38] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_9_3(self):
#         start = self.line[36][0:13]
#         end = self.line[36][16:]
#         self.line[36] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[37][0:13]
#         end = self.line[37][16:]
#         self.line[37] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[38][0:13]
#         end = self.line[38][16:]
#         self.line[38] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#
#     def selected_enter_update_9_3(self):
#         start = self.line[36][0:13]
#         end = self.line[36][16:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:13]
#         end = self.line[37][16:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[38][0:13]
#         end = self.line[38][16:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_9_3(self):
#         start = self.line[36][0:13]
#         end = self.line[36][16:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:13]
#         end = self.line[37][16:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[38][0:13]
#         end = self.line[38][16:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 9_4  // move values +12
#     def red_update_9_4(self):
#         start = self.line[36][0:17]
#         end = self.line[36][20:]
#         self.line[36] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[37][0:17]
#         end = self.line[37][20:]
#         self.line[37] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[38][0:17]
#         end = self.line[38][20:]
#         self.line[38] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_9_4(self):
#         start = self.line[36][0:17]
#         end = self.line[36][20:]
#         self.line[36] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[37][0:17]
#         end = self.line[37][20:]
#         self.line[37] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[38][0:17]
#         end = self.line[38][20:]
#         self.line[38] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_9_4(self):
#         start = self.line[36][0:17]
#         end = self.line[36][20:]
#         self.line[36] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[37][0:17]
#         end = self.line[37][20:]
#         self.line[37] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[38][0:17]
#         end = self.line[38][20:]
#         self.line[38] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_9_4(self):
#         start = self.line[36][0:17]
#         end = self.line[36][20:]
#         self.line[36] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[37][0:17]
#         end = self.line[37][20:]
#         self.line[37] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[38][0:17]
#         end = self.line[38][20:]
#         self.line[38] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_9_4(self):
#         start = self.line[36][0:17]
#         end = self.line[36][20:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:17]
#         end = self.line[37][20:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[38][0:17]
#         end = self.line[38][20:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_9_4(self):
#         start = self.line[36][0:17]
#         end = self.line[36][20:]
#         self.line[36] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[37][0:17]
#         end = self.line[37][20:]
#         self.line[37] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[38][0:17]
#         end = self.line[38][20:]
#         self.line[38] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 9_A //
#     def full_update_9_A(self):
#         start = self.line[36][:1]
#         end = self.line[36][2:]
#         self.line[36] = f"{start}{self.full}{end}"
#
#     def half_update_9_A(self):
#         start = self.line[36][:1]
#         end = self.line[36][2:]
#         self.line[36] = f"{start}{self.half}{end}"
#
# # set color for 9_B // move values +2
#     def full_update_9_B(self):
#         start = self.line[36][:3]
#         end = self.line[36][4:]
#         self.line[36] = f"{start}{self.full}{end}"
#
#     def half_update_9_B(self):
#         start = self.line[36][:3]
#         end = self.line[36][4:]
#         self.line[36] = f"{start}{self.half}{end}"
#
# # set color for 9_C // move lines +2
#     def full_update_9_C(self):
#         start = self.line[38][:1]
#         end = self.line[38][2:]
#         self.line[38] = f"{start}{self.full}{end}"
#
#     def half_update_9_C(self):
#         start = self.line[38][:1]
#         end = self.line[38][2:]
#         self.line[38] = f"{start}{self.half}{end}"
#
# # set color for 9_D // move values +2, move lines +2
#     def full_update_9_D(self):
#         start = self.line[38][:3]
#         end = self.line[38][4:]
#         self.line[38] = f"{start}{self.full}{end}"
#
#     def half_update_9_D(self):
#         start = self.line[38][:3]
#         end = self.line[38][4:]
#         self.line[38] = f"{start}{self.half}{end}"
#
# # new line
# # set color for 8_1
#     def red_update_8_1(self):
#         start = self.line[32][0:5]
#         end = self.line[32][8:]
#         self.line[32] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[33][0:5]
#         end = self.line[33][8:]
#         self.line[33] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[34][0:5]
#         end = self.line[34][8:]
#         self.line[34] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_8_1(self):
#         start = self.line[32][0:5]
#         end = self.line[32][8:]
#         self.line[32] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[33][0:5]
#         end = self.line[33][8:]
#         self.line[33] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[34][0:5]
#         end = self.line[34][8:]
#         self.line[34] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_8_1(self):
#         start = self.line[32][0:5]
#         end = self.line[32][8:]
#         self.line[32] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[33][0:5]
#         end = self.line[33][8:]
#         self.line[33] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[34][0:5]
#         end = self.line[34][8:]
#         self.line[34] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_8_1(self):
#         start = self.line[32][0:5]
#         end = self.line[32][8:]
#         self.line[32] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[33][0:5]
#         end = self.line[33][8:]
#         self.line[33] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[34][0:5]
#         end = self.line[34][8:]
#         self.line[34] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_8_1(self):
#         start = self.line[32][0:5]
#         end = self.line[32][8:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:5]
#         end = self.line[33][8:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[34][0:5]
#         end = self.line[34][8:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_8_1(self):
#         start = self.line[32][0:5]
#         end = self.line[32][8:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:5]
#         end = self.line[33][8:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[34][0:5]
#         end = self.line[34][8:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 8_2  // move values +4
#     def red_update_8_2(self):
#         start = self.line[32][0:9]
#         end = self.line[32][12:]
#         self.line[32] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[33][0:9]
#         end = self.line[33][12:]
#         self.line[33] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[34][0:9]
#         end = self.line[34][12:]
#         self.line[34] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_8_2(self):
#         start = self.line[32][0:9]
#         end = self.line[32][12:]
#         self.line[32] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[33][0:9]
#         end = self.line[33][12:]
#         self.line[33] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[34][0:9]
#         end = self.line[34][12:]
#         self.line[34] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_8_2(self):
#         start = self.line[32][0:9]
#         end = self.line[32][12:]
#         self.line[32] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[33][0:9]
#         end = self.line[33][12:]
#         self.line[33] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[34][0:9]
#         end = self.line[34][12:]
#         self.line[34] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_8_2(self):
#         start = self.line[32][0:9]
#         end = self.line[32][12:]
#         self.line[32] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[33][0:9]
#         end = self.line[33][12:]
#         self.line[33] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[34][0:9]
#         end = self.line[34][12:]
#         self.line[34] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_8_2(self):
#         start = self.line[32][0:9]
#         end = self.line[32][12:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:9]
#         end = self.line[33][12:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[34][0:9]
#         end = self.line[34][12:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_8_2(self):
#         start = self.line[32][0:9]
#         end = self.line[32][12:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:9]
#         end = self.line[33][12:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[34][0:9]
#         end = self.line[34][12:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 8_3  // move values +8
#     def red_update_8_3(self):
#         start = self.line[32][0:13]
#         end = self.line[32][16:]
#         self.line[32] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[33][0:13]
#         end = self.line[33][16:]
#         self.line[33] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[34][0:13]
#         end = self.line[34][16:]
#         self.line[34] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_8_3(self):
#         start = self.line[32][0:13]
#         end = self.line[32][16:]
#         self.line[32] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[33][0:13]
#         end = self.line[33][16:]
#         self.line[33] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[34][0:13]
#         end = self.line[34][16:]
#         self.line[34] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_8_3(self):
#         start = self.line[32][0:13]
#         end = self.line[32][16:]
#         self.line[32] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[33][0:13]
#         end = self.line[33][16:]
#         self.line[33] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[34][0:13]
#         end = self.line[34][16:]
#         self.line[34] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_8_3(self):
#         start = self.line[32][0:13]
#         end = self.line[32][16:]
#         self.line[32] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[33][0:13]
#         end = self.line[33][16:]
#         self.line[33] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[34][0:13]
#         end = self.line[34][16:]
#         self.line[34] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_8_3(self):
#         start = self.line[32][0:13]
#         end = self.line[32][16:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:13]
#         end = self.line[33][16:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[34][0:13]
#         end = self.line[34][16:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_8_3(self):
#         start = self.line[32][0:13]
#         end = self.line[32][16:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:13]
#         end = self.line[33][16:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[34][0:13]
#         end = self.line[34][16:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 8_4  // move values +12
#     def red_update_8_4(self):
#         start = self.line[32][0:17]
#         end = self.line[32][20:]
#         self.line[32] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[33][0:17]
#         end = self.line[33][20:]
#         self.line[33] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[34][0:17]
#         end = self.line[34][20:]
#         self.line[34] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_8_4(self):
#         start = self.line[32][0:17]
#         end = self.line[32][20:]
#         self.line[32] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[33][0:17]
#         end = self.line[33][20:]
#         self.line[33] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[34][0:17]
#         end = self.line[34][20:]
#         self.line[34] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_8_4(self):
#         start = self.line[32][0:17]
#         end = self.line[32][20:]
#         self.line[32] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[33][0:17]
#         end = self.line[33][20:]
#         self.line[33] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[34][0:17]
#         end = self.line[34][20:]
#         self.line[34] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_8_4(self):
#         start = self.line[32][0:17]
#         end = self.line[32][20:]
#         self.line[32] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[33][0:17]
#         end = self.line[33][20:]
#         self.line[33] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[34][0:17]
#         end = self.line[34][20:]
#         self.line[34] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_8_4(self):
#         start = self.line[32][0:17]
#         end = self.line[32][20:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:17]
#         end = self.line[33][20:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[34][0:17]
#         end = self.line[34][20:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_8_4(self):
#         start = self.line[32][0:17]
#         end = self.line[32][20:]
#         self.line[32] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[33][0:17]
#         end = self.line[33][20:]
#         self.line[33] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[34][0:17]
#         end = self.line[34][20:]
#         self.line[34] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 8_A //
#     def full_update_8_A(self):
#         start = self.line[32][:1]
#         end = self.line[32][2:]
#         self.line[32] = f"{start}{self.full}{end}"
#
#     def half_update_8_A(self):
#         start = self.line[32][:1]
#         end = self.line[32][2:]
#         self.line[32] = f"{start}{self.half}{end}"
#
# # set color for 8_B // move values +2
#     def full_update_8_B(self):
#         start = self.line[32][:3]
#         end = self.line[32][4:]
#         self.line[32] = f"{start}{self.full}{end}"
#
#     def half_update_8_B(self):
#         start = self.line[32][:3]
#         end = self.line[32][4:]
#         self.line[32] = f"{start}{self.half}{end}"
#
# # set color for 8_C // move lines +2
#     def full_update_8_C(self):
#         start = self.line[34][:1]
#         end = self.line[34][2:]
#         self.line[34] = f"{start}{self.full}{end}"
#
#     def half_update_8_C(self):
#         start = self.line[34][:1]
#         end = self.line[34][2:]
#         self.line[34] = f"{start}{self.half}{end}"
#
# # set color for 8_D // move values +2, move lines +2
#     def full_update_8_D(self):
#         start = self.line[34][:3]
#         end = self.line[34][4:]
#         self.line[34] = f"{start}{self.full}{end}"
#
#     def half_update_8_D(self):
#         start = self.line[34][:3]
#         end = self.line[34][4:]
#         self.line[34] = f"{start}{self.half}{end}"
# # END!!! 8_             stop for multi-curser select
# # END!!! self.line[32]  stop for multi-curser select
# # END!!! self.line[33]  stop for multi-curser select
# # END!!! self.line[34]  stop for multi-curser select
#
# # new line
# # set color for 7_1
#     def red_update_7_1(self):
#         start = self.line[28][0:5]
#         end = self.line[28][8:]
#         self.line[28] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[29][0:5]
#         end = self.line[29][8:]
#         self.line[29] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[30][0:5]
#         end = self.line[30][8:]
#         self.line[30] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_7_1(self):
#         start = self.line[28][0:5]
#         end = self.line[28][8:]
#         self.line[28] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[29][0:5]
#         end = self.line[29][8:]
#         self.line[29] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[30][0:5]
#         end = self.line[30][8:]
#         self.line[30] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_7_1(self):
#         start = self.line[28][0:5]
#         end = self.line[28][8:]
#         self.line[28] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[29][0:5]
#         end = self.line[29][8:]
#         self.line[29] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[30][0:5]
#         end = self.line[30][8:]
#         self.line[30] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_7_1(self):
#         start = self.line[28][0:5]
#         end = self.line[28][8:]
#         self.line[28] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[29][0:5]
#         end = self.line[29][8:]
#         self.line[29] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[30][0:5]
#         end = self.line[30][8:]
#         self.line[30] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_7_1(self):
#         start = self.line[28][0:5]
#         end = self.line[28][8:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:5]
#         end = self.line[29][8:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[30][0:5]
#         end = self.line[30][8:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_7_1(self):
#         start = self.line[28][0:5]
#         end = self.line[28][8:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:5]
#         end = self.line[29][8:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[30][0:5]
#         end = self.line[30][8:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 7_2  // move values +4
#     def red_update_7_2(self):
#         start = self.line[28][0:9]
#         end = self.line[28][12:]
#         self.line[28] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[29][0:9]
#         end = self.line[29][12:]
#         self.line[29] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[30][0:9]
#         end = self.line[30][12:]
#         self.line[30] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_7_2(self):
#         start = self.line[28][0:9]
#         end = self.line[28][12:]
#         self.line[28] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[29][0:9]
#         end = self.line[29][12:]
#         self.line[29] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[30][0:9]
#         end = self.line[30][12:]
#         self.line[30] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_7_2(self):
#         start = self.line[28][0:9]
#         end = self.line[28][12:]
#         self.line[28] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[29][0:9]
#         end = self.line[29][12:]
#         self.line[29] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[30][0:9]
#         end = self.line[30][12:]
#         self.line[30] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_7_2(self):
#         start = self.line[28][0:9]
#         end = self.line[28][12:]
#         self.line[28] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[29][0:9]
#         end = self.line[29][12:]
#         self.line[29] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[30][0:9]
#         end = self.line[30][12:]
#         self.line[30] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_7_2(self):
#         start = self.line[28][0:9]
#         end = self.line[28][12:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:9]
#         end = self.line[29][12:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[30][0:9]
#         end = self.line[30][12:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_7_2(self):
#         start = self.line[28][0:9]
#         end = self.line[28][12:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:9]
#         end = self.line[29][12:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[30][0:9]
#         end = self.line[30][12:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 7_3  // move values +8
#     def red_update_7_3(self):
#         start = self.line[28][0:13]
#         end = self.line[28][16:]
#         self.line[28] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[29][0:13]
#         end = self.line[29][16:]
#         self.line[29] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[30][0:13]
#         end = self.line[30][16:]
#         self.line[30] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_7_3(self):
#         start = self.line[28][0:13]
#         end = self.line[28][16:]
#         self.line[28] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[29][0:13]
#         end = self.line[29][16:]
#         self.line[29] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[30][0:13]
#         end = self.line[30][16:]
#         self.line[30] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_7_3(self):
#         start = self.line[28][0:13]
#         end = self.line[28][16:]
#         self.line[28] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[29][0:13]
#         end = self.line[29][16:]
#         self.line[29] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[30][0:13]
#         end = self.line[30][16:]
#         self.line[30] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_7_3(self):
#         start = self.line[28][0:13]
#         end = self.line[28][16:]
#         self.line[28] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[29][0:13]
#         end = self.line[29][16:]
#         self.line[29] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[30][0:13]
#         end = self.line[30][16:]
#         self.line[30] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_7_3(self):
#         start = self.line[28][0:13]
#         end = self.line[28][16:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:13]
#         end = self.line[29][16:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[30][0:13]
#         end = self.line[30][16:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_7_3(self):
#         start = self.line[28][0:13]
#         end = self.line[28][16:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:13]
#         end = self.line[29][16:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[30][0:13]
#         end = self.line[30][16:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 7_4  // move values +12
#     def red_update_7_4(self):
#         start = self.line[28][0:17]
#         end = self.line[28][20:]
#         self.line[28] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[29][0:17]
#         end = self.line[29][20:]
#         self.line[29] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[30][0:17]
#         end = self.line[30][20:]
#         self.line[30] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_7_4(self):
#         start = self.line[28][0:17]
#         end = self.line[28][20:]
#         self.line[28] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[29][0:17]
#         end = self.line[29][20:]
#         self.line[29] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[30][0:17]
#         end = self.line[30][20:]
#         self.line[30] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_7_4(self):
#         start = self.line[28][0:17]
#         end = self.line[28][20:]
#         self.line[28] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[29][0:17]
#         end = self.line[29][20:]
#         self.line[29] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[30][0:17]
#         end = self.line[30][20:]
#         self.line[30] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_7_4(self):
#         start = self.line[28][0:17]
#         end = self.line[28][20:]
#         self.line[28] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[29][0:17]
#         end = self.line[29][20:]
#         self.line[29] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[30][0:17]
#         end = self.line[30][20:]
#         self.line[30] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_7_4(self):
#         start = self.line[28][0:17]
#         end = self.line[28][20:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:17]
#         end = self.line[29][20:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[30][0:17]
#         end = self.line[30][20:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_7_4(self):
#         start = self.line[28][0:17]
#         end = self.line[28][20:]
#         self.line[28] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[29][0:17]
#         end = self.line[29][20:]
#         self.line[29] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[30][0:17]
#         end = self.line[30][20:]
#         self.line[30] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 7_A //
#     def full_update_7_A(self):
#         start = self.line[28][:1]
#         end = self.line[28][2:]
#         self.line[28] = f"{start}{self.full}{end}"
#
#     def half_update_7_A(self):
#         start = self.line[28][:1]
#         end = self.line[28][2:]
#         self.line[28] = f"{start}{self.half}{end}"
#
# # set color for 7_B // move values +2
#     def full_update_7_B(self):
#         start = self.line[28][:3]
#         end = self.line[28][4:]
#         self.line[28] = f"{start}{self.full}{end}"
#
#     def half_update_7_B(self):
#         start = self.line[28][:3]
#         end = self.line[28][4:]
#         self.line[28] = f"{start}{self.half}{end}"
#
# # set color for 7_C // move lines +2
#     def full_update_7_C(self):
#         start = self.line[30][:1]
#         end = self.line[30][2:]
#         self.line[30] = f"{start}{self.full}{end}"
#
#     def half_update_7_C(self):
#         start = self.line[30][:1]
#         end = self.line[30][2:]
#         self.line[30] = f"{start}{self.half}{end}"
#
# # set color for 7_D // move values +2, move lines +2
#     def full_update_7_D(self):
#         start = self.line[30][:3]
#         end = self.line[30][4:]
#         self.line[30] = f"{start}{self.full}{end}"
#
#     def half_update_7_D(self):
#         start = self.line[30][:3]
#         end = self.line[30][4:]
#         self.line[30] = f"{start}{self.half}{end}"
# # END!!! 7_             stop for multi-curser select
# # END!!! self.line[28]  stop for multi-curser select
# # END!!! self.line[29]  stop for multi-curser select
# # END!!! self.line[30]  stop for multi-curser select
#
# # new line
# # set color for 6_1
#     def red_update_6_1(self):
#         start = self.line[24][0:5]
#         end = self.line[24][8:]
#         self.line[24] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[25][0:5]
#         end = self.line[25][8:]
#         self.line[25] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[26][0:5]
#         end = self.line[26][8:]
#         self.line[26] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_6_1(self):
#         start = self.line[24][0:5]
#         end = self.line[24][8:]
#         self.line[24] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[25][0:5]
#         end = self.line[25][8:]
#         self.line[25] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[26][0:5]
#         end = self.line[26][8:]
#         self.line[26] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_6_1(self):
#         start = self.line[24][0:5]
#         end = self.line[24][8:]
#         self.line[24] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[25][0:5]
#         end = self.line[25][8:]
#         self.line[25] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[26][0:5]
#         end = self.line[26][8:]
#         self.line[26] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_6_1(self):
#         start = self.line[24][0:5]
#         end = self.line[24][8:]
#         self.line[24] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[25][0:5]
#         end = self.line[25][8:]
#         self.line[25] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[26][0:5]
#         end = self.line[26][8:]
#         self.line[26] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_6_1(self):
#         start = self.line[24][0:5]
#         end = self.line[24][8:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:5]
#         end = self.line[25][8:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[26][0:5]
#         end = self.line[26][8:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_6_1(self):
#         start = self.line[24][0:5]
#         end = self.line[24][8:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:5]
#         end = self.line[25][8:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[26][0:5]
#         end = self.line[26][8:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 6_2  // move values +4
#     def red_update_6_2(self):
#         start = self.line[24][0:9]
#         end = self.line[24][12:]
#         self.line[24] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[25][0:9]
#         end = self.line[25][12:]
#         self.line[25] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[26][0:9]
#         end = self.line[26][12:]
#         self.line[26] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_6_2(self):
#         start = self.line[24][0:9]
#         end = self.line[24][12:]
#         self.line[24] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[25][0:9]
#         end = self.line[25][12:]
#         self.line[25] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[26][0:9]
#         end = self.line[26][12:]
#         self.line[26] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_6_2(self):
#         start = self.line[24][0:9]
#         end = self.line[24][12:]
#         self.line[24] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[25][0:9]
#         end = self.line[25][12:]
#         self.line[25] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[26][0:9]
#         end = self.line[26][12:]
#         self.line[26] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_6_2(self):
#         start = self.line[24][0:9]
#         end = self.line[24][12:]
#         self.line[24] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[25][0:9]
#         end = self.line[25][12:]
#         self.line[25] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[26][0:9]
#         end = self.line[26][12:]
#         self.line[26] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_6_2(self):
#         start = self.line[24][0:9]
#         end = self.line[24][12:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:9]
#         end = self.line[25][12:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[26][0:9]
#         end = self.line[26][12:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_6_2(self):
#         start = self.line[24][0:9]
#         end = self.line[24][12:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:9]
#         end = self.line[25][12:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[26][0:9]
#         end = self.line[26][12:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 6_3  // move values +8
#     def red_update_6_3(self):
#         start = self.line[24][0:13]
#         end = self.line[24][16:]
#         self.line[24] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[25][0:13]
#         end = self.line[25][16:]
#         self.line[25] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[26][0:13]
#         end = self.line[26][16:]
#         self.line[26] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_6_3(self):
#         start = self.line[24][0:13]
#         end = self.line[24][16:]
#         self.line[24] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[25][0:13]
#         end = self.line[25][16:]
#         self.line[25] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[26][0:13]
#         end = self.line[26][16:]
#         self.line[26] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_6_3(self):
#         start = self.line[24][0:13]
#         end = self.line[24][16:]
#         self.line[24] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[25][0:13]
#         end = self.line[25][16:]
#         self.line[25] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[26][0:13]
#         end = self.line[26][16:]
#         self.line[26] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_6_3(self):
#         start = self.line[24][0:13]
#         end = self.line[24][16:]
#         self.line[24] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[25][0:13]
#         end = self.line[25][16:]
#         self.line[25] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[26][0:13]
#         end = self.line[26][16:]
#         self.line[26] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_6_3(self):
#         start = self.line[24][0:13]
#         end = self.line[24][16:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:13]
#         end = self.line[25][16:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[26][0:13]
#         end = self.line[26][16:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_6_3(self):
#         start = self.line[24][0:13]
#         end = self.line[24][16:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:13]
#         end = self.line[25][16:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[26][0:13]
#         end = self.line[26][16:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 6_4  // move values +12
#     def red_update_6_4(self):
#         start = self.line[24][0:17]
#         end = self.line[24][20:]
#         self.line[24] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[25][0:17]
#         end = self.line[25][20:]
#         self.line[25] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[26][0:17]
#         end = self.line[26][20:]
#         self.line[26] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_6_4(self):
#         start = self.line[24][0:17]
#         end = self.line[24][20:]
#         self.line[24] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[25][0:17]
#         end = self.line[25][20:]
#         self.line[25] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[26][0:17]
#         end = self.line[26][20:]
#         self.line[26] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_6_4(self):
#         start = self.line[24][0:17]
#         end = self.line[24][20:]
#         self.line[24] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[25][0:17]
#         end = self.line[25][20:]
#         self.line[25] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[26][0:17]
#         end = self.line[26][20:]
#         self.line[26] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_6_4(self):
#         start = self.line[24][0:17]
#         end = self.line[24][20:]
#         self.line[24] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[25][0:17]
#         end = self.line[25][20:]
#         self.line[25] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[26][0:17]
#         end = self.line[26][20:]
#         self.line[26] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_6_4(self):
#         start = self.line[24][0:17]
#         end = self.line[24][20:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:17]
#         end = self.line[25][20:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[26][0:17]
#         end = self.line[26][20:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_6_4(self):
#         start = self.line[24][0:17]
#         end = self.line[24][20:]
#         self.line[24] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[25][0:17]
#         end = self.line[25][20:]
#         self.line[25] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[26][0:17]
#         end = self.line[26][20:]
#         self.line[26] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 6_A //
#     def full_update_6_A(self):
#         start = self.line[24][:1]
#         end = self.line[24][2:]
#         self.line[24] = f"{start}{self.full}{end}"
#
#     def half_update_6_A(self):
#         start = self.line[24][:1]
#         end = self.line[24][2:]
#         self.line[24] = f"{start}{self.half}{end}"
#
# # set color for 6_B // move values +2
#     def full_update_6_B(self):
#         start = self.line[24][:3]
#         end = self.line[24][4:]
#         self.line[24] = f"{start}{self.full}{end}"
#
#     def half_update_6_B(self):
#         start = self.line[24][:3]
#         end = self.line[24][4:]
#         self.line[24] = f"{start}{self.half}{end}"
#
# # set color for 6_C // move lines +2
#     def full_update_6_C(self):
#         start = self.line[26][:1]
#         end = self.line[26][2:]
#         self.line[26] = f"{start}{self.full}{end}"
#
#     def half_update_6_C(self):
#         start = self.line[26][:1]
#         end = self.line[26][2:]
#         self.line[26] = f"{start}{self.half}{end}"
#
# # set color for 6_D // move values +2, move lines +2
#     def full_update_6_D(self):
#         start = self.line[26][:3]
#         end = self.line[26][4:]
#         self.line[26] = f"{start}{self.full}{end}"
#
#     def half_update_6_D(self):
#         start = self.line[26][:3]
#         end = self.line[26][4:]
#         self.line[26] = f"{start}{self.half}{end}"
# # END!!! 6_             stop for multi-curser select
# # END!!! self.line[24]  stop for multi-curser select
# # END!!! self.line[25]  stop for multi-curser select
# # END!!! self.line[26]  stop for multi-curser select
#
# # new line
# # set color for 5_1
#     def red_update_5_1(self):
#         start = self.line[20][0:5]
#         end = self.line[20][8:]
#         self.line[20] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[21][0:5]
#         end = self.line[21][8:]
#         self.line[21] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[22][0:5]
#         end = self.line[22][8:]
#         self.line[22] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_5_1(self):
#         start = self.line[20][0:5]
#         end = self.line[20][8:]
#         self.line[20] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[21][0:5]
#         end = self.line[21][8:]
#         self.line[21] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[22][0:5]
#         end = self.line[22][8:]
#         self.line[22] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_5_1(self):
#         start = self.line[20][0:5]
#         end = self.line[20][8:]
#         self.line[20] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[21][0:5]
#         end = self.line[21][8:]
#         self.line[21] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[22][0:5]
#         end = self.line[22][8:]
#         self.line[22] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_5_1(self):
#         start = self.line[20][0:5]
#         end = self.line[20][8:]
#         self.line[20] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[21][0:5]
#         end = self.line[21][8:]
#         self.line[21] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[22][0:5]
#         end = self.line[22][8:]
#         self.line[22] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_5_1(self):
#         start = self.line[20][0:5]
#         end = self.line[20][8:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:5]
#         end = self.line[21][8:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[22][0:5]
#         end = self.line[22][8:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_5_1(self):
#         start = self.line[20][0:5]
#         end = self.line[20][8:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:5]
#         end = self.line[21][8:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[22][0:5]
#         end = self.line[22][8:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 5_2  // move values +4
#     def red_update_5_2(self):
#         start = self.line[20][0:9]
#         end = self.line[20][12:]
#         self.line[20] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[21][0:9]
#         end = self.line[21][12:]
#         self.line[21] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[22][0:9]
#         end = self.line[22][12:]
#         self.line[22] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_5_2(self):
#         start = self.line[20][0:9]
#         end = self.line[20][12:]
#         self.line[20] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[21][0:9]
#         end = self.line[21][12:]
#         self.line[21] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[22][0:9]
#         end = self.line[22][12:]
#         self.line[22] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_5_2(self):
#         start = self.line[20][0:9]
#         end = self.line[20][12:]
#         self.line[20] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[21][0:9]
#         end = self.line[21][12:]
#         self.line[21] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[22][0:9]
#         end = self.line[22][12:]
#         self.line[22] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_5_2(self):
#         start = self.line[20][0:9]
#         end = self.line[20][12:]
#         self.line[20] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[21][0:9]
#         end = self.line[21][12:]
#         self.line[21] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[22][0:9]
#         end = self.line[22][12:]
#         self.line[22] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_5_2(self):
#         start = self.line[20][0:9]
#         end = self.line[20][12:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:9]
#         end = self.line[21][12:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[22][0:9]
#         end = self.line[22][12:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_5_2(self):
#         start = self.line[20][0:9]
#         end = self.line[20][12:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:9]
#         end = self.line[21][12:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[22][0:9]
#         end = self.line[22][12:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 5_3  // move values +8
#     def red_update_5_3(self):
#         start = self.line[20][0:13]
#         end = self.line[20][16:]
#         self.line[20] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[21][0:13]
#         end = self.line[21][16:]
#         self.line[21] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[22][0:13]
#         end = self.line[22][16:]
#         self.line[22] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_5_3(self):
#         start = self.line[20][0:13]
#         end = self.line[20][16:]
#         self.line[20] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[21][0:13]
#         end = self.line[21][16:]
#         self.line[21] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[22][0:13]
#         end = self.line[22][16:]
#         self.line[22] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_5_3(self):
#         start = self.line[20][0:13]
#         end = self.line[20][16:]
#         self.line[20] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[21][0:13]
#         end = self.line[21][16:]
#         self.line[21] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[22][0:13]
#         end = self.line[22][16:]
#         self.line[22] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_5_3(self):
#         start = self.line[20][0:13]
#         end = self.line[20][16:]
#         self.line[20] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[21][0:13]
#         end = self.line[21][16:]
#         self.line[21] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[22][0:13]
#         end = self.line[22][16:]
#         self.line[22] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_5_3(self):
#         start = self.line[20][0:13]
#         end = self.line[20][16:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:13]
#         end = self.line[21][16:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[22][0:13]
#         end = self.line[22][16:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_5_3(self):
#         start = self.line[20][0:13]
#         end = self.line[20][16:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:13]
#         end = self.line[21][16:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[22][0:13]
#         end = self.line[22][16:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 5_4  // move values +12
#     def red_update_5_4(self):
#         start = self.line[20][0:17]
#         end = self.line[20][20:]
#         self.line[20] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[21][0:17]
#         end = self.line[21][20:]
#         self.line[21] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[22][0:17]
#         end = self.line[22][20:]
#         self.line[22] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_5_4(self):
#         start = self.line[20][0:17]
#         end = self.line[20][20:]
#         self.line[20] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[21][0:17]
#         end = self.line[21][20:]
#         self.line[21] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[22][0:17]
#         end = self.line[22][20:]
#         self.line[22] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_5_4(self):
#         start = self.line[20][0:17]
#         end = self.line[20][20:]
#         self.line[20] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[21][0:17]
#         end = self.line[21][20:]
#         self.line[21] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[22][0:17]
#         end = self.line[22][20:]
#         self.line[22] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_5_4(self):
#         start = self.line[20][0:17]
#         end = self.line[20][20:]
#         self.line[20] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[21][0:17]
#         end = self.line[21][20:]
#         self.line[21] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[22][0:17]
#         end = self.line[22][20:]
#         self.line[22] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_5_4(self):
#         start = self.line[20][0:17]
#         end = self.line[20][20:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:17]
#         end = self.line[21][20:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[22][0:17]
#         end = self.line[22][20:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_5_4(self):
#         start = self.line[20][0:17]
#         end = self.line[20][20:]
#         self.line[20] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[21][0:17]
#         end = self.line[21][20:]
#         self.line[21] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[22][0:17]
#         end = self.line[22][20:]
#         self.line[22] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 5_A //
#     def full_update_5_A(self):
#         start = self.line[20][:1]
#         end = self.line[20][2:]
#         self.line[20] = f"{start}{self.full}{end}"
#
#     def half_update_5_A(self):
#         start = self.line[20][:1]
#         end = self.line[20][2:]
#         self.line[20] = f"{start}{self.half}{end}"
#
# # set color for 5_B // move values +2
#     def full_update_5_B(self):
#         start = self.line[20][:3]
#         end = self.line[20][4:]
#         self.line[20] = f"{start}{self.full}{end}"
#
#     def half_update_5_B(self):
#         start = self.line[20][:3]
#         end = self.line[20][4:]
#         self.line[20] = f"{start}{self.half}{end}"
#
# # set color for 5_C // move lines +2
#     def full_update_5_C(self):
#         start = self.line[22][:1]
#         end = self.line[22][2:]
#         self.line[22] = f"{start}{self.full}{end}"
#
#     def half_update_5_C(self):
#         start = self.line[22][:1]
#         end = self.line[22][2:]
#         self.line[22] = f"{start}{self.half}{end}"
#
# # set color for 5_D // move values +2, move lines +2
#     def full_update_5_D(self):
#         start = self.line[22][:3]
#         end = self.line[22][4:]
#         self.line[22] = f"{start}{self.full}{end}"
#
#     def half_update_5_D(self):
#         start = self.line[22][:3]
#         end = self.line[22][4:]
#         self.line[22] = f"{start}{self.half}{end}"
# # END!!! 5_             stop for multi-curser select
# # END!!! self.line[20]  stop for multi-curser select
# # END!!! self.line[21]  stop for multi-curser select
# # END!!! self.line[22]  stop for multi-curser select
#
# # new line
# # set color for 4_1
#     def red_update_4_1(self):
#         start = self.line[16][0:5]
#         end = self.line[16][8:]
#         self.line[16] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[17][0:5]
#         end = self.line[17][8:]
#         self.line[17] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[18][0:5]
#         end = self.line[18][8:]
#         self.line[18] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_4_1(self):
#         start = self.line[16][0:5]
#         end = self.line[16][8:]
#         self.line[16] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[17][0:5]
#         end = self.line[17][8:]
#         self.line[17] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[18][0:5]
#         end = self.line[18][8:]
#         self.line[18] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_4_1(self):
#         start = self.line[16][0:5]
#         end = self.line[16][8:]
#         self.line[16] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[17][0:5]
#         end = self.line[17][8:]
#         self.line[17] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[18][0:5]
#         end = self.line[18][8:]
#         self.line[18] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_4_1(self):
#         start = self.line[16][0:5]
#         end = self.line[16][8:]
#         self.line[16] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[17][0:5]
#         end = self.line[17][8:]
#         self.line[17] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[18][0:5]
#         end = self.line[18][8:]
#         self.line[18] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_4_1(self):
#         start = self.line[16][0:5]
#         end = self.line[16][8:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:5]
#         end = self.line[17][8:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[18][0:5]
#         end = self.line[18][8:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_4_1(self):
#         start = self.line[16][0:5]
#         end = self.line[16][8:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:5]
#         end = self.line[17][8:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[18][0:5]
#         end = self.line[18][8:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 4_2  // move values +4
#     def red_update_4_2(self):
#         start = self.line[16][0:9]
#         end = self.line[16][12:]
#         self.line[16] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[17][0:9]
#         end = self.line[17][12:]
#         self.line[17] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[18][0:9]
#         end = self.line[18][12:]
#         self.line[18] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_4_2(self):
#         start = self.line[16][0:9]
#         end = self.line[16][12:]
#         self.line[16] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[17][0:9]
#         end = self.line[17][12:]
#         self.line[17] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[18][0:9]
#         end = self.line[18][12:]
#         self.line[18] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_4_2(self):
#         start = self.line[16][0:9]
#         end = self.line[16][12:]
#         self.line[16] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[17][0:9]
#         end = self.line[17][12:]
#         self.line[17] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[18][0:9]
#         end = self.line[18][12:]
#         self.line[18] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_4_2(self):
#         start = self.line[16][0:9]
#         end = self.line[16][12:]
#         self.line[16] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[17][0:9]
#         end = self.line[17][12:]
#         self.line[17] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[18][0:9]
#         end = self.line[18][12:]
#         self.line[18] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_4_2(self):
#         start = self.line[16][0:9]
#         end = self.line[16][12:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:9]
#         end = self.line[17][12:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[18][0:9]
#         end = self.line[18][12:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_4_2(self):
#         start = self.line[16][0:9]
#         end = self.line[16][12:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:9]
#         end = self.line[17][12:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[18][0:9]
#         end = self.line[18][12:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 4_3  // move values +8
#     def red_update_4_3(self):
#         start = self.line[16][0:13]
#         end = self.line[16][16:]
#         self.line[16] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[17][0:13]
#         end = self.line[17][16:]
#         self.line[17] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[18][0:13]
#         end = self.line[18][16:]
#         self.line[18] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_4_3(self):
#         start = self.line[16][0:13]
#         end = self.line[16][16:]
#         self.line[16] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[17][0:13]
#         end = self.line[17][16:]
#         self.line[17] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[18][0:13]
#         end = self.line[18][16:]
#         self.line[18] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_4_3(self):
#         start = self.line[16][0:13]
#         end = self.line[16][16:]
#         self.line[16] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[17][0:13]
#         end = self.line[17][16:]
#         self.line[17] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[18][0:13]
#         end = self.line[18][16:]
#         self.line[18] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_4_3(self):
#         start = self.line[16][0:13]
#         end = self.line[16][16:]
#         self.line[16] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[17][0:13]
#         end = self.line[17][16:]
#         self.line[17] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[18][0:13]
#         end = self.line[18][16:]
#         self.line[18] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_4_3(self):
#         start = self.line[16][0:13]
#         end = self.line[16][16:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:13]
#         end = self.line[17][16:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[18][0:13]
#         end = self.line[18][16:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_4_3(self):
#         start = self.line[16][0:13]
#         end = self.line[16][16:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:13]
#         end = self.line[17][16:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[18][0:13]
#         end = self.line[18][16:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 4_4  // move values +12
#     def red_update_4_4(self):
#         start = self.line[16][0:17]
#         end = self.line[16][20:]
#         self.line[16] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[17][0:17]
#         end = self.line[17][20:]
#         self.line[17] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[18][0:17]
#         end = self.line[18][20:]
#         self.line[18] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_4_4(self):
#         start = self.line[16][0:17]
#         end = self.line[16][20:]
#         self.line[16] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[17][0:17]
#         end = self.line[17][20:]
#         self.line[17] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[18][0:17]
#         end = self.line[18][20:]
#         self.line[18] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_4_4(self):
#         start = self.line[16][0:17]
#         end = self.line[16][20:]
#         self.line[16] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[17][0:17]
#         end = self.line[17][20:]
#         self.line[17] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[18][0:17]
#         end = self.line[18][20:]
#         self.line[18] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_4_4(self):
#         start = self.line[16][0:17]
#         end = self.line[16][20:]
#         self.line[16] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[17][0:17]
#         end = self.line[17][20:]
#         self.line[17] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[18][0:17]
#         end = self.line[18][20:]
#         self.line[18] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_4_4(self):
#         start = self.line[16][0:17]
#         end = self.line[16][20:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:17]
#         end = self.line[17][20:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[18][0:17]
#         end = self.line[18][20:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_4_4(self):
#         start = self.line[16][0:17]
#         end = self.line[16][20:]
#         self.line[16] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[17][0:17]
#         end = self.line[17][20:]
#         self.line[17] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[18][0:17]
#         end = self.line[18][20:]
#         self.line[18] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 4_A //
#     def full_update_4_A(self):
#         start = self.line[16][:1]
#         end = self.line[16][2:]
#         self.line[16] = f"{start}{self.full}{end}"
#
#     def half_update_4_A(self):
#         start = self.line[16][:1]
#         end = self.line[16][2:]
#         self.line[16] = f"{start}{self.half}{end}"
#
# # set color for 4_B // move values +2
#     def full_update_4_B(self):
#         start = self.line[16][:3]
#         end = self.line[16][4:]
#         self.line[16] = f"{start}{self.full}{end}"
#
#     def half_update_4_B(self):
#         start = self.line[16][:3]
#         end = self.line[16][4:]
#         self.line[16] = f"{start}{self.half}{end}"
#
# # set color for 4_C // move lines +2
#     def full_update_4_C(self):
#         start = self.line[18][:1]
#         end = self.line[18][2:]
#         self.line[18] = f"{start}{self.full}{end}"
#
#     def half_update_4_C(self):
#         start = self.line[18][:1]
#         end = self.line[18][2:]
#         self.line[18] = f"{start}{self.half}{end}"
#
# # set color for 4_D // move values +2, move lines +2
#     def full_update_4_D(self):
#         start = self.line[18][:3]
#         end = self.line[18][4:]
#         self.line[18] = f"{start}{self.full}{end}"
#
#     def half_update_4_D(self):
#         start = self.line[18][:3]
#         end = self.line[18][4:]
#         self.line[18] = f"{start}{self.half}{end}"
# # END!!! 4_             stop for multi-curser select
# # END!!! self.line[16]  stop for multi-curser select
# # END!!! self.line[17]  stop for multi-curser select
# # END!!! self.line[18]  stop for multi-curser select
#
# # new line
# # set color for 3_1
#     def red_update_3_1(self):
#         start = self.line[12][0:5]
#         end = self.line[12][8:]
#         self.line[12] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[13][0:5]
#         end = self.line[13][8:]
#         self.line[13] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[14][0:5]
#         end = self.line[14][8:]
#         self.line[14] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_3_1(self):
#         start = self.line[12][0:5]
#         end = self.line[12][8:]
#         self.line[12] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[13][0:5]
#         end = self.line[13][8:]
#         self.line[13] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[14][0:5]
#         end = self.line[14][8:]
#         self.line[14] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_3_1(self):
#         start = self.line[12][0:5]
#         end = self.line[12][8:]
#         self.line[12] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[13][0:5]
#         end = self.line[13][8:]
#         self.line[13] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[14][0:5]
#         end = self.line[14][8:]
#         self.line[14] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_3_1(self):
#         start = self.line[12][0:5]
#         end = self.line[12][8:]
#         self.line[12] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[13][0:5]
#         end = self.line[13][8:]
#         self.line[13] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[14][0:5]
#         end = self.line[14][8:]
#         self.line[14] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_3_1(self):
#         start = self.line[12][0:5]
#         end = self.line[12][8:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:5]
#         end = self.line[13][8:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[14][0:5]
#         end = self.line[14][8:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_3_1(self):
#         start = self.line[12][0:5]
#         end = self.line[12][8:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:5]
#         end = self.line[13][8:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[14][0:5]
#         end = self.line[14][8:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 3_2  // move values +4
#     def red_update_3_2(self):
#         start = self.line[12][0:9]
#         end = self.line[12][12:]
#         self.line[12] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[13][0:9]
#         end = self.line[13][12:]
#         self.line[13] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[14][0:9]
#         end = self.line[14][12:]
#         self.line[14] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_3_2(self):
#         start = self.line[12][0:9]
#         end = self.line[12][12:]
#         self.line[12] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[13][0:9]
#         end = self.line[13][12:]
#         self.line[13] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[14][0:9]
#         end = self.line[14][12:]
#         self.line[14] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_3_2(self):
#         start = self.line[12][0:9]
#         end = self.line[12][12:]
#         self.line[12] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[13][0:9]
#         end = self.line[13][12:]
#         self.line[13] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[14][0:9]
#         end = self.line[14][12:]
#         self.line[14] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_3_2(self):
#         start = self.line[12][0:9]
#         end = self.line[12][12:]
#         self.line[12] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[13][0:9]
#         end = self.line[13][12:]
#         self.line[13] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[14][0:9]
#         end = self.line[14][12:]
#         self.line[14] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_3_2(self):
#         start = self.line[12][0:9]
#         end = self.line[12][12:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:9]
#         end = self.line[13][12:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[14][0:9]
#         end = self.line[14][12:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_3_2(self):
#         start = self.line[12][0:9]
#         end = self.line[12][12:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:9]
#         end = self.line[13][12:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[14][0:9]
#         end = self.line[14][12:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 3_3  // move values +8
#     def red_update_3_3(self):
#         start = self.line[12][0:13]
#         end = self.line[12][16:]
#         self.line[12] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[13][0:13]
#         end = self.line[13][16:]
#         self.line[13] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[14][0:13]
#         end = self.line[14][16:]
#         self.line[14] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_3_3(self):
#         start = self.line[12][0:13]
#         end = self.line[12][16:]
#         self.line[12] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[13][0:13]
#         end = self.line[13][16:]
#         self.line[13] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[14][0:13]
#         end = self.line[14][16:]
#         self.line[14] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_3_3(self):
#         start = self.line[12][0:13]
#         end = self.line[12][16:]
#         self.line[12] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[13][0:13]
#         end = self.line[13][16:]
#         self.line[13] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[14][0:13]
#         end = self.line[14][16:]
#         self.line[14] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_3_3(self):
#         start = self.line[12][0:13]
#         end = self.line[12][16:]
#         self.line[12] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[13][0:13]
#         end = self.line[13][16:]
#         self.line[13] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[14][0:13]
#         end = self.line[14][16:]
#         self.line[14] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_3_3(self):
#         start = self.line[12][0:13]
#         end = self.line[12][16:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:13]
#         end = self.line[13][16:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[14][0:13]
#         end = self.line[14][16:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_3_3(self):
#         start = self.line[12][0:13]
#         end = self.line[12][16:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:13]
#         end = self.line[13][16:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[14][0:13]
#         end = self.line[14][16:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 3_4  // move values +12
#     def red_update_3_4(self):
#         start = self.line[12][0:17]
#         end = self.line[12][20:]
#         self.line[12] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[13][0:17]
#         end = self.line[13][20:]
#         self.line[13] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[14][0:17]
#         end = self.line[14][20:]
#         self.line[14] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_3_4(self):
#         start = self.line[12][0:17]
#         end = self.line[12][20:]
#         self.line[12] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[13][0:17]
#         end = self.line[13][20:]
#         self.line[13] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[14][0:17]
#         end = self.line[14][20:]
#         self.line[14] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_3_4(self):
#         start = self.line[12][0:17]
#         end = self.line[12][20:]
#         self.line[12] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[13][0:17]
#         end = self.line[13][20:]
#         self.line[13] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[14][0:17]
#         end = self.line[14][20:]
#         self.line[14] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_3_4(self):
#         start = self.line[12][0:17]
#         end = self.line[12][20:]
#         self.line[12] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[13][0:17]
#         end = self.line[13][20:]
#         self.line[13] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[14][0:17]
#         end = self.line[14][20:]
#         self.line[14] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_3_4(self):
#         start = self.line[12][0:17]
#         end = self.line[12][20:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:17]
#         end = self.line[13][20:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[14][0:17]
#         end = self.line[14][20:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_3_4(self):
#         start = self.line[12][0:17]
#         end = self.line[12][20:]
#         self.line[12] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[13][0:17]
#         end = self.line[13][20:]
#         self.line[13] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[14][0:17]
#         end = self.line[14][20:]
#         self.line[14] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 3_A //
#     def full_update_3_A(self):
#         start = self.line[12][:1]
#         end = self.line[12][2:]
#         self.line[12] = f"{start}{self.full}{end}"
#
#     def half_update_3_A(self):
#         start = self.line[12][:1]
#         end = self.line[12][2:]
#         self.line[12] = f"{start}{self.half}{end}"
#
# # set color for 3_B // move values +2
#     def full_update_3_B(self):
#         start = self.line[12][:3]
#         end = self.line[12][4:]
#         self.line[12] = f"{start}{self.full}{end}"
#
#     def half_update_3_B(self):
#         start = self.line[12][:3]
#         end = self.line[12][4:]
#         self.line[12] = f"{start}{self.half}{end}"
#
# # set color for 3_C // move lines +2
#     def full_update_3_C(self):
#         start = self.line[14][:1]
#         end = self.line[14][2:]
#         self.line[14] = f"{start}{self.full}{end}"
#
#     def half_update_3_C(self):
#         start = self.line[14][:1]
#         end = self.line[14][2:]
#         self.line[14] = f"{start}{self.half}{end}"
#
# # set color for 3_D // move values +2, move lines +2
#     def full_update_3_D(self):
#         start = self.line[14][:3]
#         end = self.line[14][4:]
#         self.line[14] = f"{start}{self.full}{end}"
#
#     def half_update_3_D(self):
#         start = self.line[14][:3]
#         end = self.line[14][4:]
#         self.line[14] = f"{start}{self.half}{end}"
# # END!!! 3_             stop for multi-curser select
# # END!!! self.line[12]  stop for multi-curser select
# # END!!! self.line[13]  stop for multi-curser select
# # END!!! self.line[14]  stop for multi-curser select
#
# # new line
# # set color for 2_1
#     def red_update_2_1(self):
#         start = self.line[8][0:5]
#         end = self.line[8][8:]
#         self.line[8] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[9][0:5]
#         end = self.line[9][8:]
#         self.line[9] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[10][0:5]
#         end = self.line[10][8:]
#         self.line[10] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_2_1(self):
#         start = self.line[8][0:5]
#         end = self.line[8][8:]
#         self.line[8] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[9][0:5]
#         end = self.line[9][8:]
#         self.line[9] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[10][0:5]
#         end = self.line[10][8:]
#         self.line[10] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_2_1(self):
#         start = self.line[8][0:5]
#         end = self.line[8][8:]
#         self.line[8] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[9][0:5]
#         end = self.line[9][8:]
#         self.line[9] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[10][0:5]
#         end = self.line[10][8:]
#         self.line[10] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_2_1(self):
#         start = self.line[8][0:5]
#         end = self.line[8][8:]
#         self.line[8] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[9][0:5]
#         end = self.line[9][8:]
#         self.line[9] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[10][0:5]
#         end = self.line[10][8:]
#         self.line[10] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_2_1(self):
#         start = self.line[8][0:5]
#         end = self.line[8][8:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:5]
#         end = self.line[9][8:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[10][0:5]
#         end = self.line[10][8:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_2_1(self):
#         start = self.line[8][0:5]
#         end = self.line[8][8:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:5]
#         end = self.line[9][8:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[10][0:5]
#         end = self.line[10][8:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 2_2  // move values +4
#     def red_update_2_2(self):
#         start = self.line[8][0:9]
#         end = self.line[8][12:]
#         self.line[8] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[9][0:9]
#         end = self.line[9][12:]
#         self.line[9] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[10][0:9]
#         end = self.line[10][12:]
#         self.line[10] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_2_2(self):
#         start = self.line[8][0:9]
#         end = self.line[8][12:]
#         self.line[8] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[9][0:9]
#         end = self.line[9][12:]
#         self.line[9] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[10][0:9]
#         end = self.line[10][12:]
#         self.line[10] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_2_2(self):
#         start = self.line[8][0:9]
#         end = self.line[8][12:]
#         self.line[8] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[9][0:9]
#         end = self.line[9][12:]
#         self.line[9] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[10][0:9]
#         end = self.line[10][12:]
#         self.line[10] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_2_2(self):
#         start = self.line[8][0:9]
#         end = self.line[8][12:]
#         self.line[8] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[9][0:9]
#         end = self.line[9][12:]
#         self.line[9] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[10][0:9]
#         end = self.line[10][12:]
#         self.line[10] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_2_2(self):
#         start = self.line[8][0:9]
#         end = self.line[8][12:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:9]
#         end = self.line[9][12:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[10][0:9]
#         end = self.line[10][12:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_2_2(self):
#         start = self.line[8][0:9]
#         end = self.line[8][12:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:9]
#         end = self.line[9][12:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[10][0:9]
#         end = self.line[10][12:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 2_3  // move values +8
#     def red_update_2_3(self):
#         start = self.line[8][0:13]
#         end = self.line[8][16:]
#         self.line[8] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[9][0:13]
#         end = self.line[9][16:]
#         self.line[9] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[10][0:13]
#         end = self.line[10][16:]
#         self.line[10] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_2_3(self):
#         start = self.line[8][0:13]
#         end = self.line[8][16:]
#         self.line[8] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[9][0:13]
#         end = self.line[9][16:]
#         self.line[9] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[10][0:13]
#         end = self.line[10][16:]
#         self.line[10] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_2_3(self):
#         start = self.line[8][0:13]
#         end = self.line[8][16:]
#         self.line[8] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[9][0:13]
#         end = self.line[9][16:]
#         self.line[9] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[10][0:13]
#         end = self.line[10][16:]
#         self.line[10] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_2_3(self):
#         start = self.line[8][0:13]
#         end = self.line[8][16:]
#         self.line[8] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[9][0:13]
#         end = self.line[9][16:]
#         self.line[9] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[10][0:13]
#         end = self.line[10][16:]
#         self.line[10] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_2_3(self):
#         start = self.line[8][0:13]
#         end = self.line[8][16:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:13]
#         end = self.line[9][16:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[10][0:13]
#         end = self.line[10][16:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_2_3(self):
#         start = self.line[8][0:13]
#         end = self.line[8][16:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:13]
#         end = self.line[9][16:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[10][0:13]
#         end = self.line[10][16:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 2_4  // move values +12
#     def red_update_2_4(self):
#         start = self.line[8][0:17]
#         end = self.line[8][20:]
#         self.line[8] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[9][0:17]
#         end = self.line[9][20:]
#         self.line[9] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[10][0:17]
#         end = self.line[10][20:]
#         self.line[10] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_2_4(self):
#         start = self.line[8][0:17]
#         end = self.line[8][20:]
#         self.line[8] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[9][0:17]
#         end = self.line[9][20:]
#         self.line[9] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[10][0:17]
#         end = self.line[10][20:]
#         self.line[10] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_2_4(self):
#         start = self.line[8][0:17]
#         end = self.line[8][20:]
#         self.line[8] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[9][0:17]
#         end = self.line[9][20:]
#         self.line[9] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[10][0:17]
#         end = self.line[10][20:]
#         self.line[10] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_2_4(self):
#         start = self.line[8][0:17]
#         end = self.line[8][20:]
#         self.line[8] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[9][0:17]
#         end = self.line[9][20:]
#         self.line[9] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[10][0:17]
#         end = self.line[10][20:]
#         self.line[10] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_2_4(self):
#         start = self.line[8][0:17]
#         end = self.line[8][20:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:17]
#         end = self.line[9][20:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[10][0:17]
#         end = self.line[10][20:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_2_4(self):
#         start = self.line[8][0:17]
#         end = self.line[8][20:]
#         self.line[8] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[9][0:17]
#         end = self.line[9][20:]
#         self.line[9] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[10][0:17]
#         end = self.line[10][20:]
#         self.line[10] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 2_A //
#     def full_update_2_A(self):
#         start = self.line[8][:1]
#         end = self.line[8][2:]
#         self.line[8] = f"{start}{self.full}{end}"
#
#     def half_update_2_A(self):
#         start = self.line[8][:1]
#         end = self.line[8][2:]
#         self.line[8] = f"{start}{self.half}{end}"
#
# # set color for 2_B // move values +2
#     def full_update_2_B(self):
#         start = self.line[8][:3]
#         end = self.line[8][4:]
#         self.line[8] = f"{start}{self.full}{end}"
#
#     def half_update_2_B(self):
#         start = self.line[8][:3]
#         end = self.line[8][4:]
#         self.line[8] = f"{start}{self.half}{end}"
#
# # set color for 2_C // move lines +2
#     def full_update_2_C(self):
#         start = self.line[10][:1]
#         end = self.line[10][2:]
#         self.line[10] = f"{start}{self.full}{end}"
#
#     def half_update_2_C(self):
#         start = self.line[10][:1]
#         end = self.line[10][2:]
#         self.line[10] = f"{start}{self.half}{end}"
#
# # set color for 2_D // move values +2, move lines +2
#     def full_update_2_D(self):
#         start = self.line[10][:3]
#         end = self.line[10][4:]
#         self.line[10] = f"{start}{self.full}{end}"
#
#     def half_update_2_D(self):
#         start = self.line[10][:3]
#         end = self.line[10][4:]
#         self.line[10] = f"{start}{self.half}{end}"
# # END!!! 2_             stop for multi-curser select
# # END!!! self.line[8]  stop for multi-curser select
# # END!!! self.line[9]  stop for multi-curser select
# # END!!! self.line[10]  stop for multi-curser select
#
# # new line
# # set color for 1_1
#     def red_update_1_1(self):
#         start = self.line[4][0:5]
#         end = self.line[4][8:]
#         self.line[4] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[5][0:5]
#         end = self.line[5][8:]
#         self.line[5] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[6][0:5]
#         end = self.line[6][8:]
#         self.line[6] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_1_1(self):
#         start = self.line[4][0:5]
#         end = self.line[4][8:]
#         self.line[4] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[5][0:5]
#         end = self.line[5][8:]
#         self.line[5] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[6][0:5]
#         end = self.line[6][8:]
#         self.line[6] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_1_1(self):
#         start = self.line[4][0:5]
#         end = self.line[4][8:]
#         self.line[4] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[5][0:5]
#         end = self.line[5][8:]
#         self.line[5] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[6][0:5]
#         end = self.line[6][8:]
#         self.line[6] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_1_1(self):
#         start = self.line[4][0:5]
#         end = self.line[4][8:]
#         self.line[4] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[5][0:5]
#         end = self.line[5][8:]
#         self.line[5] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[6][0:5]
#         end = self.line[6][8:]
#         self.line[6] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_1_1(self):
#         start = self.line[4][0:5]
#         end = self.line[4][8:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:5]
#         end = self.line[5][8:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[6][0:5]
#         end = self.line[6][8:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_1_1(self):
#         start = self.line[4][0:5]
#         end = self.line[4][8:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:5]
#         end = self.line[5][8:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[6][0:5]
#         end = self.line[6][8:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 1_2  // move values +4
#     def red_update_1_2(self):
#         start = self.line[4][0:9]
#         end = self.line[4][12:]
#         self.line[4] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[5][0:9]
#         end = self.line[5][12:]
#         self.line[5] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[6][0:9]
#         end = self.line[6][12:]
#         self.line[6] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_1_2(self):
#         start = self.line[4][0:9]
#         end = self.line[4][12:]
#         self.line[4] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[5][0:9]
#         end = self.line[5][12:]
#         self.line[5] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[6][0:9]
#         end = self.line[6][12:]
#         self.line[6] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_1_2(self):
#         start = self.line[4][0:9]
#         end = self.line[4][12:]
#         self.line[4] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[5][0:9]
#         end = self.line[5][12:]
#         self.line[5] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[6][0:9]
#         end = self.line[6][12:]
#         self.line[6] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_1_2(self):
#         start = self.line[4][0:9]
#         end = self.line[4][12:]
#         self.line[4] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[5][0:9]
#         end = self.line[5][12:]
#         self.line[5] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[6][0:9]
#         end = self.line[6][12:]
#         self.line[6] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_1_2(self):
#         start = self.line[4][0:9]
#         end = self.line[4][12:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:9]
#         end = self.line[5][12:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[6][0:9]
#         end = self.line[6][12:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_1_2(self):
#         start = self.line[4][0:9]
#         end = self.line[4][12:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:9]
#         end = self.line[5][12:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[6][0:9]
#         end = self.line[6][12:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 1_3  // move values +8
#     def red_update_1_3(self):
#         start = self.line[4][0:13]
#         end = self.line[4][16:]
#         self.line[4] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[5][0:13]
#         end = self.line[5][16:]
#         self.line[5] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[6][0:13]
#         end = self.line[6][16:]
#         self.line[6] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_1_3(self):
#         start = self.line[4][0:13]
#         end = self.line[4][16:]
#         self.line[4] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[5][0:13]
#         end = self.line[5][16:]
#         self.line[5] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[6][0:13]
#         end = self.line[6][16:]
#         self.line[6] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_1_3(self):
#         start = self.line[4][0:13]
#         end = self.line[4][16:]
#         self.line[4] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[5][0:13]
#         end = self.line[5][16:]
#         self.line[5] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[6][0:13]
#         end = self.line[6][16:]
#         self.line[6] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_1_3(self):
#         start = self.line[4][0:13]
#         end = self.line[4][16:]
#         self.line[4] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[5][0:13]
#         end = self.line[5][16:]
#         self.line[5] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[6][0:13]
#         end = self.line[6][16:]
#         self.line[6] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_1_3(self):
#         start = self.line[4][0:13]
#         end = self.line[4][16:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:13]
#         end = self.line[5][16:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[6][0:13]
#         end = self.line[6][16:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_1_3(self):
#         start = self.line[4][0:13]
#         end = self.line[4][16:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:13]
#         end = self.line[5][16:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[6][0:13]
#         end = self.line[6][16:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 1_4  // move values +12
#     def red_update_1_4(self):
#         start = self.line[4][0:17]
#         end = self.line[4][20:]
#         self.line[4] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[5][0:17]
#         end = self.line[5][20:]
#         self.line[5] = f"{start}{self.red}{self.red}{self.red}{end}"
#         start = self.line[6][0:17]
#         end = self.line[6][20:]
#         self.line[6] = f"{start}{self.red}{self.red}{self.red}{end}"
#
#     def green_update_1_4(self):
#         start = self.line[4][0:17]
#         end = self.line[4][20:]
#         self.line[4] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[5][0:17]
#         end = self.line[5][20:]
#         self.line[5] = f"{start}{self.green}{self.green}{self.green}{end}"
#         start = self.line[6][0:17]
#         end = self.line[6][20:]
#         self.line[6] = f"{start}{self.green}{self.green}{self.green}{end}"
#
#     def blue_update_1_4(self):
#         start = self.line[4][0:17]
#         end = self.line[4][20:]
#         self.line[4] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[5][0:17]
#         end = self.line[5][20:]
#         self.line[5] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#         start = self.line[6][0:17]
#         end = self.line[6][20:]
#         self.line[6] = f"{start}{self.blue}{self.blue}{self.blue}{end}"
#
#     def yellow_update_1_4(self):
#         start = self.line[4][0:17]
#         end = self.line[4][20:]
#         self.line[4] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[5][0:17]
#         end = self.line[5][20:]
#         self.line[5] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#         start = self.line[6][0:17]
#         end = self.line[6][20:]
#         self.line[6] = f"{start}{self.yellow}{self.yellow}{self.yellow}{end}"
#
#     def selected_enter_update_1_4(self):
#         start = self.line[4][0:17]
#         end = self.line[4][20:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:17]
#         end = self.line[5][20:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected_enter}{self.selected_right}{end}"
#         start = self.line[6][0:17]
#         end = self.line[6][20:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
#     def selected_update_1_4(self):
#         start = self.line[4][0:17]
#         end = self.line[4][20:]
#         self.line[4] = f"{start}{self.selected}{self.selected_up}{self.selected}{end}"
#         start = self.line[5][0:17]
#         end = self.line[5][20:]
#         self.line[5] = f"{start}{self.selected_left}{self.selected}{self.selected_right}{end}"
#         start = self.line[6][0:17]
#         end = self.line[6][20:]
#         self.line[6] = f"{start}{self.selected}{self.selected_down}{self.selected}{end}"
#
# # set color for 1_A //
#     def full_update_1_A(self):
#         start = self.line[4][:1]
#         end = self.line[4][2:]
#         self.line[4] = f"{start}{self.full}{end}"
#
#     def half_update_1_A(self):
#         start = self.line[4][:1]
#         end = self.line[4][2:]
#         self.line[4] = f"{start}{self.half}{end}"
#
# # set color for 1_B // move values +2
#     def full_update_1_B(self):
#         start = self.line[4][:3]
#         end = self.line[4][4:]
#         self.line[4] = f"{start}{self.full}{end}"
#
#     def half_update_1_B(self):
#         start = self.line[4][:3]
#         end = self.line[4][4:]
#         self.line[4] = f"{start}{self.half}{end}"
#
# # set color for 1_C // move lines +2
#     def full_update_1_C(self):
#         start = self.line[6][:1]
#         end = self.line[6][2:]
#         self.line[6] = f"{start}{self.full}{end}"
#
#     def half_update_1_C(self):
#         start = self.line[6][:1]
#         end = self.line[6][2:]
#         self.line[6] = f"{start}{self.half}{end}"
#
# # set color for 1_D // move values +2, move lines +2
#     def full_update_1_D(self):
#         start = self.line[6][:3]
#         end = self.line[6][4:]
#         self.line[6] = f"{start}{self.full}{end}"
#
#     def half_update_1_D(self):
#         start = self.line[6][:3]
#         end = self.line[6][4:]
#         self.line[6] = f"{start}{self.half}{end}"
# # END!!! 1_             stop for multi-curser select
# # END!!! self.line[4]  stop for multi-curser select
# # END!!! self.line[5]  stop for multi-curser select
# # END!!! self.line[6]  stop for multi-curser select
#
#     def print_screen(self):
#         """1. clears the screen
#         2. prints every element of the 'line' attribute"""
#         print('\033[H\033[J', end='')
#         for position in range(44):
#             print(self.line[position])
