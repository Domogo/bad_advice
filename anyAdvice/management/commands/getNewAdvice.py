from django.core.management.base import BaseCommand
from anyAdvice.models import AdviceModel
import requests as rq
from django.utils import timezone


class Command(BaseCommand):
    help = 'Requests new advice from API'

    def handle(self, *args, **kwargs):
        response = rq.get('https://api.adviceslip.com/advice')

        # If response is valid save the advice or change it's pub_date if
        # existing
        if(response.ok):
            r = response.json()
            if(AdviceModel.objects.filter(
                    advice=r['slip']['advice']).exists()):
                existingAdvice = AdviceModel.objects.get(
                    advice=r['slip']['advice'])
                existingAdvice.pub_date = timezone.now()
                existingAdvice.save()
            else:
                a = AdviceModel(advice=r['slip']['advice'],
                                slip_id=r['slip']['slip_id'])
                a.save()
        else:
            response.raise_for_status()
