from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # future feture author = models.ForeignKey()
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self) -> str:
        return self.title