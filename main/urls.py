from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("direct/", views.direct, name="direct"),
    path("group/", views.group, name="group"),
]
