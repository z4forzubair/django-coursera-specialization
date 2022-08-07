from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 05d11317 is the polls index.")