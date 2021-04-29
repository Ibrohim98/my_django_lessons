from django.http import HttpResponse
from django.http import HttpResponse


# Create your views here.
def greeting(request):
    return HttpResponse("Hello World")


def show_item(request):
    return HttpResponse("This is an item view")
