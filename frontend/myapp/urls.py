from django.urls import path
from . import views
urlpatterns = [
    path('myform/',views.myform,name='myform')
    ]