from django.shortcuts import render
# from .models import Football

def home(request):
    return render(request, 'home.html')

def football_index(request):
    footballs = Football.objects.all()
    return render(request, 'football/index.html', {
        'footballs': footballs
    }) 

def basketball_index(request):
    basketballs = Basketball.objects.all()
    return render(request, 'basketball/index.html', {
        'basketballs': basketballs
    }) 

def baseball_index(request):
    baseballs = Baseball.objects.all()
    return render(request, 'baseball/index.html', {
        'baseballs': baseballs
    }) 

def mma_index(request):
    mmas = Mma.objects.all()
    return render(request, 'mma/index.html', {
        'mmas': mmas
    }) 

def soccer_index(request):
    soccers = Soccer.objects.all()
    return render(request, 'soccer/index.html', {
        'soccers': soccers
    }) 

def hockey_index(request):
    hockeys = Hockey.objects.all()
    return render(request, 'hockey/index.html', {
        'hockeys': hockeys
    }) 