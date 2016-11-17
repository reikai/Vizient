from GLExpenseFunctions import *
from ExpensesData import *

FileLocation = r'I:\VhaFinance\Ty Tippawang\GL Pivot Data\VHA GL'
FileName = r'2015 Data.xlsx'
SheetName = r'Data'

SaveLocation = 'I:\VhaFinance\Ty Tippawang\GL Pivot Data\VHA GL\Saved!'
FileSaveName = 'L-Vizient Expense Report 2015.xlsx'

xlsxwriter = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

