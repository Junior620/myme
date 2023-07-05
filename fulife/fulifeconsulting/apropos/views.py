from django.shortcuts import render

# Create your views here.

def propos(request):
    return render(request,'a-propos.html')
