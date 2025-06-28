from django.shortcuts import render

# Create your views here.

def atenush_list_view(request):
	context = {}
	return render(request, 'atenush_list.html', context)
