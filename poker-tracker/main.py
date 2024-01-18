########################################
'''
Automatic poker cash game tracker

Last updated:   Jan 17, 2024
Author:         Samson Chow
'''
import auth as au
import spreadsheet_functions

# put names here as list: ie. 'samson', 'daniel', ...
people = []

# name of spreadsheet
title = 'put title here';

if __name__ == '__main__':
    au.get_authed();

