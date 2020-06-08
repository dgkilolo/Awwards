## Awwards
- Awwards is a python web application that has been made with Django.
- Awwards is meant to help users add their projects to be reviewed by other users.
- Users can view the posted applications when they view the homepage, they are however required to sign in in order to add their own applications as well as editing their profile page.

### Required Features
- View posted projects on homepage.
- Sign in to the application to upload my own projects.
- Upload my project to the application.
- See my profile with all mt projects.

### Additional Features
- Search for projects by their title name.

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

## Technologies & Languages

- Django 3.0.6
- Python 3.6.9
- Html
- Css
- Bootstrap4

# Installation and Setup

Clone the repository below

```
git clone https://github.com/dgkilolo/Awwards
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   |        /auth/signup             | sign up a user                        | users         |
| POST   |        /accounts/login          | log in  a user                        | users         |
| POST   |        /accounts/logout         | logout a user                         | users         |
| GET    |        /search                  | search projects using title name      | users         |
| POST   |        /profile/edit            | edit profile, and picture and bio     | users         |
| POST   |        /new/project             | and new project instance              | users         |

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
Copyright{ 2020 }