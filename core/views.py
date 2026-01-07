from django.http import HttpResponse


def home(request):
    return HttpResponse("Opsin Site - Home OK")
