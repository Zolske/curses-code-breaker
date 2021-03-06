"""
Contains the functions to gatherer data from the Google spreadsheet and to update it.
Note that I originally had print statements printing the process of the functions to the
background, which worked nicely in the terminal but messed up the browser-terminal
"""
import datetime
import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('code_breaker_global_high_score')


def get_this_month_high_score(file_name_date):
    """
    Gets the this_month_high_score from the Google sheet, sorts it from highest to lowest score and saves it
    .this_month_high_score, If there is not such sheet then it creates on with 5 rows and 20 columns,
    the score set to 0 (must have an integer otherwise the program will raise error later. The sheet is named after
    the current year and month (2022_02). The YYYY_MM needs to be passed as argument.
    :param file_name_date: is this month, structured in the format YYYY_MM, the name of the Google sheet for this month
    is structured in the same way
    :return: the Google sheet this_month_high_score sorted from highest to lowest as list of list
    e.g.[[name,date,score],[name,date,score]]
    """
    # originally the function was looking for the current date itself, but it slowed the program too much down
    # (when function is used again to check for update)
    try:
        # saves the date of the worksheet if it exists
        this_month_high_score_worksheet = SHEET.worksheet(file_name_date)
    except:  # making the exception more specific e.g. ValueError, curses the browser-terminal to rais an error!!!!
        # if not exist, then it is created
        # must be commented out for heroku
        this_month_high_score_worksheet = SHEET.add_worksheet(title=file_name_date, rows="20", cols="5")
        # the column for the score (column C and E) must have an integer,
        # assigns 0 to all 20 columns (C, D, E)
        list_template = [[]]
        for index in range(20):
            list_template.insert(index, ['', '', 0, 0, 0])
        update_high_score_list(file_name_date, list_template)

    # converts the date in a list of list row [[cell], [cell], [cell]]
    data = this_month_high_score_worksheet.get_all_values()
    # convert the score and date string type into integer
    for index in range(len(data)):
        data[index][2] = int(data[index][2])  # only the 3th column of each row
    data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
    return data[:20]  # returns only the first 20 entries, should be only 20 any way


def get_all_time_high_score():
    """
    Gets the all_time_high_score from the google sheet, sorts it from highest to lowest score and saves it
    .all_time_high_score
    :return: the google sheet all_time_high_score sorted from highest to lowest as list of list
    e.g.[[name,date,score],[name,date,score]]
    """
    # saves the date of the worksheet
    all_time_high_score_worksheet = SHEET.worksheet('all_time_high_score')
    # converts the date in a list of list row [[cell], [cell], [cell]]
    data = all_time_high_score_worksheet.get_all_values()
    # convert the score and date string type into integer
    for index in range(len(data)):
        data[index][2] = int(data[index][2])  # only the 3th column of each row
    data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
    return data[:20]  # returns only the first 20 entries, should be only 20 any way


def get_today_month_year():
    """
    Checks today date.
    :return: [[year_today 2022], [month_word_today February], [score_date 22.02.07], [file_name_date 2022_02],
    [today_day_name Wednesday], [today_date_num 12/31/18]]
    """
    date_today = datetime.datetime.now()  # '2022-02-07 19:42:22.815959'
    month_word_today = date_today.strftime("%B")  # 'February'
    day_today = date_today.strftime("%d")  # 07
    day_number_today = date_today.strftime("%j")  # Day number of year 001-366
    today_day_name = date_today.strftime("%A")  # Weekday, full version, Wednesday
    today_date_num = date_today.strftime("%x")  # Local version of date	12/31/18
    month_today = date_today.strftime("%m")  # '02'
    year_today = date_today.strftime("%Y")  # '2022'
    year_today_short = date_today.strftime("%y")  # '22' year without century
    score_date = f"{year_today_short}.{month_today}.{day_today}"  # 22.02.07
    file_name_date = f"{year_today}_{month_today}"  # 2022_02
    file_name_day_date = f"({year_today_short}{day_number_today})"  # (YYDDD) E.g 22044, year 2022, day of the year 044,
    # (2022.02.13)
    date_list = [[year_today], [month_word_today], [score_date], [file_name_date], [today_day_name], [today_date_num],
                 [file_name_day_date]]
    return date_list


