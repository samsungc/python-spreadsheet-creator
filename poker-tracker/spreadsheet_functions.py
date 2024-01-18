import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def create_spreadsheet(creds, title):
    '''
    Creates a spreadsheet on the users account with the title 'title'
    '''
    try:
        service = build("sheets", "v4", credentials=creds)
        spreadsheet = {"properties": {"title": title}}
        spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
        )
        return spreadsheet.get("spreadsheetId")
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def write_to_sheet(creds, spreadsheet_id, range, input_option, data):
    '''
    range: uses A1 notation
    input_option: RAW or USER_ENTERED
    
    this function write to the spreadsheet
    '''

    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": data}

        service.spreadsheets().values().update(
            spreadsheetId = spreadsheet_id,
            range = range,
            valueInputOption = input_option,
            body = body
            ).execute()
        return
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return
    
def batch_write_to_sheet(creds, spreadsheet_id, input_option, data):

    try:
        service = build('sheets', 'v4', credentials=creds)
        body = {'valueInputOption':input_option, 'data':data}
        res = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        return res
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


    
def build_sheet(names):
    '''
    builds the spreadsheet in one go for more efficiency
    returns data = [{range:range, values:[values]}, {range:range, etc}]
    '''
    data = []
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # left hand side legend
    # includes: date, buyin, names + guest, night total, totals
    data.append({})
    data[0]['range'] = f'A1:A{4 + len(names) + 3 + 3}'
    data[0]['majorDimension'] = 'COLUMNS'
    data[0]['values'] = [['date', 'buy in', ''] + names + ['guest', '', '', 'night total:', '', '', 'totals:']]

    # putting in the names for the totals
    data.append({})
    data[1]['range'] = f'B{3 + len(names) + 3 + 3}:{alpha[len(names)]}{3 + len(names) + 3 + 3}'
    data[1]['values'] = [names]

    # putting in the formulas for night total
    data.append({})
    data[2]['range'] = f'B{4 + len(names) + 3}:Z{4 + len(names) + 3}'
    res = []
    for letter in alpha:
        if letter == 'A':
            continue
        res.append(f'=sum({letter}4:{letter}{4 + len(names) - 1})')
    data[2]['values'] = [res]

    # putting in the formulas for the total
    data.append({})
    data[3]['range'] = f'B{4 + len(names) + 3 + 3}:{alpha[len(names)]}{4 + len(names) + 3 + 3}'
    res = []
    for i in range(4, len(names) + 4):
        res.append(f'=sum({i}:{i})')
    data[3]['values'] = [res]

    return data


    
def format_sheet(creds, spreadsheet, names):
    '''
    puts everything together, formats sheet
    '''

    data = build_sheet(names)
    batch_write_to_sheet(creds, spreadsheet, 'USER_ENTERED', data)


if __name__ == '__main__':
    test = ['samson', 'daniel', 'test', 'L']
    print(build_sheet(test))



