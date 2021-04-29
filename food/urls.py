from . import views
from django.urls import path

urlpatterns = [
    path('salom/', views.greeting, name='greeting'),
    path('item/', views.show_item, name='items'),

]
