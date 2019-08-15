import imaplib
import base64
import os
import email
from bs4 import BeautifulSoup
import requests
import requests.exceptions

username = os.environ['EMAIL']
password = os.environ['PASSWORD']

mail = imaplib.IMAP4_SSL('outlook.office365.com', 993)
mail.login(username, password)
mail.select('openlaw')


type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]

    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    print(email_message)




mail.close()
mail.logout()