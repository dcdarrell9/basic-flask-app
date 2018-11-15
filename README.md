# basic-flask-app
Basic Flask app with health and info blueprint endpoints

# Running in docker
- Git clone this app

- Set a PROJECTS_HOME env pointing to the directory where this app was cloned

- cd into basic-flask-app

- Run `make update`

- Run `make build`

- Run `make start`

- 2 Docker containers running on `localhost:8000` and `localhost:8080`

- Try hit `localhost:8080/health/basic-sanic-app/8000` which should return the status of that app

# Running locally
- The above endpoint won't work when running locally as the docker containers wouldn't be on the same network.
- By running this locally (terminal/pycharm etc) you can hit the `localhost:8080/health/images` endpoint which gets a response from the docker api to return a json response of all images on your machine that contain 'basic-flask-app_' (can be changed to anything or removed and display all local images)

