## Project Example

Copy of this project are located on [Heroku](https://flight-data-project.herokuapp.com/).

---

## Dataset

In this project data for database based on this [dataset](https://www.kaggle.com/datasets/usdot/flight-delays).


---

## Instructions

---

### Configuration:

##### [config.py](config.py)

    username - Username to use for connection to database
    password - Password to use for connection to database
    database - Name of database to connect
    host - Host of database to connect
    port - Port of database to connect

    Config - Class with hyperparameters for application
    DevelopmentConfig - Class derived from Config. Hyperparameters for Development mode
    ProductionConfig - Class derived from Config. Hyperparameters for Production mode

---

### Deploy the application:


1. Download/unpack project into desire folder.


2. Check if ProductionConfig are used in [app.py](app.py)


2. Open console in the same folder as project.  


3. Make sure that Python 3.7+ was installed.


4. Make sure that Git was installed and log in.


5. Make sure that Heroku CLI was installed and log in.


6. Create app on heroku with following command:

       heroku create flight-data-project

7. Create postgres database on heroku with following command:

       heroku addons:create heroku-postgresql:hobby-dev --app flight-data-project

8. Deploy project with following commands:

       git init
       heroku git:clone -a flight-data-project
       git add . 
       git commit -m "Initial commit"
       git push heroku master

---