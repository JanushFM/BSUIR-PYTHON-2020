from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Order)
admin.site.register(Painting)
admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(MyMail)