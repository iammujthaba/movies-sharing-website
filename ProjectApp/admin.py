from django.contrib import admin
from . models import Category, Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_1','description', 'date', 'category','link', 'created','update']
    list_editable = ['image_1','description', 'date', 'category','link']
    list_display_links = ['name']
    list_per_page = 12
admin.site.register(Movie,MovieAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

