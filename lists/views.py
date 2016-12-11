from django.shortcuts import render
from django.http import HttpResponse
from lists.models import User
# Create your views here.
def home_page(request):
	if request.method == 'POST':
		entered_username, entered_password = request.POST['username'], request.POST['password']
		User.objects.create(username=entered_username, password=entered_password)
	else:
		entered_username = ''
		entered_password = ''

	return render(request, 'home.html', {'entered_username': entered_username, 'entered_password': entered_password})
