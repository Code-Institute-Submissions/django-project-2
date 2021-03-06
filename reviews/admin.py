from django.contrib import admin
from .models import Review, Comment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['written_by', 'title', 'content', 'published_date']

admin.site.register(Review)
admin.site.register(Comment)