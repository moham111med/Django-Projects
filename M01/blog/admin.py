from django.contrib import admin
from .models import Post
# Register your models here.


#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #المعروض
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    #فلتر عن طريق استخدام
    list_filter = ['status', 'created', 'publish', 'author']
    #ابحث عن طريق
    search_fields = ['title', 'body']
    #slug يتولد تلقائيا من title اثناء عمل بوست
    prepopulated_fields = {'slug': ('title',)}
    #اثناء انشاء بوست يمكنك اختيار المؤلف عن طريق id
    raw_id_fields = ['author']
    #فلتر بالتاريخ
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']