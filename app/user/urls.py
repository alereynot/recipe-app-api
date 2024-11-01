from django.urls import path

from user import views


app_name = 'user'

url_paterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
