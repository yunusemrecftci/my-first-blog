from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title','date','slug']
    list_filter = ['date']
    search_fields = ['title','text']
    
    

admin.site.register(Post,PostAdmin)