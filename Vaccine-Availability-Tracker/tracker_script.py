import requests
from datetime import date,datetime, timedelta
import os
from time import time,ctime
import sys

class Vaccine_Availability_Tracker:

    def api_Call(self, pin, v_name, date_):
      '''
        This script uses "Appointment Availability API" povided by API Setu.
      '''

      url =  "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pin+"&date="+date_
      response_page = requests.get(url, {"accept": "application/json" , "Accept-Language": "hi_IN"})

      if response_page.status_code == 200:
        print("\nYour request has been successfully submitted. \n\n")
        response_json = response_page.json()
        sessions = response_json['sessions']
        data = []
        center_id = []
        for session in sessions:
          if session['available_capacity'] >= 0:
            res = { 'name': session['name'], 'address':session['address'], \
            'available_capacity':session['available_capacity'], 'fee':session['fee'] , \
            'vaccine':session['vaccine'],'slots':session['slots'] }
            if ( res['vaccine']== v_name and (session['center_id'] not in center_id)):
              data.append(res)
              center_id.append(session['center_id'])

        return data


if __name__ == '__main__':

  #class object
  tracker_obj = Vaccine_Availability_Tracker()

  #Take input
  pin = input("Enter pin: ")
  print("Which Vaccine you want? 1. COVISHIELD 2. COVAXIN : ")
  v_name = int(input("Type 1 or 2: "))
  if(v_name == 1): vname = "COVISHIELD"
  else: vname = "COVAXIN"
  d_num = int(input("What is dose number? "))
  if(d_num>2):
    print("Sorry you are not allowed")
    sys.exit("Sorry, more than 2 doses are not allowed")
  date = input("Enter Date DD-MM-YYYY: ")

  #api call
  data = tracker_obj.api_Call(pin, vname, date)


  if(data == None or len(data) == 0):
    sys.exit("Sorry data is not available")

  for i in data:
    multiline_string = (f"Center Name : {i['name']}\n"
                        f"Address : {i['address']}\n"
                        f"Dose quantity available : {i['available_capacity']}\n"
                        f"Fee : {i['fee']}")
    print(multiline_string)
    print("Slots :", end =" ")
    slots = i['slots']
    for slot in slots:
        print(slot, end ="  ")
    print("\n-----------------------------------------------------\n")
