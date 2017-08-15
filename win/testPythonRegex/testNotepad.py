from pywinauto import application
import re

print "start"
try:
    
    app =application.Application()

    app.start_('notepad.exe')

    app.Notepad.MenuSelect("File->Open")
    
    app.dialog.edit.TypeKeys("C:\\ProgPython\\test.txt")

    app.dialog.Open.Click()

    #edit_box = app.Notepad.WindowText() #Title
    alltext = app.Notepad.Edit1.WindowText()
    
    #print alltext

    app.Notepad.MenuSelect("File->Exit")
    
    pattern = re.compile(r'\w')
    match = pattern.match(alltext)
    if match:
    print match.groups()
  
    #items = re.findall("\w+", alltext)
    #print items
except:
    print "except"
    
print "end"

'''
app.UntitledNotepad.MenuSelect("File->SaveAs")
app.SaveAs.ComboBox5.Select("UTF-8")
app.SaveAs.edit1.SetText("Example-utf8.txt")
app.SaveAs.Save.Click()

app.Open.Open.Click() # opening large file
app.Open.WaitNot('visible') # make sure "Open" dialog became invisible
# wait for up to 30 seconds until data.txt is loaded
app.Window(title='data.txt - Notepad').Wait('ready', timeout=30)


'''
        



    


