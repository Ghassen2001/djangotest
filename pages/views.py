from django.http import HttpResponse
from django.template import loader

def homePageView(request):
    return HttpResponse("Welcome to the Home Page!")

def index(request):
    context = {"message": "Ahla bel GASTON"}
    template = loader.get_template("pages/index.html")
    return HttpResponse(template.render(context, request))