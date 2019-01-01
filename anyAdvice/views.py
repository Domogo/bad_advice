from django.shortcuts import render
# from django.http import HttpResponse
from anyAdvice.models import AdviceModel
from random import choice


# Create your views here.
# Homepage - latest question here (changes every 10min via management command)
colors = ('1abc9c', '2ecc71', '3498db', '9b59b6', 'f1c40f', 'f39c12', 'e74c3c')


def index(request):
    if(AdviceModel.objects.all().exists()):
        rand_color = choice(colors)
        latest = AdviceModel.objects.latest('pub_date')
        return render(request, 'anyAdvice/index.html',
                      {'advice': latest, 'color': rand_color})
    else:
        error = 'There is currently no advice to give.'
        return render(request, 'anyAdvice/index.html', {'error': error})


# show all advice currently in database
def allAdvice(request):
    if(AdviceModel.objects.all()):
        rand_color = choice(colors)
        all_advice = AdviceModel.objects.all().order_by('-pub_date')
        return render(request, 'anyAdvice/allAdvice.html',
                      {'allAdvice': all_advice, 'color': rand_color})
    else:
        error = 'There is currently no advice to give.'
        return render(request, 'anyAdvice/allAdvice.html', {'error': error})


# Get a random advice from database
def randAdvice(request):
    if(AdviceModel.objects.all()):
        rand_color = choice(colors)
        keys = AdviceModel.objects.values_list('id', flat=True).order_by('id')
        rand_key = choice(keys)
        rand_advice = AdviceModel.objects.get(id=rand_key)
        return render(request, 'anyAdvice/randAdvice.html',
                      {'randAdvice': rand_advice, 'color': rand_color})
    else:
        error = 'There is currently no advice to give.'
        return render(request, 'anyAdvice/randAdvice.html', {'error': error})
