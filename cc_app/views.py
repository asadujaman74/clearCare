from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request, 'cc_app/index.html')

def login(request):
    return render(request,'cc_app/login.html')

def registration(request):
    return render(request,'cc_app/register.html')

def doctorList(request):
    return render(request,'cc_app/list.html')

def doctorDetails(request):
    return render(request,'cc_app/detail-page.html')

def aboutUs(request):
    return render(request,'cc_app/about.html')

def bookingPage(request):
    return render(request,'cc_app/booking-page.html')

def blogPage(request):
    return render(request,'cc_app/blog.html')
