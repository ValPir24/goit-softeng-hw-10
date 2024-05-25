from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=255, unique=True, default='')
    born_date = models.CharField(max_length=255, blank=True, null=True)
    born_location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, related_name='quotes', on_delete=models.CASCADE)
    tags = models.JSONField(default=list)  # Add default value here

    # Оновлений метод __str__ для моделі Quote
    def __str__(self):
        return self.quote



