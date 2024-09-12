from django.db import models

class Comment(models.Model):
    PENDING = 'pending'
    SAVED = 'saved'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SAVED, 'Saved'),
    ]

    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    status = models.CharField(
        max_length=250,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    def __str__(self):
        return f'{self.name} - {self.status}'
