from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from Task.utils import unique_slug_generator


# Create your models here.

class Tasks(models.Model):
    STATUS_CHOICES = (
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done")
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="To Do")
    due_date = models.DateField()
    slug = models.SlugField(max_length=250, null=True, blank=False, unique=True)

    def __str__(self):
        return str(self.title)


# To create url slug
@receiver(pre_save, sender=Tasks)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title)
