from django.urls import path
from .views import index

urlpatterns = [
    path('', index) # index will come from the main function from views.py file added later.
]