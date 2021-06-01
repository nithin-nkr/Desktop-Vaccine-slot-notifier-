import requests
from requests.exceptions import Timeout
from plyer import notification
import time
import datetime


try:
    pincode = 690514
    x = datetime.date.today()
    date = x.strftime("%d-%m-%y")
    url ='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,date)


except:
    print("check your internet connection")

if url != None:
    response = requests.get(url)
    data = response.json()
    


    while True:
        for sessions in data["sessions"]:

            notification.notify(
                title = "Vaccine Status{}",
                message ="Centre :{name}\n Date :{date}\n Age limit :{age_limit}\n Available_capacity :{capacity}".format(
                        name = sessions['name'],
                        date = sessions["date"],
                        age_limit = sessions['min_age_limit'],
                        capacity =sessions['available_capacity']
                        ),
                        app_icon = 'bell.ico',
                        timeout =80
                    )

        time.sleep(60*60)