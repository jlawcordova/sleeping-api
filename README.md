Sleeping API
============

Content
- [Setup](#setup)

`Sleeping API` is a base project for creating RESTful API applications with
Flask. This application makes use of `Flask`, `Flask-RESTful`,
`Flask-Mongoengine` and `Flask-Marshmallow` to quickly create RESTful APIs.

Setup
-----
1. Change the information in `setup.py`.

   Normally, the `name`, `version`, `description`, `url`, `author`, `author`,
   `email`, `license`, `long description` would be edited to fit the actual
   information of the application. `install_requires` should be modified if
   additional packages are needed.

2. Rename the `sleepingapi` module to use the name of the actual application.