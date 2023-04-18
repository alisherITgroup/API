from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import login, authenticate


@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        try:
            data = dict(request.POST)
            user = User.objects.create_user(
                username=data['username'][0], 
                password=data['password'][0],
                first_name=data['first_name'][0],
                last_name=data['last_name'][0],
                email=data['email'][0],
                city=data['city'][0],
                town=data['town'][0],
                education=data['education'][0],
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({"error": "Bu username oldin olingan"})
    return JsonResponse({"signup": 200})

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = dict(request.POST)
        user = authenticate(request, username=data['username'][0], password=data['password'][0])
        if user is None:
            return JsonResponse({"error": "Authenticated failed"}, status=404)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token)}, status=200)
    return JsonResponse({"login": 200})
