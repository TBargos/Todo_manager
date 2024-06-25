from django.shortcuts import render
from django.http import HttpResponse

from main.services import load_actual_tasks, load_completed_tasks

# Create your views here.

def index(request):
    actual_tasks = load_actual_tasks()
    completed_tasks = load_completed_tasks()

    context = {
        "actual_tasks": actual_tasks,
        "completed_tasks": completed_tasks
    }
    
    return render(request, 'main/index.html', context)