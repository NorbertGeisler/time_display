from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

# Create your views here.
# def index(request):
#     return HttpResponse("terst!?")

def index(request):
    context = {
        "timeDate": strftime("%b %d, %Y", localtime()),
        "timeTime": strftime("%H:%M %p", localtime())
    }
    return render(request,'index.html', context)