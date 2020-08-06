from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('author',)

    search_fields = ('title',)
    ordering = ('date_posted',)
    readonly_fields = ('date_posted',)

    fieldsets = (
        ('Post', {'fields': ('title', 'content', 'author', 'date_posted')}),
    )
    filter_horizontal = ()

admin.site.register(Post, PostAdmin)