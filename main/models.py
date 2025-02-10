from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book',
        verbose_name_plural = 'Books'
        ordering = ['title']
