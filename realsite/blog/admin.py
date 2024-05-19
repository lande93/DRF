from django.contrib import admin
from .models import Post

from django.contrib import admin
from .models import Post,Rating,Category,Comment,Postviewed


admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Postviewed)



