from flask import Flask, render_template
import os
import requests
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)      # Initialize Flask

@app.route('/')
def main():
    
    load_dotenv(find_dotenv())                            # Load API KEYS from .env
        
    AUTH_URL = "https://accounts.spotify.com/api/token"   # Spotify URL for authentication token
    
    
    # Send spotify request of auth token using our ID and Secret Key
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SPOTIFY_ID'),
        'client_secret': os.getenv('SPOTIFY_SECRET'),
    })
    
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']     # Access Token returned by Spotify
    
    # Place token header
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    # Spotify URL for new releases API
    BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'
    
    # Query for 10 new releases
    response = requests.get(BASE_URL + '?country=US' + '&' + 'limit=10', headers=headers)
    
    # Data from query
    data = response.json()
    
    song_names = [] # Empty list for songs
    
    # Sort through JSON
    for i in range (0,10):
        print(data['albums']['items'][i]['name'])
    
    
    
    return render_template(
        "index.html"
        
    )





app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
