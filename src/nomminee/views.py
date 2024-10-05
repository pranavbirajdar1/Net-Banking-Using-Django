from django.shortcuts import render

# Create your views here.
def nominee(request):
    return render(request,'nominee.html')