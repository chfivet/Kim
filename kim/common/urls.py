from django.urls import path

from .views import home
from .controler import authentication


app_name = 'common'
urlpatterns = [
    path('', home.home, name='home'),
    path('login', home.login, name='login'),
    path('controler', authentication.validation_user, name='authentication')
    ]