def get_today_high_score(file_name_day_date):
    """
    Checks google sheet if there is a today high score list, if not then it will overwrite the one before the last
    (not the last). It needs today's date from the get_today_year_day_num() in the format (YYDDD) as input. Test have
    shown to that performance is faster when the date is created separated and only once, not with every
    google sheet score request.
    :param file_name_day_date: from the get_today_year_day_num() in the format (YYDDD)
    :return: the google sheet of todays high score sorted from highest to lowest as list of list
    e.g.[[name,date,score],[name,date,score]]
    """
    try:
        # saves the date of the worksheet if it exists
        today_high_score_worksheet = SHEET.worksheet(file_name_day_date)
        # print(f">Found 'google sheet' <{file_name_day_date}> which is today's high score list ...")
        # must be commented out for heroku
    except:  # making the exception more specific e.g. ValueError, curses the browser-terminal to rais an error!!!!
        # if not exist, then it is created
        # print(f">No 'google sheet' <{file_name_day_date}> found with today's high score list ...")
        # must be commented out for heroku
        old_high_score_title = get_google_sheet_titles_day_oldest()
        old_high_score_id = SHEET.worksheet(old_high_score_title)
        SHEET.del_worksheet(old_high_score_id)
        # print(f">Delete old 'google sheet' {old_high_score_title} with old day high score list ...")
        # must be commented out for heroku
        today_high_score_worksheet = SHEET.add_worksheet(title=file_name_day_date, rows="20", cols="5")
        # the column for the score (column C and E) must have an integer,
        # assigns 0 to all 20 columns (C, D, E)
        list_template = [[]]
        for index in range(20):
            list_template.insert(index, ['', '', 0, 0, 0])
        update_high_score_list(file_name_day_date, list_template)

    # # converts the date in a list of list row [[cell], [cell], [cell]]
    data = today_high_score_worksheet.get_all_values()
    # convert the score and date string type into integer
    for index in range(len(data)):
        data[index][2] = int(data[index][2])  # only the 3th column of each row
    data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
    return data[:20]  # returns only the first 20 entries, should be only 20 any way


def get_google_sheet_titles_day_oldest():
    """
    Gets the Google sheet titles which are enclosed in ( ). Do not enclose any other titles or parts of a title
    in () when creating titles for Google sheet.
    :return: the first element of a sorted list, of the titles which are in ( ) and as a string.
    Starting with the smallest (oldest, because older dates have smaller values) value.
    e.g ['(22042)', '(22044)']
    """
    google_sheet = SHEET.worksheets()
    google_sheet = "".join(str(e) for e in google_sheet)  # creates a list from the Google sheet titles as string
    file_name_daily = re.findall(r'\B[(]\w+[)]\B', google_sheet, re.I)  # list from strings within ( )
    for index in range(len(file_name_daily)):  # removes the first and last character which should be ( )
        file_name_daily[index] = file_name_daily[index][1:-1]

    for index in range(len(file_name_daily)):
        file_name_daily[index] = int(file_name_daily[index])  # converts the string element to int
    file_name_daily.sort(key=lambda x: x, reverse=False)  # sort the lowest score to the beginning

    for index in range(len(file_name_daily)):  # adds to every element ( ) and converts int into string
        file_name_daily[index] = f"({file_name_daily[index]})"

    return file_name_daily[0]  # returns the first element of a sorted list of the Google sheet titles
    # which are in (). Lowest first


def update_high_score_list(score_list, new_high_score):
    """
    Updates the specified high score list to the specified Google sheet.
    :param score_list: determent which score list is updated (needs to be the correct file name)
    :param new_high_score: contains the list of the new data
    """
    old_google_sheet = SHEET.worksheet(score_list)
    old_google_sheet.update('A1:E20', new_high_score)
