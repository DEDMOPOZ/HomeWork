from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=100)
    content = models.TextField('Text')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
