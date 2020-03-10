from django.shortcuts import render
from .models import JobOrder

# Create your views here.

def login(request):
    context = {
        'result': JobOrder.objects.get(isbn='451800')
    }
    return render(request, 'index.html',context)