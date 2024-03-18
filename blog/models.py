from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=212)


class Tag(models.Model):
    title = models.CharField(max_length=212)


class City(models.Model):
    country = models.CharField(max_length=212)
    image = models.ImageField(upload_to='city')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.country
