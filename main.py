import requests
import datetime

nutrix_ID = YOUR NUTRIX ID HERE
APP_APIKEY = PUT YOUR NUTRIXTIONIX API KEY HERE
nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

#  The headers for the api call
headers = {
    "x-app-id": nutrix_ID,
    "x-app-key": APP_APIKEY,
}
# get user exercise
exercise_text = input("what exercise did u make? : ")
# params for the api call
nutrix_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 178.64,
    "age": 24
}
# API CALL
exercise= requests.post(nutrix_endpoint, json=nutrix_params, headers=headers)
exercise.raise_for_status()
data = exercise.json()
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

# GETTING THE RESPONSE FROM THE NUTRITIONX API AND PUTTING IT IN A DICT to send it to the microsoft sheet
for result in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"]
        }
    }

    sheet_response = requests.post(nutrix_endpoint, json=sheet_inputs)

    print(sheet_response.text)
