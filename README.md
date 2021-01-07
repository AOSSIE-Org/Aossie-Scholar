# Aossie Scholar
A Google Chrome extension which calculates performance-based metrics for researchers from Google Scholar profile.

## Install from Chrome Web Store
[<img src="https://lh3.googleusercontent.com/ZECqdgjuGeSzU46fRFWyzt8cfBIG-hjSSh25oWRDluLcwEUsxN2wc8WULkSxAfjrXoGzl8nhpIifCqNmBsTcGu94fg=w640-h400-e365-rj-sc0x00ffffff">](https://chrome.google.com/webstore/detail/scholar/bgoiffehmhngmehlbmcepkfikalopkgo?hl=en-GB)


### Prerequisites

* `node: v8.10.0`
* `npm: v6.14.41`
* `Postgres`

## Installing on Local Machine

* Fork to get your own copy of the project 
* Clone the repo
* `cd aossie-scholar/`
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

#### Testing
* For unit testing, run `npm run unit-test`
* For e2e testing, run `npm run ee-test`
* For all testing, run `npm test`

#### Code linting and formatting
Aossie Scholar uses **Prettier + Eslint** for code listing and formatting. To check if your code follows the guidelines, run `npm run prettier`

**Note :** The project uses **Husky**, a pre-commit GIT hook which checks if the code follows linting guidelines before commiting. This helps prevent unwanted linting errors in the pipelines.

## Contributing

Please read [CONTRIBUTING.md](https://gitlab.com/aossie/aossie-scholar/-/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](https://gitlab.com/adityabisoi/aossie-scholar/-/blob/master/LICENSE) file for details

## Support

Join our [Gitter](https://gitter.im/AOSSIE/AossieScholar) to talk to developers of this project.
