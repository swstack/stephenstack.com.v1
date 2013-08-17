from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import http_handler
import random

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def handle_json_req(request):
    data = http_handler.getprofile(request)
    return render(request, 'profile.html', {'profile_data': data})

def login(request):
    print request
    return home(request)

def teleport(request):
    random_sites = {
                    0: 'reddit',
                    1: 'digg',
                    2: 'youtube',
                    3: 'imdb',
                    4: 'rottentomatoes',
                    5: 'ebay',
                    6: 'pandora',
                    7: 'grooveshark',
                    8: 'ign',
                    9: 'gamespot',
                    10: 'break',
                    11: 'nfl',
                    12: 'mlb',
                    13: 'dealsucker',
                    14: 'lifehacker',
                    }
    site = random_sites[random.randrange(0, 15, 2)]
    return redirect('http://%s.com' % site)