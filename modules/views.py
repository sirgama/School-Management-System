from django.shortcuts import render

# Create your views here.

def dashboard(request):
    
    context = {
      'title':'Dashboard'
        
    }
    return render(request, 'modules/dashboard.html', context)


def students(request):
    
    context = {
      'title':'Students'
        
    }
    return render(request, 'modules/students.html', context)