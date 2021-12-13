from django.shortcuts import render
from user.forms import UserLoginForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# Create your views here.

class Login(LoginView):
	template_name='user/login.html'
	authentication_form=UserLoginForm
	LOGIN_REDIRECT_URL = '/profiles/'
	

@login_required(login_url='/login/')
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
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
	return render(request, 'user/register.html')

