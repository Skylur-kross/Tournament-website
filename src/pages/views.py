from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from pages.models import players

# Create your views here.

def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "HomePage.html",{})

def tregister_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "TeamRegistration.html",{})

def sregister_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "SoloRegistration.html",{})

def registered_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "registered.html",{})

def register_user(request, *args):
    if(request.method=='POST'):
        usr=players()
        usr.player_fullname =request.POST.get("name")
        usr.player_login_email    =request.POST.get("email")
        usr.player_username = request.POST.get("usrname")
        usr.player_Steam_id  = request.POST.get("steamid")
        usr.player_contactno = request.POST.get("phone_no")
        usr.player_Dota_rank= request.POST.get("Dota_Rank")
        usr.save()
        return render(request,'registered/')
        print(player_fullname)
        print(player_login_email)
        print(player_username)