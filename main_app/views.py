from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def soccer_detail(request, soccer_id):
    soccer = Soccer.objects.get(id=soccer_id)
    return render(request, 'soccer/detail.html', {
        'soccer': soccer
    })

class FootballCreate(CreateView):
  model = Football
  fields = '__all__'

class BaseballCreate(CreateView):
  model = Baseball
  fields = '__all__'

class BasketballCreate(CreateView):
  model = Basketball
  fields = '__all__'

class HockeyCreate(CreateView):
  model = Hockey
  fields = '__all__'

class MmaCreate(CreateView):
  model = Mma
  fields = '__all__'

class SoccerCreate(CreateView):
  model = Soccer
  fields = '__all__'

class FootballUpdate(UpdateView):
  model = Football
  fields = ['name', 'brand', 'description', 'quantity', 'price']

class BaseballUpdate(UpdateView):
  model = Baseball
  fields = ['name', 'brand', 'description', 'quantity', 'price']

class BasketballUpdate(UpdateView):
  model = Basketball
  fields = ['name', 'brand', 'description', 'quantity', 'price']

class HockeyUpdate(UpdateView):
  model = Hockey
  fields = ['name', 'brand', 'description', 'quantity', 'price']

class MmaUpdate(UpdateView):
  model = Mma
  fields = ['name', 'brand', 'description', 'quantity', 'price']

class SoccerUpdate(UpdateView):
  model = Soccer
  fields = ['name', 'brand', 'description', 'quantity', 'price']

class FootballDelete(DeleteView):
  model = Football
  success_url = '/football'

class BaseballDelete(DeleteView):
  model = Baseball
  success_url = '/baseball'

class BasketballDelete(DeleteView):
  model = Basketball
  success_url = '/basketball'

class HockeyDelete(DeleteView):
  model = Hockey
  success_url = '/hockey'

class MmaDelete(DeleteView):
  model = Mma
  success_url = '/mma'

class SoccerDelete(DeleteView):
  model = Soccer
  success_url = '/soccer'