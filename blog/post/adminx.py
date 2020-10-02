import xadmin
from post.models import *
# Register your models here.


class PostAdmin():
    list_display = ['title', 'category', 'created']
    list_filter = ['title', 'category']


xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(Post, PostAdmin)
