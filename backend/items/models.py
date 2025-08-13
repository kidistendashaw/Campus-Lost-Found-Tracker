from django.db import models


class Item(models.Model):
    STATUS_CHOICES = (
        ("lost", "Lost"),
        ("found", "Found"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="item_images/")
