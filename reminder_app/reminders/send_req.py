import requests

# Define the API endpoint
url = 'http://127.0.0.1:8000/api/create-reminder/'

# Define a list of data (each dictionary represents a reminder)
data_list = [
    {
        "date": "2024-03-15",
        "time": "08:00:00",
        "message": "Don't forget to call mom!",
        "remind_via": "SMS"
    },
    {
        "date": "2024-03-16",
        "time": "09:30:00",
        "message": "Buy groceries for the weekend",
        "remind_via": "Email"
    },
    {
        "date": "2024-03-17",
        "time": "15:00:00",
        "message": "Meeting with the team",
        "remind_via": "SMS"
    },
    {
        "date": "2024-03-18",
        "time": "11:00:00",
        "message": "Submit report to the manager",
        "remind_via": "Email"
    },
    {
        "date": "2024-03-19",
        "time": "10:30:00",
        "message": "Dentist appointment",
        "remind_via": "SMS"
    }
]

# Loop through the list and send a POST request for each set of data
for data in data_list:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    print("-----------------------------")
