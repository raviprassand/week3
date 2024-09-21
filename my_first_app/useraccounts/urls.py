from django.urls import path
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]

from .views import home

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('signup/', signup, name='signup'),
    path('signup/success/', signup_success, name='signup_success'),
]

