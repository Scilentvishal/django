from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Your Are At vishal's Django App.")

def about(request):
    return HttpResponse("Hello Your Are At vishal's Django App about page.")

def contact(request):
    return HttpResponse("Hello Your Are At vishal's Django App contact page.")