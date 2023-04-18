from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Problem
from django.http import JsonResponse

@api_view(http_method_names=["POST", "GET"])
@csrf_exempt
def buy_cases(request, pk):
    user = request.user
    problem = Problem.objects.get(id=pk)
    problem.casebuyers.add(user)
    return JsonResponse({
        "status": "200 OK",
        "info": "Siz masala caselarini sotib oldingiz",
    })

@api_view(http_method_names=["POST", "GET"])
@csrf_exempt
def buy(request, pk):
    user = request.user
    problem = Problem.objects.get(id=pk)
    problem.buyers.add(user)
    return JsonResponse({
        "status": "200 OK",
        "info": "Siz masala yechimini sotib oldingiz",
    })

@api_view(http_method_names=["POST", "GET"])
@csrf_exempt
def like(request, pk):
    user = request.user
    problem = Problem.objects.get(id=pk)
    problem.likes.add(user)
    problem.unlikes.remove(user)
    return JsonResponse({
        "status": "200 OK",
        "info": f"Siz {problem.name} ga like bosdingiz",
    })

@api_view(http_method_names=["POST", "GET"])
@csrf_exempt
def unlike(request, pk):
    user = request.user
    problem = Problem.objects.get(id=pk)
    problem.unlikes.add(user)
    problem.likes.remove(user)
    return JsonResponse({
        "status": "200 OK",
        "info": f"Siz {problem.name} ga unlike bosdingiz",
    })
