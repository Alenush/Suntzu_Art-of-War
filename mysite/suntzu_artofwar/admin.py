from django.contrib import admin

# Register your models here.
from .models import ChaptersTranslation, Comments

admin.site.register(ChaptersTranslation)
admin.site.register(Comments)
