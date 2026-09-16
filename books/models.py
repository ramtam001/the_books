from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()
    genre = models.CharField(max_length=100, blank=True)
    pages = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
