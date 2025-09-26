from django.contrib import admin
from .models import Fotografia

from user.models import AuthorizedPersonnel

# Register your models here.
admin.site.register(Fotografia)
admin.site.register(AuthorizedPersonnel)


