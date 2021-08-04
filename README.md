# Project 1 - Music Discovery
By: Andre Alvarados

This app calls Spotify's API to query new song releases and output artist info such as song name, artist, and song preview to an HTML page deployed by Heroku.

## Requirements
1. `pip install Flask`
2. `pip install python-dotenv`
3. `pip install requests`

## Copy this repo to your own personal one
1. On https://github.com/new, create a new repository called `Music-Disc` (or the repo name you want)
2. In terminal, clone the repo:`git clone https://github.com/NJIT-CS490-SP21/project1-aa2748.git`
3. `cd` into the repository and you should see all the files now.
4. Then, connect this repo to your personal repo from Step 1: `git remote set-url origin https://www.github.com/[your-username]/Music-Disc` (be sure to change your username and repo name if you used name other than Music-Disc)
5. Run `git push origin main` to push the local repo to remote.

## Setup Spotify Account
1. Sign up at https://www.spotify.com
2. Go to Dashboard at the Spotify Developer website and accept the latest Developer Terms of Service to complete your account setup.
3. Register your app: https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app

## Setup Genius Account
1. Sign up at https://genius.com/
2. Register your application and get your access token here: https://genius.com/api-clients
3. Documentation on using Genius API located here: https://docs.genius.com/#/getting-started-h1

## Setup access token
1. Go to your Spotify Dashboard and clicking on your app will show you a page with your `Client ID` and `Client Secret` keys.
2. Create `.env` file in main directory
3. Add your Client ID with the line: `export SPOTIFY_ID = 'YOUR_KEY'` (replace YOUR_KEY)
4. Add your Client Secret with the line: `export SPOTIFY_SECRET = 'YOUR_SECRET'` (replace YOUR_SECRET)
5. Add your Genius token with the line: `export GENIUS_AUTH = 'YOUR_TOKEN'` (replace YOUR_TOKEN)

## Run Application
1. Run command in terminal `python main.py`
2. Preview web page in browser '/'

## Deploy to Heroku
1. Install Heroku CLI: `npm install -g heroku`. This could take a few minutes. In the meantime...
2. Create a free account on Heroku https://signup.heroku.com/login
3. Create a `requirements.txt` file with all your dependencies (`Flask` w/ a capital F, `requests`, `python-dotenv`)
4. Create a `Procfile` with the command needed to run your app: https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile
5. Add + commit all changed files with git
6. Log in to Heroku: `heroku login -i`
5. Create a Heroku app: `heroku create`
6. Push your code to Heroku: `git push heroku main`
7. Open your app on the INTERNET (it won't work yet): `heroku open`
8. Go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars"
10. Add your Client ID from `.env` with the matching variable name (`SPOTIFY_ID`) and value (your key, without quotation marks!)
11. Add your Client Secret from `.env` with the matching variable name (`SPOTIFY_SECRET`) and value
12. Add Your Genius Authentication key from `.env`with the matching variable name (`GENIUS_AUTH`) and value

## Technical Issues
1. AWS doesn't update the css changes. Add to main `app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0`
2. Some songs in the album API do not have a preview song mp4. When `song_preview == 'none'` have to omit `<audio>`
3. Initially my spotify and genius links were unclickable because the album images were in the foreground. In my html, I had to make sure the album info layer was ontop the image layer by having the album info written after the album image.

## Future Implementation
1. Add html input and javascript to send user input data back to server and api calls to find that artist info.
2. Clean up Album API call(the params are `song_id[0] +','+ song_id[1]`...). Should implement a loop that creates a list variable with all the song_ids.
3. Play full song with maybe youtube video or audio and scrape the genius lyrics page and add that lyric info to a div.
4. Add Spotify and Genius logo images to our static folder and and replace the links with the clickable logos.
5. Add left-right scrolling instead of up down. Maybe by hiding the current div with `display=none` javascript after clicking a right arrow. Research other left-right scrolling methods.
