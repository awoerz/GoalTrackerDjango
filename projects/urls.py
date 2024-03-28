from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("goals", views.goals, name="goals"),
    path("goals/<int:id>", views.single_goal)
]
