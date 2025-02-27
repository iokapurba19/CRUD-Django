from django.db import models
import os

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='images/') 

    def __str__(self):
        return self.title

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        # Jika ada gambar yang sudah ada, hapus dari filesystem
        if self.pk:  # Memastikan objek sudah ada di database
            old_image = MyModel.objects.get(pk=self.pk).image
            if old_image and os.path.isfile(old_image.path):
                os.remove(old_image.path)
        super(MyModel, self).save(*args, **kwargs)