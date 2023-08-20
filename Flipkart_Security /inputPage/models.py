from django.db import models
class data_file(models.Model):
    file1=models.FileField(upload_to="inputPage/SOURCE_DOCUMENTS/")
# Create your models here.
