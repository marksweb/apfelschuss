from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class Voting(models.Model):
    title = models.CharField(max_length=160)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('votes.Author', on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    video_url = models.URLField(max_length=200)
    categories = models.ManyToManyField('votes.Category')
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title
