
# Aossie-Scholar

The project is related to Google Scholar profiles and metrics. Many researchers have a Google Scholar profile. 
It is used by people to see how many papers a researcher has written, how many citations they have received, their h-index, i10-index... 
But these metrics are flawed. The goal of the project would be to extract information from Google Scholar and compute better metrics about a researcher's performance.
And then display this information and metrics with more fairer stats in another website.

# How the app works currently ?
    Currently the homepage of Aossie Scholar has two options to either search for an already registered Scholar or to register (or see metrics for) a Google Scholar.
    To register a scholar, it is must that s/he owns a Google Scholar profile because it is from there Aossie Scholar scraps the data required for calculating other new metrics.
    So the home page contains a registeration form which is to be filled with a Scholar's Google Scholar profile URL. Once you do that, s/he is registered on Aossie Scholar and 
    you will be directed to his/her profile where you can see all his publications and other metrics.
    There is also a metric page which defines the metrics.


# Setting up the database

This project runs on postgresql database. For downloading and documentation, please go to https://www.postgresql.org/ .

## To run the app locally,
    # git remote add origin https://gitlab.com/aossie/aossie-scholar.git
    # git pull origin master
    # pip install -r requirements.txt
    # Enter your Postgresql credentials in ```settings.py```
    # python manage.py runserver
    
   Now, you should be able to see the app running on your local server here -http://127.0.0.1:8000/metrics/
   You can now use any profile url from google scholar website like this -https://scholar.google.com/citations?hl=en&user=m8dFEawAAAAJ , to fill in the form.
