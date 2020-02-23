# Aossie-Scholar

Aossie scholar is a metric computation system for researchers with a Google Scholar profile. Google Scholar provides researchers with stats such as the number of publications, citations, h-index and i10 index. But, these metrics are flawed. Aossie Scholar extracts some basic information form Google Scholar and computes better metrics, and displays them on another website. So, researchers can now see better, effective metrics with a single click.

## Requirements

Aossie Scholar requires Django 2.2.x, which and more dependencies are installed by ```requirements.txt```.

Postgres as a database server is required. For downloading and documentation, visit https://www.postgresql.org/


### Installation
 
* git remote add origin https://gitlab.com/aossie/aossie-scholar.git
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

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](https://gitlab.com/adityabisoi/aossie-scholar/-/blob/master/LICENSE) file for details

## Support

If you would like to talk to other Aossie Scholar users and developers, visit our [Gitter channel](https://gitter.im/AOSSIE/AossieScholar)
