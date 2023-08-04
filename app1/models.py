from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=150, default='')
    body = models.TextField()
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
