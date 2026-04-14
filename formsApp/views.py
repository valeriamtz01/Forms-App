from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request));

# def login(request):
#     email = request.POST["email"]
#     pwd = request.POST["password"]
    
#     # validate email (yourself)
#     if "@" not in email:
#         print("Invalid email.")
   
#     Login.objects.create(email = email, password = pwd)
   
   
#     context = {"usersemail": email}
#     template = loader.get_template("home.html");
#     return HttpResponse(template.render(context, request));


def login(request):
    if request.method == "POST": 
        form = LoginForm(request.POST)

        # validate form using django
        if form.is_valid():
            form.save() 
            print("Form saved."); # shows in terminal (not website)
        else:
            print("Invalid form.")

        email = request.POST["email"]
        pwd = request.POST["password"]
    
    
        context = {"usersemail": email}
        template = loader.get_template("index.html");
        return HttpResponse(template.render(context, request));

def details(request):
    detailsList = Login.objects.all
    context = {"details": detailsList}
    template = loader.get_template("details.html");
    return HttpResponse(template.render(context, request));

