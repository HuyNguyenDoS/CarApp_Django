from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'carpages/home.html')

def about(request):
    return render(request, 'carpages/about.html')

def services(request):
    return render(request, 'carpages/services.html')

def contact(request):
    return render(request, 'carpages/contact.html')