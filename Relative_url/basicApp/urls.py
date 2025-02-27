from django.urls import path
from basicApp import views


app_name = 'basicApp'


urlpatterns = [
    path('Relative/',views.Relative,name='Relative'),
    path('other/',views.other,name='other'),
]
