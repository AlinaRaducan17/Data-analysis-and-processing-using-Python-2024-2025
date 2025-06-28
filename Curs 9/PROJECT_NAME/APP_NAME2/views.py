from django.shortcuts import render

# Create your views here.

def NUME_VIEW3_view(request):
	context = {}
	return render(request, 'NUME_TEMPLATE3.html', context)
