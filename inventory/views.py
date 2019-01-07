from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from meals.models import Food

def validate_request(request):
    fields = {
        "food_name": "",
        "calories": 0,
        "totalfat": 0,
        "saturatedfat": 0,
        "transfat": 0,
        "carbs": 0,
        "cholestorol": 0,
        "sodium": 0,
        "fiber": 0,
        "sugars": 0,
        "protein": 0
    }

    valid = True
    if request.method == "POST":
        for i in request.POST:
            if "food_name" in i:
                fields[i] = request.POST[i]

                if fields[i] == "":
                    valid = False
                    break

            elif request.POST[i] and "csrf" not in i:
                try:
                    fields[i] = int(request.POST[i])
                except:
                    valid = False
                    break

    if not valid:
        return False

    return fields

@login_required
def add_food(request):
    fields = validate_request(request)
    username = request.user.username

    if not fields:
        messages.error(request, "Invalid request")
        return HttpResponseRedirect("/inventory")

    # Check if the food exists
    if Food.objects.filter(food_name=fields["food_name"], user=username).exists():
        messages.error(request, "Food already exists")
        return HttpResponseRedirect("/inventory")

    new_food = Food(
        food_name=fields["food_name"], user=username, calories=fields["calories"], totalfat=fields["totalfat"],
        saturatedfat=fields["saturatedfat"], transfat=fields["transfat"], carbs=fields["carbs"],
        cholestorol=fields["cholestorol"], sodium=fields["sodium"], fiber=fields["fiber"],
        sugars=fields["sugars"], protein=fields["protein"]
    )
    new_food.save()

    messages.success(request, "Successfully added " + fields["food_name"])
    return HttpResponseRedirect("/inventory")

@login_required
def update_food(request):
    fields = validate_request(request)
    username = request.user.username

    if not fields:
        messages.error(request, "Invalid request")
        return HttpResponseRedirect("/inventory")

    food = Food.objects.get(food_name=fields["food_name"], user=username)

    food.calories = fields["calories"]
    food.totalfat = fields["totalfat"]
    food.saturatedfat = fields["saturatedfat"]
    food.transfat = fields["transfat"]
    food.carbs = fields["carbs"]
    food.cholestorol = fields["cholestorol"]
    food.sodium = fields["sodium"]
    food.fiber = fields["fiber"]
    food.sugars = fields["sugars"]
    food.protein = fields["protein"]

    food.save()

    messages.success(request, "Successfully updated " + fields["food_name"])
    return HttpResponseRedirect("/inventory")

@login_required
def delete_food(request):
    fields = validate_request(request)
    username = request.user.username

    if not fields:
        messages.error(request, "Invalid request")
        return HttpResponseRedirect("/inventory")

    food = Food.objects.get(food_name=fields["food_name"], user=username)
    food.delete()

    messages.success(request, "Successfully deleted " + fields["food_name"])
    return HttpResponseRedirect("/inventory")

@login_required
def index(request):
    username = request.user.username
    foods = Food.objects.filter(user=username)

    food_names = []
    for food in foods:
        food_names.append(food)

    form_responses = messages.get_messages(request)
    response_message = None

    for response in form_responses:
        response_message = response
        break

    form_responses.used = True

    return render(request, "webapp/foodinventory.html", {"names": food_names, "response_message": response_message})