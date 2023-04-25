from django.db import models
from main.models import Category, Tag
from account.models import Profile
from ckeditor.fields import RichTextField


class Timestamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def file_path_cover(instance, filename):
    return f"courses/{instance.title}/cover/{filename}"


class Course(Timestamp):
    DIFFICULTY = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advanced'),
    )
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={"role": 1})
    title = models.CharField(max_length=221)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    body = RichTextField()
    cover = models.ImageField(upload_to=file_path_cover, null=True)
    detail_cover = models.ImageField(upload_to=file_path_cover, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='course')
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    discount_price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)

    def __str__(self):
        return self.title


def file_path(instance, filename):
    return f"courses/{instance.lesson.course.title}/{instance.lesson.title}/{filename}"


class Lesson(Timestamp):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=221)
    body = RichTextField()


class LessonFiles(Timestamp):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_files')
    file = models.FileField(upload_to=file_path)
    is_main = models.BooleanField(default=False)


class SoldCourse(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)