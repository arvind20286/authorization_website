from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User
from google.oauth2 import id_token
from google.auth.transport import requests

import json

CLIENT_ID = "775820619887-949m71g9o41l44qu8evrg83ivbi4tbhq.apps.googleusercontent.com"

def sessionExists(request):
    if request.session.__contains__("loggedin") and request.session.get("loggedin"):
        return True
    return False

def index(request):
    if request.session.__contains__("loggedin") and request.session.get("loggedin"):
        return HttpResponseRedirect(reverse("auth_app:welcome"))
    return render(request, "index.html")


def welcome(request):
    if request.session.__contains__("loggedin") and request.session.get("loggedin"):
        return render(request, "welcome.html", {"email": request.session.get("email")})
    return HttpResponseRedirect(reverse("auth_app:index"))

def register(request):
    if(sessionExists(request)):
        return HttpResponseRedirect(reverse("auth_app:welcome"))
    return render(request, "registration.html")

@csrf_exempt
def checkRegistration(request):
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({
            "registration_successful":True
        })

@csrf_exempt
def verify(request):
    if request.method == "POST":
        response = json.loads(request.body)
        print(response)
        email = response["email"]
        password = response["password"]
        context = {
            "user_exists": True,
        }
        user = User.objects.filter(email=email)
        if not user.exists() or user[0].password != password:
            context["user_exists"] = False
            
        request.session.__setitem__("loggedin", True)
        request.session.__setitem__("email", email)
        return JsonResponse(context)


def logout(request):
    if request.method == "POST":
        request.session.__setitem__("loggedin", False)
        return HttpResponseRedirect(reverse("auth_app:index"))


@csrf_exempt
def googleSignin(request):
    if request.method == "POST":
        print("Verifying")
        token = request.POST["credential"]
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            print(idinfo)
            userid = idinfo["sub"]
            email = idinfo["email"]
            context = {}
            context["email"] = email
            request.session.__setitem__("loggedin", True)
            request.session.__setitem__("email", email)
            return HttpResponseRedirect(reverse("auth_app:welcome"))

        except ValueError:
            # Invalid token
            return HttpResponseRedirect(reverse("auth_app:index"))
            pass
