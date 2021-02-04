from flask import Flask, render_template
import os
import requests
import random
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)      # Initialize Flask

@app.route('/')
def main():
    
    NUM_SONGS = 5
    
    load_dotenv(find_dotenv())                            # Load API KEYS from .env
        
    AUTH_URL = "https://accounts.spotify.com/api/token"   
    
    
    # Send spotify request of auth token using our ID and Secret Key
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SPOTIFY_ID'),
        'client_secret': os.getenv('SPOTIFY_SECRET'),
    })
    
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']     # Access Token returned by Spotify
    
    # Place token in header
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'
    
    # Query for new releases
    response = requests.get(BASE_URL, 
            headers=headers,
            params={'country': 'US', 'limit' : 20}
            )
    
    data = response.json()
    
    song_names = [] 
    artist_names = []
    song_pic = []
    song_url = []
    
    # Random index for random artist on every load
    rand = random.sample(range(20), NUM_SONGS)
    
    # Sort through JSON and to song info lists
    for i in rand:
        
        stuff = data['albums']['items'][i]['name']
        song_names.append(stuff)
        
        stuff = data['albums']['items'][i]['artists'][0]['name']
        artist_names.append(stuff)
        
        stuff = data['albums']['items'][i]['images'][0]['url']
        song_pic.append(stuff)
        
        stuff = data['albums']['items'][i]['external_urls']['spotify']
        song_url.append(stuff)
        
    
    
    print(song_names)
    print(artist_names)
    print(song_pic)
    print(song_url)
    
    # Pass song data to index.HTML
    return render_template(
        "index.html",
        NUM_SONGS = NUM_SONGS,
        song_names = song_names,
        artist_names = artist_names,
        song_pic = song_pic,
        song_url = song_url
    )


# Instruct Flask which port and IP to run on
app.run(
    port=int(os.getenv('PORT', 8080)), 
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
