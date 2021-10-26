*   This google meet bot automatically join Google Meet meetings at the specified time, day and link.
*   To use this script you'll have to download FireFox since, in 2021 google driver have so many restrictions for automation so you cannot use google chrome browser for this. 

## Steps to perform before using GmeetBot.py for first time<br>
1. Install all required packages by running `pip install -r requirements.txt` in terminal.
2. Download firefox driver <https://github.com/mozilla/geckodriver/releases>.<br>
3. Keep firefox driver in same directory.
4. Open FireFox and go to *about:profiles*<br>
5. Create a new profile by clicking *Create a New Profile*.
6. Copy the *Root Directory* of newly create profile and assign it to **Firefox_driver_dir** variable.<br>
7. FireFox will automatically make this profile as default after creation, so set the default profile back to what it was before.<br>
8. Now click *Launch profile in new browser* button below our newly created profile. This will open a new FireFox window using your profile. After that you have login for first time.<br>
9. Once you logged in, the profile is ready to be used in this script.<br>
