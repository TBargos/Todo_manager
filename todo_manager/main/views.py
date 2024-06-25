from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "text": "text",
    }
    
    return render(request, 'main/main.html', context)