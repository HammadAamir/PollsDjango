from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['questionText']}),
        ('Date information', {'fields': ['pubDate'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    
    list_display = ('questionText', 'pubDate', 'wasPublishedRecently')
    list_filter = ['pubDate']
    search_fields = ['questionText']
admin.site.register(Question, QuestionAdmin)
