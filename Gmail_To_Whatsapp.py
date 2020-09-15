import imaplib
import email
import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your sid"
# Your Auth Token from twilio.com/console
auth_token  = "your auth token"
client = Client(account_sid, auth_token)
def send_whatsapp(email_from,email_subject):
#    client = Client()

    message = client.messages.create(
        to="whatsapp:+91xxxxxxxxxx",#your phone number 
        from_="whatsapp:+1xxxxxxxxx",# twilio number
        body=email_from+email_subject)

    print(message.sid)
# import csv
done_mails=[]
while True:
    count = ''
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')	
        mail.login('email_address', 'password')
        mail.select("inbox",True) # connect to inbox.
        return_code, data = mail.search(None, 'UnSeen') #selects only unseen
        mail_ids = data[0].decode()
        count = len(mail_ids[0].split(" "))
        id_list = mail_ids.split()
        for i in id_list:
            if i not in done_mails:
                typ, data = mail.fetch(str(i),'(RFC822)')
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1].decode("utf-8"))
                        email_subject = msg['subject']
                        email_from = msg['from']
                        done_mails.append(i)
                        print(email_from,email_subject)
                        send_whatsapp(email_from,email_subject)      
    except Exception as e: print(e)