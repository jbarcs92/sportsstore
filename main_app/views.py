from django.shortcuts import render
from .models import Football
from .models import Baseball
from .models import Basketball
from .models import Hockey
from .models import Mma
from .models import Soccer

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

def football_detail(request, football_id):
    football = Football.objects.get(id=football_id)
    return render(request, 'football/detail.html', {
        'football': football
    })

def baseball_detail(request, baseball_id):
    baseball = Baseball.objects.get(id=baseball_id)
    return render(request, 'baseball/detail.html', {
        'baseball': baseball
    })

def basketball_detail(request, basketball_id):
    basketball = Basketball.objects.get(id=basketball_id)
    return render(request, 'basketball/detail.html', {
        'basketball': basketball
    })

def hockey_detail(request, hockey_id):
    hockey = Hockey.objects.get(id=hockey_id)
    return render(request, 'hockey/detail.html', {
        'hockey': hockey
    })

def mma_detail(request, mma_id):
    mma = Mma.objects.get(id=mma_id)
    return render(request, 'mma/detail.html', {
        'mma': mma
    })

def soccer_detail(request, mma_id):
    mma = Soccer.objects.get(id=soccer_id)
    return render(request, 'soccer/detail.html', {
        'soccer': soccer
    })