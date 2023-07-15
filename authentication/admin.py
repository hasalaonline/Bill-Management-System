from django.contrib import admin

# Register your models here.
from .models import WaitingList, ApprovedUser

admin.site.register(WaitingList)
admin.site.register(ApprovedUser)