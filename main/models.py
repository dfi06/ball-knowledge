import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('accessory', 'Accessory'),
        ('footwear', 'Footwear'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name