from django.urls import path
from . import views
urlpatterns = [
    path('myform/',views.myform_view,name='myform')
    ]