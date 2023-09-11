from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
    if request.method == "POST":
        iban = request.POST["iban"]
        owner = User.objects.get(username=request.user)
        if Account.objects.filter(iban=iban).exists():
            return "It is already exist"
        else:
            ac = Account(owner=owner, iban=iban)
            ac.save()
    return redirect('/')


@login_required
def homePageView(request):
	return render(request, 'pages/index.html',{
		"accounts": Account.objects.filter(owner=request.user)
	})
