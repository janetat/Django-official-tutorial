from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_title = 'Polls system site_title'
admin.site.site_header = 'Polls system site_header'
admin.site.index_title = "Polls system index_title"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ('question_text',)}),
        ('Date information', {'fields': ('pub_date',), 'classes': ('collapse', 'extrapretty')}),
    ]

    # http://127.0.0.1:8000/admin/polls/question/
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # fields = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
    date_hierarchy = 'pub_date'

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
