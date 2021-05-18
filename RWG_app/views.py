from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    if "count" in request.session.keys():
        request.session['count'] += 1
    else:
        request.session['count'] = 0
    context = {
        'count': request.session['count'],
        'rand_word': get_random_string(length = 14)
    }
    return render(request, 'index.html', context)

def reset(request):
    request.session['count'] = 0
    return redirect('/')