from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=221)


class Tag(models.Model):
    title = models.CharField(max_length=221)


class FAQ(models.Model):
    question = models.CharField(max_length=221)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(max_length=221, unique=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Subscribe(models.Model):
    email = models.EmailField(unique=True, db_index=True)