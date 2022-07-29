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

def exams(request):
    
    context = {
      'title':'Examinations'
        
    }
    return render(request, 'modules/exams.html', context)

def cbc(request):
    
    context = {
      'title':'CBC EXAMS'
        
    }
    return render(request, 'modules/cbc.html', context)

def timetable(request):
    
    context = {
      'title':'TimeTable'
        
    }
    return render(request, 'modules/timetable.html', context)