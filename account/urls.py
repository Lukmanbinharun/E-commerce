from django.urls import path
from . import views

urlpatterns = [
    path("signin/",views.signin, name= 'signin'),
    path("login/",views.userlogin, name= 'login'),
    path("logout/",views.userlogout, name= 'logout'),
]