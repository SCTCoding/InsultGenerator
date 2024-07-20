# InsultGenerator
Just a stupid little insult generator.

### Notice: Delivered as is.
Have fun with this. I would not suggest putting this on the internet as is. 

# Usage
1. `git clone` this repository
2. cd into the InsultGenerator folder
3. Build the container with: `sudo docker build -t insultgenerator .`
4. Run the container with: `sudo docker run -p 8080:5000 StupidInsultGenerator`

You may have issues with the build if you aren't signed into Docker. You can sign in or you can simply pull the base image with: `docker pull python:3.9-slim`

# Heroku
You can easily spin this up in Heroku if desired since this is just an extremely basic Flask app. In the current state the app is not desinged to be exposed to the internet so keep that in mind if you decide to.
