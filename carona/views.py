from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')


def procurar(request):
	return render(request, 'procurar.html')