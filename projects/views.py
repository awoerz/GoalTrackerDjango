from django.shortcuts import render, HttpResponse
from .models import Note, Goal

# Create your views here.
def home(request):
    return render(request, "home.html") 

def goals(request):
    goals = Goal.objects.all()
    return render(request, "goals.html", {"goals": goals})

def single_goal(request, id):
    goal = Goal.objects.get(id=id)
    notes = Note.objects.select_related().filter(goal=id)
    return render(request, "single_goal.html", {"goal": goal, "notes": notes})