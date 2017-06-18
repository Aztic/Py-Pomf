from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
	if request.method == 'POST':
		#form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username,password=password)
		#if form.is_valid():
		if user is not None:
			login(request,user)
			request.session.set_expiry(300)
			print(":)")
			print(request.user.is_authenticated())
			print(request.user.id)
			return HttpResponse('You are logged in')
		else:
			return HttpResponse('Is not valid')
	else:
		if request.user.is_authenticated():
			return HttpResponse("Already logged")
		form = AuthenticationForm()
		return render(request, 'login.html', {'form': form})