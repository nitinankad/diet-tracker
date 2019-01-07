# diet-tracker

A calorie counting CRUD web application built with Python & Django. It aims to make calorie calculations and macronutrient tracking less stressful.
![screenshot](https://user-images.githubusercontent.com/46038298/50744893-94ec9f00-11ec-11e9-9c8e-19cf37301dc0.png)

## Demo
Click [here](http://diet-tracker.herokuapp.com "here") for a demo link

## Features
* Create a new diet
![create diet](https://user-images.githubusercontent.com/46038298/50744892-94ec9f00-11ec-11e9-8bf2-c0691dc659f6.gif)

* Add food to the food inventory
![add food to inventory](https://user-images.githubusercontent.com/46038298/50744889-94540880-11ec-11e9-8a03-ad01405ebf45.gif)

* Or add food to inventory by entering a direct image link to a nutrition label
![add food to inventory via ocr](https://user-images.githubusercontent.com/46038298/50744888-94540880-11ec-11e9-88bb-17522a068ecc.gif)
 Note: This feature is still in development, it is a bit buggy and slow but the PoC works.

* And finally, add meals & foods to the diet
![add meals and food to diet](https://user-images.githubusercontent.com/46038298/50744890-94540880-11ec-11e9-9323-90044ca4b891.gif)

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
