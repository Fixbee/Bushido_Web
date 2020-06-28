from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from home.models import Articles, NewRegistration
from home.forms import RegistrationForm
from django.contrib import messages
def index(request):
	return render(request, 'home/index.html')

def achievements(request):
	return render(request, 'home/achievement.html')

def forms(request):
	return render(request, 'home/form.html')

def events(request):
	return render(request, 'home/events.html')

def instructors(request):
	return render(request, 'home/instructors.html')

def gallery(request):
	articles = Articles.objects.all()
	
	return render(request, 'home/gallery.html', {'articles':articles})

def registration(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()

		#messages.success(request, "Registration successfully completed")
		return redirect('/')
	return render(request, 'home/register.html', {"form":form})
