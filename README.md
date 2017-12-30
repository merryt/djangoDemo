To run the virtual environment go to the root of this repo and run `source djangoDemo/bin/activate` 

To install requirements use the command `pip3 install -r requirements.txt`

If its your first time running the application you will need to run the following commands
- `python manage.py migrate` 
- do we even need a database for now?

To run the server run `python3 manage.py runserver`

If you add any packages via the pip command, use `pip3 freeze > requirements.txt` afterwards to make sure the requirements file is up to date.


About the file structure
 - blogproject is the project
 - djangoDemo is the virtual env files
 - html is from support files (I might be removing as I go)
 - newsapp is the application
 