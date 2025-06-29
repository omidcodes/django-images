from django.db import models

from core.azure_storage import AzureMediaStorage


class Image(models.Model):
    title = models.CharField(max_length=128)
    file = models.ImageField(
        storage=AzureMediaStorage(),
        upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title}"
