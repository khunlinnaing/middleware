from django.shortcuts import render, HttpResponse
def index(request):
    print(kajsd)
    return HttpResponse("Successful at "+str(request.current_time) )