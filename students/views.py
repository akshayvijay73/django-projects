from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, StudentForm
from django.contrib.auth.decorators import login_required
from .models import Student

# Add views for register, login, logout and profile

def hi(request):
    return render(request, 'hi.html')

def register_view(request):
	if request.method == "POST":
		user_form = UserRegisterForm(request.POST)
		student_form = StudentForm(request.POST)

		if user_form.is_valid() and student_form.is_valid():
			user = user_form.save(commit=False)
			user.set_password(user.password)
			user.save()

			Student.user = user
			Student.save()

			return redirect('login')

	else:
		user_form = UserRegisterForm()
		student_form = StudentForm()

	return render(request, 'register.html', {
		'user_form' : user_form,
		'student_form' : student_form
		})


def login_view(request):
	if request.method == "POST":
		user_name = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=user_name, password=password)

		if user:
			login(request, user)
			return redirect('profile')
	return render(request, 'login.html')

def logout_view(request):
	logout(request)
	return redirect('login')

@login_required
def profile_view(request):
	student = Student.objects.get(user=request.user)
	return render(request, 'profile.html', {
		'student' : student
		})

