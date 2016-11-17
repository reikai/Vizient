#! python3
# Reduces each Excel file to usable amounts of data.
# Each file is 1 month of MDAS GL Data.
# Files returned are NOT mapped to Vizient CCs or GLs. They're simply stripped down to certain columns.

import pandas as pd
import os

files = ['May 2016.xlsx',
         'June 2016.xlsx',
         'July 2016.xlsx']

columns = ['PerPost',
           'Company ID',
           'Subaccount',
           'Subaccount Description',
           'Transaction Description',
           'Account',
           'Amount']

location = 'I:\VhaFinance\Ty Tippawang\MDAS GL'
os.chdir(location)

def ColumnReduce(file, fields):
    # File is a excel file name. Make sure you're in the correct directory.
    print('Reading in file name: ' + file + '.')
    df = pd.read_excel(file)
    print('Reducing workbook to appropriate columns...')
    df = df[fields]
    print('Saving file...')
    df.to_excel('Reduced ' + file, index=False)

for file in files:
    ColumnReduce(file, columns)



