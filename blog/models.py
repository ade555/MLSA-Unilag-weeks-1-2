from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    date_created = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    # TO DO: ADD IMAGES
    # Wura-backend
    # josephB-backend