import xlwt

wb = xlwt.Workbook()

ws = wb.add_sheet('sheetly')

ws.write(1, 1, "11")

wb.save('lyworkbook.xls')

print "done"
