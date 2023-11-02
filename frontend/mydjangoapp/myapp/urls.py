from django.urls import path
from . import views
urlpatterns = [
    path('myform/',views.myform_view,name='myform'),
    path('peticiones/',views.myform_view2,name='myform2'),
    path('',views.index,name='index')
    ]