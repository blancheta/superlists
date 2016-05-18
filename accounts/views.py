import sys
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from .authentification import PersonaAuthentificationBackend
from django.shortcuts import redirect

def login(request):
	print('login view', file=sys.stderr)
	# user = PersonaAuthentificationBackend().authenticate(request.POST['assertion'])
	user = authenticate(assertion=request.POST['assertion'])
	user.backend = 'django.contrib.auth.backends.ModelBackend'

	if user is not None:
		auth_login(request, user)
	return redirect('/')


def logout(request):
	auth_logout(request)
	return redirect('/')
