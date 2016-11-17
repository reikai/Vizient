import smtplib

username = 'practicingpython006@gmail.com'          # Who is sending the email
password = 'practicingpython'                       # Password of sender
fromemail = username                                # Who is the 'from' email
to = 'ty.tippawang@vizientinc.com'                  # Who are you send the email to
content = 'test email message!'                     # Is this the body of the email?

mail = smtplib.SMTP('smtp.gmail.com', 465)          #  Or you can use Port 465
mail.ehlo()
mail.starttls()  # prepares to log you in
mail.login(username, password)
mail.sendmail(fromemail, to, content)
mail.close()                                        # Close the connection to the server.

