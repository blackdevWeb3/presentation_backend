from django.db import models

# Create your models here.


class Presentation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/')
    float_value = models.FloatField()
    link = models.URLField()

    def __str__(self):
        return self.title
