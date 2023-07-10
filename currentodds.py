#get request to theoddsapi for whichever sport we want.
#current odds for all games

#store these odds in a dataframe.
#run the get every hour

import requests
import time

# Define the API endpoint and other necessary parameters
API_URL = "https://api.example.com/odds"

last_odds = None

def get_current_odds():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch odds data.")
        return None

def send_signal():
    # Replace this with your own signaling mechanism
    print("Odds have changed! Sending signal to user...")

while True:
    current_odds = get_current_odds()


    '''
    parse the json to get the odds for the games
    store said odds into a dictionary. key is the teams. value is the ML odds for both sides
    '''
    
    if current_odds is not None:
        if last_odds is not None and current_odds != last_odds: #bare bones comparison. should go thru entire dict and find which games had a change
            send_signal()
        
        last_odds = current_odds
    
    time.sleep(3600)  # Sleep for 1 hour before making the next request

