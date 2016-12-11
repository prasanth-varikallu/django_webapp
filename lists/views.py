from django.shortcuts import render
from django.http import HttpResponse
from lists.models import User
# Create your views here.
def home_page(request):

	user = User()
	user.username = request.POST.get('username', '')
	user.password = request.POST.get('password', '')
	user.save()
	return render(request, 'home.html', {'entered_username': request.POST.get('username', ''), 'entered_password': request.POST.get('password', '')})
