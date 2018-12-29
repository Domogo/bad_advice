from django.test import TestCase
from .models import AdviceModel
from django.urls import reverse


# Create your tests here.
class AdviceModelTest(TestCase):
    """docstring for AdviceModelTest"""
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        AdviceModel.objects.create(
            advice='A problem shared is a problem halved.',
            slip_id=106,)

    def test_str_method(self):
        advice = AdviceModel.objects.get(slip_id=106)
        self.assertEquals(advice.__str__(), advice.advice)

    def test_advice_label(self):
        advice = AdviceModel.objects.get(slip_id=106)
        field_label = advice._meta.get_field('advice').verbose_name
        self.assertEquals(field_label, 'advice')

    def test_advice_max_length(self):
        advice = AdviceModel.objects.get(slip_id=106)
        max_length = advice._meta.get_field('advice').max_length
        self.assertEquals(max_length, 100)


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create advice for homepage tests
        AdviceModel.objects.create(
            advice='A problem shared is a problem halved.',
            slip_id=106,)

    def test_index_view_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'anyAdvice/index.html')

    def test_all_advice_view_correct_template(self):
        response = self.client.get(reverse('allAdvice'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'anyAdvice/allAdvice.html')

    def test_random_advice_view_correct_template(self):
        response = self.client.get(reverse('randAdvice'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'anyAdvice/randAdvice.html')

    def test_index_context_correct(self):
        advice = AdviceModel.objects.get(slip_id=106)
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.context['advice'] == advice)
