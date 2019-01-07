from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from meals.models import Diet, Meal, Food
from meals.macros import Macros

@login_required
def add_meal(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        meal_name = request.POST["meal_name"]
        username = request.user.username

        print(request.POST)

        diet = Diet.objects.get(diet_name=diet_name, user=username)

        if diet.meals.filter(meal_name=meal_name).exists():
            messages.error(request, "Meal already exist")
            return HttpResponseRedirect("/")

        diet = Diet.objects.get(diet_name=diet_name, user=username)
        diet.meals.create(meal_name=meal_name, user=username)
        diet.save()

        messages.success(request, "Successfully added " + meal_name)
        return HttpResponseRedirect("/viewdiet/"+diet_name)

@login_required
def delete_meal(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        meal_name = request.POST["meal_name"]
        username = request.user.username

        if not Meal.objects.filter(meal_name=meal_name, user=username).exists():
            messages.error(request, "Meal does not exist")
            return HttpResponseRedirect("/viewdiet/"+diet_name)

        meal = Meal.objects.get(meal_name=meal_name, user=username)
        meal.delete()

        messages.success(request, "Successfully deleted " + meal_name)
        return HttpResponseRedirect("/viewdiet/" + diet_name)

@login_required
def add_food_to_meal(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        meal_name = request.POST["meal_name"]
        food_name = request.POST["food_name"]
        username = request.user.username

        diet = Diet.objects.get(diet_name=diet_name, user=username)
        meal = diet.meals.get(meal_name=meal_name, user=username)
        food = Food.objects.get(food_name=food_name, user=username)

        meal.foods.add(food)
        meal.save()

        messages.success(request, "Successfully added " + food_name + " to " + meal_name)
        return HttpResponseRedirect("/viewdiet/" + diet_name)

@login_required
def delete_food_from_meal(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        meal_name = request.POST["meal_name"]
        food_name = request.POST["food_name"]
        username = request.user.username

        diet = Diet.objects.get(diet_name=diet_name, user=username)
        meal = diet.meals.get(meal_name=meal_name, user=username)

        food = meal.foods.get(food_name=food_name, user=username)
        meal.foods.remove(food)

        messages.success(request, "Successfully deleted " + food_name + " from " + meal_name)
        return HttpResponseRedirect("/viewdiet/" + diet_name)

@login_required
def create_diet(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        username = request.user.username

        if Diet.objects.filter(diet_name=diet_name, user=username).exists():
            messages.error(request, "Diet already exists")
            return HttpResponseRedirect("/")

        new_diet = Diet(diet_name=diet_name, user=username)
        new_diet.save()

        messages.success(request, "Successfully created new diet " + diet_name)
        return HttpResponseRedirect("/")

@login_required
def rename_diet(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        new_diet_name = request.POST["new_diet_name"]
        username = request.user.username

        if not Diet.objects.filter(diet_name=diet_name, user=username).exists():
            messages.error(request, "Diet does not exist")
            return HttpResponseRedirect("/")

        diet = Diet.objects.get(diet_name=diet_name, user=username)
        diet.diet_name = new_diet_name
        diet.save()

        messages.success(request, "Successfully renamed diet to " + new_diet_name)
        return HttpResponseRedirect("/")

@login_required
def delete_diet(request):
    if request.method == "POST":
        diet_name = request.POST["diet_name"]
        username = request.user.username

        if not Diet.objects.filter(diet_name=diet_name, user=username).exists():
            messages.error(request, "Diet does not exist")
            return HttpResponseRedirect("/")

        new_diet = Diet.objects.get(diet_name=diet_name, user=username)
        new_diet.delete()

        messages.success(request, "Successfully deleted diet " + diet_name)
        return HttpResponseRedirect("/")


@login_required
def view_diet(request, diet_name=None):
    username = request.user.username

    if not diet_name:
        return HttpResponseRedirect("/")

    if not Diet.objects.filter(diet_name=diet_name, user=username).exists():
        return HttpResponseRedirect("/")

    meals = Diet.objects.get(diet_name=diet_name, user=username).meals.all()
    foods = Food.objects.filter(user=username)

    # For the export to text feature
    text_format = ""

    # Add up the calories, protein, carbs, fats in all the meals
    macro_sum = {}

    # Sum of all the meals
    total_macro_sum = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}

    # Sum of all nutrient values of foods in an individual meal
    for meal in meals:
        meal_sum = Macros()

        text_format += meal.meal_name + "\n"

        for food in meal.foods.filter(user=username):
            meal_sum.add_macros(food.calories, food.protein, food.carbs, food.totalfat)
            text_format += "\t{0} [{1} calories, {2}g protein, {3}g carbs, {4}g fats]\n".format(food.food_name, food.calories, food.protein, food.carbs, food.totalfat)

        text_format += "\n"

        macro_sum[meal.meal_name] = meal_sum.get_total()

    for meal in macro_sum:
        for macro in ["calories", "protein", "carbs", "fats"]:
            total_macro_sum[macro] += macro_sum[meal][macro]

    form_responses = messages.get_messages(request)
    response_message = None

    for response in form_responses:
        response_message = response
        break

    form_responses.used = True

    return render(request, "webapp/meals.html",
                  {"meals": meals, "diet_name": diet_name, "foods": foods, "macro_sum": macro_sum,
                   "total_macro_sum": total_macro_sum, "text_format": text_format, "response_message": response_message})

@login_required
def index(request):
    username = request.user.username

    diet_names = Diet.objects.filter(user=username)

    return render(request, "webapp/dietplans.html", {"diet_names": diet_names})

