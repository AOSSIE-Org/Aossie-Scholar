# Aossie Scholar
A Google Chrome extension which calculates performance-based metrics for researchers from Google Scholar profile.

### Prerequisites

Minimum Node requirements:

`
node: v8.10.0
`
`
npm: v6.14.4
`
Postgres - see the download instructions [here](https://www.postgresql.org/download/)

## Installing

* Fork to get your own copy of the project 
* Clone the repo
* `cd aossie-scholar/`
##### Fire up the server 
* `pip install -r requirements.txt`
* Enter your database credentials in `settings.py`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py runserver`
#### Build and load the extension
* `npm install`
* Run `gulp` for workflow automation. Any changes made in the `src/` folder will be automatically reflected in a `dist/` folder
* In Google Chrome, go to Extensions>Enable Developer Mode(On top-right)>Click on Load Unpacked(On top-left)>Browse to the project directory>Select `dist/`
* Visit your Google Scholar profile to register

## Contributing

Please read [CONTRIBUTING.md](https://gitlab.com/aossie/aossie-scholar/-/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](https://gitlab.com/adityabisoi/aossie-scholar/-/blob/master/LICENSE) file for details

## Support

Join our [Gitter](https://gitter.im/AOSSIE/AossieScholar) to talk to developers of this project.