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
    # make sure selenium webdriver is in it's correct path(eg. for Ubuntu in `usr/local/bin`)
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py runserver
    
## Contributions Best Practices

### Commits

-   Write clear meaningful git commit messages (Do read [https://chris.beams.io/posts/git-commit/](https://chris.beams.io/posts/git-commit/))
-   Make sure your PR's description contains Gitlab's special keyword references that automatically close the related issue when the PR is merged. 
-   When you make very minor changes to a PR of yours (like for example fixing a failing Travis build or some small style corrections or minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at [https://davidwalsh.name/squash-commits-git](https://davidwalsh.name/squash-commits-git) )
-   When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.

### Feature Requests and Bug Reports

When you file a feature request or when you are submitting a bug report to the [issue tracker](https://gitlab.com/aossie/aossie-scholar/issues), make sure you add steps to reproduce it. Especially if that bug is some weird/rare one.

### Join the development

-   Commit on the `develop` branch that  is currently in development and `master` branch is in production.
-   Before you join development, please set up the project on your local machine, run it and go through the application completely. Press on any button you can find and see where it leads to. Explore. (Don't worry ... Nothing will happen to the app or to you due to the exploring :wink: Only thing that will happen is, you'll be more familiar with what is where and might even get some cool ideas on how to improve various aspects of the app.)
-   If you would like to work on an issue, drop in a comment at the issue. If it is already assigned to someone, but there is no sign of any work being done, please feel free to drop in a comment so that the issue can be assigned to you if the previous assignee has dropped it entirely.


    
   Now, you should be able to see the app running on your local server here -http://127.0.0.1:8000/metrics/
   You can now use any profile url from google scholar website like this -https://scholar.google.com/citations?hl=en&user=m8dFEawAAAAJ , to fill in the form.
   
   ## Communication
[chat channel](https://gitter.im/AOSSIE/AossieScholar) to get in touch with the developers.
