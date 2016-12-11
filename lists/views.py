from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import User
# Create your views here.
def home_page(request):
	if request.method == 'POST':
		User.objects.create(username=request.POST['username'], password=request.POST['password'])
		return redirect('/')

	return render(request, 'home.html')
