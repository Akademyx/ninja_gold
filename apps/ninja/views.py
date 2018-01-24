from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'msg' in request.session:
        request.session['msg'] = []
    
    context = {
        'gold': request.session['gold'],
        'log': request.session['msg']
    }
    return render(request, 'index.html',context)

def process(request):
    if request.POST['building'] == 'farm':
        amount = random.randrange(10,21)
        request.session['gold'] += amount
    if request.POST['building'] == 'cave':
        amount = random.randrange(5,11)
        request.session['gold'] += amount
    if request.POST['building'] == 'house':
        amount = random.randrange(2, 6)
        request.session['gold'] += amount
    if request.POST['building'] == 'casino':
        amount = random.randrange(-50, 52)
        request.session['gold'] += amount

    if amount > 0:
        request.session['msg'].append({'result': 'won', 'msg': "You have earned {} gold".format(amount)})   
    else:
        request.session['msg'].append({'result': 'lost', 'msg': "You have lost {} gold".format(abs(amount))})

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')