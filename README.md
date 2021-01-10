### ChatBot

### Build and run the app locally
To run the Django app on your local computer, you'll need to set up a Python development environment, including Python, pip, and virtualenv. For instructions, refer to Setting Up a Python Development Environment for Google Cloud Platform.

Create an isolated Python environment, and install dependencies:
```js
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
Run the Django migrations to set up your models:
```js
python3 manage.py makemigrations
python3 manage.py migrate
```
Start a local web server:
```js
python3 manage.py runserver
```
In your web browser, enter this address:

http://localhost:8000/
You should see a simple webpage with the text: "Dialogflow" a text box and **submit** button. 
The sample app pages are delivered by the Django web server running on your computer. When you're ready to move forward, press Ctrl+C to stop the local web server.

### Use the Django admin console
Create a superuser:
```js
python3 manage.py createsuperuser
```
Start a local web server:
```js
python3 manage.py runserver
```
Enter this address in your web browser. To log on to the admin site, use the username and password you created when you ran createsuperuser.

http://localhost:8000/admin/


