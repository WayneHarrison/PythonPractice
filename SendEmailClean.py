import smtplib
conn = smtplib.smtp('emailserver', port)
conn.ehlo()
conn.starttls()
conn.login('email', 'password')
conn.sendmail('sendingemail', 'sendingemail', 'Subject: Subject \n\n Body.')
