from selenium import webdriver
import time
import schedule

driver = ""
Firefox_driver_dir = r'geckodriver.exe'
Firefox_profile_dir = r'ROOT DIR'


def setup_schedule():
    # time should be in HH:MM 24 hours formate
    scheduleMeeting("tuesday", "21:54", "21:55",
                    "meet link 1")
    scheduleMeeting("tuesday", "21:43", "21:42",
                    "meet link 2")


def scheduleMeeting(day, startHour, endHour, link):
    if str(day).lower() == "monday":
        schedule.every().monday.at(startHour).do(join_meet, link)
        schedule.every().monday.at(endHour).do(leave_meet)
    elif str(day).lower() == "tuesday":
        schedule.every().tuesday.at(startHour).do(join_meet, link)
        schedule.every().tuesday.at(endHour).do(leave_meet)
    elif str(day).lower() == "wednesday":
        schedule.every().wednesday.at(startHour).do(join_meet, link)
        schedule.every().wednesday.at(endHour).do(leave_meet)
    elif str(day).lower() == "thursday":
        schedule.every().thursday.at(startHour).do(join_meet, link)
        schedule.every().thursday.at(endHour).do(leave_meet)
    elif str(day).lower() == "friday":
        schedule.every().friday.at(startHour).do(join_meet, link)
        schedule.every().friday.at(endHour).do(leave_meet)
    elif str(day).lower() == "saturday":
        schedule.every().saturday.at(startHour).do(join_meet, link)
        schedule.every().saturday.at(endHour).do(leave_meet)
    elif str(day).lower() == "sunday":
        schedule.every().sunday.at(startHour).do(join_meet, link)
        schedule.every().sunday.at(endHour).do(leave_meet)
    elif str(day).lower() == "today":
        schedule.every().day.at(startHour).do(join_meet, link)
        schedule.every().day.at(endHour).do(leave_meet)


def initFirefox():
    global driver

    options = webdriver.FirefoxOptions()
    options.set_preference("permissions.default.microphone", 1)
    options.set_preference("permissions.default.camera", 1)
    driver = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(
        Firefox_profile_dir), executable_path=Firefox_driver_dir, options=options)


def join_meet(link):
    driver.get(link)
    driver.implicitly_wait(30000)
    time.sleep(4)

    # click mic button
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[9]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]").click()
    driver.implicitly_wait(30000)
    time.sleep(3)

    # click video button
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[9]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]").click()
    driver.implicitly_wait(30000)
    time.sleep(3)

    # click join button
    driver.find_element_by_xpath(
        '/html[1]/body[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[9]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]').click()


def leave_meet():
    # change link to leave meeting
    driver.get("https://www.google.com/")


if __name__ == "__main__":
    initFirefox()
    setup_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)
