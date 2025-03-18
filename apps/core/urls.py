from django.urls import path
from .views import *

urlpatterns = [
    #path('industry/', IndustryApiView.as_view()),
    path('projects/', ProjectListApiView.as_view()),

 
]
