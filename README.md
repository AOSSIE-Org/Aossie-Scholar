# Aossie-Scholar

Aossie scholar is a metric computation system for researchers with a Google Scholar profile. Google Scholar provides researchers with stats such as the number of publications, citations, h-index and i10 index. But, these metrics are flawed. Aossie Scholar extracts some basic information form Google Scholar and computes better metrics, and displays them on another website. So, researchers can now see better, effective metrics with a single click.

## Requirements

Aossie Scholar requires Django 2.2.x, which and more dependencies are installed by ```requirements.txt```.

Postgres as a database server is required. For downloading and documentation, visit https://www.postgresql.org/


### Installation
 
* #### setting up postgres - 
* Dependencies required to run Server
    * Python 3.7
    * Postgres
    ### For mac users
        ```sh
        brew install postgresql
        ````
    ### For debian-based linux users
        ```sh
        sudo apt-get update
        sudo apt-get install postgresql postgresql-contrib libssl-dev
        ```
        Also, Linux users need to install some dependencies for PostgreSQL to work with Python.
        ```
        sudo apt-get install libpq-dev python3-dev
        ```
    * **Next Step ** - Create the database. For that we first open the psql shell. Go to the directory where your postgres file is stored.
    
        ```sh
        # For linux users
        sudo -u postgres psql
        
        # For macOS users
        psql -d postgres
        ```
    
    * When inside psql, create a user for project and then using the user create the database. 
    
        ```sql
        CREATE USER aossie WITH PASSWORD 'aossie';
        CREATE DATABASE aossie WITH OWNER aossie;
        
        ```
    * Now, all we need to do is give our database user access rights to the database we created:
        ```
        GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
        ```
    * Go to Settings.py and change accordingly - 
        ```
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'aossie-scholar',
            'USER': 'aossie',
            'PASSWORD': 'aossie',
            'HOST': 'localhost',
            'PORT': '',
                }
            }
        ```
    
    * Once the databases are created, exit the psql shell with `\q` followed by ENTER.
    
    * ###follow this blog if you have any doubts remaining - 
    * https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04   
*  ## Using pipenv
    
    Using pipenv, you will not need to set up virtualenv. It will do it automatically for you
    
    To setup a virtual environment and install the dependices, enter in a terminal
    
    ```sh
    pipenv --python 3.7.3 install
    ```
    
    Now to activate the virtual environemnt, type
    
    ```sh
    pipenv shell
        

* git remote add origin https://gitlab.com/aossie/aossie-scholar.git
* cd aossie-scholar
* 
* git pull origin master
* pip install -r requirements.txt
* Enter your Postgresql credentials in ```settings.py```
* Make sure selenium webdriver is in correct path(eg. for Ubuntu in `usr/local/bin`)
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

## Running
After running the server, point your browser to http://127.0.0.1:8000/metrics/ .To register, enter your Google Scholar profile URL(such as https://scholar.google.com/citations?hl=en&user=m8dFEawAAAAJ) and click ```Register```. You will be directed to the profiles page showing better stats. You can click on individual metrics for details. To search for an already registered scholar, simply search his/her name in the search bar.

## Contributing

Please read [CONTRIBUTING.md](https://gitlab.com/aossie/aossie-scholar/-/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](https://gitlab.com/adityabisoi/aossie-scholar/-/blob/master/LICENSE) file for details

## Support

If you would like to talk to other Aossie Scholar users and developers, visit our [Gitter channel](https://gitter.im/AOSSIE/AossieScholar)
