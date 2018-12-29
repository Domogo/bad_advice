from django.contrib import admin
from anyAdvice.models import AdviceModel


# Register your models here.
class AdviceAdmin(admin.ModelAdmin):
    fields = ('advice', 'slip_id', 'pub_date')


admin.site.register(AdviceModel, AdviceAdmin)
