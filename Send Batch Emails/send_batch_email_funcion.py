
from email import message
import smtplib

from decouple import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import re

# Login credentiales of sender (You can directly put your email address and password here, if you are not going to publish it publically)
EMAIL_ADDRESS = config('EMAIL_ADDRESS')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')

# Utility function which sen the batch mails to the 
# email_subject - subject of the email
# receipent_list_file_path - file path for receipents' list
# mail_col_in_excel - which column contains the email IDs
# html_file_path - the message which sender wants to send
def send_batch_emails(email_subject, recipient_list_file_path, mail_col_in_excel, html_file_path):
    #converting foward slashing file path to backward slashing file path 
    for c in html_file_path:
        if c == '\\':
            c = '/'
    for c in recipient_list_file_path:
        if c == '\\':
            c = '/'


    # setting up the Email message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = EMAIL_ADDRESS

    with open(html_file_path, 'rt') as f:
        file_data = f.read()
        part = MIMEText(file_data, 'html')
        msg.attach(part)


    # load data in excel file using pandas
    df = pd.read_excel (recipient_list_file_path)

    # regular expression for email for validation
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # Make connection and
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)    

        # Send email to all email in the excel file (which is loaded in df)
        for email in df.iloc[:,mail_col_in_excel]:
            if(re.search(email_regex, email)):      
                msg['To'] = email    
                smtp.sendmail(EMAIL_ADDRESS, email, msg.as_string())

        smtp.quit()
