from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string

from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(request):
	return render(request, 'index.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = RegisterForm()
		if request.method == "POST":
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				emailAddr = form.cleaned_data.get('email')
				messages.success(request, 'Account successfully created for ' + user)

				if form.save():
					template = render_to_string('doorb1/email_template.html', {'name': user})

					email = EmailMessage(
						'Kitchen237 Account',
						template,
						settings.EMAIL_HOST_USER,
						[emailAddr],
					)
					email.fail_silently = False
					email.send()

					return redirect('login')

		context = {'form': form}
		return render(request, 'register.html', context)


# def registerPage(request):
# 	# check if the user is already loged ..if yes redirest to homepage
# 	if request.user.is_authenticated:
# 		return redirect('index')
# 	# form = RegisterForm(request.POST)
# 	# if no then login the user in
# 	else:
# 		form = RegisterForm()
# 		if request.method == "POST":
# 			form = RegisterForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				email = form.cleaned_data.get('email')
# 				messages.success(request, 'Account successfully created for ' + user)
#
# 				if form.save():
# 					template = render_to_string('doorb1/email_template.html', {'name': user})
#
# 					email = EmailMessage(
# 						'Just-In-Time Account',
# 						template,
# 						settings.EMAIL_HOST_USER,
# 						[email],
# 					)
#
# 					email.fail_silently = False
# 					email.send()
#
# 					return redirect('login')
#
# 		context = {'form': form}
# 		return render(request, 'register.html', context)


def loginPage(request):
	form = UserCreationForm()

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password1')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Username or password incorrect! ')
			return redirect('login')

	context = {'form': form}
	return render(request, 'login.html', context)


def logoutPage(request):
	logout(request)
	return redirect('login')
