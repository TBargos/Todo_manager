from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from main.services import *

# Create your views here.

@csrf_exempt
def index(request):
    actual_tasks = load_actual_tasks()
    completed_tasks = load_completed_tasks()

    context = {
        "actual_tasks": actual_tasks,
        "completed_tasks": completed_tasks
    }
    
    if request.POST:
        if request.POST.get('newtask'):
            add_new_task(request.POST.get('newtask'))
        if request.POST.get('taskoff'):
            mark_task_finished(request.POST.get('taskoff'))
        if request.POST.get('clear_finished_tasks'):
            del_finished_tasks()
        return redirect(request.build_absolute_uri())
    
    
    return render(request, 'main/index.html', context)