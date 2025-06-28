from django.shortcuts import render

# Create your views here.

def NUME_VIEW_view(request):
	context = {}
	return render(request, 'NUME_TEMPLATE.html', context)

def NUME_VIEW2_view(request):
	context = {}
	return render(request, 'NUME_TEMPLATE2.html', context)
