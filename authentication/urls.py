from django.urls import path

from .views import home, login, signup

app_name = 'authentication'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]