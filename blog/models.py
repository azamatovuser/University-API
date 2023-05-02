from django.db import models
from main.models import Category, Tag
from django.db.models.signals import post_save
from account.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='post/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='post')
    tags = models.ManyToManyField(Tag, related_name='post')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Body(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='body')
    body = RichTextField()
    is_script = models.BooleanField(default=False)


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    @property
    def get_related_comments(self):
        qs = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.id)
        if qs:
            return qs
        else:
            return None


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        top_level_comment = instance
        while top_level_comment.parent_comment:
            top_level_comment = top_level_comment.parent_comment
        instance.top_level_comment_id = top_level_comment.id
        instance.save()


post_save.connect(comment_post_save, sender=Comment)