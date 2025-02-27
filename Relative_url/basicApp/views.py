from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'basicApp/index.html')

def other(request):
    return render(request,'basicApp/other.html')

def Relative(request):
    return render(request,'basicApp/Relative_url.html')
