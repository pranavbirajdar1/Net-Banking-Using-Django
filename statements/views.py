from django.shortcuts import render

# Create your views here.


def statement(request):
    return render(request, 'statement.html')
