#! python3
# This file takes inputs from ExpensesData (Has GL accounts, CCs, and lists of necessary columns in the GL Pivots)
# and uses them in functions from GLExpenseFunctions.
# Final result: The GL should be able to be filtered down to anything you need and saved in Excel 2010.

from GLExpenseFunctions import *
from ExpensesData import *

FileLocation = r'I:\VhaFinance\GL Pivot'
FileName = r'2016 GL Table_Pivot.xlsm'
SheetName = r'table'

SaveLocation = 'I:\VhaFinance\Ty Tippawang\Short Requests\Tony Romano'
FileSaveName = 'TempHelp & Consulting Expense 2016.xlsx'

# Navigate to the file and specific sheet, put it in a DataFrame:
df = ExcelToDataFrame(FileLocation, FileName, SheetName)

# Drop last row.
df = DropRow(df, [-1])

# Filter down to necessary columns:  (columns2016 is from ExpensesData)
df = ReduceColumns(df, columns2016)

# Reduce DataFrame to just our list of CCs:
df = FilterDown(df, CCs, 'ACCT_UNIT')

# Filter again to get just the GL accounts we want:
df = FilterDown(df, GLs, 'ACCOUNT')

# Save the file!
SaveDataFrame(df, SaveLocation, FileSaveName)
