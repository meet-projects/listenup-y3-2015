from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
def home(request):
	return render(request, 'app/home.html', {})
<<<<<<< HEAD
def aboutus(request):
	return render(request, 'app/aboutus.html', {})
def FAQ(request):
	return render(request, 'app/FAQ.html', {})
=======
def signup(request):
	return render(request, 'app/signup.html', {})
def login(request):
	return render(request, 'app/login.html', {})
def achievements(request):
	return render(request, 'app/achievements.html', {})
>>>>>>> 114db56b023cd398233052c0595cba9808266dde
