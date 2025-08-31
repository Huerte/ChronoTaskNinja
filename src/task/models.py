from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=700, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True) # If empty it means no due date

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.title[:10]}'

