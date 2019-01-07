from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('addmeal', views.add_meal, name='add_meal'),
    path('deletemeal', views.delete_meal, name='delete_meal'),

    path('addfoodtomeal', views.add_food_to_meal, name='add_food_to_meal'),
    path('deletefoodfrommeal', views.delete_food_from_meal, name='delete_food_from_meal'),

    path('creatediet', views.create_diet, name='create_diet'),
    path('renamediet', views.rename_diet, name='rename_diet'),
    path('deletediet', views.delete_diet, name='delete_diet'),
    path('viewdiet', views.view_diet),
    path('viewdiet/<str:diet_name>', views.view_diet),
]