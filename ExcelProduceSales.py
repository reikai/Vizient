#! python3

# Cycles over a workbook and updates prices.

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')

# The dictionary of price updates.
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}

print('Updating prices...')
for row in range(2, sheet.max_row + 1):                   # Skip the header row of the data.
    PRODUCE = sheet['A' + str(row)].value
    COSTPERPOUND = sheet['B' + str(row)].value

    if PRODUCE in PRICE_UPDATES:
        sheet['B' + str(row)] = PRICE_UPDATES[PRODUCE]


wb.save('updatedProduceSales.xlsx')
print('Done.')


