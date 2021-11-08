# secret-santa

This Python program will take a .json file as input, containing names and emails, and randomly assigns another person on that list to you! In this context, this will be used for a secret santa event for my friend group!

## Dependencies
 - Python 3.8
 - Pipenv: https://pypi.org/project/pipenv/

## Installation
1. Edit the `.env` file to the following:
```
  BASE_EMAIL: The gmail account that you want to send emails through.
  BASE_EMAIL_PASSWORD: The gmail account's password that you want to send emails through.
  FILE_NAME: The .json file's name.
```
2. Edit the `.json` file using the following as an example:
```
{
	"Coltin": "email@gmail.com",
	"Sushi": "email@gmail.com",
	"Patrick": "email@gmail.com",
	"Mac": "email@gmail.com",
	"Riley": "email@gmail.com",
	"Erica": "email@gmail.com",
	"Liz": "email@gmail.com"
}
```

3. Run `pipenv install` in your project directory in your terminal to install all project packages.

## Usage
1. Run `pipenv shell` to run a virtual environment with all dependencies installed.
2. Run `python santa.py` to run Secret Santa!
