# diet-tracker

A calorie counting CRUD web application built with Python & Django. It aims to make calorie calculations and macronutrient tracking less stressful.
![add food to inventory via ocr](https://user-images.githubusercontent.com/46038298/50744888-94540880-11ec-11e9-88bb-17522a068ecc.gif)

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
- [ ] Update the UI
- [ ] Speed up the Pytesseract OCR feature

## License
MIT
