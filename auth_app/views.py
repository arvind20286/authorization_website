from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import re

from .models import User, AuthProvider
from google.oauth2 import id_token
from google.auth.transport import requests

import json

CLIENT_ID = "775820619887-949m71g9o41l44qu8evrg83ivbi4tbhq.apps.googleusercontent.com"

def sessionExists(request):
    if request.session.__contains__("loggedin") and request.session.get("loggedin"):
        return True
    return False

def isValidPassword(password):
    if(len(password) < 8):
        return (False, "Length of password should be atleast 8 characters")

    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is valid."

def index(request):
    if(sessionExists(request)):
        return HttpResponseRedirect(reverse("auth_app:welcome"))
    return render(request, "index.html")


def welcome(request):
    if(sessionExists(request)):
        return render(request, "welcome.html", {"email": request.session.get("email")})
    return HttpResponseRedirect(reverse("auth_app:index"))

def register(request):
    if(sessionExists(request)):
        return HttpResponseRedirect(reverse("auth_app:welcome"))
    return render(request, "registration.html")

@csrf_exempt
def checkRegistration(request):
    if request.method == "POST":
        user_data = json.loads(request.body)
        print(user_data)
        response = {
            "registration_successful":False
        }
        if(user_data['email'] == '' or user_data['name'] == '' or user_data['password'] == ''):
            response["rejct_reason_messg"] = "Please fill all fields!"
            return JsonResponse(response)
        
        if(User.objects.filter(email=user_data["email"]).exists()):
            response["rejct_reason_messg"] = "Email ID Already in use"
            return JsonResponse(response)
        
        is_valid, message = isValidPassword(user_data["password"])
        if(not is_valid):
            response["rejct_reason_messg"] = message
            return JsonResponse(response)

        hashed_password = make_password(user_data["password"])
        User.objects.create(email=user_data["email"], password=hashed_password, auth_provider=AuthProvider.objects.get(name="email"))
        response["registration_successful"] = True
        return JsonResponse(response)

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
        if not user.exists() or not check_password(password, user[0].password):
            context["user_exists"] = False
        else:
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
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            print(idinfo)
            google_id = idinfo["sub"]
            email = idinfo["email"]
            if(not User.objects.filter(email=email, google_id=google_id).exists()):
                User.objects.create(
                    email=email,
                    google_id=google_id,
                    auth_provider=AuthProvider.objects.get(name="gmail")
                )
            
            request.session.__setitem__("loggedin", True)
            request.session.__setitem__("email", email)
            return HttpResponseRedirect(reverse("auth_app:welcome"))

        except ValueError as e:
            # Invalid token
            print(f"Google sign-in failed: {e}")
            return HttpResponseRedirect(reverse("auth_app:index"))
            pass
