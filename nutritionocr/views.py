from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from urllib.request import Request, urlopen
import os, re
import pytesseract
from PIL import Image

from meals.models import Food

@login_required
def index(request):
	if request.method == "POST":
		link = request.POST["imglink"]

		req = Request(link)
		req.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5")

		contents = urlopen(req)

		file_name = link.split("/")[-1]

		if not ".png" in file_name and not ".jpg" in file_name and not ".jpeg" in file_name:
			return HttpResponseRedirect("/")

		meta = contents.info()

		file_path = os.path.normpath(os.path.dirname(__file__)) + "\\images\\"+file_name
		if meta["content-type"] in ["image/png", "image/jpeg"]:
			file = open(file_path, "wb")
			file.write(contents.read())
			file.close()

		data = pytesseract.image_to_string(Image.open(file_path))

		macros = dict(re.findall(r"(Total Fat|Saturated Fat|Trans Fat|Carbohydrate|Sugars|Calories|Cholesterol|Sodium|Dietary Fiber|Protein):? (\d+)", data))

		ocr_data = Food()

		if "Calories" in macros:
			ocr_data.calories = int(macros["Calories"])

		if "Total Fat" in macros:
			ocr_data.totalfat = int(macros["Total Fat"])

		if "Saturated Fat" in macros:
			ocr_data.saturatedfat = int(macros["Saturated Fat"])

		if "Trans Fat" in macros:
			ocr_data.transfat = int(macros["Trans Fat"])

		if "Carbohydrate" in macros:
			ocr_data.carbs = int(macros["Carbohydrate"])

		if "Dietary Fiber" in macros:
			ocr_data.fiber = int(macros["Dietary Fiber"])

		if "Cholesterol" in macros:
			ocr_data.cholestorol = int(macros["Cholesterol"])

		if "Sodium" in macros:
			ocr_data.sodium = int(macros["Sodium"])

		if "Sugars" in macros:
			ocr_data.sugars = int(macros["Sugars"])

		if "Protein" in macros:
			ocr_data.protein = int(macros["Protein"])

		os.remove(file_path)

		return render(request, "ocr/ocr.html", {"ocr_data": ocr_data, "link": link})

	return HttpResponseRedirect("/")