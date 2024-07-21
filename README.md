# InsultGenerator
Just a stupid little insult generator.

### Notice: Delivered as is.
Have fun with this. I would not suggest putting this on the internet as is. 

# Usage
1. `git clone` this repository
2. cd into the InsultGenerator folder
3. Build the container with: `sudo docker build -t insultgenerator .`
4. Run the container with: `sudo docker run -p 8080:5000 StupidInsultGenerator`

# app_alt.py
This is a different version of the insult generator. This has a different word list. It uses a noun adjective method rather than a three column approach. To use it either rename the app file in the Dockerfile or just rename app.py and change app_alt.py to app.py.

You may have issues with the build if you aren't signed into Docker. You can sign in or you can simply pull the base image with: `docker pull python:3.9-slim`

# Operation
Refresh the page to get a new insult. Or you can use curl or similar to return the insult as a json respone using the /api endpoint. If you got to /last10 you can get json output of the last 10 insults.

# Heroku
You can easily spin this up in Heroku if desired since this is just an extremely basic Flask app. In the current state the app is not desinged to be exposed to the internet so keep that in mind if you decide to.
