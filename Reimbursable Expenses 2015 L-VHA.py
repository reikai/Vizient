from GLExpenseFunctions import *
from ExpensesData import *

FileLocation = r'I:\VhaFinance\Ty Tippawang\GL Pivot Data\VHA GL'
FileName = r'2015 Data.xlsx'
SheetName = r'Data'

SaveLocation = 'I:\VhaFinance\Ty Tippawang\GL Pivot Data\VHA GL\Saved!'
FileSaveName = 'L-Vizient Expense Report 2015.xlsx'


# Navigate to the file and specific sheet, put it in a DataFrame:
df = ExcelToDataFrame(FileLocation, FileName, SheetName)

# Filter down to necessary columns:  (columns2016 is from ExpensesData)
df = ReduceColumns(df, columns2016)

# Reduce DataFrame to just our list of CCs:
df = FilterDown(df, co1ccs, 'ACCT_UNIT')

# Filter again to get just the GL accounts we want:
df = FilterDown(df, reimGLs, 'ACCOUNT')

# Save the file!
SaveDataFrame(df, SaveLocation, FileSaveName)

