from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products')
    
    def __str__(self):
        return f"{self.id}. {self.name}. {self.image}"
    
    
class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Tambahkan bidang-bidang lain yang diperlukan untuk pesanan

    def __str__(self):
        return self.full_name
