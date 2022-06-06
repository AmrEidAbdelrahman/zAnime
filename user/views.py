from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from user.forms import UserLoginForm, UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Notification



import json
# Create your views here.

class Login(LoginView):
	template_name='user/login.html'
	authentication_form=UserLoginForm
	LOGIN_REDIRECT_URL = '/profiles/'




@login_required(login_url='/accounts/login/')
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		#print(request.FILES)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			print(request.user.profile.pic.url)
			p_form.save()
			print(request.user.profile.pic.url)
			messages.success(request, f'You Profile save')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'user/profile.html', context)


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'welcome {username}, your account created successfully')
			return redirect("login")

	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form':form})

def NotificationView(request):
	if request.method == "GET":
		try:
			user = request.user
			notifications = user.notification_set.all().order_by("-arr_date").values("message")
			if len(notifications) > 2:
				notifications = notifications[0:2]
			return JsonResponse(data={'data': list(notifications)})
		except Exception as e:
			print(e)
			return JsonResponse({"error":str(e)}, status=404)
	
