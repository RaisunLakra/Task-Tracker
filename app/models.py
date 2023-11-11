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

    def save(self, *args, **kwargs):
        if self.deadline is None or (self.deadline and self.deadline < self.date):
            self.deadline = self.date
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Description(models.Model):
    title = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True) # blank = True means that the description is alowed to be blank during form validation and null = True means that if value is empty then it will be null

    def __str__(self):
        return self.title.title

    # makemigration command convertes the python code in sql and save the changes
    # table will be created after migrate command to show the table in the admin panel go to admin.py page and register the table in the admin panel
    # to register enter the command
    # from app.model import Task => importing task from app.models
    # admin.site.register(Task)