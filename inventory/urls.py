from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
	# /inventory/
	path('', views.index, name='index'),

	# /inventory/addfood
	path('addfood', views.add_food, name='add_food'),

	path('updatefood', views.update_food, name='update_food'),

	path('deletefood', views.delete_food, name='delete_food'),
]