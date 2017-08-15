##import winshell
from win32com.shell import shell, shellcon
##print 'Desktop =>', winshell.desktop ()


print shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
print shell.SHGetFolderPath(0, shellcon.CSIDL_PROGRAM_FILES, None, 0)
print shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0)

