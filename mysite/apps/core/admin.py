from django.contrib import admin
from .models import Employer,Candidate,Job,Application
# Register your models here.

admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(Application)