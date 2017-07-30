#!/usr/local/bin/python
"""
###########################################################################
use the Python SMTP mail interface module to send email messages; this
is just a simple one-shot send script--see pymail, PyMailGUI, and
PyMailCGI for clients with more user interaction features; also see
popmail.py for a script that retrieves mail, and the mailtools pkg
for attachments and formatting with the standard library email package;
###########################################################################
"""

import smtplib, sys, email.utils, mailconfig
mailserver = 'smtp.qq.com' # ex: smtp.rmi.net

From = '675686066@qq.com' # or import from mailconfig
To   = 'leiyang-ge@163.com' # ex: python-list@python.org
Tos  = To.split(';')                           # allow a list of recipients
Subj = 'sub\nbody' 
Date = email.utils.formatdate()                # curr datetime, rfc2822

# standard headers, followed by blank line, followed by text
text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')

print('Connecting...')
server = smtplib.SMTP_SSL(mailserver)              # connect, no log-in step
server.set_debuglevel(1)
server.login(From,'code')
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:                                     # smtplib may raise exceptions
    print('Failed recipients:', failed)        # too, but let them pass here
else:
    print('No errors.')
print('Bye.')
