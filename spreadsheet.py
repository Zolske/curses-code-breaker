import datetime
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


def get_this_month_high_score(file_name_date):
    """
    Gets the this_month_high_score from the google sheet, sorts it from highest to lowest score and saves it
    .this_month_high_score, If there is not such sheet then it creates on with 3 rows and 20 columns,
    the score set to 0 (must have an integer otherwise the program will raise error later. The sheet is named after
    the current year and month (2022_02). The YYYY_MM needs to be passed as argument.
    :return: the google sheet this_month_high_score sorted from highest to lowest
    """
    # originaly the function was looking for the current date itself, but it slowed the program too much down
    # (when function is used again to check for update)
    try:
        # saves the date of the worksheet if it exists
        this_month_high_score_worksheet = SHEET.worksheet(file_name_date)
    except:
        # if not exist, then it is created
        this_month_high_score_worksheet = SHEET.add_worksheet(title=file_name_date, rows="20", cols="3")
        # the column for the score (3th from left, column C) must have an integer, assigns 0 to all 20 columns
        for index in range(1, 21):
            cell = f"C{index}"
            this_month_high_score_worksheet.update(cell, 0)
        pass
    # converts the date in a list of list row [[cell], [cell], [cell]]
    data = this_month_high_score_worksheet.get_all_values()
    # convert the score and date string type into integer
    for index in range(len(data)):
        data[index][2] = int(data[index][2])  # only the 3th column of each row
    data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
    return data[:19]  # returns only the first 20 entries, should be only 20 any way


def get_all_time_high_score():
    """
    Gets the all_time_high_score from the google sheet, sorts it from highest to lowest score and saves it
    .all_time_high_score
    :return: the google sheet all_time_high_score sorted from highest to lowest
    """
    # saves the date of the worksheet
    all_time_high_score_worksheet = SHEET.worksheet('all_time_high_score')
    # converts the date in a list of list row [[cell], [cell], [cell]]
    data = all_time_high_score_worksheet.get_all_values()
    # convert the score and date string type into integer
    for index in range(len(data)):
        data[index][2] = int(data[index][2])  # only the 3th column of each row
    data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
    return data[:19]  # returns only the first 20 entries, should be only 20 any way


def get_today_month_year():
    """
    Checks today date.
    :return: [[year_today 2022], [month_word_today February], [score_date 22.02.07], [file_name_date 2022_02]]
    """
    date_today = datetime.datetime.now()  # '2022-02-07 19:42:22.815959'
    month_word_today = date_today.strftime("%B")  # 'February'
    day_today = date_today.strftime("%d")  # 07
    month_today = date_today.strftime("%m")  # '02'
    year_today = date_today.strftime("%Y")  # '2022'
    year_today_short = date_today.strftime("%y")  # '22'
    score_date = f"{year_today_short}.{month_today}.{day_today}"  # 22.02.07
    file_name_date = f"{year_today}_{month_today}"  # 2022_02
    date_list = [[year_today], [month_word_today], [score_date], [file_name_date]]
    return date_list

