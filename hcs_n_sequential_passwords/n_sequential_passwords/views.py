from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'n_sequential_passwords/index.html')

def pattern_lock(request):
    return render(request, 'n_sequential_passwords/pattern_lock.html')
