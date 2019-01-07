from django.db import models

class Food(models.Model):
	food_name = models.CharField(max_length=60, default="")
	user = models.CharField(max_length=60, default="")
	calories = models.IntegerField(default=0)
	totalfat = models.IntegerField(default=0)
	saturatedfat = models.IntegerField(default=0)
	transfat = models.IntegerField(default=0)
	carbs = models.IntegerField(default=0)
	cholestorol = models.IntegerField(default=0)
	sodium = models.IntegerField(default=0)
	fiber = models.IntegerField(default=0)
	sugars = models.IntegerField(default=0)
	protein = models.IntegerField(default=0)

	def __str__(self):
		return self.food_name


# Meal is a collection of foods, ex: breakfast, lunch, dinner
class Meal(models.Model):
	meal_name = models.CharField(max_length=20)
	user = models.CharField(max_length=60, default="")
	foods = models.ManyToManyField(Food)

	def __str__(self):
		return self.meal_name

# Diet consists of a collection of meals, ex: breakfast, lunch, snack, dinner, snack
class Diet(models.Model):
	diet_name = models.CharField(max_length=20)
	user = models.CharField(max_length=60, default="")
	meals = models.ManyToManyField(Meal)

	def __str__(self):
		return self.diet_name
