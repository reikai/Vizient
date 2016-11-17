#! python3

# Testing the module, 'GmailNotifier.py'.
# Put your own addresses, subject lines, and messages.

from GmailNotifier import *

# information for GmailNotifier.
tolist = ['ty.tippawang@vizientinc.com']
subject = 'Notification.'
message = '''
Good morning!

Ty Tippawang
'''

gmail = Gmail()
print('Sending an email to: ' + ', '.join(tolist))
gmail.sendemail(tolist, subject, message)

