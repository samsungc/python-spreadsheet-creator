########################################
'''
spreadsheet creator for poker cash games

Last updated:   Jan 17, 2024
Author:         Samson Chow
'''
import auth as au
import spreadsheet_functions as sf

# names and title 
people = ['samson', 'daniel', 'etc']
title = 'get hacked 101';

'''
TODO: figure out how to get users to auth themselves
'''

if __name__ == '__main__':
    # get the auth cred
    creds = au.get_authed();

    # creating the spreadsheet
    spreadsheet = sf.create_spreadsheet(creds, title)
    print(f"Spreadsheet created: https://docs.google.com/spreadsheets/d/{spreadsheet}/edit#gid=0")

    # format spreadsheet
    sf.format_sheet(creds, spreadsheet, people)



