from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Food
# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Food.objects.create(main_dish=request.POST['main_dish'], side_dish=request.POST['side_dish'])
		return redirect('/orders/first-order-ever/')
	return render(request, 'home.html')

def view_list(request):
	items = Food.objects.all()
	return render(request, 'order.html', {'items': items})
