from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=9,choices=STATUS_CHOICES, default='Pending')
    date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES,default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.deadline is None or (self.deadline and self.deadline < self.date):
            self.deadline = self.date
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # makemigration command convertes the python code in sql and save the changes
    # table will be created after migrate command to show the table in the admin panel go to admin.py page and register the table in the admin panel
    # to register enter the command
    # from app.model import Task => importing task from app.models
    # admin.site.register(Task)