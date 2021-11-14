# CV Builder

## About
This repository contains the source code for the online app 'CV Builder' (preliminary name), an app which lets you build your resume/CV by filling easy-to-use forms (an online wizard). The app will then automatically generate a .pdf file or .html file (that offers more printing options). Along the process, the user is offered multiple templates and multiple customizations are allowed.

## Code collaboration
The app is written using 'Django' web framework and 'Bootstrap' CSS framework. 
Steps to run the code on your machine:
1. Create a Python virtual environment, activate it and install django. You can follow the steps from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)
2. Clone the repository `git clone https://github.com/ahmdhjj92/cv-builder.git`
3. Install project requirements (python packages) inside the virtual environment from *requirements.txt*: `pip3 install -r requirements.txt`
[Learn more about installing packages](https://packaging.python.org/tutorials/installing-packages/)
3. cd to the directory where *manage.py* exits: `cd cv_builder/`
4. Create the database: `python3 manage.py makemigrations` then `python3 manage.py migrate`.
You'll need to run these commands every 
time you create a new model, or modify an existing model. 
6. Create a superuser (a user account that has access to all aspects of the 
project): `python3 manage.py createsuperuser`
7. Run the server `python3 manage.py runserver`
8. After issuing the command above, you can view the project at 
http://localhost:8000/. View the admin site at 
http://localhost:8000/admin/.

## Some useful resources
1. [Django Beginner's Cheat Sheet](https://edu.anarcho-copy.org/Programming%20Languages/Python/Python%20CheatSheet/beginners_python_cheat_sheet_pcc_django.pdf)
2. [Django documentation](https://docs.djangoproject.com/en/3.2/)
3. [Django Web Framework (Python) - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
4. [Bootstrap documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
