from django.contrib import admin
from home.models import *


admin.site.register(Articles)
class NewRegst(admin.ModelAdmin):
	list_display = ['first_name', 'second_name', 'gender', 'phone_number', 'photo', 'address']
admin.site.register(NewRegistration, NewRegst)