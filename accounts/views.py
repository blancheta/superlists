from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def persona_login(request):
	user = authenticate(assertion=request.POST['assertion'])
	print(user)
	if user:
		print("Connection as ",user.email)
		login(request, user)

	return HttpResponse('OK')