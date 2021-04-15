# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
#     return render(request,'index.html')

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    first_name = 'Chandra'
    last_name = 'Karim'

    context = {
        'first_name':first_name,
        'last_name':last_name,
    }
    return render(request, "index.html", context) 