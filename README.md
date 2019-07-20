# diet-tracker

A calorie counting CRUD web application built with Python & Django.

## Demo
Click [here](http://diet-tracker.herokuapp.com "here") for a demo link

## Usage
Once you have cloned the repo, create a virtualenv and install the requirements by entering ```pip install -r requirements.txt```

Then, make the migrations for the Django DB
```python manage.py makemigrations```
```python manage.py migrate```

Finally, run the server
```python manage.py runserver```

The application will be running on http://127.0.0.1:8000

## TODO
- [ ] Add documentation
- [ ] Improve UI
- [ ] Speed up the Pytesseract OCR nutrition label reading

## License
MIT
