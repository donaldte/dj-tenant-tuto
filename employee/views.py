from django.shortcuts import render

from django.http import HttpResponse

from .models import Employe

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    employees = Employe.objects.all()
    
    if request.POST:
        
        name = request.POST.get('name')
        
        Employe.objects.create(name=name)
        
        employees = Employe.objects.all()
    
    
    return render(request, 'employee.html', {'employees': employees})