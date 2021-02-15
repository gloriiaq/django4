from django.shortcuts import HttpResponseRedirect

# Create your views here.
def myhouse(request):
    return HttpResponseRedirect("/static/index.html")