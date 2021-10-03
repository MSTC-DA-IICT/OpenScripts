## Send Batch Emails

### In order to run this script
1. [Download python IDLE](https://www.python.org/downloads/)
2. Install decouple package by running `pip install python-decouple` in terminal. This package is used to support environment variables

### Scripts description
There are two version of scripts
1) Use `send_batch_email_interactive.py` for using the script from terminal. Just run the script from terminal and enter the details as script ask to do.
2) Use `send_batch_email_function.py` for integreating these utility in projects. Import these script and use `send_batch_emails` function to send the emails. <br/>
   Inputs to function: <br/>
   i. First input is the Subject of the mails. <br/>
   ii. Second input is the full path of excel file which contains the Email IDs of recipients.<br/>
   iii. Third input is the column number of excel file which contains the Email IDs.<br/>
   iv. Forth input is the message, which requires the full path of html file.<br/>
   
### How to use scripts 
Download the script which you want to use and add it to the relevent folder. Now, in order to provide the sender's login credentials download `.env.example` and rename it to `.env` and then put your email address and password to EMAIL_ADDRESS and EMAIL_PASSWORD respectively.
Note: For project purpose, you can make another file `.env` rather than renaming `.env.example` and don't forget to include `.env` in `.gitignore` file of your project. 
