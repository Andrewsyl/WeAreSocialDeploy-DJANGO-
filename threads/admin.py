from django.contrib import admin
from .models import Thread, Posts, Subject
# Register your models here.
admin.site.register(Thread)
admin.site.register(Posts)
admin.site.register(Subject)