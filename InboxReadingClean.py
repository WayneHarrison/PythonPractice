import imapclient, pyzmail #Import 3rd party moduldes
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) #Connect to gmail IMAP server
conn.login('email', 'password') #Login using email and password
conn.select_folder('INBOX', readonly=True) #Selecting the inbox
UIDs = conn.search(['SINCE', '16-Dec-2020']) #Search for emails from a certain date.
message = pyzmail.PyzMessage.factory(raw[9696][b'BODY[]']) #Use PYZMail to store the message based on its unique ID
message.get_address('from') #Get who sent the email
message.get_address('to') #Get who it was sent to
message.text_part.get_payload().decode('UTF-8') #Get the body of the message.
