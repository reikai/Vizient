#! python3

# Opens the GL Pivot, narrows it downs to a Data frame involving the following:
# Cost Centers: 734, 773, 780, 766, 774,
#               8018, 8029, 8030, 8035, 8069, 8470, 8503
# GL Accounts: 60100 (TempHelp/Contract Labor), 74600 (Consulting), 74610 (Purchased Services)
#
import pandas as pd
import os

def ExcelToDataFrame(startLoc, fileName, sheetName):
    # This function navigates to an excel file, opens it, grabs the contents,
    # and filters down base on content you specify.
    # The resulting file is then save in a different location, also specified by the user.
    print('Navigating to file location...')
    os.chdir(startLoc)
    print('Opening Excel File...')
    xlsx = pd.ExcelFile(fileName)
    print('Parsing the table into a Pandas Dataframe...')
    df = xlsx.parse(sheetName)
    return df

def SaveDataFrame(DataFrame, endLoc, fileName):
    # Pass this a DataFrame, a file location, and a full filename for Excel 2010 with the .xlsx suffix.
    print('Changing location to practice folder...')
    os.chdir(endLoc)
    print('Saving...')
    DataFrame.to_excel(fileName, index=False)
    print('File Saved! Please check here for the newly saved file:')
    print(endLoc)

def DropRow(DataFrame, i):
    # Drops a given list of rows. Pass a DataFrame and which row(s) you want to drop. Make sure i is a list.
    print('Dropping the row(s) you specified...')
    DataFrame = DataFrame.drop(DataFrame.index[i])
    print('Rows dropped, DataFrame returned.')
    return DataFrame

def FilterDown(DataFrame, criteria, column):
    # Filters down a DataFrame's Column based on the criteria in that column.
    # criteria = list, column = string name of a column.
    print('Filtering a column down to your specified list...')
    DataFrame = DataFrame[DataFrame[column].isin(criteria)]
    print('DataFrame filtered and returned.')
    return DataFrame

def ReduceColumns(DataFrame, columnList):
    # Reduces DataFrame down to a list of necessary columns. Other columns are dropped.
    print('Reducing a DataFrame to your list of columns.')
    DataFrame = DataFrame[columnList]
    print('DataFrame reduced and returned.')
    return DataFrame

def PivotTable(DataFrame, values, index, columns):
    # Makes a pivot table. values, index, and columns can all be lists or strings.
    # Warning; if you save this in Excel, it's hard coded with no formatting and merged cells. It's not the greatest.
    # It may be better to just get in there and pivot it yourself. D:
    DataFrame = pd.pivot_table(DataFrame, values=values, index=index, columns=columns)
    return DataFrame