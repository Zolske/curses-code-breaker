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


#data = global_high_score.get_all_records()
# temp_sheet = SHEET.worksheets()
# print(temp_sheet[0])
class Spreadsheet:
    def __init__(self):
        self.all_time_high_score = []
        self.this_month_high_score = []
        self.top_6_all_time_high_score = []
        self.top_6_this_month_high_score = []
        self.this_month_year_data = ['', '']  # [0]year [1]Month

    def get_this_month_high_score(self):
        date_today = datetime.datetime.now()  # '2022-02-07 19:42:22.815959'
        year_today = date_today.strftime("%Y")  # '2022'
        self.this_month_year_data[0] = year_today
        month_word_today = date_today.strftime("%B")  # 'February'
        self.this_month_year_data[1] = month_word_today
        month_today = date_today.strftime("%m")  # '02'
        date_today = f"{year_today}_{month_today}"  # '2022_02'
        try:
            this_month_high_score_worksheet = SHEET.worksheet(date_today)  # saves the date of the worksheet if it exists
        except:
            this_month_high_score_worksheet = SHEET.add_worksheet(title=date_today, rows="20", cols="3")  # if not exist, then it is created
            pass
        data = this_month_high_score_worksheet.get_all_values()  # converts the date in a list of list row [[cell], [cell], [cell]]
        for index in range(len(data)):  # convert the score and date string type into integer
            # data[index][2] == score must be an int!
            if isinstance(data[index][2], str):
                data[index][2] = 0
            data[index][2] = int(data[index][2])  # only the 3th column of each row
            # data[index][1] = int(data[index][1])  # only the 2nd column of each row
        data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
        self.this_month_high_score = data[:19]  # only the first 20, should not be more any nway
        self.top_6_this_month_high_score = data[:5]  # only the first 6

    def get_all_time_high_score(self):
        all_time_high_score_worksheet = SHEET.worksheet('all_time_high_score')  # saves the date of the worksheet
        data = all_time_high_score_worksheet.get_all_values()   # converts the date in a list of list row [[cell], [cell], [cell]]
        for index in range(len(data)):  # convert the score and date string type into integer
            # data[index][2] == score must be an int!
            if isinstance(data[index][2], str):
                data[index][2] = 0
            data[index][2] = int(data[index][2])  # only the 3th column of each row
            # data[index][1] = int(data[index][1])  # only the 2nd column of each row
        data.sort(key=lambda x: x[2], reverse=True)  # sort the highest score to the beginning
        self.all_time_high_score = data[:19]  # only the first 20, should not be more any nway
        self.top_6_all_time_high_score = data[:5]  # only the first 6

spreadsheet = Spreadsheet()
spreadsheet.get_this_month_high_score()
#print(f'this is month {spreadsheet.this_month_high_score}')
#print(f'this is month {spreadsheet.top_6_this_month_high_score}')
#print(f'this is month {spreadsheet.this_month_high_score}')
print(f"{spreadsheet.this_month_year_data[0]} and {spreadsheet.this_month_year_data[1]}")
spreadsheet.get_all_time_high_score()
print(f'this is all time {spreadsheet.all_time_high_score}')

