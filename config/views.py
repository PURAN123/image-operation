from django.shortcuts import render



def about_page(request):
    """Render the about us page"""
    return render(request, 'about.html')


def pricing_page(request):
    """Render the pricing page"""
    return render(request, 'pricing.html')

def home_page(request):
    """Render the home page"""
    return render(request, 'home.html')

def services_page(request):
    """Render the services page"""
    return render(request, 'services.html')