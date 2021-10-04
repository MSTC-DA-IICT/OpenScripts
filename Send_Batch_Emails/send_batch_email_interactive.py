import smtplib

from decouple import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import re

# Login credentiales of sender (You can directly put your email address and password here, if you are not going to publish it publically)
EMAIL_ADDRESS = config('EMAIL_ADDRESS')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')


# take the inputs as interactive input
email_subject = input('Enter the subject of the mail ...\n')

recipient_list_file_path = input('Enter the full path of spreadsheet along with file name and extension....\n')
mail_col = int(input('Which Column (staring with 0) contains the email IDs\n'))

html_file_path = input('Enter the full path of HTML file along with file name and extension...\n')


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
    for email in df.iloc[:,mail_col]:
        if(re.search(email_regex, email)):      
            msg['To'] = email    
            smtp.sendmail(EMAIL_ADDRESS, email, msg.as_string())

    smtp.quit()

print('mail sent successfully\n')