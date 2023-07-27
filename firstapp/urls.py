from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= 'home'),
    path("contac/", views.contac, name= 'contact'),
    path("about/", views.about, name= 'about'),
    path("search/", views.search, name= 'search'),
    path("multisearch/", views.multisearch, name= 'multisearch'),
    path("chickout/", views.chickout, name= 'chickout'),
    path("orderfinish/", views.orderfinish, name= 'orderfinish'),
]