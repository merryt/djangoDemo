This is a sample financial blog/podcasting site. 

##The fastest way to get it up and running is 
`python3 manage.py start` -- this will activate a virtual env, install requirements, and then start the server.



## About the file structure
 - blogproject is the project
 - djangoDemo is the virtual env files
 - html is from support files (I might be removing as I go)
 - newsapp is the application
 
 ## TODO:
 - Individual pages for reach article type (10 promise series etc)
 - Podcast
 - Individual stock pages
 - Author page




 ----
## Helpful commands 

 To run the virtual environment go to the root of this repo and run `source djangoDemo/bin/activate` 

To install requirements use the command `pip3 install -r requirements.txt`

If its your first time running the application you will need to run the following commands
- `python manage.py migrate` 
- Currently database isn't in use.

To run the server run `python3 manage.py runserver`

If you add any packages via the pip command, use `pip3 freeze > requirements.txt` afterwards to make sure the requirements file is up to date.
