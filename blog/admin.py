from django.contrib import admin
from .models import Blog
from .models import Appointment
from .models import Book

# Register your models here.
admin.site.register(Blog)
admin.site.register(Appointment)
admin.site.register(Book)
