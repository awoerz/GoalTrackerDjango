from django.shortcuts import render, HttpResponse
from .models import Note, Goal

# Create your views here.
def home(request):
    notes = Note.objects.all()
    goals = Goal.objects.all()
    return render(request, "home.html", {"notes": notes, "goals": goals}) 

def goals(request):
    goals = Goal.objects.all()
    return render(request, "goals.html", {"goals": goals})

def single_goal(request, id):
    goal = Goal.objects.get(id=id)
    return render(request, "single_goal.html", {"goal": goal})