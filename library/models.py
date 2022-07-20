from django.db import models


class Author(models.Model):
    """
    Our author model
    """

    public_id = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)


    class Meta:
        ordering = [
            "first_name"
        ]
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Book(models.Model):
    """
    Our book model
    """

    public_id = models.CharField(unique=True, max_length=255)
    title = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(unique=True, max_length=255, null=False)


    class Meta:
        ordering = [
            "title"
        ]
        verbose_name = "Book"
        verbose_name_plural = "Books"
