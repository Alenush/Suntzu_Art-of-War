from django.contrib import admin

# Register your models here.
from .models import Chapters, ChaptersTranslation, Comments

admin.site.register(Chapters)
admin.site.register(ChaptersTranslation)
admin.site.register(Comments)
