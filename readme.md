# On-screen logging with Flask

Repository containing code to add on-screen logging for a Flask application. It is as simple as a `app.py` that contains the flask application and some custom `HTML` and `CSS` files. The config file in the `.ebextensions` folder is only necessary as the app is deployed on `AWS Elasic Beanstalk` to configure the nginx server (more specifically to prevent proxy buffering).

For a detailed description on how to set it up, see https://towardsdatascience.com/how-to-add-on-screen-logging-to-your-flask-application-and-deploy-it-on-aws-elastic-beanstalk-aa55907730f


### Folder structure

    ├── app
    |    └── static
    |       ├── assets
    |       ├── css
    |       |   └── custom.css
    |       └── index.html
    └── app.py
