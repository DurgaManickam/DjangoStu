from django.contrib import admin
from .models import Post, TestModel,UserModel
# Register your models here.
admin.site.register(Post)
admin.site.register(TestModel)
admin.site.register(UserModel)
