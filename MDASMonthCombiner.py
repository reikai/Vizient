#! python3
# Takes a bunch of tables in excel files and appends them to each other.
# Then, it writes a Pandas Pivot Table to summarize the data.

import pandas as pd
import os

filelocation = 'I:\VhaFinance\Ty Tippawang\MDAS GL\Month-by-Month Pivots & Data\Full Month Pivots'
os.chdir(filelocation)



def AddSheetToDataFrame(ListofExcelFiles, SheetNum):
    # Will return this df after it's been concat'd
    print('Empty DataFrame created.')
    df = pd.DataFrame()

    for file in ListofExcelFiles:
        print('Reading in ' + str(file))
        xlsx = pd.ExcelFile(file)
        print('Creating a temporary DataFrame...')
        tempdf = xlsx.parse(SheetNum)

        if df.empty:
            print('Overwriting empty DataFrame...')
            df = tempdf
        else:
            print('Concatenating DataFrame df and the current temporary DataFrame...')
            df = pd.concat([df, tempdf])
    print('Done.')
    return df


df = AddSheetToDataFrame(os.listdir(os.getcwd()), 1)

pivot = pd.pivot_table(df, values='Amount', index=['Vizient CC', 'GL Description', 'Vizient GL', 'Transaction Description'], columns='PerPost')

pivot.to_excel('test.xlsx')
