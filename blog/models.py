from django.db import models
import uuid
# Create your models here.


class Post(models.Model):
    id = id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
