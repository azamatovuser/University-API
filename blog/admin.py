from django.contrib import admin
from blog.models import Post, Body, Comment


class BodyInline(admin.TabularInline):
    model = Body
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (BodyInline, )
    list_display = ('id', 'author', 'title', 'created_date')
    date_hierarchy = 'created_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')